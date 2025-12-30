"""
株式スクリーニング機能のテスト

ゼロ除算対策やエッジケースのテストを含む
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from src.analysis.screener import StockScreener


class TestStockScreenerZeroDivision:
    """ゼロ除算対策のテストクラス"""

    @pytest.fixture
    def screener(self):
        """スクリーナーインスタンスを生成"""
        return StockScreener()

    def test_safe_division_正常系(self, screener):
        """安全な除算：正常な除算は計算結果を返す"""
        result = screener._safe_division(10.0, 2.0)
        assert result == 5.0

    def test_safe_division_ゼロ除算(self, screener):
        """安全な除算：分母が0の場合はNoneを返す"""
        result = screener._safe_division(10.0, 0.0)
        assert result is None

    def test_safe_division_負の分母(self, screener):
        """安全な除算：分母が負の場合はNoneを返す"""
        result = screener._safe_division(10.0, -1.0)
        assert result is None

    def test_calculate_breakout_score_正常系(self, screener):
        """ブレイクアウトスコア計算：正常なケース"""
        score = screener._calculate_breakout_score(
            current_price=110.0,
            reference_price=100.0,
            bonus=5.0,
        )
        # (110 - 100) / 100 * 100 + 5 = 10 + 5 = 15
        assert score == pytest.approx(15.0)

    def test_calculate_breakout_score_reference_price_zero(self, screener):
        """ブレイクアウトスコア計算：reference_priceが0の場合"""
        score = screener._calculate_breakout_score(
            current_price=110.0,
            reference_price=0.0,
            bonus=5.0,
        )
        # reference_priceが0の場合、ボーナスのみ返す
        assert score == 5.0

    def test_calculate_breakout_score_reference_price_negative(self, screener):
        """ブレイクアウトスコア計算：reference_priceが負の場合"""
        score = screener._calculate_breakout_score(
            current_price=110.0,
            reference_price=-10.0,
            bonus=5.0,
        )
        # reference_priceが負の場合、ボーナスのみ返す
        assert score == 5.0

    def test_bb_lower_bounce_filter_bb_lower_zero(self, screener):
        """BB下限反転フィルタ：bb_lowerが0の場合はスキップ"""
        # テストデータを作成
        df = pd.DataFrame(
            {
                "date": [datetime(2025, 1, 1), datetime(2025, 1, 2)],
                "close": [100.0, 110.0],
                "volume": [100000, 150000],
                "bb_lower": [50.0, 0.0],  # 最新行のbb_lowerが0
                "rsi": [25.0, 25.0],
                "macd_histogram": [-1.0, -0.5],
            }
        )

        result = screener.bb_lower_bounce_filter(
            stock_code="1234",
            stock_name="テスト銘柄",
            df=df,
        )

        # bb_lowerが0の場合はNoneを返す
        assert result is None

    def test_bb_lower_bounce_filter_bb_lower_negative(self, screener):
        """BB下限反転フィルタ：bb_lowerが負の場合はスキップ"""
        # テストデータを作成
        df = pd.DataFrame(
            {
                "date": [datetime(2025, 1, 1), datetime(2025, 1, 2)],
                "close": [100.0, 110.0],
                "volume": [100000, 150000],
                "bb_lower": [50.0, -10.0],  # 最新行のbb_lowerが負
                "rsi": [25.0, 25.0],
                "macd_histogram": [-1.0, -0.5],
            }
        )

        result = screener.bb_lower_bounce_filter(
            stock_code="1234",
            stock_name="テスト銘柄",
            df=df,
        )

        # bb_lowerが負の場合はNoneを返す
        assert result is None

    def test_bb_lower_bounce_filter_正常系(self, screener):
        """BB下限反転フィルタ：正常なケース"""
        # テストデータを作成（25日分のデータを用意）
        dates = pd.date_range(start="2025-01-01", periods=30, freq="D")
        df = pd.DataFrame(
            {
                "date": dates,
                "close": [100.0] * 29 + [102.0],
                "volume": [100000] * 30,
                "bb_lower": [95.0] * 29 + [98.0],
                "rsi": [30.0] * 29 + [28.0],
                "macd_histogram": [-1.0] * 29 + [-0.5],
            }
        )

        result = screener.bb_lower_bounce_filter(
            stock_code="1234",
            stock_name="テスト銘柄",
            df=df,
        )

        # 条件を満たす場合はScreenResultを返す
        assert result is not None
        assert result.stock_code == "1234"
        assert result.category == "bb_lower_bounce"

    def test_technical_breakout_ma_zero(self, screener):
        """テクニカルブレイクアウト：MA値が0の場合はスキップ"""
        # 26日分のデータ（25日MA + 前日 + 当日）
        ohlcv_data = []
        for i in range(27):
            ohlcv_data.append(
                {
                    "date": f"2025-01-{i+1:02d}",
                    "close": 100.0 if i < 26 else 110.0,
                    "volume": 100000,
                }
            )

        # MA値を手動で0にするため、すべての終値を0に設定
        for d in ohlcv_data:
            d["close"] = 0.0

        result = screener.technical_breakout(
            stock_code="1234",
            stock_name="テスト銘柄",
            ohlcv_data=ohlcv_data,
        )

        # MA値が0の場合はNoneを返す
        assert result is None

    def test_screen_stock_with_dataframe_ma_deviation_zero(self, screener):
        """MA乖離率計算：ma25が0の場合はNoneを設定"""
        # テストデータを作成
        df = pd.DataFrame(
            {
                "date": [datetime(2025, 1, 1), datetime(2025, 1, 2)],
                "close": [100.0, 110.0],
                "volume": [100000, 220000],
                "volume_ratio": [1.0, 2.2],
                "ma25": [100.0, 0.0],  # 最新行のma25が0
                "bb_upper": [120.0, 130.0],
                "bb_lower": [80.0, 90.0],
                "rsi": [50.0, 60.0],
                "macd_histogram": [-1.0, 1.0],
            }
        )

        results = screener.screen_stock_with_dataframe(
            stock_code="1234",
            stock_name="テスト銘柄",
            df=df,
        )

        # 出来高急増の結果が1件取得できる
        assert len(results) >= 1
        volume_surge_result = next(
            (r for r in results if r.category == "volume_surge"), None
        )
        assert volume_surge_result is not None

    def test_screen_stock_with_dataframe_ma_deviation_positive(self, screener):
        """MA乖離率計算：ma25が正の値の場合は正常に計算"""
        # テストデータを作成
        df = pd.DataFrame(
            {
                "date": [datetime(2025, 1, 1), datetime(2025, 1, 2)],
                "close": [95.0, 110.0],
                "volume": [100000, 220000],
                "volume_ratio": [1.0, 2.2],
                "ma25": [100.0, 100.0],
                "bb_upper": [120.0, 120.0],
                "bb_lower": [80.0, 80.0],
                "rsi": [50.0, 60.0],
                "macd_histogram": [-1.0, 1.0],
            }
        )

        results = screener.screen_stock_with_dataframe(
            stock_code="1234",
            stock_name="テスト銘柄",
            df=df,
        )

        # 出来高急増とブレイクアウト（MA上抜け）の結果が取得できる
        assert len(results) >= 2
        breakout_result = next(
            (r for r in results if r.category == "breakout"), None
        )
        assert breakout_result is not None
        # MA乖離率が正しく計算されている
        assert breakout_result.details["price_deviation"] is not None
