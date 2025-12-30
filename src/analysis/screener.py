"""
株式スクリーニングモジュール

出来高急増、テクニカルブレイクアウト、値上がり率などの条件で銘柄を抽出します。
"""

from typing import List, Dict, Any, Optional
import pandas as pd
import logging
from src.analysis.indicators import TechnicalIndicators


class ScreenResult:
    """スクリーニング結果を格納するクラス"""

    def __init__(
        self,
        stock_code: str,
        stock_name: str,
        category: str,
        score: float,
        details: Dict[str, Any],
    ):
        """
        スクリーニング結果を初期化する

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            category: カテゴリ（volume_surge, breakout, price_change等）
            score: スコア
            details: 詳細情報
        """
        self.stock_code = stock_code
        self.stock_name = stock_name
        self.category = category
        self.score = score
        self.details = details

    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換する"""
        return {
            "stock_code": self.stock_code,
            "stock_name": self.stock_name,
            "category": self.category,
            "score": self.score,
            "details": self.details,
        }


class StockScreener:
    """株式スクリーニングクラス"""

    def __init__(self):
        """スクリーナーを初期化する"""
        self.indicators = TechnicalIndicators()
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _safe_division(numerator: float, denominator: float) -> Optional[float]:
        """
        安全な除算（ゼロ除算チェック）

        Args:
            numerator: 分子
            denominator: 分母

        Returns:
            計算結果（denominator <= 0の場合はNone）
        """
        if denominator <= 0:
            return None
        return numerator / denominator

    @staticmethod
    def _get_rounded_value(
        df_row: pd.Series, column: str, decimals: int = 2
    ) -> Optional[float]:
        """
        DataFrameの値を取得し、丸めて返す

        Args:
            df_row: DataFrameの行（Series）
            column: カラム名
            decimals: 小数点以下の桁数（デフォルト: 2）

        Returns:
            丸められた値（欠損値の場合はNone）
        """
        value = df_row[column]
        return round(float(value), decimals) if pd.notna(value) else None

    @staticmethod
    def _calculate_breakout_score(
        current_price: float, reference_price: float, bonus: float
    ) -> float:
        """
        ブレイクアウトスコアを計算する

        Args:
            current_price: 現在価格
            reference_price: 基準価格（ボリンジャーバンド上限またはMA）
            bonus: ボーナススコア

        Returns:
            スコア（乖離率 + ボーナス）

        Note:
            reference_priceが0以下の場合はボーナスのみを返す
        """
        if reference_price <= 0:
            return bonus
        deviation = (
            (current_price - reference_price) / reference_price
        ) * 100
        return deviation + bonus

    def volume_surge(
        self,
        stock_code: str,
        stock_name: str,
        ohlcv_data: List[Dict[str, Any]],
        threshold: float = 2.0,
    ) -> Optional[ScreenResult]:
        """
        出来高急増を検出する

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            ohlcv_data: OHLCVデータ（古い順）
            threshold: 出来高比率の閾値（デフォルト: 2.0倍）

        Returns:
            条件に合致した場合はScreenResult、不合致の場合はNone
        """
        if not ohlcv_data or len(ohlcv_data) < 2:
            return None

        # 当日と前日の出来高を取得
        current_volume = ohlcv_data[-1]["volume"]
        prev_volume = ohlcv_data[-2]["volume"]

        # 出来高比率を計算（ゼロ除算チェック込み）
        volume_ratio = self._safe_division(current_volume, prev_volume)
        if volume_ratio is None:
            return None

        # 閾値チェック
        if volume_ratio >= threshold:
            score = volume_ratio * 10  # スコア計算

            return ScreenResult(
                stock_code=stock_code,
                stock_name=stock_name,
                category="volume_surge",
                score=score,
                details={
                    "current_volume": current_volume,
                    "prev_volume": prev_volume,
                    "volume_ratio": round(volume_ratio, 2),
                    "current_price": ohlcv_data[-1]["close"],
                    "date": ohlcv_data[-1]["date"],
                },
            )

        return None

    def technical_breakout(
        self,
        stock_code: str,
        stock_name: str,
        ohlcv_data: List[Dict[str, Any]],
        ma_period: int = 25,
        volume_threshold: float = 1.5,
    ) -> Optional[ScreenResult]:
        """
        テクニカルブレイクアウトを検出する

        条件:
        1. 終値 > 25日移動平均線
        2. 前日終値 <= 25日移動平均線（上抜け確認）
        3. 当日出来高 / 前日出来高 >= 1.5

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            ohlcv_data: OHLCVデータ（古い順）
            ma_period: 移動平均線の期間（デフォルト: 25日）
            volume_threshold: 出来高比率の閾値（デフォルト: 1.5倍）

        Returns:
            条件に合致した場合はScreenResult、不合致の場合はNone
        """
        if not ohlcv_data or len(ohlcv_data) < ma_period + 1:
            return None

        # 終値と出来高のリストを抽出
        closes = [d["close"] for d in ohlcv_data]
        volumes = [d["volume"] for d in ohlcv_data]

        # 移動平均線を計算
        ma_values = self.indicators.moving_average(closes, ma_period)

        # 当日と前日のデータ
        current_close = closes[-1]
        prev_close = closes[-2]
        current_ma = ma_values[-1]
        prev_ma = ma_values[-2]

        current_volume = volumes[-1]
        prev_volume = volumes[-2]

        # データ不足チェック
        if current_ma is None or prev_ma is None or current_ma <= 0:
            return None

        # 条件1: 終値 > 25日移動平均線
        if current_close <= current_ma:
            return None

        # 条件2: 前日終値 <= 25日移動平均線（上抜け確認）
        if prev_close > prev_ma:
            return None

        # 条件3: 当日出来高 / 前日出来高 >= 1.5
        volume_ratio = self._safe_division(current_volume, prev_volume)
        if volume_ratio is None or volume_ratio < volume_threshold:
            return None

        # スコア計算
        price_deviation = ((current_close - current_ma) / current_ma) * 100
        score = price_deviation + volume_ratio

        return ScreenResult(
            stock_code=stock_code,
            stock_name=stock_name,
            category="breakout",
            score=score,
            details={
                "current_price": current_close,
                "ma_value": round(current_ma, 2),
                "price_deviation": round(price_deviation, 2),
                "volume_ratio": round(volume_ratio, 2),
                "date": ohlcv_data[-1]["date"],
            },
        )

    def screen_stock(
        self, stock_code: str, stock_name: str, ohlcv_data: List[Dict[str, Any]]
    ) -> List[ScreenResult]:
        """
        1銘柄を全条件でスクリーニングする

        注: 現在はscreen_stock_with_dataframe()を使用しています。
        このメソッドは将来の拡張用（辞書形式データの直接処理）のため保持。

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            ohlcv_data: OHLCVデータ（古い順）

        Returns:
            合致した条件のScreenResultリスト
        """
        results = []

        # 出来高急増チェック
        volume_result = self.volume_surge(stock_code, stock_name, ohlcv_data)
        if volume_result:
            results.append(volume_result)

        # テクニカルブレイクアウトチェック
        breakout_result = self.technical_breakout(stock_code, stock_name, ohlcv_data)
        if breakout_result:
            results.append(breakout_result)

        return results

    def screen_multiple_stocks(
        self, stocks_data: Dict[str, Dict[str, Any]], top_n: int = 20
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        複数銘柄を一括スクリーニングする

        注: 現在はscreen_stock_with_dataframe()を使用しています。
        このメソッドは将来の拡張用（一括スクリーニング）のため保持。

        Args:
            stocks_data: 銘柄データの辞書
                {
                    'stock_code': {
                        'name': '銘柄名',
                        'ohlcv': [OHLCVデータ]
                    }
                }
            top_n: 各カテゴリの上位N銘柄を保持（デフォルト: 20）

        Returns:
            カテゴリ別のスクリーニング結果
            {
                'volume_surge': [結果リスト],
                'breakout': [結果リスト]
            }
        """
        # カテゴリ別に結果を格納
        results_by_category: Dict[str, List[ScreenResult]] = {
            "volume_surge": [],
            "breakout": [],
        }

        # 全銘柄をスクリーニング
        for stock_code, data in stocks_data.items():
            stock_name = data.get("name", stock_code)
            ohlcv_data = data.get("ohlcv", [])

            # スクリーニング実行
            screen_results = self.screen_stock(stock_code, stock_name, ohlcv_data)

            # カテゴリ別に振り分け
            for result in screen_results:
                results_by_category[result.category].append(result)

        # 各カテゴリをスコア順にソートして上位N件を保持
        final_results = {}
        for category, results in results_by_category.items():
            sorted_results = sorted(results, key=lambda x: x.score, reverse=True)
            top_results = sorted_results[:top_n]
            final_results[category] = [r.to_dict() for r in top_results]

        return final_results

    def screen_stock_with_dataframe(
        self, stock_code: str, stock_name: str, df: pd.DataFrame
    ) -> List[ScreenResult]:
        """
        DataFrameから1銘柄を全条件でスクリーニングする

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            df: テクニカル指標を含むDataFrame

        Returns:
            合致した条件のScreenResultリスト
        """
        if df is None or len(df) < 2:
            return []

        results = []
        latest = df.iloc[-1]
        previous = df.iloc[-2]

        # 条件1: 出来高急増（平均出来高の2倍以上）
        if pd.notna(latest["volume_ratio"]) and latest["volume_ratio"] >= 2.0:
            score = latest["volume_ratio"] * 10

            # 平均出来高（25日）を計算
            avg_volume_25d = int(df["volume"].tail(25).mean())

            results.append(
                ScreenResult(
                    stock_code=stock_code,
                    stock_name=stock_name,
                    category="volume_surge",
                    score=score,
                    details={
                        "current_volume": int(latest["volume"]),
                        "avg_volume_25d": avg_volume_25d,
                        "volume_ratio": round(latest["volume_ratio"], 2),
                        "current_price": float(latest["close"]),
                        "rsi": self._get_rounded_value(latest, "rsi"),
                        "date": latest["date"].strftime("%Y-%m-%d"),
                    },
                )
            )

        # 条件2: テクニカルブレイクアウト
        # - ボリンジャーバンド上限突破 OR 25日移動平均線上抜け
        bb_breakout = (
            pd.notna(latest["bb_upper"]) and latest["close"] > latest["bb_upper"]
        )
        ma_crossover = (
            pd.notna(latest["ma25"])
            and pd.notna(previous["ma25"])
            and previous["close"] <= previous["ma25"]
            and latest["close"] > latest["ma25"]
        )

        if bb_breakout or ma_crossover:
            # スコア計算
            if bb_breakout:
                score = self._calculate_breakout_score(
                    latest["close"], latest["bb_upper"], 10
                )
            else:
                score = self._calculate_breakout_score(
                    latest["close"], latest["ma25"], 5
                )

            # MA乖離率と出来高比率を計算
            if pd.notna(latest["ma25"]) and latest["ma25"] > 0:
                ma_deviation = ((latest["close"] - latest["ma25"]) / latest["ma25"]) * 100
            else:
                ma_deviation = None

            # 出来高比率を計算（前日比、ゼロ除算チェック込み）
            volume_ratio_calc = self._safe_division(latest["volume"], previous["volume"])

            results.append(
                ScreenResult(
                    stock_code=stock_code,
                    stock_name=stock_name,
                    category="breakout",
                    score=score,
                    details={
                        "current_price": float(latest["close"]),
                        "ma_value": (
                            round(float(latest["ma25"]), 2)
                            if pd.notna(latest["ma25"])
                            else None
                        ),
                        "price_deviation": (
                            round(ma_deviation, 2) if ma_deviation is not None else None
                        ),
                        "volume_ratio": (
                            round(volume_ratio_calc, 2)
                            if volume_ratio_calc is not None
                            else None
                        ),
                        "rsi": self._get_rounded_value(latest, "rsi"),
                        "macd_histogram": self._get_rounded_value(
                            latest, "macd_histogram"
                        ),
                        "breakout_type": "bollinger" if bb_breakout else "ma_crossover",
                        "date": latest["date"].strftime("%Y-%m-%d"),
                    },
                )
            )

        # 条件3: ボリンジャーバンド下限反転（逆張り戦略）
        bb_bounce_result = self.bb_lower_bounce_filter(stock_code, stock_name, df)
        if bb_bounce_result:
            results.append(bb_bounce_result)

        # 条件4: 押し目買いチャンス
        pullback_result = self.pullback_dip_filter(stock_code, stock_name, df)
        if pullback_result:
            results.append(pullback_result)

        # 条件5: ゴールデンクロス直前
        golden_cross_result = self.golden_cross_approaching_filter(
            stock_code, stock_name, df
        )
        if golden_cross_result:
            results.append(golden_cross_result)

        return results

    def value_stock_inflation_adjusted_filter(
        self,
        stock_code: str,
        stock_name: str,
        stock_info: Dict[str, Any],
        current_price: float,
        per_threshold: float = 25.0,
        pbr_threshold: float = 2.5,
        dividend_yield_threshold: float = 2.0,
        roe_threshold: float = 8.0,
    ) -> Optional[ScreenResult]:
        """
        インフレ対応バリュー株を検出する（緩和基準）

        インフレ環境下では成長投資により一時的にPER/PBRが上昇するため、
        基準を緩和し、ROEで収益性を担保します。

        条件（少なくとも2つを満たす必要がある）:
        1. PER（予想） < 25倍
        2. PBR（実績） < 2.5倍
        3. 配当利回り（予想） >= 2.0%
        4. ROE（実績） >= 8.0%

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            stock_info: 銘柄情報（PER/PBR/配当利回り/ROE）
            current_price: 現在値
            per_threshold: PER閾値（デフォルト: 25.0倍）
            pbr_threshold: PBR閾値（デフォルト: 2.5倍）
            dividend_yield_threshold: 配当利回り閾値（デフォルト: 2.0%）
            roe_threshold: ROE閾値（デフォルト: 8.0%）

        Returns:
            ScreenResult または None
        """
        # データ取得
        per = stock_info.get("per")
        pbr = stock_info.get("pbr")
        dividend_yield = stock_info.get("dividend_yield")
        roe = stock_info.get("roe")

        # 少なくとも2つの条件を満たす必要がある
        conditions_met = 0
        has_per = per is not None and per < per_threshold and per > 0
        has_pbr = pbr is not None and pbr < pbr_threshold and pbr > 0
        has_dividend = (
            dividend_yield is not None and dividend_yield >= dividend_yield_threshold
        )
        has_roe = roe is not None and roe >= roe_threshold

        if has_per:
            conditions_met += 1
        if has_pbr:
            conditions_met += 1
        if has_dividend:
            conditions_met += 1
        if has_roe:
            conditions_met += 1

        if conditions_met < 2:
            return None

        # スコア計算
        score = 0.0
        if per is not None and per > 0:
            score += (per_threshold / per) * 8  # PERスコア（最大8点）

        if pbr is not None and pbr > 0:
            score += (pbr_threshold / pbr) * 8  # PBRスコア（最大8点）

        if dividend_yield is not None:
            score += dividend_yield * 4  # 配当利回りスコア（3%で12点）

        if roe is not None and roe > 0:
            score += roe * 2  # ROEスコア（10%で20点）

        return ScreenResult(
            stock_code=stock_code,
            stock_name=stock_name,
            category="value_inflation_adjusted",
            score=score,
            details={
                "current_price": current_price,
                "per": round(per, 2) if per is not None else None,
                "pbr": round(pbr, 2) if pbr is not None else None,
                "dividend_yield": (
                    round(dividend_yield, 2) if dividend_yield is not None else None
                ),
                "roe": round(roe, 2) if roe is not None else None,
            },
        )

    def pullback_dip_filter(
        self,
        stock_code: str,
        stock_name: str,
        df: pd.DataFrame,
    ) -> Optional[ScreenResult]:
        """
        押し目買いチャンス検出フィルタ

        条件:
        1. 25日MAが上昇中
        2. 現在値が25日MAを-5%～0%の範囲で下回る
        3. RSI 40～60
        4. MACDヒストグラム > 0
        5. 平均出来高 >= 100,000株

        スコア計算:
        - MA上昇率スコア（最大10点）
        - RSIスコア（最大20点）
        - MACDヒストグラムスコア（変動）
        - 出来高スコア（変動）

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            df: テクニカル指標を含むDataFrame

        Returns:
            ScreenResult または None
        """
        if df is None or len(df) < 26:
            # 25日MA比較には最低26日必要
            return None

        latest_row = df.iloc[-1]
        prev_row = df.iloc[-2]

        # 必要なデータチェック
        if pd.isna(latest_row["ma25"]) or pd.isna(prev_row["ma25"]) or pd.isna(latest_row["rsi"]):
            return None

        current_price = float(latest_row["close"])
        ma25 = float(latest_row["ma25"])
        ma25_prev = float(prev_row["ma25"])
        rsi = float(latest_row["rsi"])

        # ma25が0または負の場合は異常データとしてスキップ
        if ma25 <= 0 or ma25_prev <= 0:
            self.logger.debug(
                f"押し目買いスキップ: {stock_name}({stock_code}) - "
                f"MA25が異常値（現在: {ma25:.2f}, 前日: {ma25_prev:.2f}）"
            )
            return None

        # 平均出来高（25日）を計算
        avg_volume_25d = int(df["volume"].tail(25).mean())

        # 条件1: 25日MAが上昇中
        ma_change = ((ma25 - ma25_prev) / ma25_prev) * 100
        if ma_change <= 0:
            return None

        # 条件2: 現在値が25日MAを-5%～0%の範囲で下回る
        ma_deviation = ((current_price - ma25) / ma25) * 100
        if not (-5.0 <= ma_deviation <= 0.0):
            return None

        # 条件3: RSI 40～60
        if not (40 <= rsi <= 60):
            return None

        # 条件4: MACDヒストグラム > 0
        macd_histogram = latest_row.get("macd_histogram", 0)
        if pd.isna(macd_histogram):
            return None

        macd_histogram = float(macd_histogram)
        if macd_histogram <= 0:
            return None

        # 条件5: 平均出来高 >= 100,000株
        if avg_volume_25d < 100000:
            return None

        # スコア計算
        # 1. MA上昇率スコア（上昇率×10、最大10点）
        ma_score = ma_change * 10
        ma_score = min(10, ma_score)

        # 2. RSIスコア（50に近いほど高スコア、最大20点）
        rsi_score = (60 - abs(rsi - 50)) * (20 / 10)  # abs(rsi-50)が0の時20点、10の時0点
        rsi_score = max(0, rsi_score)

        # 3. MACDヒストグラムスコア
        macd_score = macd_histogram * 10

        # 4. 出来高スコア
        current_volume = int(latest_row["volume"])
        volume_ratio = current_volume / avg_volume_25d if avg_volume_25d > 0 else 1.0
        volume_score = (volume_ratio - 1.0) * 3
        volume_score = max(0, volume_score)

        # 合計スコア
        score = ma_score + rsi_score + macd_score + volume_score

        return ScreenResult(
            stock_code=stock_code,
            stock_name=stock_name,
            category="pullback_dip",
            score=score,
            details={
                "current_price": current_price,
                "ma25": ma25,
                "ma_deviation": round(ma_deviation, 2),
                "ma_change": round(ma_change, 2),
                "rsi": round(rsi, 2),
                "macd_histogram": round(macd_histogram, 2),
                "volume_ratio": round(volume_ratio, 2),
                "avg_volume_25d": avg_volume_25d,
                "date": str(latest_row["date"]),
            },
        )

    def golden_cross_approaching_filter(
        self,
        stock_code: str,
        stock_name: str,
        df: pd.DataFrame,
    ) -> Optional[ScreenResult]:
        """
        ゴールデンクロス直前検出フィルタ

        条件:
        1. 5日MA < 25日MA（まだクロスしていない）
        2. MA差が1%以内
        3. 5日MAが上昇中
        4. RSI > 50
        5. 平均出来高 >= 100,000株

        スコア計算:
        - MA差率スコア（最大50点）
        - 5日MA上昇率スコア（最大10点）
        - RSIスコア（変動）
        - 出来高スコア（変動）

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            df: テクニカル指標を含むDataFrame

        Returns:
            ScreenResult または None
        """
        if df is None or len(df) < 26:
            # 5日MA・25日MA比較には最低26日必要
            return None

        latest_row = df.iloc[-1]
        prev_row = df.iloc[-2]

        # 必要なデータチェック
        if pd.isna(latest_row["ma5"]) or pd.isna(latest_row["ma25"]) or pd.isna(prev_row["ma5"]) or pd.isna(latest_row["rsi"]):
            return None

        current_price = float(latest_row["close"])
        ma5 = float(latest_row["ma5"])
        ma5_prev = float(prev_row["ma5"])
        ma25 = float(latest_row["ma25"])
        rsi = float(latest_row["rsi"])

        # MA値が0または負の場合は異常データとしてスキップ
        if ma5 <= 0 or ma25 <= 0 or ma5_prev <= 0:
            self.logger.debug(
                f"ゴールデンクロス直前スキップ: {stock_name}({stock_code}) - "
                f"MA値が異常（5日MA: {ma5:.2f}, 25日MA: {ma25:.2f}）"
            )
            return None

        # 平均出来高（25日）を計算
        avg_volume_25d = int(df["volume"].tail(25).mean())

        # 条件1: 5日MA < 25日MA（まだクロスしていない）
        if ma5 >= ma25:
            return None

        # 条件2: MA差が1%以内
        ma_diff_ratio = ((ma25 - ma5) / ma25) * 100
        if ma_diff_ratio > 1.0:
            return None

        # 条件3: 5日MAが上昇中
        ma5_change = ((ma5 - ma5_prev) / ma5_prev) * 100
        if ma5_change <= 0:
            return None

        # 条件4: RSI > 50
        if rsi <= 50:
            return None

        # 条件5: 平均出来高 >= 100,000株
        if avg_volume_25d < 100000:
            return None

        # スコア計算
        # 1. MA差率スコア（差が小さいほど高スコア、最大50点）
        ma_diff_score = (1.0 - ma_diff_ratio) * 50
        ma_diff_score = max(0, ma_diff_score)

        # 2. 5日MA上昇率スコア（上昇率×10）
        ma5_score = ma5_change * 10

        # 3. RSIスコア
        rsi_score = rsi / 10  # RSI 60で6点

        # 4. 出来高スコア
        current_volume = int(latest_row["volume"])
        volume_ratio = current_volume / avg_volume_25d if avg_volume_25d > 0 else 1.0
        volume_score = (volume_ratio - 1.0) * 3
        volume_score = max(0, volume_score)

        # 合計スコア
        score = ma_diff_score + ma5_score + rsi_score + volume_score

        return ScreenResult(
            stock_code=stock_code,
            stock_name=stock_name,
            category="golden_cross_approaching",
            score=score,
            details={
                "current_price": current_price,
                "ma5": ma5,
                "ma25": ma25,
                "ma_diff_ratio": round(ma_diff_ratio, 2),
                "ma5_change": round(ma5_change, 2),
                "rsi": round(rsi, 2),
                "volume_ratio": round(volume_ratio, 2),
                "avg_volume_25d": avg_volume_25d,
                "date": str(latest_row["date"]),
            },
        )

    def bb_lower_bounce_filter(
        self,
        stock_code: str,
        stock_name: str,
        df: pd.DataFrame,
    ) -> Optional[ScreenResult]:
        """
        ボリンジャーバンド下限反転銘柄を検出する（逆張り戦略）

        条件:
        1. 現在価格がBB下限の-5%〜+5%の範囲内
        2. RSI <= 30（売られ過ぎ）
        3. MACDヒストグラムが底を打っている
        4. 平均出来高 >= 100,000株

        スコア計算:
        - BB下限乖離スコア（最大15点）
        - RSIスコア（最大60点）
        - MACDスコア（変動）
        - 出来高スコア（変動）

        Args:
            stock_code: 銘柄コード
            stock_name: 銘柄名
            df: テクニカル指標を含むDataFrame

        Returns:
            ScreenResult または None
        """
        if df is None or len(df) < 2:
            return None

        latest_row = df.iloc[-1]

        # 必要なデータチェック
        if pd.isna(latest_row["bb_lower"]) or pd.isna(latest_row["rsi"]):
            return None

        current_price = float(latest_row["close"])
        bb_lower = float(latest_row["bb_lower"])
        rsi = float(latest_row["rsi"])

        # bb_lowerが0または負の場合は異常データとしてスキップ
        # ボリンジャーバンドは価格の標準偏差を使うため、通常は正の値
        if bb_lower <= 0:
            self.logger.debug(
                f"BB下限反転スキップ: {stock_name}({stock_code}) - "
                f"BB下限が異常値（{bb_lower:.2f}）"
            )
            return None

        # 平均出来高（25日）を計算
        avg_volume_25d = int(df["volume"].tail(25).mean())

        # 条件1: BB下限付近（-5%〜+5%の範囲内）
        bb_lower_deviation = ((current_price - bb_lower) / bb_lower) * 100
        if not (-5.0 <= bb_lower_deviation <= 5.0):
            return None

        # 条件2: RSI <= 30
        if rsi > 30:
            return None

        # 条件3: MACDヒストグラムが底を打っている
        macd_histogram = latest_row.get("macd_histogram", 0)
        macd_histogram_prev = df.iloc[-2].get("macd_histogram", 0)

        if pd.isna(macd_histogram) or pd.isna(macd_histogram_prev):
            return None

        macd_histogram = float(macd_histogram)
        macd_histogram_prev = float(macd_histogram_prev)
        macd_improvement = macd_histogram - macd_histogram_prev

        # MACDヒストグラムが改善していない場合は除外
        if macd_improvement <= 0:
            return None

        # 条件4: 平均出来高 >= 100,000株
        if avg_volume_25d < 100000:
            return None

        # スコア計算
        # 1. BB下限乖離スコア（下限に近いほど高スコア、最大15点）
        bb_score = (5.0 - abs(bb_lower_deviation)) * 3
        bb_score = max(0, bb_score)

        # 2. RSIスコア（売られ過ぎが強いほど高スコア、最大60点）
        rsi_score = (30 - rsi) * 2

        # 3. MACDスコア（改善度に応じて加点）
        macd_score = macd_improvement * 5

        # 4. 出来高スコア（前日の2倍で3点）
        current_volume = int(latest_row["volume"])
        volume_ratio = current_volume / avg_volume_25d if avg_volume_25d > 0 else 1.0
        volume_score = (volume_ratio - 1.0) * 3
        volume_score = max(0, volume_score)

        # 合計スコア
        score = bb_score + rsi_score + macd_score + volume_score

        return ScreenResult(
            stock_code=stock_code,
            stock_name=stock_name,
            category="bb_lower_bounce",
            score=score,
            details={
                "current_price": current_price,
                "bb_lower": bb_lower,
                "bb_lower_deviation": round(bb_lower_deviation, 2),
                "rsi": round(rsi, 2),
                "macd_histogram": round(macd_histogram, 2),
                "macd_histogram_prev": round(macd_histogram_prev, 2),
                "macd_improvement": round(macd_improvement, 2),
                "volume_ratio": round(volume_ratio, 2),
                "avg_volume_25d": avg_volume_25d,
                "date": str(latest_row["date"]),
            },
        )
