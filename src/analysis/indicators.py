"""
テクニカル指標計算モジュール

移動平均線などのテクニカル指標を計算します。
pandas-taは利用せず、純粋なpandas/numpyで実装します。
"""

from typing import List, Optional, Dict, Any, Tuple
import pandas as pd
import numpy as np


class TechnicalIndicators:
    """テクニカル指標を計算するクラス"""

    @staticmethod
    def moving_average(
        prices: List[float], period: int
    ) -> List[Optional[float]]:
        """
        単純移動平均（SMA: Simple Moving Average）を計算する
        （pandas vectorization版）

        Args:
            prices: 価格のリスト（古い順）
            period: 移動平均の期間（例: 25日）

        Returns:
            移動平均のリスト。データ不足の期間はNone

        Example:
            >>> prices = [100, 102, 101, 103, 105]
            >>> TechnicalIndicators.moving_average(prices, 3)
            [None, None, 101.0, 102.0, 103.0]
        """
        if not prices or period <= 0:
            return []

        if period > len(prices):
            # 全期間データ不足
            return [None] * len(prices)

        # pandasのrolling()を使用して高速化
        series = pd.Series(prices)
        ma_series = series.rolling(window=period, min_periods=period).mean()

        # NaNをNoneに変換
        return [None if pd.isna(v) else v for v in ma_series]

    @staticmethod
    def exponential_moving_average(
        prices: List[float], period: int
    ) -> List[Optional[float]]:
        """
        指数移動平均（EMA: Exponential Moving Average）を計算する（pandas ewm版）

        Args:
            prices: 価格のリスト（古い順）
            period: 移動平均の期間（例: 25日）

        Returns:
            指数移動平均のリスト。データ不足の期間はNone
        """
        if not prices or period <= 0:
            return []

        if period > len(prices):
            return [None] * len(prices)

        # pandasのewm()を使用して高速化
        series = pd.Series(prices)
        ema_series = series.ewm(
            span=period, adjust=False, min_periods=period
        ).mean()

        # NaNをNoneに変換
        return [None if pd.isna(v) else v for v in ema_series]

    @staticmethod
    def volume_ratio(
        volumes: List[float], period: int = 20
    ) -> List[Optional[float]]:
        """
        出来高比率を計算する（当日出来高 / 平均出来高）

        Args:
            volumes: 出来高のリスト（古い順）
            period: 平均出来高の計算期間（デフォルト: 20日）

        Returns:
            出来高比率のリスト
        """
        if not volumes or period <= 0:
            return []

        avg_volumes = TechnicalIndicators.moving_average(volumes, period)
        result: List[Optional[float]] = []

        for i, (vol, avg_vol) in enumerate(zip(volumes, avg_volumes)):
            if avg_vol is None or avg_vol == 0:
                result.append(None)
            else:
                ratio = vol / avg_vol
                result.append(ratio)

        return result

    @staticmethod
    def price_change_rate(prices: List[float]) -> List[Optional[float]]:
        """
        前日比変化率を計算する（%）

        Args:
            prices: 価格のリスト（古い順）

        Returns:
            前日比変化率のリスト（%）。初日はNone
        """
        if not prices:
            return []

        result: List[Optional[float]] = [None]  # 初日はNone

        for i in range(1, len(prices)):
            prev_price = prices[i - 1]
            current_price = prices[i]

            if prev_price == 0:
                result.append(None)
            else:
                change_rate = ((current_price - prev_price) / prev_price) * 100
                result.append(change_rate)

        return result

    @staticmethod
    def bollinger_bands(
        prices: List[float], period: int = 20, num_std: float = 2.0
    ) -> tuple[
        List[Optional[float]], List[Optional[float]], List[Optional[float]]
    ]:  # noqa: E501
        """
        ボリンジャーバンドを計算する

        Args:
            prices: 価格のリスト（古い順）
            period: 移動平均の期間（デフォルト: 20日）
            num_std: 標準偏差の倍数（デフォルト: 2.0）

        Returns:
            (上限バンド, 中心線（SMA）, 下限バンド) のタプル
        """
        if not prices or period <= 0:
            return [], [], []

        sma = TechnicalIndicators.moving_average(prices, period)
        upper_band: List[Optional[float]] = []
        lower_band: List[Optional[float]] = []

        for i in range(len(prices)):
            if sma[i] is None:
                upper_band.append(None)
                lower_band.append(None)
            else:
                # 標準偏差を計算
                window = prices[max(0, i - period + 1) : i + 1]
                if len(window) < period:
                    upper_band.append(None)
                    lower_band.append(None)
                else:
                    std_dev = np.std(window, ddof=1)  # 不偏標準偏差
                    upper_band.append(sma[i] + num_std * std_dev)
                    lower_band.append(sma[i] - num_std * std_dev)

        return upper_band, sma, lower_band

    @staticmethod
    def rsi(prices: List[float], period: int = 14) -> List[Optional[float]]:
        """
        RSI（Relative Strength Index）を計算する

        Args:
            prices: 価格のリスト（古い順）
            period: RSIの期間（デフォルト: 14日）

        Returns:
            RSIのリスト（0-100の値）
        """
        if not prices or period <= 0 or len(prices) < period + 1:
            return [None] * len(prices)

        result: List[Optional[float]] = [None]  # 初日はNone

        gains = []
        losses = []

        # 価格変動を計算
        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        # RSI計算
        for i in range(len(gains)):
            if i < period - 1:
                result.append(None)
            else:
                avg_gain = sum(gains[i - period + 1 : i + 1]) / period
                avg_loss = sum(losses[i - period + 1 : i + 1]) / period

                if avg_loss == 0:
                    rsi_value = 100.0
                else:
                    rs = avg_gain / avg_loss
                    rsi_value = 100 - (100 / (1 + rs))

                result.append(rsi_value)

        return result

    @staticmethod
    def macd(
        prices: List[float],
        fast_period: int = 12,
        slow_period: int = 26,
        signal_period: int = 9,
    ) -> Tuple[
        List[Optional[float]], List[Optional[float]], List[Optional[float]]
    ]:
        """
        MACD（Moving Average Convergence Divergence）を計算する

        Args:
            prices: 価格のリスト（古い順）
            fast_period: 短期EMAの期間（デフォルト: 12日）
            slow_period: 長期EMAの期間（デフォルト: 26日）
            signal_period: シグナルラインの期間（デフォルト: 9日）

        Returns:
            (MACD, シグナル, ヒストグラム) のタプル
        """
        if not prices or len(prices) < slow_period:
            empty = [None] * len(prices)
            return empty, empty, empty

        # EMAの計算
        ema_fast = TechnicalIndicators.exponential_moving_average(
            prices, fast_period
        )
        ema_slow = TechnicalIndicators.exponential_moving_average(
            prices, slow_period
        )

        # MACDラインの計算
        macd_line: List[Optional[float]] = []
        for fast, slow in zip(ema_fast, ema_slow):
            if fast is None or slow is None:
                macd_line.append(None)
            else:
                macd_line.append(fast - slow)

        # シグナルラインの計算（MACDラインのEMA）
        # Noneを除外してシグナル計算
        macd_values_for_signal = [
            v if v is not None else 0.0 for v in macd_line
        ]
        signal_line = TechnicalIndicators.exponential_moving_average(
            macd_values_for_signal, signal_period
        )

        # ヒストグラムの計算
        histogram: List[Optional[float]] = []
        for macd_val, signal_val in zip(macd_line, signal_line):
            if macd_val is None or signal_val is None:
                histogram.append(None)
            else:
                histogram.append(macd_val - signal_val)

        return macd_line, signal_line, histogram

    @staticmethod
    def calculate_all_from_price_data(
        price_data: List[Dict[str, Any]],
    ) -> Optional[pd.DataFrame]:
        """
        株価データから全てのテクニカル指標を計算する

        Args:
            price_data: 株価データのリスト（aCLMMfdsMarketPriceHistory）
                各要素は以下のフィールドを含む：
                - sDate: 日付（YYYYMMDD）
                - pDOP: 始値
                - pDHP: 高値
                - pDLP: 安値
                - pDPP: 終値
                - pDV: 出来高

        Returns:
            テクニカル指標を含むDataFrame、またはNone（データ不足時）
                カラム:
                - date: 日付（datetime）
                - open: 始値
                - high: 高値
                - low: 安値
                - close: 終値
                - volume: 出来高
                - ma25: 25日移動平均
                - bb_upper: ボリンジャーバンド上限
                - bb_middle: ボリンジャーバンド中心線
                - bb_lower: ボリンジャーバンド下限
                - rsi: RSI（14日）
                - macd: MACDライン
                - macd_signal: MACDシグナル
                - macd_histogram: MACDヒストグラム
        """
        if not price_data or len(price_data) < 50:
            # 最低50日分のデータが必要
            return None

        # DataFrameに変換
        df = pd.DataFrame(price_data)

        # 日付をdatetime型に変換
        df["date"] = pd.to_datetime(df["sDate"], format="%Y%m%d")

        # 日付順にソート（古い順）
        df = df.sort_values("date").reset_index(drop=True)

        # 数値型に変換
        df["open"] = pd.to_numeric(df["pDOP"], errors="coerce")
        df["high"] = pd.to_numeric(df["pDHP"], errors="coerce")
        df["low"] = pd.to_numeric(df["pDLP"], errors="coerce")
        df["close"] = pd.to_numeric(df["pDPP"], errors="coerce")
        df["volume"] = pd.to_numeric(df["pDV"], errors="coerce")

        # 欠損値を削除
        df = df.dropna(subset=["close", "volume"]).reset_index(drop=True)

        if len(df) < 50:
            return None

        # 価格リストを取得
        closes = df["close"].tolist()
        volumes = df["volume"].tolist()

        # 5日移動平均
        ma5 = TechnicalIndicators.moving_average(closes, 5)
        df["ma5"] = ma5

        # 25日移動平均
        ma25 = TechnicalIndicators.moving_average(closes, 25)
        df["ma25"] = ma25

        # ボリンジャーバンド（20日、±2σ）
        bb_upper, bb_middle, bb_lower = TechnicalIndicators.bollinger_bands(
            closes, period=20, num_std=2.0
        )
        df["bb_upper"] = bb_upper
        df["bb_middle"] = bb_middle
        df["bb_lower"] = bb_lower

        # RSI（14日）
        rsi = TechnicalIndicators.rsi(closes, period=14)
        df["rsi"] = rsi

        # MACD
        macd_line, macd_signal, macd_histogram = TechnicalIndicators.macd(
            closes, fast_period=12, slow_period=26, signal_period=9
        )
        df["macd"] = macd_line
        df["macd_signal"] = macd_signal
        df["macd_histogram"] = macd_histogram

        # 出来高比率
        volume_ratio = TechnicalIndicators.volume_ratio(volumes, period=25)
        df["volume_ratio"] = volume_ratio

        return df
