"""
データ取得統合モジュール

API呼び出し、データ検証、フィルタリングを統合して管理します。
"""

from typing import List, Dict, Any, Optional
from datetime import date
from src.api.client import TachibanaAPIClient
from src.api.stock_info import StockInfoAPI
from src.api.price_volume import PriceVolumeAPI
from src.data.validator import DataValidator, ValidationError
from src.data.filter import StockFilter
from src.utils.logger import Logger
from src.utils.calendar import JapaneseCalendar


class DataFetcher:
    """
    データ取得統合クラス

    API呼び出し、検証、フィルタリングを組み合わせて、
    個別株の株価・出来高データを取得します。
    """

    def __init__(
        self,
        api_client: TachibanaAPIClient,
        logger: Logger,
        calendar: Optional[JapaneseCalendar] = None,
    ):
        """
        データフェッチャーを初期化する

        Args:
            api_client: APIクライアント
            logger: ロガー
            calendar: カレンダー（祝日判定用）
        """
        self.api_client = api_client
        self.logger = logger
        self.calendar = calendar or JapaneseCalendar()

        # APIモジュール
        self.stock_info_api = StockInfoAPI(api_client)
        self.price_volume_api = PriceVolumeAPI(api_client)

        # データ検証・フィルタリング
        self.validator = DataValidator()
        self.filter = StockFilter()

    def fetch_individual_stocks(self) -> List[Dict[str, Any]]:
        """
        個別株のリストを取得する

        ETF・REIT・インフラファンドを除外した個別株のみを返します。

        Returns:
            個別株情報のリスト

        Raises:
            APIError: API呼び出しに失敗した場合
        """
        self.logger.info("銘柄リストの取得を開始")

        try:
            # 全銘柄を取得
            all_stocks = self.stock_info_api.get_all_stocks()
            self.logger.info(f"全銘柄数: {len(all_stocks)}")

            # 個別株のみをフィルタリング
            individual_stocks = self.filter.filter_stocks(all_stocks)
            self.logger.info(f"個別株数: {len(individual_stocks)}")

            # フィルタリング統計を出力
            stats = self.filter.get_filter_statistics(all_stocks)
            self.logger.info(
                f"フィルタリング結果: "
                f"除外={stats['excluded']}銘柄, "
                f"個別株比率={stats['individual_stock_ratio']:.1%}"
            )

            return individual_stocks

        except Exception as e:
            self.logger.error(f"銘柄リストの取得に失敗: {str(e)}", exc_info=True)
            raise

    def fetch_stock_price_data(
        self,
        stock_code: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> List[Dict[str, Any]]:
        """
        指定銘柄の株価データを取得する

        Args:
            stock_code: 銘柄コード
            start_date: 開始日
            end_date: 終了日

        Returns:
            OHLCVデータのリスト

        Raises:
            ValidationError: データ検証に失敗した場合
            APIError: API呼び出しに失敗した場合
        """
        # 銘柄コードの検証
        self.validator.validate_stock_code(stock_code)

        # 日付範囲の検証
        if start_date and end_date:
            self.validator.is_valid_date_range(start_date, end_date)

        try:
            # OHLCVデータを取得
            ohlcv_data = self.price_volume_api.get_daily_ohlcv(
                stock_code, start_date, end_date
            )

            if not ohlcv_data:
                self.logger.warning(
                    f"銘柄コード {stock_code} のデータが取得できませんでした"
                )
                return []

            # データ検証
            self.validator.validate_ohlcv_list(ohlcv_data)

            self.logger.debug(
                f"銘柄コード {stock_code} のデータ取得完了: {len(ohlcv_data)}件"
            )

            return ohlcv_data

        except ValidationError as e:
            self.logger.error(f"データ検証エラー（銘柄コード: {stock_code}）: {str(e)}")
            raise

        except Exception as e:
            self.logger.error(
                f"銘柄コード {stock_code} のデータ取得に失敗: {str(e)}", exc_info=True
            )
            raise

    def fetch_latest_prices(
        self, stock_codes: List[str]
    ) -> Dict[str, Optional[Dict[str, Any]]]:
        """
        複数銘柄の最新株価を一括取得する

        Args:
            stock_codes: 銘柄コードのリスト

        Returns:
            銘柄コードをキーとする最新株価データの辞書
            {
                '7203': {'price': 1520, 'change': 20, ...},
                '6758': {'price': 2340, 'change': -15, ...},
                ...
            }
        """
        result = {}

        self.logger.info(f"{len(stock_codes)}銘柄の最新株価を取得開始")

        for stock_code in stock_codes:
            try:
                # 銘柄コードの検証
                self.validator.validate_stock_code(stock_code)

                # 最新株価を取得
                price_data = self.price_volume_api.get_latest_price(stock_code)

                if price_data:
                    # データ検証
                    self.validator.validate_price_data(price_data)
                    result[stock_code] = price_data
                else:
                    result[stock_code] = None
                    self.logger.warning(
                        f"銘柄コード {stock_code} の株価データが取得できませんでした"
                    )

            except ValidationError as e:
                self.logger.error(
                    f"データ検証エラー（銘柄コード: {stock_code}）: {str(e)}"
                )
                result[stock_code] = None

            except Exception as e:
                self.logger.error(f"銘柄コード {stock_code} の株価取得に失敗: {str(e)}")
                result[stock_code] = None

        success_count = sum(1 for v in result.values() if v is not None)
        self.logger.info(f"最新株価取得完了: {success_count}/{len(stock_codes)}銘柄")

        return result

    def fetch_multiple_stocks_data(
        self,
        stock_codes: List[str],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        複数銘柄の株価データを一括取得する

        Args:
            stock_codes: 銘柄コードのリスト
            start_date: 開始日
            end_date: 終了日

        Returns:
            銘柄コードをキーとするOHLCVデータの辞書
        """
        result = {}

        self.logger.info(
            f"{len(stock_codes)}銘柄の株価データ取得を開始 "
            f"({start_date} - {end_date})"
        )

        success_count = 0
        error_count = 0

        for i, stock_code in enumerate(stock_codes, 1):
            try:
                ohlcv_data = self.fetch_stock_price_data(
                    stock_code, start_date, end_date
                )

                result[stock_code] = ohlcv_data
                success_count += 1

                # 進捗ログ（100銘柄ごと）
                if i % 100 == 0:
                    self.logger.info(f"進捗: {i}/{len(stock_codes)}銘柄処理完了")

            except Exception as e:
                self.logger.error(f"銘柄コード {stock_code} の処理に失敗: {str(e)}")
                result[stock_code] = []
                error_count += 1

        self.logger.info(
            f"株価データ取得完了: 成功={success_count}, 失敗={error_count}"
        )

        return result

    def is_trading_day(self, target_date: Optional[date] = None) -> bool:
        """
        指定日が取引日かどうかを判定する

        Args:
            target_date: 判定する日付（デフォルト: 本日）

        Returns:
            取引日の場合True
        """
        if target_date is None:
            target_date = date.today()

        return self.calendar.is_trading_day(target_date)

    def get_next_trading_day(self, base_date: Optional[date] = None) -> date:
        """
        次の取引日を取得する

        Args:
            base_date: 基準日（デフォルト: 本日）

        Returns:
            次の取引日
        """
        if base_date is None:
            base_date = date.today()

        return self.calendar.get_next_trading_day(base_date)

    def get_previous_trading_day(self, base_date: Optional[date] = None) -> date:
        """
        前の取引日を取得する

        Args:
            base_date: 基準日（デフォルト: 本日）

        Returns:
            前の取引日
        """
        if base_date is None:
            base_date = date.today()

        return self.calendar.get_previous_trading_day(base_date)
