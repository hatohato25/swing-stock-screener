"""
株価データ取得モジュール

立花証券APIから株価データ（日足）を取得します。
GitHubサンプル（e_api_get_histrical_price_daily_tel.py）を参考に実装
"""

import json
import requests
from typing import Dict, Optional, Any
from src.utils.logger import Logger
from src.api.auth import AuthManager
from src.api.rate_limiter import RateLimiter


class StockPriceClient:
    """立花証券APIから株価データを取得するクライアント"""

    def __init__(self, auth_manager: AuthManager, logger: Logger):
        """
        株価データクライアントを初期化する

        Args:
            auth_manager: 認証マネージャー
            logger: ロガーオブジェクト
        """
        self.auth_manager = auth_manager
        self.logger = logger
        self.rate_limiter = RateLimiter(max_requests=10, time_window=1.0)

    def get_daily_price(
        self, issue_code: str, market_code: str = "00"
    ) -> Optional[Dict[str, Any]]:
        """
        日足株価データを取得

        API: CLMMfdsGetMarketPriceHistory
        エンドポイント: sUrlPrice（仮想URL）

        Args:
            issue_code: 銘柄コード（4桁または5桁）
            market_code: 市場コード（"00"=東証、デフォルト"00"）

        Returns:
            株価データ（辞書）または None（エラー時）
            成功時の辞書構造:
            {
                "p_errno": "0",
                "sResultCode": "0",
                "aDailyStockPrice_FLG_NoData": "0",
                "aDailyStockPrice": [
                    {
                        "sDate": "20251224",  # 日付（YYYYMMDD）
                        "pDOP": "3418",       # 始値
                        "pDHP": "3420",       # 高値
                        "pDLP": "3353",       # 安値
                        "pDPP": "3353",       # 終値
                        "pDV": "12845800",    # 出来高
                        "pDOPxK": "3418",     # 始値（分割調整済み）
                        "pDHPxK": "3420",     # 高値（分割調整済み）
                        "pDLPxK": "3353",     # 安値（分割調整済み）
                        "pDPPxK": "3353",     # 終値（分割調整済み）
                        "pDVxK": "12845800",  # 出来高（分割調整済み）
                        ...
                    },
                    ...
                ]
            }

        Raises:
            None（エラー時はNoneを返す）

        Note:
            - レート制限（10 req/sec）を自動的に守る
            - エラー時はログ出力してNoneを返す
            - 過去約3年分のデータを取得
        """
        # レート制限を遵守
        self.rate_limiter.acquire()

        # リクエストパラメータを構築
        request_params = {
            "p_no": self.auth_manager.get_next_p_no(),
            "p_sd_date": self.auth_manager._format_p_sd_date(),
            "sCLMID": "CLMMfdsGetMarketPriceHistory",
            "sIssueCode": issue_code,
            "sSizyouC": market_code,
            "sJsonOfmt": "5",  # ブラウザ見やすい形式 + 引数項目名称
        }

        # URLを構築（仮想URL Price + JSONパラメータ）
        base_url = self.auth_manager.get_virtual_url_price()
        url = f"{base_url}?{json.dumps(request_params)}"

        # デバッグログを削減（パフォーマンス向上）
        # self.logger.debug(f"株価取得リクエスト: {issue_code}")

        try:
            # API呼び出し
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # Shift-JISでデコード（立花証券APIの仕様）
            text = response.content.decode("shift-jis", errors="ignore")
            data = json.loads(text)

            # p_errnoチェック（通信エラー）
            p_errno = int(data.get("p_errno", -1))
            if p_errno != 0:
                self.logger.warning(
                    f"株価取得エラー ({issue_code}): p_errno={p_errno}, "
                    f"p_err={data.get('p_err', 'Unknown')}"
                )
                return None

            # データなしフラグチェック
            # aCLMMfdsMarketPriceHistoryが存在しない場合、データなし
            stock_prices = data.get("aCLMMfdsMarketPriceHistory")
            if stock_prices is None:
                self.logger.debug(f"株価データなし: {issue_code}")
                return None

            # データが空の場合
            if not stock_prices or len(stock_prices) == 0:
                # デバッグログを削減（パフォーマンス向上）
                # self.logger.debug(f"株価データが空: {issue_code}")
                return None

            # デバッグログを削減（パフォーマンス向上）
            # self.logger.debug(
            #     f"株価取得成功: {issue_code}（{len(stock_prices)}日分）"
            # )
            return data

        except requests.exceptions.Timeout:
            self.logger.warning(f"株価取得タイムアウト: {issue_code}")
            return None

        except requests.exceptions.HTTPError as e:
            self.logger.warning(f"株価取得HTTPエラー ({issue_code}): {e}")
            return None

        except json.JSONDecodeError as e:
            self.logger.error(f"株価取得JSONパースエラー ({issue_code}): {e}")
            return None

        except Exception as e:
            self.logger.error(
                f"株価取得エラー ({issue_code}): {e}", exc_info=True
            )
            return None
