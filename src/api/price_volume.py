"""
株価・出来高情報取得APIモジュール

立花証券APIから株価と出来高データを取得します。
"""

from typing import List, Dict, Any, Optional
from datetime import date, timedelta
from src.api.client import TachibanaAPIClient


class PriceVolumeAPI:
    """株価・出来高情報取得API"""

    def __init__(self, client: TachibanaAPIClient):
        """
        株価・出来高APIを初期化する

        Args:
            client: APIクライアント
        """
        self.client = client

    def get_daily_ohlcv(
        self,
        stock_code: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> List[Dict[str, Any]]:
        """
        日次OHLCVデータ(始値・高値・安値・終値・出来高)を取得する

        Args:
            stock_code: 銘柄コード(4桁)
            start_date: 開始日(デフォルト: 90日前)
            end_date: 終了日(デフォルト: 本日)

        Returns:
            OHLCVデータのリスト
            [
                {
                    'date': '2025-11-20',
                    'open': 1500.0,
                    'high': 1550.0,
                    'low': 1480.0,
                    'close': 1520.0,
                    'volume': 1000000
                },
                ...
            ]
        """
        # デフォルト期間の設定
        if end_date is None:
            end_date = date.today()
        if start_date is None:
            start_date = end_date - timedelta(days=90)

        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }

        response = self.client.get(f"/stocks/{stock_code}/ohlcv", params=params)

        # レスポンス形式は実際のAPIに合わせて調整
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        elif isinstance(response, list):
            return response
        else:
            return []

    def get_latest_price(self, stock_code: str) -> Optional[Dict[str, Any]]:
        """
        最新の株価情報を取得する

        Args:
            stock_code: 銘柄コード(4桁)

        Returns:
            最新株価情報
            {
                'stock_code': '7203',
                'price': 1520.0,
                'change': 20.0,
                'change_percent': 1.33,
                'volume': 1000000,
                'timestamp': '2025-11-20T15:00:00'
            }
        """
        response = self.client.get(f"/stocks/{stock_code}/price")
        return response if response else None

    def get_volume_data(self, stock_code: str, days: int = 20) -> List[Dict[str, Any]]:
        """
        出来高データを取得する

        Args:
            stock_code: 銘柄コード(4桁)
            days: 取得日数

        Returns:
            出来高データのリスト
        """
        end_date = date.today()
        start_date = end_date - timedelta(days=days)

        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }

        response = self.client.get(f"/stocks/{stock_code}/volume", params=params)

        # レスポンス形式は実際のAPIに合わせて調整
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        elif isinstance(response, list):
            return response
        else:
            return []

    def get_historical_prices(
        self, stock_code: str, period: str = "3M"
    ) -> List[Dict[str, Any]]:
        """
        期間指定で過去の株価データを取得する

        Args:
            stock_code: 銘柄コード(4桁)
            period: 期間指定('1W', '1M', '3M', '6M', '1Y', '5Y')

        Returns:
            株価データのリスト
        """
        params = {"period": period}

        response = self.client.get(f"/stocks/{stock_code}/historical", params=params)

        # レスポンス形式は実際のAPIに合わせて調整
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        elif isinstance(response, list):
            return response
        else:
            return []

    def get_intraday_prices(
        self, stock_code: str, interval: str = "5m"
    ) -> List[Dict[str, Any]]:
        """
        当日の分足データを取得する

        Args:
            stock_code: 銘柄コード(4桁)
            interval: 時間間隔('1m', '5m', '15m', '30m', '1h')

        Returns:
            分足データのリスト
        """
        params = {"interval": interval}

        response = self.client.get(f"/stocks/{stock_code}/intraday", params=params)

        # レスポンス形式は実際のAPIに合わせて調整
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        elif isinstance(response, list):
            return response
        else:
            return []
