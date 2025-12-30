"""
銘柄情報取得のテストスクリプト

バリュー株スクリーニングが失敗している原因を調査するため、
実際にAPI呼び出しを行って取得できるデータを確認します。
"""

import sys
from src.utils.config import Config
from src.utils.logger import Logger
from src.api.client import TachibanaAPIClient
from src.api.stock_info import StockInfoClient

def main():
    """メイン処理"""
    # 設定読み込み
    config = Config()

    # ログ初期化（DEBUGレベル）
    logger = Logger(log_dir="data/logs", name="test-stock-info")
    logger.set_level("DEBUG")

    # APIクライアント初期化
    api_client = TachibanaAPIClient(config, logger)

    # 銘柄情報クライアント初期化
    stock_info_client = StockInfoClient(
        api_client.auth_manager,
        api_client.rate_limiter,
        logger
    )

    # テスト対象銘柄（代表的な銘柄をいくつか）
    test_codes = [
        "7203",  # トヨタ自動車
        "9984",  # ソフトバンクグループ
        "6758",  # ソニーグループ
        "6861",  # キーエンス
        "8306",  # 三菱UFJ
    ]

    print("\n" + "=" * 60)
    print("銘柄情報取得テスト")
    print("=" * 60 + "\n")

    for code in test_codes:
        print(f"\n--- 銘柄コード: {code} ---")
        stock_info = stock_info_client.get_stock_info(issue_code=code)

        if stock_info:
            print("✅ 取得成功:")
            print(f"  PER: {stock_info.get('per')}")
            print(f"  PBR: {stock_info.get('pbr')}")
            print(f"  配当利回り: {stock_info.get('dividend_yield')}")
            print(f"  ROE: {stock_info.get('roe')}")
        else:
            print("❌ 取得失敗: データなし")

    print("\n" + "=" * 60)
    print("テスト完了")
    print("=" * 60)

if __name__ == "__main__":
    sys.exit(main())
