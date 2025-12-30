#!/usr/bin/env python3
"""
立花証券API接続テスト（Phase 1: 緊急対応）

固定銘柄コード（7203=トヨタ自動車）で株価データ取得をテストする
"""

import json
import requests
from src.utils.config import Config
from src.utils.logger import Logger
from src.api.auth import AuthManager

# ロガー初期化
logger = Logger(log_dir="data/logs")


def test_api_connection():
    """API接続テストを実行"""
    logger.info("=== 立花証券API接続テスト開始 ===")

    try:
        # 1. 設定を読み込み
        logger.info("STEP 1: 設定読み込み")
        config = Config()
        logger.info(f"  環境: {config.environment}")
        logger.info(f"  認証URL: {config.auth_url}")

        # 2. 認証マネージャーを初期化（自動ログイン）
        logger.info("STEP 2: ログイン処理")
        auth_manager = AuthManager(config)
        auth_manager.login()
        logger.info("  ログイン成功")

        # 3. 株価データ取得テスト（トヨタ自動車: 7203）
        logger.info("STEP 3: 株価データ取得テスト（7203=トヨタ自動車）")
        issue_code = "7203"
        market_code = "00"  # 東証

        # CLMMfdsGetMarketPriceHistoryリクエストを構築
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
        logger.info(f"  リクエストURL: {url[:100]}...")
        params_str = json.dumps(request_params, ensure_ascii=False)
        logger.info(f"  リクエストパラメータ: {params_str}")

        # HTTPリクエスト実行
        logger.info("  HTTPリクエスト実行中...")
        response = requests.get(url, timeout=30)
        logger.info(f"  HTTPステータス: {response.status_code}")

        # レスポンスをデコード（Shift-JIS）
        try:
            text = response.content.decode("shift-jis", errors="ignore")
            logger.info(f"  レスポンスサイズ: {len(text)} 文字")
            logger.info(f"  レスポンス（先頭500文字）:\n{text[:500]}")

            # JSONとしてパース
            data = json.loads(text)
            logger.info("  JSONパース成功")

            # p_errnoをチェック
            p_errno = int(data.get("p_errno", -1))
            logger.info(f"  p_errno: {p_errno}")

            if p_errno != 0:
                logger.error(f"  API通信エラー: p_errno={p_errno}")
                return False

            # 結果コードをチェック（存在する場合のみ）
            result_code = data.get("sResultCode")
            result_text = data.get("sResultText", "")

            if result_code is not None:
                logger.info(f"  結果コード: {result_code} - {result_text}")
                if result_code != "0" and result_code != "":
                    logger.error(f"  APIエラー: [{result_code}] {result_text}")
                    return False
            else:
                logger.info("  結果コード: （レスポンスに含まれず）")

            # 株価データを表示
            logger.info("  株価データ取得成功:")
            logger.info(f"    銘柄コード: {data.get('sIssueCode', 'N/A')}")
            logger.info(f"    銘柄名: {data.get('sIssueName', 'N/A')}")
            logger.info(f"    市場コード: {data.get('sSizyouC', 'N/A')}")

            # レスポンス全体を出力（デバッグ用）
            full_response = json.dumps(data, ensure_ascii=False, indent=2)
            logger.debug(f"  レスポンス全体:\n{full_response}")

            logger.info("=== API接続テスト成功 ===")
            return True

        except json.JSONDecodeError as e:
            logger.error(f"  JSONパースエラー: {e}")
            logger.error(f"  レスポンステキスト:\n{text}")
            return False

        except UnicodeDecodeError as e:
            logger.error(f"  デコードエラー: {e}")
            return False

    except Exception as e:
        logger.error(f"テストエラー: {type(e).__name__} - {str(e)}")
        import traceback

        logger.error(f"スタックトレース:\n{traceback.format_exc()}")
        return False


if __name__ == "__main__":
    success = test_api_connection()
    exit(0 if success else 1)
