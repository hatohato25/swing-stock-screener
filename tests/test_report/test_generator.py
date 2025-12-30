"""
レポート生成モジュールのテスト
"""

import pytest
from pathlib import Path
from src.report.generator import ReportGenerator
from src.utils.logger import Logger


@pytest.fixture
def test_logger():
    """テスト用ロガーを生成する"""
    return Logger(log_dir="data/logs/test", name="test-report")


@pytest.fixture
def test_output_dir(tmp_path):
    """テスト用の出力ディレクトリを生成する"""
    return tmp_path / "test_reports"


@pytest.fixture
def sample_screened_stocks():
    """サンプルのスクリーニング結果を生成する"""
    return [
        {
            "stock_code": "7203",
            "stock_name": "トヨタ自動車",
            "category": "volume_surge",
            "score": 25.5,
            "details": {
                "current_price": 2500,
                "current_volume": 15000000,
                "prev_volume": 6000000,
                "volume_ratio": 2.5,
            },
        },
        {
            "stock_code": "9984",
            "stock_name": "ソフトバンクグループ",
            "category": "breakout",
            "score": 18.3,
            "details": {
                "current_price": 6500,
                "ma_value": 6200,
                "price_deviation": 4.84,
                "volume_ratio": 1.8,
            },
        },
        {
            "stock_code": "6758",
            "stock_name": "ソニーグループ",
            "category": "price_change",
            "score": 12.7,
            "details": {
                "current_price": 13000,
                "change_amount": 400,
                "change_rate": 3.17,
            },
        },
    ]


def test_report_generator_initialization(test_logger, test_output_dir):
    """ReportGeneratorが正常に初期化されるか"""
    generator = ReportGenerator(
        output_dir=str(test_output_dir), logger=test_logger
    )

    assert generator.output_dir == test_output_dir
    assert generator.logger == test_logger
    assert generator.output_dir.exists()


def test_categorize_stocks(test_logger, test_output_dir, sample_screened_stocks):
    """スクリーニング結果がカテゴリ別に正しく分類されるか"""
    generator = ReportGenerator(
        output_dir=str(test_output_dir), logger=test_logger
    )

    categorized = generator._categorize_stocks(sample_screened_stocks)

    # カテゴリが正しく存在するか
    assert "volume_surge" in categorized
    assert "breakout" in categorized
    assert "price_change" in categorized

    # 各カテゴリに正しい銘柄が分類されているか
    assert len(categorized["volume_surge"]) == 1
    assert len(categorized["breakout"]) == 1
    assert len(categorized["price_change"]) == 1

    # 銘柄コードで確認
    assert categorized["volume_surge"][0]["stock_code"] == "7203"
    assert categorized["breakout"][0]["stock_code"] == "9984"
    assert categorized["price_change"][0]["stock_code"] == "6758"


def test_calculate_stats(test_logger, test_output_dir, sample_screened_stocks):
    """統計情報が正しく計算されるか"""
    generator = ReportGenerator(
        output_dir=str(test_output_dir), logger=test_logger
    )

    categorized = generator._categorize_stocks(sample_screened_stocks)
    stats = generator._calculate_stats(categorized)

    assert stats["total_stocks"] == 3
    assert stats["volume_surge_count"] == 1
    assert stats["breakout_count"] == 1
    assert stats["price_change_count"] == 1


def test_generate_report(test_logger, test_output_dir, sample_screened_stocks):
    """レポートが正しく生成されるか"""
    generator = ReportGenerator(
        output_dir=str(test_output_dir), logger=test_logger
    )

    report_date = "2025-12-26"
    generator.generate(sample_screened_stocks, report_date)

    # レポートディレクトリが作成されているか
    report_dir = test_output_dir / report_date
    assert report_dir.exists()

    # HTMLレポートが生成されているか
    html_file = report_dir / "index.html"
    assert html_file.exists()
    html_content = html_file.read_text(encoding="utf-8")
    assert "株式スクリーニングレポート" in html_content
    assert "トヨタ自動車" in html_content
    assert "ソフトバンクグループ" in html_content

    # Markdownレポートが生成されているか
    md_file = report_dir / "README.md"
    assert md_file.exists()
    md_content = md_file.read_text(encoding="utf-8")
    assert "株式スクリーニングレポート" in md_content
    assert "トヨタ自動車" in md_content

    # インデックスページが生成されているか
    index_file = test_output_dir / "index.html"
    assert index_file.exists()
    index_content = index_file.read_text(encoding="utf-8")
    assert "アーカイブ" in index_content
    assert report_date in index_content


def test_multiple_reports(test_logger, test_output_dir, sample_screened_stocks):
    """複数のレポートが正しく生成されるか"""
    generator = ReportGenerator(
        output_dir=str(test_output_dir), logger=test_logger
    )

    # 3つのレポートを生成
    dates = ["2025-12-24", "2025-12-25", "2025-12-26"]
    for date in dates:
        generator.generate(sample_screened_stocks, date)

    # すべてのレポートディレクトリが存在するか
    for date in dates:
        report_dir = test_output_dir / date
        assert report_dir.exists()
        assert (report_dir / "index.html").exists()

    # インデックスページにすべての日付が含まれているか
    index_file = test_output_dir / "index.html"
    index_content = index_file.read_text(encoding="utf-8")
    for date in dates:
        assert date in index_content

    # 最新レポートが正しく表示されているか（降順でソート）
    assert "2025-12-26" in index_content
