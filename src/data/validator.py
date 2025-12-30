"""
データバリデーションモジュール

APIから取得したデータの妥当性を検証します。
"""

from typing import Dict, Any, List
from datetime import datetime, date
import re


class ValidationError(Exception):
    """データバリデーションエラー"""

    pass


class DataValidator:
    """データ検証クラス"""

    # 銘柄コードのパターン(4桁の数字)
    STOCK_CODE_PATTERN = re.compile(r"^\d{4}$")

    @staticmethod
    def validate_stock_code(stock_code: str) -> bool:
        """
        銘柄コードの妥当性を検証する

        Args:
            stock_code: 銘柄コード

        Returns:
            妥当な場合True

        Raises:
            ValidationError: 銘柄コードが不正な場合
        """
        if not stock_code or not isinstance(stock_code, str):
            raise ValidationError("銘柄コードが指定されていません")

        if not DataValidator.STOCK_CODE_PATTERN.match(stock_code):
            raise ValidationError(f"不正な銘柄コード形式: {stock_code}")

        return True

    @staticmethod
    def validate_stock_info(stock_info: Dict[str, Any]) -> bool:
        """
        銘柄情報の妥当性を検証する

        Args:
            stock_info: 銘柄情報辞書

        Returns:
            妥当な場合True

        Raises:
            ValidationError: 銘柄情報が不正な場合
        """
        if not isinstance(stock_info, dict):
            raise ValidationError("銘柄情報が辞書形式ではありません")

        # 必須フィールドのチェック
        required_fields = ["stock_code", "name"]
        missing_fields = [field for field in required_fields if field not in stock_info]

        if missing_fields:
            raise ValidationError(
                f"必須フィールドが不足しています: {', '.join(missing_fields)}"
            )

        # 銘柄コードの検証
        DataValidator.validate_stock_code(stock_info["stock_code"])

        # 銘柄名の検証
        if not stock_info["name"] or not isinstance(stock_info["name"], str):
            raise ValidationError("銘柄名が不正です")

        return True

    @staticmethod
    def validate_ohlcv_data(ohlcv: Dict[str, Any]) -> bool:
        """
        OHLCVデータ(始値・高値・安値・終値・出来高)の妥当性を検証する

        Args:
            ohlcv: OHLCVデータ辞書

        Returns:
            妥当な場合True

        Raises:
            ValidationError: データが不正な場合
        """
        if not isinstance(ohlcv, dict):
            raise ValidationError("OHLCVデータが辞書形式ではありません")

        # 必須フィールドのチェック
        required_fields = ["date", "open", "high", "low", "close", "volume"]
        missing_fields = [field for field in required_fields if field not in ohlcv]

        if missing_fields:
            raise ValidationError(
                f"必須フィールドが不足しています: {', '.join(missing_fields)}"
            )

        # 日付の検証
        try:
            if isinstance(ohlcv["date"], str):
                datetime.strptime(ohlcv["date"], "%Y-%m-%d")
            elif not isinstance(ohlcv["date"], (date, datetime)):
                raise ValidationError("日付形式が不正です")
        except ValueError:
            raise ValidationError(f"日付形式が不正です: {ohlcv['date']}")

        # 価格データの検証
        price_fields = ["open", "high", "low", "close"]
        for field in price_fields:
            value = ohlcv[field]
            if not isinstance(value, (int, float)) or value < 0:
                raise ValidationError(f"{field}の値が不正です: {value}")

        # 高値・安値の関係性チェック
        if ohlcv["high"] < ohlcv["low"]:
            raise ValidationError(
                f"高値({ohlcv['high']})が安値({ohlcv['low']})より低いです"
            )

        # 終値が高値・安値の範囲内かチェック
        if not (ohlcv["low"] <= ohlcv["close"] <= ohlcv["high"]):
            raise ValidationError(
                f"終値({ohlcv['close']})が高値({ohlcv['high']})・安値({ohlcv['low']})の範囲外です"
            )

        # 始値が高値・安値の範囲内かチェック
        if not (ohlcv["low"] <= ohlcv["open"] <= ohlcv["high"]):
            raise ValidationError(
                f"始値({ohlcv['open']})が高値({ohlcv['high']})・安値({ohlcv['low']})の範囲外です"
            )

        # 出来高の検証
        volume = ohlcv["volume"]
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValidationError(f"出来高の値が不正です: {volume}")

        return True

    @staticmethod
    def validate_ohlcv_list(ohlcv_list: List[Dict[str, Any]]) -> bool:
        """
        OHLCVデータのリストを検証する

        Args:
            ohlcv_list: OHLCVデータのリスト

        Returns:
            妥当な場合True

        Raises:
            ValidationError: データが不正な場合
        """
        if not isinstance(ohlcv_list, list):
            raise ValidationError("OHLCVデータがリスト形式ではありません")

        if len(ohlcv_list) == 0:
            raise ValidationError("OHLCVデータが空です")

        # 各要素を検証
        for i, ohlcv in enumerate(ohlcv_list):
            try:
                DataValidator.validate_ohlcv_data(ohlcv)
            except ValidationError as e:
                raise ValidationError(f"インデックス{i}のデータが不正です: {str(e)}")

        return True

    @staticmethod
    def validate_price_data(price_data: Dict[str, Any]) -> bool:
        """
        株価データの妥当性を検証する

        Args:
            price_data: 株価データ辞書

        Returns:
            妥当な場合True

        Raises:
            ValidationError: データが不正な場合
        """
        if not isinstance(price_data, dict):
            raise ValidationError("株価データが辞書形式ではありません")

        # 必須フィールドのチェック
        required_fields = ["stock_code", "price"]
        missing_fields = [field for field in required_fields if field not in price_data]

        if missing_fields:
            raise ValidationError(
                f"必須フィールドが不足しています: {', '.join(missing_fields)}"
            )

        # 銘柄コードの検証
        DataValidator.validate_stock_code(price_data["stock_code"])

        # 価格の検証
        price = price_data["price"]
        if not isinstance(price, (int, float)) or price < 0:
            raise ValidationError(f"価格の値が不正です: {price}")

        # 変動額・変動率の検証(存在する場合)
        if "change" in price_data:
            change = price_data["change"]
            if not isinstance(change, (int, float)):
                raise ValidationError(f"変動額の値が不正です: {change}")

        if "change_percent" in price_data:
            change_percent = price_data["change_percent"]
            if not isinstance(change_percent, (int, float)):
                raise ValidationError(f"変動率の値が不正です: {change_percent}")

        return True

    @staticmethod
    def is_valid_date_range(start_date: date, end_date: date) -> bool:
        """
        日付範囲の妥当性を検証する

        Args:
            start_date: 開始日
            end_date: 終了日

        Returns:
            妥当な場合True

        Raises:
            ValidationError: 日付範囲が不正な場合
        """
        if not isinstance(start_date, date):
            raise ValidationError("開始日が日付型ではありません")

        if not isinstance(end_date, date):
            raise ValidationError("終了日が日付型ではありません")

        if start_date > end_date:
            raise ValidationError(f"開始日({start_date})が終了日({end_date})より後です")

        # 未来の日付チェック
        today = date.today()
        if end_date > today:
            raise ValidationError(f"終了日({end_date})が未来の日付です")

        return True
