"""
立花証券APIクライアントモジュール

立花証券APIへのHTTPリクエストを管理します。
Phase 7修正: Bearer認証から仮想URL方式に変更
"""

import requests
from typing import Dict, Any, Optional
from src.utils.config import Config
from src.utils.logger import Logger
from src.api.auth import AuthManager
from src.api.rate_limiter import RateLimiter


class APIError(Exception):
    """API呼び出しエラー"""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_data: Optional[Dict] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(self.message)


class TachibanaAPIClient:
    """立花証券APIクライアント"""

    def __init__(self, config: Config, logger: Logger):
        """
        APIクライアントを初期化する

        Args:
            config: 設定オブジェクト
            logger: ロガーオブジェクト

        Raises:
            APIError: ログインに失敗した場合
        """
        self.config = config
        self.logger = logger
        self.auth_manager = AuthManager(config)
        self.rate_limiter = RateLimiter(max_requests=10, time_window=1.0)

        # Phase 7修正: 初期化時にログイン処理を実行
        self.logger.info("立花証券APIにログイン中...")
        try:
            if not self.auth_manager.login():
                raise APIError("ログインに失敗しました")
            self.logger.info("ログイン成功")
        except ValueError as e:
            self.logger.error(f"ログインエラー: {str(e)}")
            raise APIError(f"ログインに失敗しました: {str(e)}")

        # Phase 7修正: 旧コード（base_url）をコメントアウト
        # self.base_url = config.base_url

        self.timeout = 30  # タイムアウト(秒)

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        use_master_url: bool = False,
    ) -> Dict[str, Any]:
        """
        HTTPリクエストを実行する

        Args:
            method: HTTPメソッド(GET, POST等)
            endpoint: APIエンドポイント(/stocks等)
            params: クエリパラメータ
            json_data: JSONボディデータ
            use_master_url: マスターURL使用フラグ
                （デフォルト: False = PRICE URL）

        Returns:
            APIレスポンスのJSON

        Raises:
            APIError: API呼び出しに失敗した場合
        """
        # レート制限を適用
        self.rate_limiter.acquire()

        # Phase 7修正: 仮想URLを使用してリクエストを構築
        if use_master_url:
            base_url = self.auth_manager.get_virtual_url_master()
        else:
            base_url = self.auth_manager.get_virtual_url_price()

        url = f"{base_url}{endpoint}"
        headers = self.auth_manager.get_headers()

        try:
            self.logger.debug(f"API Request: {method} {url}")

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_data,
                timeout=self.timeout,
            )

            # ステータスコードチェック
            if response.status_code >= 400:
                error_message = f"API Error: {response.status_code}"
                try:
                    error_data = response.json()
                    error_detail = error_data.get("message", "Unknown error")
                    error_message += f" - {error_detail}"
                except Exception:
                    error_message += f" - {response.text}"

                self.logger.error(error_message)
                raise APIError(
                    message=error_message,
                    status_code=response.status_code,
                    response_data=response.json() if response.text else None,
                )

            # レスポンスをJSONとしてパース
            response_data = response.json()
            self.logger.debug(f"API Response: {response.status_code}")

            return response_data

        except requests.exceptions.Timeout:
            error_message = f"API request timeout: {url}"
            self.logger.error(error_message)
            raise APIError(message=error_message)

        except requests.exceptions.ConnectionError:
            error_message = f"API connection error: {url}"
            self.logger.error(error_message)
            raise APIError(message=error_message)

        except requests.exceptions.RequestException as e:
            error_message = f"API request failed: {str(e)}"
            self.logger.error(error_message)
            raise APIError(message=error_message)

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        GETリクエストを実行する

        Args:
            endpoint: APIエンドポイント
            params: クエリパラメータ

        Returns:
            APIレスポンスのJSON
        """
        return self._make_request("GET", endpoint, params=params)

    def post(
        self, endpoint: str, json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        POSTリクエストを実行する

        Args:
            endpoint: APIエンドポイント
            json_data: JSONボディデータ

        Returns:
            APIレスポンスのJSON
        """
        return self._make_request("POST", endpoint, json_data=json_data)

    def get_rate_limit_status(self) -> Dict[str, Any]:
        """
        レート制限の状態を取得する

        Returns:
            レート制限の状態情報
        """
        return {
            "current_usage": self.rate_limiter.get_current_usage(),
            "max_requests": self.rate_limiter.max_requests,
            "time_window": self.rate_limiter.time_window,
            "wait_time": self.rate_limiter.get_wait_time(),
        }
