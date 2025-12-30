"""
銘柄情報取得APIモジュール

立花証券APIから銘柄の基本情報（PER/PBR/配当利回り等）を取得します。
"""

from typing import Dict, Any, Optional
import json
from src.api.auth import AuthManager
from src.api.rate_limiter import RateLimiter
from src.utils.logger import Logger
import requests


class StockInfoClient:
    """銘柄情報取得クライアント（CLMMfdsGetIssueDetail）"""

    def __init__(
        self,
        auth_manager: AuthManager,
        rate_limiter: RateLimiter,
        logger: Logger,
    ):
        """
        銘柄情報クライアントを初期化する

        Args:
            auth_manager: 認証マネージャー
            rate_limiter: レート制限マネージャー
            logger: ロガー
        """
        self.auth_manager = auth_manager
        self.rate_limiter = rate_limiter
        self.logger = logger

    def get_stock_info(self, issue_code: str) -> Optional[Dict[str, Any]]:
        """
        銘柄情報（PER/PBR/配当利回り/ROE等）を取得する

        Args:
            issue_code: 銘柄コード（例: "7203"）

        Returns:
            銘柄情報辞書（PER/PBR/配当利回り/ROE等）
            {
                'per': float,  # PER（予想）
                'pbr': float,  # PBR（実績）
                'dividend_yield': float,  # 配当利回り（予想）
                'roe': float,  # ROE（予想）
            }
            取得失敗時はNone
        """
        # レート制限を適用
        self.rate_limiter.acquire()

        # リクエストパラメータを構築
        request_params = {
            "p_no": self.auth_manager.get_next_p_no(),
            "p_sd_date": self.auth_manager._format_p_sd_date(),
            "sCLMID": "CLMMfdsGetIssueDetail",
            # 銘柄コード（APIリファレンス: sTargetIssueCode）
            "sTargetIssueCode": issue_code,
            "sJsonOfmt": "5",
        }

        # リクエストURL構築（仮想URL + JSONパラメータ）
        virtual_url = self.auth_manager.get_virtual_url_master()
        url = f"{virtual_url}?{json.dumps(request_params)}"

        try:
            # API呼び出し
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # レスポンスをパース
            response_data = response.json()

            # デバッグログを削減（パフォーマンス向上）
            # self.logger.debug(
            #     f"API Full Response for {issue_code}: "
            #     f"{json.dumps(response_data, ensure_ascii=False, indent=2)}"
            # )

            # エラーチェック（CLMMfdsGetIssueDetailはp_errnoのみで判定）
            # 注: sResultCodeは注文系APIのみで、情報取得系APIには存在しない
            p_errno = int(response_data.get("p_errno", -1))
            if p_errno != 0:
                self.logger.warning(
                    f"銘柄情報取得失敗: {issue_code} (p_errno={p_errno})"
                )
                return None

            # レスポンスから銘柄詳細配列を取得
            issue_details = response_data.get("aCLMMfdsIssueDetail", [])
            if not issue_details:
                self.logger.warning(
                    f"銘柄情報なし: {issue_code} (aCLMMfdsIssueDetailが空)"
                )
                return None

            # 最初の銘柄データ（通常1銘柄のみリクエストするため）を取得
            issue_data = issue_details[0] if issue_details else {}

            # デバッグログを削減（パフォーマンス向上）
            # self.logger.debug(
            #     f"銘柄詳細レスポンス: {issue_code} "
            #     f"pRPER={issue_data.get('pRPER')}, "
            #     f"pSPBR={issue_data.get('pSPBR')}, "
            #     f"pSYIE={issue_data.get('pSYIE')}"
            # )

            # 必要な情報を抽出
            stock_info = self._extract_stock_info(issue_data, issue_code)

            # デバッグログを削減（パフォーマンス向上）
            # if stock_info:
            #     self.logger.debug(
            #         f"銘柄情報取得成功: {issue_code} "
            #         f"PER={stock_info.get('per')}, "
            #         f"PBR={stock_info.get('pbr')}, "
            #         f"配当利回り={stock_info.get('dividend_yield')}"
            #     )

            return stock_info

        except requests.exceptions.RequestException as e:
            self.logger.warning(f"銘柄情報取得エラー: {issue_code} - {str(e)}")
            return None
        except (ValueError, KeyError) as e:
            self.logger.warning(
                f"銘柄情報パースエラー: {issue_code} - {str(e)}"
            )
            return None

    def _extract_stock_info(
        self, response_data: Dict[str, Any], issue_code: str
    ) -> Optional[Dict[str, Any]]:
        """
        APIレスポンスから必要な情報を抽出する

        Args:
            response_data: APIレスポンス
            issue_code: 銘柄コード（ログ用）

        Returns:
            抽出した銘柄情報辞書
            データ不足時はNone
        """
        try:
            # PER（予想）: pRPER
            per_str = response_data.get("pRPER", "")
            per = float(per_str) if per_str and per_str != "---" else None

            # PBR（実績）: pSPBR
            pbr_str = response_data.get("pSPBR", "")
            pbr = float(pbr_str) if pbr_str and pbr_str != "---" else None

            # 配当利回り（予想）: pSYIE（%表記）
            dividend_yield_str = response_data.get("pSYIE", "")
            dividend_yield = (
                float(dividend_yield_str)
                if dividend_yield_str and dividend_yield_str != "---"
                else None
            )

            # ROE（予想）: pROEL（%表記）
            roe_str = response_data.get("pROEL", "")
            roe = float(roe_str) if roe_str and roe_str != "---" else None

            # PER/PBR/配当利回りが全て取得できない場合はNone
            if per is None and pbr is None and dividend_yield is None:
                self.logger.warning(
                    f"銘柄情報不足: {issue_code} "
                    f"(PER/PBR/配当利回りすべて未取得)"
                )
                return None

            return {
                "per": per,
                "pbr": pbr,
                "dividend_yield": dividend_yield,
                "roe": roe,
            }

        except (ValueError, TypeError) as e:
            self.logger.warning(f"銘柄情報抽出エラー: {issue_code} - {str(e)}")
            return None
