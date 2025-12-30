"""
祝日判定モジュール

日本の祝日・休場日を判定します。
"""

import datetime
from typing import Set
import jpholiday


class JapaneseCalendar:
    """日本の祝日・休場日を判定するクラス"""

    def __init__(self):
        """カレンダーを初期化する"""
        self.holidays = self._load_holidays()

    def _load_holidays(self) -> Set[datetime.date]:
        """
        祝日データを読み込む

        Returns:
            祝日の日付セット
        """
        holidays = set()
        current_year = datetime.datetime.now().year

        # 当年と翌年の祝日を取得
        for year in [current_year, current_year + 1]:
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        date = datetime.date(year, month, day)
                        if jpholiday.is_holiday(date):
                            holidays.add(date)
                    except ValueError:
                        # 無効な日付（例: 2月30日）はスキップ
                        continue

        return holidays

    def is_trading_day(self, date: datetime.date) -> bool:
        """
        指定された日付が取引日かどうかを判定する

        Args:
            date: 判定する日付

        Returns:
            取引日の場合True、休場日の場合False
        """
        # 土日は休み
        if date.weekday() >= 5:  # 5=土曜日, 6=日曜日
            return False

        # 祝日は休み
        if date in self.holidays:
            return False

        # 年末年始（12/31-1/3）は休み
        if (date.month == 12 and date.day == 31) or (date.month == 1 and date.day <= 3):
            return False

        return True

    def is_weekend(self, date: datetime.date) -> bool:
        """
        指定された日付が週末(土日)かどうかを判定する

        Args:
            date: 判定する日付

        Returns:
            週末の場合True、それ以外False
        """
        return date.weekday() >= 5  # 5=土曜日, 6=日曜日

    def is_holiday(self, date: datetime.date) -> bool:
        """
        指定された日付が祝日または休場日かどうかを判定する

        Args:
            date: 判定する日付

        Returns:
            祝日または休場日の場合True、それ以外False
        """
        # 祝日のチェック
        if date in self.holidays:
            return True

        # 年末年始の休場日のチェック
        if (date.month == 12 and date.day == 31) or (date.month == 1 and date.day <= 3):
            return True

        return False

    def get_next_trading_day(self, date: datetime.date) -> datetime.date:
        """
        指定された日付の次の取引日を取得する

        Args:
            date: 基準日

        Returns:
            次の取引日
        """
        next_day = date + datetime.timedelta(days=1)
        while not self.is_trading_day(next_day):
            next_day += datetime.timedelta(days=1)
        return next_day

    def get_previous_trading_day(self, date: datetime.date) -> datetime.date:
        """
        指定された日付の前の取引日を取得する

        Args:
            date: 基準日

        Returns:
            前の取引日
        """
        prev_day = date - datetime.timedelta(days=1)
        while not self.is_trading_day(prev_day):
            prev_day -= datetime.timedelta(days=1)
        return prev_day

    def get_holidays_in_year(self, year: int) -> set:
        """
        指定された年の祝日と休場日のセットを取得する

        Args:
            year: 年

        Returns:
            祝日と休場日の日付セット
        """
        holidays = set()

        # jpholidayから祝日を取得
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    date = datetime.date(year, month, day)
                    if jpholiday.is_holiday(date):
                        holidays.add(date)
                except ValueError:
                    # 無効な日付（例: 2月30日）はスキップ
                    continue

        # 年末年始の休場日を追加
        holidays.add(datetime.date(year, 12, 31))  # 大晦日
        holidays.add(datetime.date(year, 1, 1))  # 元日
        holidays.add(datetime.date(year, 1, 2))  # 1月2日
        holidays.add(datetime.date(year, 1, 3))  # 1月3日

        return holidays
