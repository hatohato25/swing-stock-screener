#!/usr/bin/env python3
"""
立花証券API株価データ解析テスト

取得した株価データの構造を解析する
"""

import json
import requests
from src.utils.config import Config
from src.utils.logger import Logger
from src.api.auth import AuthManager

# ロガー初期化
logger = Logger(log_dir="data/logs")


def test_parse_price_data():
    """株価データ解析テストを実行"""
    logger.info("=== 株価データ解析テスト開始 ===")

    try:
        # 認証
        config = Config()
        auth_manager = AuthManager(config)
        auth_manager.login()

        # 株価データ取得（トヨタ自動車: 7203）
        issue_code = "7203"
        market_code = "00"

        request_params = {
            "p_no": auth_manager.get_next_p_no(),
            "p_sd_date": auth_manager._format_p_sd_date(),
            "sCLMID": "CLMMfdsGetMarketPriceHistory",
            "sIssueCode": issue_code,
            "sSizyouC": market_code,
            "sJsonOfmt": "5",
        }

        url = (
            f"{auth_manager.get_virtual_url_price()}"
            f"?{json.dumps(request_params)}"
        )
        response = requests.get(url, timeout=30)
        text = response.content.decode("shift-jis", errors="ignore")
        data = json.loads(text)

        # データ構造を解析
        logger.info("=== データ構造 ===")
        logger.info(f"  sCLMID: {data.get('sCLMID')}")
        logger.info(f"  sIssueCode: {data.get('sIssueCode')}")
        logger.info(f"  sSizyouC: {data.get('sSizyouC')}")

        # 株価履歴配列を取得
        history = data.get("aCLMMfdsMarketPriceHistory", [])
        logger.info(f"  データ件数: {len(history)}件")

        if history:
            # 最初の3件を表示
            logger.info("\n=== 最初の3件のデータ ===")
            for i, record in enumerate(history[:3], 1):
                logger.info(f"\n  [{i}件目]")
                logger.info(f"    日付(sDate): {record.get('sDate')}")
                logger.info(f"    始値(pDOP): {record.get('pDOP')}")
                logger.info(f"    高値(pDHP): {record.get('pDHP')}")
                logger.info(f"    安値(pDLP): {record.get('pDLP')}")
                logger.info(f"    終値(pDPP): {record.get('pDPP')}")
                logger.info(f"    出来高(pDV): {record.get('pDV')}")

            # 最後の3件を表示（最新データ）
            logger.info("\n=== 最後の3件のデータ（最新） ===")
            for i, record in enumerate(history[-3:], len(history) - 2):
                logger.info(f"\n  [{i}件目]")
                logger.info(f"    日付(sDate): {record.get('sDate')}")
                logger.info(f"    始値(pDOP): {record.get('pDOP')}")
                logger.info(f"    高値(pDHP): {record.get('pDHP')}")
                logger.info(f"    安値(pDLP): {record.get('pDLP')}")
                logger.info(f"    終値(pDPP): {record.get('pDPP')}")
                logger.info(f"    出来高(pDV): {record.get('pDV')}")

            # データのキーを確認
            logger.info("\n=== 利用可能なフィールド ===")
            first_record = history[0]
            for key in sorted(first_record.keys()):
                logger.info(f"    {key}: {first_record[key]}")

        logger.info("\n=== 株価データ解析テスト成功 ===")
        return True

    except Exception as e:
        logger.error(f"テストエラー: {type(e).__name__} - {str(e)}")
        import traceback

        logger.error(f"スタックトレース:\n{traceback.format_exc()}")
        return False


if __name__ == "__main__":
    success = test_parse_price_data()
    exit(0 if success else 1)
