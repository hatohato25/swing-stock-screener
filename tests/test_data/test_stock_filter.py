"""
銘柄フィルタリングのテストモジュール

個別株フィルタリングの精度を確認するテストケース。
ETF、REIT、インフラファンド、投資信託の除外を検証します。
"""

import pytest
from src.data.stock_filter import StockFilter
from src.utils.logger import Logger


@pytest.fixture
def stock_filter():
    """StockFilterのフィクスチャ"""
    logger = Logger(log_dir="data/logs", name="test")
    return StockFilter(logger)


class TestStockFilterCodeRange:
    """銘柄コード範囲による除外テスト"""

    def test_individual_stock_normal(self, stock_filter):
        """個別株の判定：通常の個別株はフィルタリングを通過する"""
        # Arrange
        stock = {"sIssueCode": "7203", "sIssueName": "トヨタ自動車"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is True

    def test_exclude_etf_1300_range(self, stock_filter):
        """ETF除外：1300番台のETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1306", "sIssueName": "TOPIX連動型ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_etf_1400_range(self, stock_filter):
        """ETF除外：1400番台のETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1489", "sIssueName": "日経平均高配当株50 ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_mutual_fund_2000_range(self, stock_filter):
        """投資信託除外：2000番台の投資信託（ETF/ETN）が除外される"""
        # Arrange
        stock = {"sIssueCode": "2046", "sIssueName": "NEXT FUNDS TOPIX連動型上場投信"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_reit_8950_range(self, stock_filter):
        """REIT除外：8950番台のREITが除外される"""
        # Arrange
        stock = {"sIssueCode": "8951", "sIssueName": "日本ビルファンド投資法人"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_infrastructure_fund(self, stock_filter):
        """インフラファンド除外：9280番台のインフラファンドが除外される"""
        # Arrange
        stock = {"sIssueCode": "9282", "sIssueName": "いちごグリーンインフラ投資法人"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False


class TestStockFilterKeyword:
    """銘柄名キーワードによる除外テスト"""

    def test_exclude_by_etf_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「ETF」を含む銘柄が除外される"""
        # Arrange
        stock = {"sIssueCode": "1320", "sIssueName": "ダイワ上場投信-東証REIT指数 ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_etn_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「ETN」を含む銘柄が除外される"""
        # Arrange
        stock = {"sIssueCode": "2036", "sIssueName": "トップシェアETN"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_reit_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「REIT」を含む銘柄が除外される"""
        # Arrange
        stock = {"sIssueCode": "8952", "sIssueName": "ジャパンリアルエステイト投資法人REIT"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_nzam_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「NZAM」を含む投信ブランドが除外される"""
        # Arrange
        stock = {"sIssueCode": "2525", "sIssueName": "NZAM 上場投信 TOPIX"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_mx_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「MX」を含む投信ブランドが除外される"""
        # Arrange
        stock = {"sIssueCode": "2526", "sIssueName": "MXS 全世界株式"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_ishares_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「iシェアーズ」を含む投信ブランドが除外される"""
        # Arrange
        stock = {"sIssueCode": "2527", "sIssueName": "iシェアーズ TOPIX ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_inverse_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「インバース」を含むETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1357", "sIssueName": "日経平均インバース・インデックス連動型ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_leverage_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「レバレッジ」を含むETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1570", "sIssueName": "日経平均レバレッジ・インデックス連動型ETF"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_bull_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「ブル」を含むETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1579", "sIssueName": "日経平均ブル2倍上場投信"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False

    def test_exclude_by_bear_keyword(self, stock_filter):
        """キーワード除外：銘柄名に「ベア」を含むETFが除外される"""
        # Arrange
        stock = {"sIssueCode": "1580", "sIssueName": "日経平均ベア上場投信"}

        # Act
        result = stock_filter.is_individual_stock(stock)

        # Assert
        assert result is False


class TestStockFilterBatchProcessing:
    """一括フィルタリングのテスト"""

    def test_filter_individual_stocks_batch(self, stock_filter):
        """一括フィルタリング：個別株のみを抽出できる"""
        # Arrange
        master_data = [
            {"sIssueCode": "7203", "sIssueName": "トヨタ自動車"},
            {"sIssueCode": "6758", "sIssueName": "ソニーグループ"},
            {"sIssueCode": "1306", "sIssueName": "TOPIX連動型ETF"},  # ETF（除外）
            {"sIssueCode": "2046", "sIssueName": "NEXT FUNDS TOPIX"},  # 投信（除外）
            {"sIssueCode": "8951", "sIssueName": "日本ビルファンド投資法人"},  # REIT（除外）
            {"sIssueCode": "9503", "sIssueName": "関西電力"},
            {"sIssueCode": "1357", "sIssueName": "日経平均インバースETF"},  # インバース（除外）
        ]

        # Act
        result = stock_filter.filter_individual_stocks(master_data)

        # Assert
        assert len(result) == 3  # 個別株のみ3件
        assert result[0]["sIssueCode"] == "7203"
        assert result[1]["sIssueCode"] == "6758"
        assert result[2]["sIssueCode"] == "9503"

    def test_filter_individual_stocks_all_excluded(self, stock_filter):
        """一括フィルタリング：全件除外される場合は空リストを返す"""
        # Arrange
        master_data = [
            {"sIssueCode": "1306", "sIssueName": "TOPIX連動型ETF"},
            {"sIssueCode": "8951", "sIssueName": "日本ビルファンド投資法人"},
            {"sIssueCode": "2046", "sIssueName": "NEXT FUNDS TOPIX"},
        ]

        # Act
        result = stock_filter.filter_individual_stocks(master_data)

        # Assert
        assert len(result) == 0

    def test_filter_individual_stocks_empty_input(self, stock_filter):
        """一括フィルタリング：空リストを入力した場合は空リストを返す"""
        # Arrange
        master_data = []

        # Act
        result = stock_filter.filter_individual_stocks(master_data)

        # Assert
        assert len(result) == 0

    def test_filter_individual_stocks_invalid_code(self, stock_filter):
        """一括フィルタリング：無効な銘柄コードは除外される"""
        # Arrange
        master_data = [
            {"sIssueCode": "7203", "sIssueName": "トヨタ自動車"},
            {"sIssueCode": "", "sIssueName": "無効コード1"},  # 空文字（除外）
            {"sIssueCode": "ABC", "sIssueName": "無効コード2"},  # 数値でない（除外）
            {"sIssueCode": "6758", "sIssueName": "ソニーグループ"},
        ]

        # Act
        result = stock_filter.filter_individual_stocks(master_data)

        # Assert
        assert len(result) == 2
        assert result[0]["sIssueCode"] == "7203"
        assert result[1]["sIssueCode"] == "6758"
