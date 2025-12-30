"""
バリュー株API動作確認スクリプト

テクニカルスクリーニングで検出された銘柄のうち、
数銘柄でPER/PBR/配当利回りの取得を試みます。
"""

import sys
import json
from src.utils.config import Config
from src.utils.logger import Logger
from src.api.client import TachibanaAPIClient
from src.api.stock_info import StockInfoClient

def main():
    """メイン処理"""
    # 設定とロガーを初期化
    config = Config()
    logger = Logger(log_dir="data/logs", name="test")
    logger.set_level("DEBUG")  # DEBUGレベルに設定

    # APIクライアント初期化（自動的にログイン処理が実行される）
    print("⏳ APIクライアント初期化中（ログイン処理含む）...")
    try:
        api_client = TachibanaAPIClient(config, logger)
        print("✅ APIクライアント初期化成功")
    except Exception as e:
        print(f"❌ APIクライアント初期化に失敗: {e}")
        sys.exit(1)

    # StockInfoClient初期化
    stock_info_client = StockInfoClient(
        api_client.auth_manager,
        api_client.rate_limiter,
        logger
    )

    # テスト用銘柄コード（テクニカルスクリーニングで検出された銘柄から）
    test_codes = [
        "1711",  # 三井E&S
        "1717",  # 明豊ファシリティワークス
        "1798",  # 守谷商会
        "3777",  # 環境フレンドリーHD
        "4199",  # ワンダープラネット
    ]

    print(f"\n⏳ {len(test_codes)}銘柄のPER/PBR/配当利回りを取得します...\n")

    for code in test_codes:
        print(f"--- 銘柄コード: {code} ---")

        # 銘柄情報取得
        stock_info = stock_info_client.get_stock_info(issue_code=code)

        if stock_info is None:
            print(f"❌ データなし")
        else:
            print(f"✅ データ取得成功:")
            print(f"  PER: {stock_info.get('per')} 倍")
            print(f"  PBR: {stock_info.get('pbr')} 倍")
            print(f"  配当利回り: {stock_info.get('dividend_yield')} %")
            print(f"  ROE: {stock_info.get('roe')} %")

        print()

    print("\n✅ テスト完了")

if __name__ == "__main__":
    main()
