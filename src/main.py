"""
メインスクリプト

株式スクリーニングとレポート生成を統合実行します。
"""

import sys
import time
from datetime import date
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional, Dict, Any, List, Tuple

from src.utils.config import Config
from src.utils.logger import Logger
from src.api.client import TachibanaAPIClient
from src.api.master_data import MasterDataClient
from src.api.stock_price import StockPriceClient
from src.api.stock_info import StockInfoClient
from src.data.stock_filter import StockFilter
from src.analysis.indicators import TechnicalIndicators
from src.analysis.screener import StockScreener
from src.report.generator import ReportGenerator


def process_single_stock(
    stock: Dict[str, Any],
    price_client: StockPriceClient,
    technical_calc: TechnicalIndicators,
    screener: StockScreener,
    logger: Logger,
) -> Tuple[bool, Optional[Tuple[str, str, Optional[Dict[str, Any]], Optional[List[Any]]]]]:
    """
    単一銘柄の株価データ取得とスクリーニングを実行する（並列処理用）

    Args:
        stock: 銘柄情報
        price_client: 株価データクライアント
        technical_calc: テクニカル指標計算クラス
        screener: スクリーナークラス
        logger: ロガー

    Returns:
        (処理成功フラグ, スクリーニング結果タプル)
        - 処理成功フラグ: True=株価データ取得成功, False=エラー
        - スクリーニング結果タプル: 該当時のみ(銘柄コード, 銘柄名, 株価データ, スクリーニング結果)、該当なしはNone
    """
    issue_code = stock.get("sIssueCode")
    issue_name = stock.get("sIssueName")

    # 株価データ取得（既にrate_limiter.acquire()を内部で呼んでいる）
    price_data = price_client.get_daily_price(issue_code)
    if not price_data:
        return (False, None)  # エラー

    # テクニカル指標計算
    daily_prices = price_data.get("aCLMMfdsMarketPriceHistory", [])
    df = technical_calc.calculate_all_from_price_data(daily_prices)

    if df is None:
        return (False, None)  # エラー

    # スクリーニング
    screen_results = screener.screen_stock_with_dataframe(
        issue_code, issue_name, df
    )

    if screen_results:
        for result in screen_results:
            logger.info(
                f"✅ スクリーニング該当: {issue_name}({issue_code}) "
                f"カテゴリ={result.category}, スコア={result.score:.2f}"
            )
        return (True, (issue_code, issue_name, price_data, screen_results))

    return (True, None)  # 処理成功、該当なし


def process_single_value_stock(
    stock_dict: Dict[str, Any],
    stock_info_client: StockInfoClient,
    screener: StockScreener,
    logger: Logger,
) -> Optional[Any]:
    """
    単一銘柄のバリュー株判定を実行する（並列処理用）

    Args:
        stock_dict: スクリーニング結果辞書
        stock_info_client: 銘柄情報クライアント
        screener: スクリーナークラス
        logger: ロガー

    Returns:
        バリュー株判定結果（該当時）または None
    """
    stock_code = stock_dict["stock_code"]
    stock_name = stock_dict["stock_name"]
    current_price = stock_dict["details"].get("current_price")

    # 現在価格が取得できない場合はスキップ
    if current_price is None:
        logger.debug(f"現在価格不明のためスキップ: {stock_name}({stock_code})")
        return None

    # 銘柄情報（PER/PBR/配当利回り/ROE）を取得（既にrate_limiter.acquire()を内部で呼んでいる）
    stock_info = stock_info_client.get_stock_info(issue_code=stock_code)

    if stock_info is None:
        # データなし（WARNINGログは stock_info_client 内で出力済み）
        return None

    # インフレ対応バリュー株判定（緩和基準）
    value_inflation_result = screener.value_stock_inflation_adjusted_filter(
        stock_code=stock_code,
        stock_name=stock_name,
        stock_info=stock_info,
        current_price=current_price,
        per_threshold=25.0,
        pbr_threshold=2.5,
        dividend_yield_threshold=2.0,
        roe_threshold=8.0,
    )

    if value_inflation_result:
        logger.info(
            f"✅ インフレ対応バリュー株該当: {stock_name}({stock_code}) "
            f"PER={stock_info.get('per', '-')}倍, "
            f"PBR={stock_info.get('pbr', '-')}倍, "
            f"配当={stock_info.get('dividend_yield', '-')}%, "
            f"ROE={stock_info.get('roe', '-')}%, "
            f"スコア={value_inflation_result.score:.1f}"
        )
        return value_inflation_result

    return None


def main():
    """メイン処理"""
    start_time = time.time()

    # 1. 設定読み込み
    try:
        config = Config()
        print("✅ 設定を読み込みました")
    except Exception as e:
        print(f"❌ 設定の読み込みに失敗: {e}")
        sys.exit(1)

    # 2. ログ初期化
    try:
        logger = Logger(log_dir="data/logs", name="kabu-report")
        logger.set_level(config.log_level)
        logger.info("=" * 60)
        logger.info("株式スクリーニングレポート生成開始")
        logger.info("=" * 60)
        print("✅ ロガーを初期化しました")
    except Exception as e:
        print(f"❌ ロガーの初期化に失敗: {e}")
        sys.exit(1)

    # 3. APIクライアント初期化
    try:
        api_client = TachibanaAPIClient(config, logger)
        logger.info("APIクライアントを初期化しました")
        print("✅ APIクライアントを初期化しました")
    except Exception as e:
        logger.error(f"APIクライアントの初期化に失敗: {e}", exc_info=True)
        print(f"❌ APIクライアントの初期化に失敗: {e}")
        sys.exit(1)

    # 4. マスターデータ取得
    try:
        logger.info("銘柄マスターデータ取得を開始します")
        print("⏳ 銘柄マスターデータ取得中（数分かかります）...")

        master_client = MasterDataClient(api_client.auth_manager, logger)
        master_data = master_client.download_master_data()

        logger.info(f"銘柄マスターデータ取得完了: {len(master_data)}件")
        print(f"✅ マスターデータ: {len(master_data)}件")
    except Exception as e:
        logger.error(f"マスターデータ取得に失敗: {e}", exc_info=True)
        print(f"❌ マスターデータ取得に失敗: {e}")
        sys.exit(1)

    # 5. 個別株フィルタリング
    try:
        logger.info("個別株フィルタリングを開始します")
        print("⏳ 個別株フィルタリング中（ETF/REIT除外）...")

        stock_filter = StockFilter(logger)
        individual_stocks = stock_filter.filter_individual_stocks(master_data)

        logger.info(f"個別株フィルタリング完了: {len(individual_stocks)}件")
        print(f"✅ 個別株: {len(individual_stocks)}件")

        # 上位10件の銘柄名を表示（動作確認用）
        print("\n--- 個別株サンプル（上位10件） ---")
        for i, stock in enumerate(individual_stocks[:10], 1):
            code = stock.get("sIssueCode", "N/A")
            name = stock.get("sIssueName", "N/A")
            print(f"  {i}. {code}: {name}")
        print("---\n")

    except Exception as e:
        logger.error(f"個別株フィルタリングに失敗: {e}", exc_info=True)
        print(f"❌ 個別株フィルタリングに失敗: {e}")
        sys.exit(1)

    # 6. 株価データ取得とスクリーニング（Phase 3）- 並列処理版
    try:
        logger.info("株価データ取得とスクリーニングを開始します（並列処理）")
        print("⏳ 株価データ取得中（並列処理で高速化）...")

        # テスト用に上位1000件に制限（本番はNone）
        test_limit = 1000
        target_stocks = individual_stocks[:test_limit]
        logger.info(f"対象銘柄数: {len(target_stocks)}件（テスト制限）")

        price_client = StockPriceClient(api_client.auth_manager, logger)
        stock_info_client = StockInfoClient(
            api_client.auth_manager, api_client.rate_limiter, logger
        )
        technical_calc = TechnicalIndicators()
        screener = StockScreener()

        screened_stocks = []
        processed_count = 0  # 処理成功数
        error_count = 0      # エラー数

        # 並列処理（ThreadPoolExecutor）
        # max_workers=7: レート制限を遵守しつつ並列化（10リクエスト/秒を守る）
        max_workers = 7
        logger.info(f"並列処理スレッド数: {max_workers}")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 全銘柄を並列実行用にサブミット
            futures = {
                executor.submit(
                    process_single_stock,
                    stock,
                    price_client,
                    technical_calc,
                    screener,
                    logger,
                ): stock
                for stock in target_stocks
            }

            # 完了した順に結果を取得
            completed = 0
            for future in as_completed(futures):
                completed += 1

                # 進捗表示（100件ごと）
                if completed % 100 == 0:
                    logger.info(
                        f"進捗: {completed}/{len(target_stocks)}件 "
                        f"(処理成功: {processed_count}, エラー: {error_count})"
                    )
                    print(
                        f"  進捗: {completed}/{len(target_stocks)}件 "
                        f"(該当: {len(screened_stocks)}件)"
                    )

                try:
                    success, result = future.result()
                    if success:
                        processed_count += 1
                        if result:
                            (
                                issue_code,
                                issue_name,
                                price_data,
                                screen_results,
                            ) = result
                            for screen_result in screen_results:
                                screened_stocks.append(screen_result.to_dict())
                    else:
                        error_count += 1
                except Exception as e:
                    error_count += 1
                    logger.error(f"株価データ処理エラー: {e}", exc_info=True)

        logger.info(
            f"株価データ取得完了: 処理成功={processed_count}件, エラー={error_count}件, 該当={len(screened_stocks)}件"
        )
        print(
            f"\n✅ 株価データ取得: 処理成功={processed_count}件, エラー={error_count}件"
        )
        print(f"✅ テクニカルスクリーニング該当: {len(screened_stocks)}件")

        # バリュー株スクリーニング（2種類に分割）
        logger.info("バリュー株スクリーニングを開始します")
        logger.info(
            f"対象銘柄数: {len(screened_stocks)}件（テクニカル条件該当銘柄）"
        )

        # テクニカルスクリーニング結果から重複を排除（銘柄コードでユニーク化）
        # 理由: 同一銘柄が複数カテゴリ（出来高急増/ブレイクアウト）に該当する場合、
        #      バリュー株判定は1回のみ実施すればよい（PER/PBRは銘柄固有の値）
        unique_stocks = {}
        for stock_dict in screened_stocks:
            code = stock_dict["stock_code"]
            if code not in unique_stocks:
                unique_stocks[code] = stock_dict

        unique_stock_list = list(unique_stocks.values())
        logger.info(
            f"ユニーク銘柄数: {len(unique_stock_list)}件 "
            f"（元の件数: {len(screened_stocks)}件）"
        )

        print(
            f"\n⏳ バリュー株スクリーニング中（対象: {len(unique_stock_list)}件）..."
        )
        print(
            "   ※テクニカル条件該当銘柄のみPER/PBR/配当利回り/ROEを取得します"
        )
        print(
            f"   ※重複除外: {len(screened_stocks)}件 → {len(unique_stock_list)}件"
        )
        print(f"   ※並列処理で高速化（スレッド数: {max_workers}）")

        value_inflation_results = []
        value_success_count = 0
        value_no_data_count = 0  # データなしカウント

        # 並列処理（ThreadPoolExecutor）
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 全銘柄を並列実行用にサブミット
            futures = {
                executor.submit(
                    process_single_value_stock,
                    stock_dict,
                    stock_info_client,
                    screener,
                    logger,
                ): stock_dict
                for stock_dict in unique_stock_list
            }

            # 完了した順に結果を取得
            completed = 0
            for future in as_completed(futures):
                completed += 1

                # 進捗表示（50件ごと）
                if completed % 50 == 0:
                    logger.info(
                        f"インフレ対応バリュー株スクリーニング進捗: "
                        f"{completed}/{len(unique_stock_list)}件 "
                        f"(該当: {len(value_inflation_results)}件)"
                    )
                    print(
                        f"  進捗: {completed}/{len(unique_stock_list)}件 "
                        f"(該当: {len(value_inflation_results)}件)"
                    )

                try:
                    result = future.result()
                    if result:
                        value_success_count += 1
                        value_inflation_results.append(result.to_dict())
                    else:
                        value_no_data_count += 1
                except Exception as e:
                    value_no_data_count += 1
                    logger.error(f"バリュー株判定エラー: {e}", exc_info=True)

        logger.info(
            f"インフレ対応バリュー株スクリーニング完了: "
            f"情報取得成功={value_success_count}件, "
            f"データなし={value_no_data_count}件"
        )
        logger.info(
            f"インフレ対応バリュー株該当: {len(value_inflation_results)}件"
        )
        print(
            f"\n✅ バリュー株情報取得: 成功={value_success_count}件, "
            f"データなし={value_no_data_count}件"
        )
        print(
            f"✅ インフレ対応バリュー株該当: {len(value_inflation_results)}件"
        )

        # スクリーニング結果にバリュー株を追加
        screened_stocks.extend(value_inflation_results)

        # カテゴリ別に集計
        category_counts = {}
        for stock in screened_stocks:
            category = stock["category"]
            category_counts[category] = category_counts.get(category, 0) + 1

        print("\n--- スクリーニング結果サマリー ---")
        for category, count in category_counts.items():
            category_name = {
                "volume_surge": "出来高急増",
                "breakout": "ブレイクアウト",
                "bb_lower_bounce": "BB下限反転",
                "value_inflation_adjusted": "インフレ対応バリュー株",
            }.get(category, category)
            print(f"  {category_name}: {count}件")
        print("---\n")

    except Exception as e:
        logger.error(
            f"株価データ取得・スクリーニングに失敗: {e}", exc_info=True
        )
        print(f"❌ 株価データ取得・スクリーニングに失敗: {e}")
        sys.exit(1)

    # 7. レポート生成
    try:
        if screened_stocks:
            logger.info("レポート生成を開始します")
            print("⏳ レポート生成中...")

            generator = ReportGenerator(
                output_dir=str(config.report_output_dir), logger=logger
            )

            # 日次レポート生成
            today = date.today()
            report_date = today.strftime("%Y-%m-%d")
            generator.generate(screened_stocks, report_date)

            logger.info(f"✅ レポート生成完了: {len(screened_stocks)}件")
            print(f"✅ レポート生成完了: docs/{report_date}/")

            # 8. AI分析実行（Phase 2: オプション）
            if config.enable_ai_analysis:
                try:
                    import os
                    from pathlib import Path
                    from src.analysis.ai_analyzer import GeminiReportAnalyzer

                    api_key = os.getenv("GEMINI_API_KEY")
                    if api_key:
                        logger.info("AI分析を開始します")
                        print("⏳ AI分析実行中（Gemini API呼び出し）...")

                        analyzer = GeminiReportAnalyzer(api_key, logger)
                        analysis_result = analyzer.analyze(report_date=report_date)

                        # 結果を保存
                        save_path = Path(config.report_output_dir) / report_date / "ai_analysis.md"
                        save_path.write_text(analysis_result, encoding="utf-8")

                        logger.info(f"✅ AI分析結果を保存しました: {save_path}")
                        print(f"✅ AI分析完了: docs/{report_date}/ai_analysis.md")

                        # HTML出力生成
                        if generator.generate_ai_analysis_html(report_date):
                            print(f"✅ AI分析HTML生成完了: docs/{report_date}/ai_analysis.html")
                    else:
                        logger.warning("GEMINI_API_KEY が設定されていないため、AI分析をスキップしました。")
                        print("⚠️  GEMINI_API_KEY が設定されていません。AI分析をスキップします。")
                except Exception as e:
                    logger.error(f"AI分析中にエラーが発生しましたが、レポート生成は成功しました: {e}", exc_info=True)
                    print(f"⚠️  AI分析失敗（レポート生成は成功）: {e}")
                    # AI分析失敗時も全体処理は成功とする（sys.exitしない）
        else:
            logger.info("該当銘柄なし: レポート生成をスキップ")
            print("ℹ️  該当銘柄なし: レポート生成をスキップ")

    except Exception as e:
        logger.error(f"レポート生成に失敗: {e}", exc_info=True)
        print(f"❌ レポート生成に失敗: {e}")
        sys.exit(1)

    # 9. 統計情報
    elapsed_time = time.time() - start_time
    logger.info("=" * 60)
    logger.info(f"処理完了: 所要時間 {elapsed_time:.1f}秒")
    logger.info("=" * 60)

    print("\n" + "=" * 60)
    print(f"✅ 全処理完了 (所要時間: {elapsed_time:.1f}秒)")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
