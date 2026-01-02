#!/usr/bin/env python3
"""
スクリーニングレポートのAI分析を実行するCLIスクリプト

使用方法:
    # 最新レポートを分析
    python3 -m src.analysis.analyze_report

    # 特定日付のレポートを分析
    python3 -m src.analysis.analyze_report --date 2025-12-30

    # 結果をファイルに保存
    python3 -m src.analysis.analyze_report --save
"""

import argparse
import os
import sys
from pathlib import Path

from src.analysis.ai_analyzer import GeminiReportAnalyzer
from src.utils.logger import Logger
from src.utils.config import Config


def main() -> int:
    """
    メイン処理

    1. コマンドライン引数のパース
    2. 設定とロガーの初期化
    3. APIキーの取得
    4. AI分析の実行
    5. 結果の表示とオプションでファイル保存

    Returns:
        終了コード（0: 正常終了、1: エラー）
    """
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(
        description="スクリーニングレポートのAI分析を実行します。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 最新レポートを分析
  python3 -m src.analysis.analyze_report

  # 特定日付のレポートを分析
  python3 -m src.analysis.analyze_report --date 2025-12-30

  # 結果をファイルに保存
  python3 -m src.analysis.analyze_report --save
        """
    )
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="分析対象のレポート日付（YYYY-MM-DD形式）。指定しない場合は最新レポート。"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="分析結果をファイル（ai_analysis.md）に保存する。"
    )

    args = parser.parse_args()

    # 設定とロガーの初期化
    try:
        config = Config()
    except ValueError as e:
        print(f"エラー: 設定の初期化に失敗しました: {e}")
        return 1

    logger = Logger(log_dir="data/logs", name="ai-analyzer")

    # APIキーの取得
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("環境変数 GEMINI_API_KEY が設定されていません。")
        print("\nエラー: 環境変数 GEMINI_API_KEY が設定されていません。")
        print("\n設定方法:")
        print("  1. .envファイルに以下を追加:")
        print("     GEMINI_API_KEY=your_gemini_api_key_here")
        print("\n  2. またはターミナルで以下を実行:")
        print("     export GEMINI_API_KEY=your_gemini_api_key_here")
        print("\nAPIキーの取得方法:")
        print("  https://aistudio.google.com/app/apikey にアクセスし、APIキーを作成してください。")
        return 1

    try:
        # AI分析の実行
        logger.info("=== AI分析を開始します ===")
        analyzer = GeminiReportAnalyzer(api_key, logger)
        analysis_result = analyzer.analyze(report_date=args.date)

        # 結果の表示
        print("\n" + "="*80)
        print("AI分析結果")
        print("="*80 + "\n")
        print(analysis_result)
        print("\n" + "="*80)

        # ファイル保存（オプション）
        if args.save:
            # 日付指定時とNone時の分岐
            if args.date:
                save_path = Path(f"docs/{args.date}/ai_analysis.md")
            else:
                # 最新日付を再取得
                report_date, _ = analyzer.read_latest_report()
                save_path = Path(f"docs/{report_date}/ai_analysis.md")

            # ディレクトリが存在しない場合は作成
            save_path.parent.mkdir(parents=True, exist_ok=True)

            # ファイルに保存
            save_path.write_text(analysis_result, encoding="utf-8")

            logger.info(f"分析結果を保存しました: {save_path}")
            print(f"\n✅ 分析結果を保存しました: {save_path}")

        logger.info("=== AI分析が正常に完了しました ===")
        return 0

    except FileNotFoundError as e:
        logger.error(f"レポートファイルが見つかりません: {e}")
        print(f"\nエラー: レポートファイルが見つかりません: {e}")
        print("\n確認事項:")
        print("  - docs/YYYY-MM-DD/ ディレクトリが存在するか")
        print("  - README.md ファイルが存在するか")
        return 1

    except ValueError as e:
        logger.error(f"AI分析に失敗しました: {e}")
        print(f"\nエラー: AI分析に失敗しました: {e}")
        print("\n考えられる原因:")
        print("  - APIキーが無効または期限切れ")
        print("  - Gemini APIの制限超過")
        print("  - 日付形式が不正（YYYY-MM-DD形式で指定してください）")
        return 1

    except TimeoutError as e:
        logger.error(f"タイムアウト: {e}")
        print(f"\nエラー: {e}")
        print("\n考えられる原因:")
        print("  - ネットワーク接続が不安定")
        print("  - Gemini APIサーバーが混雑している")
        print("\n対処方法:")
        print("  - 時間をおいて再実行してください")
        return 1

    except Exception as e:
        logger.error(f"予期しないエラーが発生しました: {e}", exc_info=True)
        print(f"\nエラー: 予期しないエラーが発生しました: {e}")
        print("\n詳細はログファイルを確認してください: data/logs/")
        return 1


if __name__ == "__main__":
    sys.exit(main())
