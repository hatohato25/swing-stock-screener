"""
レポート生成モジュール

スクリーニング結果からHTMLレポートとMarkdownレポートを生成します。
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import markdown
from src.utils.logger import Logger


class ReportGenerator:
    """HTMLレポート生成クラス"""

    def __init__(self, output_dir: str, logger: Logger):
        """
        レポートジェネレーターを初期化する

        Args:
            output_dir: 出力ディレクトリのパス
            logger: ロガー
        """
        self.output_dir = Path(output_dir)
        self.logger = logger

        # テンプレートディレクトリを自動検出
        self.template_dir = Path(__file__).parent / "templates"

        # Jinja2環境のセットアップ
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))

        # 出力ディレクトリを作成
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, screened_stocks: List[Dict[str, Any]], report_date: str):
        """
        レポートを生成

        Args:
            screened_stocks: スクリーニング結果のリスト
            report_date: レポート日付（YYYY-MM-DD形式）
        """
        self.logger.info("レポート生成を開始します")

        # 出力ディレクトリ作成
        report_dir = self.output_dir / report_date
        report_dir.mkdir(parents=True, exist_ok=True)

        # カテゴリ別に分類
        categorized = self._categorize_stocks(screened_stocks)

        # HTMLレポート生成
        self._generate_html(categorized, report_date, report_dir)

        # Markdownレポート生成
        self._generate_markdown(categorized, report_date, report_dir)

        # インデックスページ更新
        self._update_index(report_date)

        self.logger.info(f"レポート生成完了: {report_dir}")

    def _normalize_scores(self, stocks: List[Any]) -> List[Any]:
        """
        パーセンタイルランク方式でスコアを正規化する（偏差値方式）

        偏差値方式: score_normalized = 50 + (score - mean) / std * 15
        - 中央値が50点
        - 標準偏差が15点
        - 1位でも他と大差なければ60点程度
        - 極端に優れていれば80-90点

        Args:
            stocks: スクリーニング結果リスト（ScreenResultオブジェクトまたは辞書）

        Returns:
            正規化されたスクリーニング結果リスト
        """
        if not stocks or len(stocks) < 2:
            # 1件の場合は50点固定
            if not stocks:
                return stocks

            normalized_stocks = []
            for stock in stocks:
                if hasattr(stock, 'score'):
                    # ScreenResultオブジェクトの場合
                    from src.analysis.screener import ScreenResult
                    normalized_stock = ScreenResult(
                        stock_code=stock.stock_code,
                        stock_name=stock.stock_name,
                        category=stock.category,
                        score=50.0,
                        details=stock.details
                    )
                    normalized_stocks.append(normalized_stock)
                else:
                    # 辞書の場合
                    normalized_stock = stock.copy()
                    normalized_stock["score"] = 50.0
                    normalized_stocks.append(normalized_stock)
            return normalized_stocks

        # スコアを抽出
        scores = []
        for stock in stocks:
            if hasattr(stock, 'score'):
                scores.append(stock.score)
            else:
                scores.append(stock.get("score", 0))

        # 平均と標準偏差を計算
        mean = sum(scores) / len(scores)
        variance = sum((s - mean) ** 2 for s in scores) / len(scores)
        std = variance ** 0.5

        # 標準偏差が0の場合（全て同じスコア）は全て50点
        if std == 0:
            normalized_stocks = []
            for stock in stocks:
                if hasattr(stock, 'score'):
                    # ScreenResultオブジェクトの場合
                    from src.analysis.screener import ScreenResult
                    normalized_stock = ScreenResult(
                        stock_code=stock.stock_code,
                        stock_name=stock.stock_name,
                        category=stock.category,
                        score=50.0,
                        details=stock.details
                    )
                    normalized_stocks.append(normalized_stock)
                else:
                    # 辞書の場合
                    normalized_stock = stock.copy()
                    normalized_stock["score"] = 50.0
                    normalized_stocks.append(normalized_stock)
            return normalized_stocks

        # 偏差値方式で正規化
        normalized_stocks = []
        for stock in stocks:
            if hasattr(stock, 'score'):
                original_score = stock.score
            else:
                original_score = stock.get("score", 0)

            # 偏差値計算: 50 + (score - mean) / std * 15
            normalized_score = 50 + ((original_score - mean) / std) * 15

            # 0-100の範囲に収める（極端な外れ値対策）
            normalized_score = max(0.0, min(100.0, normalized_score))

            if hasattr(stock, 'score'):
                # ScreenResultオブジェクトの場合
                from src.analysis.screener import ScreenResult
                normalized_stock = ScreenResult(
                    stock_code=stock.stock_code,
                    stock_name=stock.stock_name,
                    category=stock.category,
                    score=normalized_score,
                    details=stock.details
                )
                normalized_stocks.append(normalized_stock)
            else:
                # 辞書の場合
                normalized_stock = stock.copy()
                normalized_stock["score"] = normalized_score
                normalized_stocks.append(normalized_stock)

        return normalized_stocks

    def _categorize_stocks(
        self, stocks: List[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        スクリーニング結果をカテゴリ別に分類し、スコアを正規化する

        Args:
            stocks: スクリーニング結果のリスト

        Returns:
            カテゴリ別の正規化されたランキング辞書
        """
        categories = {
            "volume_surge": [],  # 出来高急増
            "breakout": [],  # ブレイクアウト
            "bb_lower_bounce": [],  # BB下限反転
            "pullback_dip": [],  # 押し目買いチャンス
            "golden_cross_approaching": [],  # ゴールデンクロス直前
            "value_inflation_adjusted": [],  # インフレ対応バリュー株
        }

        for stock in stocks:
            category = stock.get("category", "other")
            if category in categories:
                categories[category].append(stock)

        # 各カテゴリでスコアを正規化してからソート
        normalized_categories = {}
        for category, stocks_list in categories.items():
            # スコアを正規化
            normalized_stocks = self._normalize_scores(stocks_list)
            # スコア降順でソート
            normalized_stocks.sort(key=lambda x: x.get("score", 0) if isinstance(x, dict) else x.score, reverse=True)
            normalized_categories[category] = normalized_stocks

        return normalized_categories

    def _generate_html(
        self,
        categorized: Dict[str, List[Dict[str, Any]]],
        report_date: str,
        report_dir: Path,
    ):
        """
        HTMLレポートを生成

        Args:
            categorized: カテゴリ別に分類された銘柄
            report_date: レポート日付
            report_dir: レポート出力ディレクトリ
        """
        template = self.env.get_template("index.html")

        # 統計情報を計算
        stats = self._calculate_stats(categorized)

        # テンプレートに渡すデータ
        context = {
            "date": report_date,
            "rankings": categorized,
            "stats": stats,
        }

        # HTML生成
        html_content = template.render(context)

        # ファイル保存
        output_file = report_dir / "index.html"
        output_file.write_text(html_content, encoding="utf-8")

        self.logger.info(f"HTMLレポート生成: {output_file}")

    def _calculate_stats(
        self, categorized: Dict[str, List[Dict[str, Any]]]
    ) -> Dict[str, int]:
        """
        スクリーニング結果の統計情報を計算

        Args:
            categorized: カテゴリ別に分類された銘柄

        Returns:
            統計情報
        """
        # ユニークな銘柄コードを集計
        all_codes = set()
        for category_stocks in categorized.values():
            for stock in category_stocks:
                all_codes.add(stock["stock_code"])

        return {
            "total_stocks": len(all_codes),
            "volume_surge_count": len(categorized["volume_surge"]),
            "breakout_count": len(categorized["breakout"]),
            "bb_lower_bounce_count": len(categorized["bb_lower_bounce"]),
            "pullback_dip_count": len(categorized["pullback_dip"]),
            "golden_cross_approaching_count": len(
                categorized["golden_cross_approaching"]
            ),
            "value_inflation_adjusted_count": len(
                categorized["value_inflation_adjusted"]
            ),
        }

    def _generate_markdown(
        self,
        categorized: Dict[str, List[Dict[str, Any]]],
        report_date: str,
        report_dir: Path,
    ):
        """
        Markdownレポートを生成

        Args:
            categorized: カテゴリ別に分類された銘柄
            report_date: レポート日付
            report_dir: レポート出力ディレクトリ
        """
        # Jinja2テンプレートを使用してMarkdown生成
        template = self.env.get_template("README.md")

        # 統計情報を計算
        stats = self._calculate_stats(categorized)

        # テンプレートに渡すデータ
        context = {
            "date": report_date,
            "rankings": categorized,
            "stats": stats,
        }

        # Markdown生成
        markdown_content = template.render(context)

        # ファイル保存
        output_file = report_dir / "README.md"
        output_file.write_text(markdown_content, encoding="utf-8")

        self.logger.info(f"Markdownレポート生成: {output_file}")

    def _update_index(self, report_date: str):
        """
        インデックスページを更新

        Args:
            report_date: 追加するレポート日付
        """
        # 全レポート日付を取得
        report_dates = self._get_existing_reports()

        # 新しい日付を追加してソート
        if report_date not in report_dates:
            report_dates.append(report_date)
        report_dates.sort(reverse=True)

        # インデックスHTML生成
        html = self._generate_index_html(report_dates)

        # ファイル保存
        index_file = self.output_dir / "index.html"
        index_file.write_text(html, encoding="utf-8")

        self.logger.info(f"インデックスページ更新: {index_file}")

    def _get_existing_reports(self) -> List[str]:
        """
        既存のレポート日付を取得

        GitHub Actions環境では`.existing_reports.json`から読み込み、
        ローカル環境では`docs/`ディレクトリをスキャンする。
        両方の結果を統合して重複を削除する。

        Returns:
            レポート日付のリスト（降順ソート済み）
        """
        report_dates = []

        # 1. .existing_reports.jsonから既存レポート一覧を読み込む（GitHub Actions用）
        existing_reports_file = self.output_dir / ".existing_reports.json"
        if existing_reports_file.exists():
            try:
                import json
                with open(existing_reports_file, "r", encoding="utf-8") as f:
                    existing_dates = json.load(f)
                    if isinstance(existing_dates, list):
                        report_dates.extend(existing_dates)
                        self.logger.info(f"既存レポート一覧を読み込みました: {len(existing_dates)}件")
                    else:
                        self.logger.warning(
                            f".existing_reports.jsonの形式が不正です: {type(existing_dates)}"
                        )
            except json.JSONDecodeError as e:
                self.logger.warning(f".existing_reports.jsonのJSON解析に失敗: {e}")
            except Exception as e:
                self.logger.warning(f".existing_reports.jsonの読み込みに失敗: {e}")

        # 2. ローカルのdocs/ディレクトリもスキャン（ローカル開発環境用 & 補完用）
        if self.output_dir.exists():
            for item in self.output_dir.iterdir():
                if item.is_dir() and len(item.name) == 10 and item.name.count("-") == 2:
                    # index.htmlが存在するかチェック
                    if (item / "index.html").exists() and item.name not in report_dates:
                        report_dates.append(item.name)

        # 重複削除してソート（降順）
        report_dates = sorted(set(report_dates), reverse=True)

        return report_dates

    def _generate_index_html(self, report_dates: List[str]) -> str:
        """
        インデックスページのHTMLを生成

        Args:
            report_dates: レポート日付のリスト（新しい順）

        Returns:
            HTML文字列
        """
        html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>株式スクリーニングレポート - アーカイブ</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }
        .latest {
            background: #e8f5e9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 4px solid #4CAF50;
        }
        .latest a {
            font-size: 20px;
            color: #2e7d32;
            text-decoration: none;
            font-weight: bold;
        }
        .latest a:hover {
            text-decoration: underline;
        }
        h2 {
            color: #555;
            margin-top: 30px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background: white;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        a {
            color: #4CAF50;
            text-decoration: none;
            font-size: 18px;
        }
        a:hover {
            text-decoration: underline;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #999;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>株式スクリーニングレポート - アーカイブ</h1>

"""

        # 最新レポート
        if report_dates:
            latest = report_dates[0]
            html += f"""    <div class="latest">
        <p style="margin-bottom: 10px;">📊 最新レポート</p>
        <a href="{latest}/index.html">{latest}</a>
    </div>

"""

        # 過去のレポート
        if len(report_dates) > 1:
            html += """    <h2>過去のレポート</h2>
    <ul>
"""
            for date in report_dates[1:]:
                html += f'        <li><a href="{date}/index.html">{date}</a></li>\n'

            html += """    </ul>
"""

        # フッター
        html += f"""    <div class="footer">
        <p>Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>
"""

        return html

    def generate_ai_analysis_html(
        self, report_date: str, ai_analysis_md_path: Optional[Path] = None
    ) -> bool:
        """
        AI分析結果のHTML出力を生成

        Args:
            report_date: レポート日付（YYYY-MM-DD形式）
            ai_analysis_md_path: AI分析Markdownファイルのパス（Noneの場合は自動検出）

        Returns:
            成功時True、失敗時False
        """
        try:
            # AI分析Markdownファイルのパス
            if ai_analysis_md_path is None:
                ai_analysis_md_path = self.output_dir / report_date / "ai_analysis.md"

            # ファイルが存在しない場合はスキップ
            if not ai_analysis_md_path.exists():
                self.logger.warning(f"AI分析ファイルが存在しません: {ai_analysis_md_path}")
                return False

            # Markdownを読み込み
            markdown_content = ai_analysis_md_path.read_text(encoding="utf-8")

            # Markdown → HTML変換
            html_content_body = markdown.markdown(
                markdown_content,
                extensions=[
                    'fenced_code',
                    'tables',
                    'nl2br'
                ]
            )

            # Jinja2テンプレートを使用してHTML生成
            template = self.env.get_template("ai_analysis.html")
            context = {
                "date": report_date,
                "analysis_content": html_content_body
            }

            html_full = template.render(context)

            # HTML保存
            output_file = self.output_dir / report_date / "ai_analysis.html"
            output_file.write_text(html_full, encoding="utf-8")

            self.logger.info(f"AI分析HTML生成完了: {output_file}")
            return True

        except Exception as e:
            self.logger.error(f"AI分析HTML生成に失敗: {e}", exc_info=True)
            return False
