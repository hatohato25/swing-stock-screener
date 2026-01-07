"""
銘柄フィルタリングモジュール

個別株のみを抽出するフィルタリング機能を提供します。
ETF、REIT、インフラファンド等を除外します。
"""

from typing import List, Dict, Any
from src.utils.logger import Logger


class StockFilter:
    """銘柄フィルタリングクラス"""

    # 除外する銘柄コード範囲
    EXCLUDED_CODE_RANGES = [
        (1300, 1699),  # ETF（1300番台〜1699番台）
        (2000, 2999),  # 投資信託（ETF/ETN、2000番台）
        (8950, 8999),  # REIT（8950番台〜8999番台）
        (9280, 9289),  # インフラファンド（9280番台〜9289番台）
    ]

    # 除外キーワード（銘柄名に含まれる場合除外）
    EXCLUDED_KEYWORDS = [
        "ETF",
        "ETN",  # 上場投資証券
        "REIT",
        "インフラファンド",
        "上場投信",
        "インフラ",
        "投資法人",
        "優先",
        "NZAM",  # 投信ブランド
        "MX",  # 投信ブランド（MXS等）
        "GX",  # 投信ブランド
        "iシェアーズ",  # 投信ブランド
        "ヘッジ有",  # 投資信託の特徴
        "インバース",  # インバース型ETF
        "レバレッジ",  # レバレッジ型ETF
        "ブル",  # ブル型ETF
        "ベア",  # ベア型ETF
        "配当貴族",  # 配当ETF
        "高配株",  # 高配当ETF
        "トップシェア",  # トップシェアETN
        "ニッチトップ",  # ニッチトップETF
    ]

    # 許可する業種コード
    ALLOWED_SECTORS = {
        "3650": "電気機器",
        "3800": "その他製品",
        "5250": "情報・通信業",
        "9050": "サービス業",
    }

    def __init__(self, logger: Logger):
        """
        銘柄フィルターを初期化する

        Args:
            logger: ロガーオブジェクト
        """
        self.logger = logger

    def filter_individual_stocks(self, master_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        個別株のみを抽出（ETF、REIT、インフラファンドを除外）

        複数の判定基準を組み合わせて、確実に個別株のみを抽出します：
        1. 銘柄コード範囲による判定
        2. 銘柄名キーワードによる判定
        3. 銘柄コードの妥当性チェック

        Args:
            master_data: 銘柄マスターデータ

        Returns:
            個別株のみのリスト

        Example:
            >>> filter = StockFilter(logger)
            >>> master_data = [
            ...     {"sIssueCode": "7203", "sIssueName": "トヨタ自動車"},
            ...     {"sIssueCode": "1306", "sIssueName": "TOPIX連動型ETF"},
            ... ]
            >>> individual_stocks = filter.filter_individual_stocks(master_data)
            >>> len(individual_stocks)
            1
        """
        individual_stocks = []
        excluded_by_code_range = 0
        excluded_by_keyword = 0
        excluded_by_invalid_code = 0

        for stock in master_data:
            issue_code = stock.get("sIssueCode", "")
            issue_name = stock.get("sIssueName", "")

            # 1. 銘柄コードの妥当性チェック
            if not issue_code:
                excluded_by_invalid_code += 1
                continue

            # 銘柄コードを数値に変換
            try:
                code_num = int(issue_code)
            except ValueError:
                excluded_by_invalid_code += 1
                self.logger.debug(f"無効な銘柄コード: {issue_code}")
                continue

            # 2. 銘柄コード範囲による判定
            is_excluded_by_range = False
            for start, end in self.EXCLUDED_CODE_RANGES:
                if start <= code_num <= end:
                    is_excluded_by_range = True
                    excluded_by_code_range += 1
                    self.logger.debug(f"コード範囲除外: {issue_code} {issue_name}")
                    break

            if is_excluded_by_range:
                continue

            # 3. 銘柄名によるキーワード除外
            is_excluded_by_keyword = False
            for keyword in self.EXCLUDED_KEYWORDS:
                if keyword in issue_name:
                    is_excluded_by_keyword = True
                    excluded_by_keyword += 1
                    self.logger.debug(
                        f"キーワード除外: {issue_code} {issue_name} (キーワード: {keyword})"
                    )
                    break

            if is_excluded_by_keyword:
                continue

            # すべてのチェックを通過した場合のみ追加
            individual_stocks.append(stock)

        # フィルタリング結果のサマリーをログ出力
        self.logger.info(
            f"個別株フィルタリング完了: {len(master_data)}件 → {len(individual_stocks)}件"
        )
        self.logger.info(f"  除外内訳: コード範囲={excluded_by_code_range}件, "
                        f"キーワード={excluded_by_keyword}件, "
                        f"無効コード={excluded_by_invalid_code}件")

        return individual_stocks

    def filter_by_sector(self, stocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        業種コードによるフィルタリング（許可された業種のみ抽出）

        Args:
            stocks: 銘柄リスト

        Returns:
            許可された業種の銘柄リスト

        Example:
            >>> filter = StockFilter(logger)
            >>> stocks = [
            ...     {"sIssueCode": "6758", "sIssueName": "ソニー", "sGyousyuCode": "3650"},
            ...     {"sIssueCode": "7203", "sIssueName": "トヨタ", "sGyousyuCode": "3050"},
            ... ]
            >>> filtered = filter.filter_by_sector(stocks)
            >>> len(filtered)  # ソニーのみ該当
            1
        """
        filtered_stocks = []
        sector_counts = {}  # 業種別の銘柄数をカウント

        for stock in stocks:
            sector_code = stock.get("sGyousyuCode", "")

            # 許可された業種のみ追加
            if sector_code in self.ALLOWED_SECTORS:
                filtered_stocks.append(stock)

                # 業種別カウント
                sector_name = self.ALLOWED_SECTORS[sector_code]
                sector_counts[sector_name] = sector_counts.get(sector_name, 0) + 1

        # フィルタリング結果のログ出力
        self.logger.info(
            f"業種フィルタリング完了: {len(stocks)}件 → {len(filtered_stocks)}件"
        )

        # 業種別の銘柄数を表示
        if sector_counts:
            self.logger.info("  業種別内訳:")
            for sector_name, count in sorted(sector_counts.items()):
                self.logger.info(f"    {sector_name}: {count}件")
        else:
            self.logger.warning("  ⚠️  該当する業種の銘柄がありません")

        return filtered_stocks

    def is_individual_stock(self, stock: Dict[str, Any]) -> bool:
        """
        単一の銘柄が個別株かどうかを判定する

        Args:
            stock: 銘柄情報（辞書）

        Returns:
            個別株の場合True、それ以外はFalse

        Example:
            >>> filter = StockFilter(logger)
            >>> stock = {"sIssueCode": "7203", "sIssueName": "トヨタ自動車"}
            >>> filter.is_individual_stock(stock)
            True
        """
        # 一時的に1件のリストでフィルタリングを実行
        result = self.filter_individual_stocks([stock])
        return len(result) > 0
