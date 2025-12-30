"""祝日判定モジュールのテスト"""

import datetime

from src.utils.calendar import JapaneseCalendar


class TestJapaneseCalendar:
    """JapaneseCalendarクラスのテスト"""

    def setup_method(self):
        """各テストの前処理"""
        self.calendar = JapaneseCalendar()

    def test_is_weekend(self):
        """週末判定のテスト"""
        # 2025年1月18日は土曜日
        saturday = datetime.date(2025, 1, 18)
        assert self.calendar.is_weekend(saturday) is True

        # 2025年1月19日は日曜日
        sunday = datetime.date(2025, 1, 19)
        assert self.calendar.is_weekend(sunday) is True

        # 2025年1月20日は月曜日
        monday = datetime.date(2025, 1, 20)
        assert self.calendar.is_weekend(monday) is False

    def test_is_holiday(self):
        """祝日判定のテスト"""
        # 2025年1月1日は元日（祝日）
        new_year = datetime.date(2025, 1, 1)
        assert self.calendar.is_holiday(new_year) is True

        # 2025年12月31日は大晦日（休場日）
        year_end = datetime.date(2025, 12, 31)
        assert self.calendar.is_holiday(year_end) is True

        # 2025年1月20日は平日（祝日ではない）
        regular_day = datetime.date(2025, 1, 20)
        assert self.calendar.is_holiday(regular_day) is False

    def test_is_trading_day(self):
        """取引日判定のテスト"""
        # 2025年1月20日は月曜日（取引日）
        monday = datetime.date(2025, 1, 20)
        assert self.calendar.is_trading_day(monday) is True

        # 2025年1月18日は土曜日（非取引日）
        saturday = datetime.date(2025, 1, 18)
        assert self.calendar.is_trading_day(saturday) is False

        # 2025年1月1日は元日（非取引日）
        new_year = datetime.date(2025, 1, 1)
        assert self.calendar.is_trading_day(new_year) is False

        # 2025年12月31日は大晦日（非取引日）
        year_end = datetime.date(2025, 12, 31)
        assert self.calendar.is_trading_day(year_end) is False

    def test_get_next_trading_day(self):
        """次の取引日取得のテスト"""
        # 2025年1月17日（金曜日）の次の取引日は1月20日（月曜日）
        friday = datetime.date(2025, 1, 17)
        next_day = self.calendar.get_next_trading_day(friday)
        assert next_day == datetime.date(2025, 1, 20)

        # 年末年始をまたぐケース: 2024年12月30日（月曜日）の次の取引日は2025年1月6日
        # 12/31, 1/1, 1/2, 1/3が休場、1/4-5が土日
        year_end = datetime.date(2024, 12, 30)
        next_day = self.calendar.get_next_trading_day(year_end)
        assert next_day == datetime.date(2025, 1, 6)

    def test_get_previous_trading_day(self):
        """前の取引日取得のテスト"""
        # 2025年1月20日（月曜日）の前の取引日は1月17日（金曜日）
        monday = datetime.date(2025, 1, 20)
        prev_day = self.calendar.get_previous_trading_day(monday)
        assert prev_day == datetime.date(2025, 1, 17)

    def test_get_holidays_in_year(self):
        """年間祝日取得のテスト"""
        holidays = self.calendar.get_holidays_in_year(2025)

        # 2025年の主要な祝日を確認
        assert datetime.date(2025, 1, 1) in holidays  # 元日
        assert datetime.date(2025, 12, 31) in holidays  # 大晦日（休場日）

        # 祝日のセットに少なくとも10日以上含まれているか
        # （日本の祝日+年末年始休場日）
        assert len(holidays) >= 10
