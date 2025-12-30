"""
API認証管理モジュール

立花証券APIの認証処理を管理します。
Phase 7修正: Bearer認証からユーザーID/パスワード認証に変更
Phase 7追加修正: GitHubサンプルに基づき必須パラメータ追加
"""

import datetime
import json
import requests
from typing import Dict, Optional
from src.utils.config import Config
from src.utils.logger import Logger

# ロガーを初期化
logger = Logger(log_dir="data/logs")


class AuthManager:
    """API認証を管理するクラス"""

    def __init__(self, config: Config):
        """
        認証マネージャーを初期化する

        Args:
            config: 設定オブジェクト
        """
        self.config = config
        # Phase 7修正: 仮想URLを保持
        self.virtual_url_request: Optional[str] = None
        self.virtual_url_master: Optional[str] = None
        self.virtual_url_price: Optional[str] = None
        self.session_info: Optional[Dict] = None
        # Phase 8追加: p_no管理（リクエスト番号）
        self.p_no: int = 1  # 初回ログイン時は1

    # Phase 7修正: 旧コード（Bearer認証）をコメントアウト
    # def get_headers(self) -> Dict[str, str]:
    #     """
    #     認証ヘッダーを取得する
    #
    #     Returns:
    #         認証情報を含むHTTPヘッダー辞書
    #
    #     Raises:
    #         ValueError: APIキーが未設定の場合
    #     """
    #     api_key = self.config.api_key
    #
    #     return {
    #         "Authorization": f"Bearer {api_key}",
    #         "Content-Type": "application/json",
    #         "Accept": "application/json",
    #     }

    # def validate_credentials(self) -> bool:
    #     """
    #     認証情報が有効かどうかを検証する
    #
    #     Returns:
    #         認証情報が有効な場合True
    #
    #     Note:
    #         実際のAPI呼び出しは行わず、設定の存在のみをチェックする
    #     """
    #     try:
    #         _ = self.config.api_key
    #         return True
    #     except ValueError:
    #         return False

    # Phase 7修正: 新コード（ユーザーID/パスワード認証）
    # Phase 7追加修正: GitHubサンプルに基づき必須パラメータ追加
    def _format_p_sd_date(self) -> str:
        """
        p_sd_date形式のタイムスタンプを生成する

        Format: YYYY.MM.DD-HH:MM:SS.sss

        Returns:
            タイムスタンプ文字列

        Example:
            2025.12.25-01:56:46.123
        """
        now = datetime.datetime.now()
        return (
            f"{now.year}."
            f"{now.month:02d}."
            f"{now.day:02d}-"
            f"{now.hour:02d}:"
            f"{now.minute:02d}:"
            f"{now.second:02d}."
            f"{now.microsecond // 1000:03d}"
        )

    def get_next_p_no(self) -> str:
        """
        次のp_noを取得してインクリメントする

        Returns:
            現在のp_no（文字列形式）

        Note:
            ログイン後、各APIリクエストでp_noを順次インクリメントする必要がある
        """
        current = self.p_no
        self.p_no += 1
        logger.debug(f"p_no取得: {current} (次回: {self.p_no})")
        return str(current)

    def login(self) -> bool:
        """
        ログイン処理を実行し、仮想URLを取得する

        Returns:
            ログイン成功時はTrue、失敗時はFalse

        Raises:
            ValueError: ログインに失敗した場合
        """
        # CLMAuthLoginRequestを構築
        # GitHubサンプルに基づき必須パラメータを追加
        # Phase 8修正: p_noは初回固定値"1"（ログイン時のみ）
        login_request = {
            "p_no": "1",  # リクエスト番号（初回は"1"）
            "p_sd_date": self._format_p_sd_date(),  # タイムスタンプ
            "sCLMID": "CLMAuthLoginRequest",
            "sUserId": self.config.user_id,
            "sPassword": self.config.password,
            "sJsonOfmt": "5",  # レスポンス形式（5=ブラウザ見やすい形式 + 引数項目名称）
        }

        # JSONパラメータをURL形式で送信
        # 立花証券APIの仕様: auth/?{JSON引数}
        url = f"{self.config.auth_url}?{json.dumps(login_request)}"

        # デバッグログ
        logger.info(f"認証リクエスト送信: p_no=1, p_sd_date={login_request['p_sd_date']}")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # レスポンスをパース
            response_data = response.json()

            # デバッグログ
            logger.info(f"認証レスポンス受信: {json.dumps(response_data, ensure_ascii=False, indent=2)}")

            # p_errnoをチェック（GitHubサンプルに基づく）
            p_errno = int(response_data.get("p_errno", -1))
            if p_errno != 0:
                logger.error(f"API通信エラー: p_errno={p_errno}")
                raise ValueError(f"API通信エラー: p_errno={p_errno}")

            # 結果コードをチェック
            result_code = response_data.get("sResultCode", "")
            if result_code != "0":
                result_text = response_data.get("sResultText", "Unknown error")
                logger.error(f"ログインエラー: [{result_code}] {result_text}")
                raise ValueError(
                    f"ログインに失敗しました: [{result_code}] {result_text}"
                )

            # 金商法未読フラグをチェック
            midoku_flg = response_data.get("sKinsyouhouMidokuFlg", "1")
            if midoku_flg == "1":
                logger.error("金商法交付書面が未読です")
                raise ValueError(
                    "金商法交付書面が未読です。e支店Webサイトで確認してください。"
                )

            # 仮想URLを保存
            self.virtual_url_request = response_data.get("sUrlRequest", "")
            self.virtual_url_master = response_data.get("sUrlMaster", "")
            self.virtual_url_price = response_data.get("sUrlPrice", "")

            if not self.virtual_url_request or not self.virtual_url_price:
                logger.error("仮想URLの取得に失敗しました")
                raise ValueError("仮想URLの取得に失敗しました")

            # セッション情報を保存
            self.session_info = response_data

            # Phase 8追加: ログイン後はp_noを2からスタート
            self.p_no = 2

            logger.info("認証成功: 仮想URL取得完了")
            logger.info(f"  REQUEST: {self.virtual_url_request[:50]}...")
            logger.info(f"  MASTER: {self.virtual_url_master[:50]}...")
            logger.info(f"  PRICE: {self.virtual_url_price[:50]}...")
            logger.info(f"  次回リクエストのp_no: {self.p_no}")

            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"ログインリクエストに失敗しました: {str(e)}")
            error_msg = (
                f"ログインリクエストに失敗しました: {str(e)}\n\n"
                "⚠️ 立花証券APIは電話認証が必須です。\n"
                "以下の手順で電話認証を実施してください：\n"
                "  1. 立花証券e支店Webサイト（https://www.e-shiten.jp/）にログイン\n"
                "  2. 電話認証を実施（自動音声ガイダンスに従う）\n"
                "  3. 3分以内にスクリプトを再実行\n\n"
                "電話認証の有効期限は3分間です。認証後すぐに実行してください。"
            )
            raise ValueError(error_msg)

    def get_virtual_url_request(self) -> str:
        """
        仮想URL（REQUEST）を取得する

        Returns:
            仮想URL

        Raises:
            ValueError: ログインしていない場合
        """
        if not self.virtual_url_request:
            raise ValueError("ログインしていません")
        return self.virtual_url_request

    def get_virtual_url_master(self) -> str:
        """
        仮想URL（MASTER）を取得する

        Returns:
            仮想URL

        Raises:
            ValueError: ログインしていない場合
        """
        if not self.virtual_url_master:
            raise ValueError("ログインしていません")
        return self.virtual_url_master

    def get_virtual_url_price(self) -> str:
        """
        仮想URL（PRICE）を取得する

        Returns:
            仮想URL

        Raises:
            ValueError: ログインしていない場合
        """
        if not self.virtual_url_price:
            raise ValueError("ログインしていません")
        return self.virtual_url_price

    def is_authenticated(self) -> bool:
        """
        認証済みかどうかを判定する

        Returns:
            認証済みの場合True
        """
        return bool(
            self.virtual_url_request
            and self.virtual_url_master
            and self.virtual_url_price
        )

    def get_headers(self) -> Dict[str, str]:
        """
        APIリクエスト用のHTTPヘッダーを取得する

        Returns:
            HTTPヘッダー辞書

        Note:
            仮想URLを使用する場合、Authorizationヘッダーは不要
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
