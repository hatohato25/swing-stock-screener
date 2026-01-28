"""
Gemini API連携によるレポート分析モジュール

スクリーニングレポート（Markdown形式）を読み込み、Gemini APIを活用して
AIによる分析を実施し、投資判断をサポートします。
"""

import re
import requests
from pathlib import Path
from typing import Optional

from src.utils.logger import Logger


class GeminiReportAnalyzer:
    """
    Gemini APIを使用してスクリーニングレポートを分析するクラス

    Attributes:
        api_key: Gemini APIキー（環境変数 GEMINI_API_KEY から取得）
        logger: ログ記録用のLoggerインスタンス
        api_url: Gemini APIのエンドポイントURL
        timeout: API呼び出しのタイムアウト（秒）
    """

    def __init__(self, api_key: str, logger: Logger):
        """
        GeminiReportAnalyzerを初期化する

        Args:
            api_key: Gemini APIキー（環境変数 GEMINI_API_KEY から取得）
            logger: ログ記録用のLoggerインスタンス
        """
        self.api_key = api_key
        self.logger = logger
        # 無料プランで利用可能: gemini-3-flash-preview
        # "inputTokenLimit": 1048576,
        # "outputTokenLimit": 65536,
        self.api_url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            "gemini-3-flash-preview:generateContent"
        )
        self.timeout = 60  # タイムアウト（秒）

    def read_latest_report(self, docs_dir: str = "docs") -> tuple[str, str]:
        """
        最新日付のレポートファイルを読み込む

        docs/YYYY-MM-DD/ ディレクトリから最新日付を取得し、
        README.md を読み込む。

        Args:
            docs_dir: レポートディレクトリのパス（デフォルト: "docs"）

        Returns:
            (report_date, report_content): レポート日付とMarkdown全文のタプル

        Raises:
            FileNotFoundError: レポートファイルが存在しない場合
        """
        docs_path = Path(docs_dir)

        if not docs_path.exists():
            self.logger.error(f"レポートディレクトリが存在しません: {docs_path}")
            raise FileNotFoundError(f"レポートディレクトリが存在しません: {docs_path}")

        # YYYY-MM-DD形式のディレクトリを取得（降順ソート）
        date_dirs = [
            d for d in docs_path.iterdir()
            if d.is_dir() and re.match(r'^\d{4}-\d{2}-\d{2}$', d.name)
        ]

        if not date_dirs:
            self.logger.error(f"レポートディレクトリが見つかりません: {docs_path}")
            raise FileNotFoundError(f"レポートディレクトリが見つかりません: {docs_path}")

        # 最新日付を取得
        latest_dir = sorted(date_dirs, reverse=True)[0]
        report_date = latest_dir.name

        # README.md を読み込み
        report_path = latest_dir / "README.md"
        if not report_path.exists():
            self.logger.error(f"レポートファイルが見つかりません: {report_path}")
            raise FileNotFoundError(f"レポートファイルが見つかりません: {report_path}")

        with open(report_path, "r", encoding="utf-8") as f:
            report_content = f.read()

        self.logger.info(f"レポート日付: {report_date}")
        self.logger.info(f"レポートファイル: {report_path}")

        return report_date, report_content

    def read_report_by_date(self, report_date: str, docs_dir: str = "docs") -> str:
        """
        指定日付のレポートファイルを読み込む

        Args:
            report_date: レポート日付（YYYY-MM-DD形式）
            docs_dir: レポートディレクトリのパス（デフォルト: "docs"）

        Returns:
            report_content: Markdown全文

        Raises:
            FileNotFoundError: レポートファイルが存在しない場合
            ValueError: 日付形式が不正な場合
        """
        # 日付形式のバリデーション
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', report_date):
            self.logger.error(f"日付形式が不正です: {report_date}（YYYY-MM-DD形式で指定してください）")
            raise ValueError(f"日付形式が不正です: {report_date}（YYYY-MM-DD形式で指定してください）")

        report_path = Path(docs_dir) / report_date / "README.md"

        if not report_path.exists():
            self.logger.error(f"レポートファイルが見つかりません: {report_path}")
            raise FileNotFoundError(f"レポートファイルが見つかりません: {report_path}")

        with open(report_path, "r", encoding="utf-8") as f:
            report_content = f.read()

        self.logger.info(f"レポート日付: {report_date}")
        self.logger.info(f"レポートファイル: {report_path}")

        return report_content

    def generate_prompt(self, report_content: str) -> dict:
        """
        Gemini APIに送信するプロンプトを生成する

        システムプロンプトでアナリストの役割を定義し、
        ユーザープロンプトにレポート全文と3つの分析視点を含める。

        Args:
            report_content: レポートのMarkdown全文

        Returns:
            API呼び出し用のペイロード（dict）
        """
        # システムプロンプト: アナリストの役割定義
        system_prompt = """
あなたは、日本株のスウィング取引（数日〜数週間の保有期間）を専門とする経験豊富なアナリストです。
テクニカル分析とファンダメンタルズ分析を組み合わせた投資判断をサポートします。
回答は常にmarkdown形式で、グラフィカルに読みやすく構成してください。
"""

        # ユーザープロンプト: レポート全文 + 3つの分析視点
        user_prompt = f"""
以下は、本日生成された株式スクリーニングレポートです。
このレポートを詳細に分析し、以下3つの視点で投資判断をサポートしてください。

## 分析視点

### 1. 注目銘柄の選定（5銘柄程度）
- 複数カテゴリで検出された銘柄を優先的に評価
- スコアが高く、RSI/MACDの組み合わせが良好な銘柄
- それぞれの注目理由を簡潔に説明

### 2. リスク評価
- 逆張り戦略（BB下限反転）のリスクとリターンを評価
- ストップロス設定の推奨価格帯
- 流動性（平均出来高）の確認ポイント

### 3. 投資戦略提案
- 短期（1-5日）、中期（1-2週間）、長期（2週間以上）の時間軸別戦略
- 各カテゴリの特性に応じた保有期間の推奨
- エントリー・エグジット戦略の提案

---

## レポート内容

{report_content}
"""

        # Gemini API用のペイロード構造
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": user_prompt
                        }
                    ]
                }
            ],
            "systemInstruction": {
                "parts": [
                    {
                        "text": system_prompt
                    }
                ]
            }
        }

        return payload

    def call_gemini_api(self, payload: dict) -> str:
        """
        Gemini APIを呼び出し、分析結果を取得する

        Args:
            payload: API呼び出し用のペイロード

        Returns:
            分析結果のMarkdown文字列

        Raises:
            ValueError: API呼び出しに失敗した場合
            TimeoutError: タイムアウトした場合
        """
        # cURLサンプル通り、APIキーはヘッダーで渡す
        url = self.api_url

        # APIキーの一部のみをログに記録（セキュリティ対策）
        masked_key = self.api_key[:8] + "***" if len(self.api_key) > 8 else "***"
        self.logger.info(f"Gemini APIを呼び出しています（APIキー: {masked_key}）...")

        try:
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "X-goog-api-key": self.api_key
                },
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            result = response.json()

            # レスポンスから分析結果を抽出
            # candidates[0].content.parts[0].text の構造
            text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

            if not text:
                self.logger.error("AIからの有効な回答を得られませんでした。")
                raise ValueError("AIからの有効な回答を得られませんでした。")

            self.logger.info("Gemini API呼び出しが成功しました。")
            return text

        except requests.exceptions.Timeout:
            self.logger.error(f"Gemini API呼び出しがタイムアウトしました（{self.timeout}秒）")
            raise TimeoutError(f"Gemini API呼び出しがタイムアウトしました（{self.timeout}秒）")

        except requests.exceptions.HTTPError as e:
            # 429エラーの場合、レスポンスボディに詳細な制限情報が含まれる
            if e.response.status_code == 429:
                try:
                    error_detail = e.response.json()
                    self.logger.error(
                        f"Gemini API Rate Limit到達 (429エラー):\n"
                        f"レスポンスボディ: {error_detail}\n"
                        f"HTTPエラー: {e}"
                    )
                except Exception:
                    # JSONパースに失敗した場合はテキストで取得
                    error_text = e.response.text
                    self.logger.error(
                        f"Gemini API Rate Limit到達 (429エラー):\n"
                        f"レスポンステキスト: {error_text}\n"
                        f"HTTPエラー: {e}"
                    )
            else:
                self.logger.error(f"Gemini API呼び出しに失敗: {e}")
            raise ValueError(f"Gemini API呼び出しに失敗: {e}")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Gemini API呼び出しに失敗: {e}")
            raise ValueError(f"Gemini API呼び出しに失敗: {e}")

    def analyze(self, report_date: Optional[str] = None) -> str:
        """
        レポートを分析し、AI分析結果を返す

        1. レポート読み込み（report_date指定時とNone時の分岐）
        2. プロンプト生成（generate_prompt）
        3. Gemini API呼び出し（call_gemini_api）
        4. 免責事項の追加

        Args:
            report_date: レポート日付（YYYY-MM-DD形式）。Noneの場合は最新日付

        Returns:
            AI分析結果のMarkdown文字列（免責事項含む）

        Raises:
            FileNotFoundError: レポートファイルが存在しない場合
            ValueError: API呼び出しに失敗した場合
            TimeoutError: タイムアウトした場合
        """
        # 1. レポート読み込み
        if report_date:
            self.logger.info(f"指定日付のレポートを分析します: {report_date}")
            report_content = self.read_report_by_date(report_date)
        else:
            self.logger.info("最新レポートを分析します")
            report_date, report_content = self.read_latest_report()

        # 2. プロンプト生成
        payload = self.generate_prompt(report_content)

        # 3. Gemini API呼び出し
        analysis_result = self.call_gemini_api(payload)

        # 4. 免責事項を追加
        disclaimer = """
---

## 免責事項

- この分析はAIによって生成されたものであり、情報提供のみを目的としています。
- 専門的な投資助言に代わるものではありません。
- 投資判断は必ず自己責任で行ってください。
- AI分析の精度は保証されません。銘柄の詳細なファンダメンタルズ分析、企業の業績、市場環境等を総合的に考慮することをお勧めします。
- 本分析の利用によって生じたいかなる損害についても、当方は一切の責任を負いません。
"""

        self.logger.info("AI分析が完了しました。")

        return analysis_result + disclaimer
