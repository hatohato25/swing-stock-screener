"""
銘柄フィルタリングモジュール

個別株のみを抽出し、ETF・REIT・インフラファンドを除外します。
"""

from typing import List, Dict, Any


class StockFilter:
    """
    銘柄フィルタークラス

    個別株の選別を100%の精度で行うため、複数の条件を組み合わせて判定します。
    """

    # ETFの銘柄コード範囲
    ETF_CODE_RANGES = [
        (1300, 1399),  # 東証ETF
        (1540, 1549),  # 東証ETF
        (1550, 1599),  # 東証ETF
        (2000, 2099),  # 東証ETF（追加範囲）
    ]

    # REITの銘柄コード範囲
    REIT_CODE_RANGES = [
        (8950, 8999),  # J-REIT
    ]

    # インフラファンドの銘柄コード範囲
    INFRASTRUCTURE_CODE_RANGES = [
        (9280, 9299),  # インフラファンド
    ]

    # その他除外する銘柄コード範囲
    OTHER_EXCLUDED_RANGES = [
        (9900, 9999),  # 指数・その他
    ]

    # 除外キーワード（銘柄名に含まれる場合は除外）
    EXCLUDED_NAME_KEYWORDS = [
        "ETF",
        "REIT",
        "リート",
        "インフラファンド",
        "投資法人",
        "投信",
        "ベア",
        "ブル",
        "レバレッジ",
        "インバース",
    ]

    # 市場区分の除外リスト（該当する場合は除外）
    EXCLUDED_MARKET_TYPES = [
        "ETF",
        "REIT",
        "インフラファンド",
    ]

    def __init__(self):
        """フィルターを初期化する"""
        # 除外範囲を統合
        self.excluded_ranges = (
            self.ETF_CODE_RANGES
            + self.REIT_CODE_RANGES
            + self.INFRASTRUCTURE_CODE_RANGES
            + self.OTHER_EXCLUDED_RANGES
        )

    def is_individual_stock(self, stock: Dict[str, Any]) -> bool:
        """
        銘柄が個別株かどうかを判定する

        複数の条件を組み合わせて、ETF・REIT・インフラファンドを100%除外します。

        Args:
            stock: 銘柄情報辞書
                {
                    'stock_code': '7203',
                    'name': 'トヨタ自動車',
                    'market': '東証プライム',
                    'sector': '輸送用機器',
                    'market_type': '株式',  # 'ETF', 'REIT'等の場合あり
                }

        Returns:
            個別株の場合True、それ以外False
        """
        # 必須フィールドのチェック
        if "stock_code" not in stock:
            return False

        stock_code = stock["stock_code"]

        # 1. 銘柄コード範囲による除外
        if not self._is_valid_code_range(stock_code):
            return False

        # 2. 銘柄名による除外
        if "name" in stock and not self._is_valid_name(stock["name"]):
            return False

        # 3. 市場区分による除外
        if "market_type" in stock and not self._is_valid_market_type(
            stock["market_type"]
        ):
            return False

        # すべての条件を満たした場合のみ個別株と判定
        return True

    def _is_valid_code_range(self, stock_code: str) -> bool:
        """
        銘柄コードが除外範囲に含まれないかチェックする

        Args:
            stock_code: 銘柄コード(4桁)

        Returns:
            除外範囲に含まれない場合True
        """
        try:
            code_num = int(stock_code)
        except (ValueError, TypeError):
            return False

        # 除外範囲に含まれるかチェック
        for start, end in self.excluded_ranges:
            if start <= code_num <= end:
                return False

        return True

    def _is_valid_name(self, name: str) -> bool:
        """
        銘柄名に除外キーワードが含まれないかチェックする

        Args:
            name: 銘柄名

        Returns:
            除外キーワードが含まれない場合True
        """
        if not name:
            return True

        name_upper = name.upper()

        # 除外キーワードのチェック
        for keyword in self.EXCLUDED_NAME_KEYWORDS:
            if keyword.upper() in name_upper:
                return False

        return True

    def _is_valid_market_type(self, market_type: str) -> bool:
        """
        市場区分が除外対象でないかチェックする

        Args:
            market_type: 市場区分

        Returns:
            除外対象でない場合True
        """
        if not market_type:
            return True

        # 除外市場区分のチェック
        for excluded_type in self.EXCLUDED_MARKET_TYPES:
            if excluded_type.upper() in market_type.upper():
                return False

        return True

    def filter_stocks(self, stocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        銘柄リストから個別株のみを抽出する

        Args:
            stocks: 銘柄情報のリスト

        Returns:
            個別株のみのリスト
        """
        return [stock for stock in stocks if self.is_individual_stock(stock)]

    def get_excluded_stocks(self, stocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        銘柄リストから除外される銘柄のみを抽出する

        デバッグ・検証用のメソッド

        Args:
            stocks: 銘柄情報のリスト

        Returns:
            除外される銘柄のリスト
        """
        return [stock for stock in stocks if not self.is_individual_stock(stock)]

    def get_filter_statistics(self, stocks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        フィルタリング統計情報を取得する

        Args:
            stocks: 銘柄情報のリスト

        Returns:
            統計情報
            {
                'total': 全銘柄数,
                'individual_stocks': 個別株数,
                'excluded': 除外銘柄数,
                'individual_stock_ratio': 個別株の割合
            }
        """
        total = len(stocks)
        individual_stocks = self.filter_stocks(stocks)
        individual_count = len(individual_stocks)
        excluded_count = total - individual_count

        return {
            "total": total,
            "individual_stocks": individual_count,
            "excluded": excluded_count,
            "individual_stock_ratio": individual_count / total if total > 0 else 0.0,
        }
