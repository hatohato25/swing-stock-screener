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


# --- _format_date_with_weekday のテスト ---


def test_format_date_with_weekday_月曜日(test_logger, test_output_dir):
    """_format_date_with_weekday: 月曜日は (月) と表示される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 2026-02-02 は月曜日
    result = generator._format_date_with_weekday("2026-02-02")

    assert result == "2026-02-02 (月)"


def test_format_date_with_weekday_金曜日(test_logger, test_output_dir):
    """_format_date_with_weekday: 金曜日は (金) と表示される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 2026-02-06 は金曜日
    result = generator._format_date_with_weekday("2026-02-06")

    assert result == "2026-02-06 (金)"


def test_format_date_with_weekday_全曜日(test_logger, test_output_dir):
    """_format_date_with_weekday: 月〜日の7曜日すべてが正しくマッピングされる"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 2026-02-02(月) から 2026-02-08(日) の1週間で全曜日を確認
    expected = [
        ("2026-02-02", "月"),
        ("2026-02-03", "火"),
        ("2026-02-04", "水"),
        ("2026-02-05", "木"),
        ("2026-02-06", "金"),
        ("2026-02-07", "土"),
        ("2026-02-08", "日"),
    ]
    for date_str, weekday_ja in expected:
        result = generator._format_date_with_weekday(date_str)
        assert result == f"{date_str} ({weekday_ja})", f"{date_str} の曜日が不正"


# --- _group_dates_by_month のテスト ---


def test_group_dates_by_month_単一月(test_logger, test_output_dir):
    """_group_dates_by_month: 同一月の日付は1グループにまとまる"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    dates = ["2026-01-05", "2026-01-06", "2026-01-07"]
    groups = generator._group_dates_by_month(dates)

    assert len(groups) == 1
    month_label, dates_in_month = groups[0]
    assert month_label == "2026年01月"
    assert dates_in_month == ["2026-01-05", "2026-01-06", "2026-01-07"]


def test_group_dates_by_month_複数月(test_logger, test_output_dir):
    """_group_dates_by_month: 複数月にまたがる日付は月ごとにグループ化される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 降順（新しい順）で渡す
    dates = [
        "2026-02-27",
        "2026-02-26",
        "2026-01-30",
        "2026-01-29",
        "2025-12-26",
    ]
    groups = generator._group_dates_by_month(dates)

    assert len(groups) == 3
    assert groups[0][0] == "2026年02月"
    assert groups[0][1] == ["2026-02-27", "2026-02-26"]
    assert groups[1][0] == "2026年01月"
    assert groups[1][1] == ["2026-01-30", "2026-01-29"]
    assert groups[2][0] == "2025年12月"
    assert groups[2][1] == ["2025-12-26"]


def test_group_dates_by_month_順序保持(test_logger, test_output_dir):
    """_group_dates_by_month: 降順入力に対して新しい月が先頭になる"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    dates = ["2026-03-01", "2026-02-28", "2026-01-31"]
    groups = generator._group_dates_by_month(dates)

    month_labels = [label for label, _ in groups]
    assert month_labels == ["2026年03月", "2026年02月", "2026年01月"]


# --- _generate_index_html のテスト ---


def test_generate_index_html_空リスト(test_logger, test_output_dir):
    """_generate_index_html: 日付リストが空でもHTMLが生成される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    html = generator._generate_index_html([])

    assert "<!DOCTYPE html>" in html
    assert "アーカイブ" in html
    # 最新レポートセクションは存在しない
    assert "最新レポート" not in html


def test_generate_index_html_最新レポートのみ(test_logger, test_output_dir):
    """_generate_index_html: 日付が1件のとき最新レポートのみ表示、過去のレポートセクションはない"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    html = generator._generate_index_html(["2026-02-28"])

    assert "最新レポート" in html
    assert "2026-02-28" in html
    # 過去のレポートセクションは表示されない
    assert "過去のレポート" not in html
    assert "<details" not in html


def test_generate_index_html_月別グルーピング(test_logger, test_output_dir):
    """_generate_index_html: 過去レポートが月別の<details>タグでグループ化される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    dates = [
        "2026-02-28",  # 最新レポート（カード表示）
        "2026-02-27",
        "2026-02-26",
        "2026-01-30",
        "2026-01-29",
    ]
    html = generator._generate_index_html(dates)

    assert "2026年02月" in html
    assert "2026年01月" in html
    # 月ごとの件数表示
    assert "(2件)" in html  # 2月は27, 26の2件
    assert "(2件)" in html  # 1月は30, 29の2件


def test_generate_index_html_最新月はopen属性あり(test_logger, test_output_dir):
    """_generate_index_html: 最新月の<details>にはopen属性が付与される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    dates = [
        "2026-02-28",  # 最新レポート（カード表示）
        "2026-02-27",
        "2026-01-30",
    ]
    html = generator._generate_index_html(dates)

    # 最新月（2月）はopenあり
    assert "<details open>" in html
    # 2番目以降の月はopenなし（<details> のみ）
    # detailsタグが2つあり、最初の1つだけopen
    assert html.count("<details open>") == 1
    assert html.count("<details>") == 1


def test_generate_index_html_曜日表示(test_logger, test_output_dir):
    """_generate_index_html: 各日付に日本語曜日が表示される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 2026-02-02は月曜日、2026-02-06は金曜日
    dates = ["2026-02-06", "2026-02-02"]
    html = generator._generate_index_html(dates)

    assert "2026-02-06 (金)" in html
    assert "2026-02-02 (月)" in html


def test_generate_index_html_最新レポートにも曜日表示(test_logger, test_output_dir):
    """_generate_index_html: 最新レポートのカードにも曜日が表示される"""
    generator = ReportGenerator(output_dir=str(test_output_dir), logger=test_logger)

    # 2026-02-27は金曜日
    html = generator._generate_index_html(["2026-02-27"])

    assert "2026-02-27 (金)" in html
