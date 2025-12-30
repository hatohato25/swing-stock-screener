"""
設定管理モジュール

環境変数とアプリケーション設定を管理します。
"""

import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """アプリケーション設定を管理するクラス"""

    def __init__(self):
        """
        設定を初期化する

        .envファイルが存在する場合は環境変数を読み込む
        """
        # プロジェクトルートディレクトリのパス
        self.project_root = Path(__file__).parent.parent.parent

        # .envファイルを読み込み
        env_path = self.project_root / ".env"
        if env_path.exists():
            load_dotenv(env_path)

        # 必須環境変数のチェック
        self._validate_required_env()

    def _validate_required_env(self) -> None:
        """
        必須環境変数が設定されているか検証する

        Raises:
            ValueError: 必須環境変数が未設定の場合
        """
        # Phase 7修正: 必須環境変数を新しい認証方式に変更
        required_vars = ["TACHIBANA_USER_ID", "TACHIBANA_PASSWORD"]

        missing_vars = [var for var in required_vars if not os.getenv(var)]

        if missing_vars:
            raise ValueError(
                f'以下の必須環境変数が設定されていません: {", ".join(missing_vars)}\n'
                f".envファイルを作成するか、環境変数を設定してください。"
            )

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        環境変数の値を取得する

        Args:
            key: 環境変数名
            default: デフォルト値（環境変数が未設定の場合に返す値）

        Returns:
            環境変数の値、または default
        """
        return os.getenv(key, default)

    # Phase 7修正: 旧コード（APIキー方式）をコメントアウト
    # @property
    # def api_key(self) -> str:
    #     """立花証券APIキーを取得する"""
    #     key = self.get("TACHIBANA_API_KEY")
    #     if not key:
    #         raise ValueError("TACHIBANA_API_KEY が設定されていません")
    #     return key

    # @property
    # def base_url(self) -> str:
    #     """APIベースURLを取得する"""
    #     return self.get("BASE_URL", "https://api.tachibana.example.com")

    # Phase 7修正: 新コード（ユーザーID/パスワード方式）
    @property
    def user_id(self) -> str:
        """立花証券ユーザーIDを取得する"""
        user_id = self.get("TACHIBANA_USER_ID")
        if not user_id:
            raise ValueError("TACHIBANA_USER_ID が設定されていません")
        return user_id

    @property
    def password(self) -> str:
        """立花証券パスワードを取得する"""
        password = self.get("TACHIBANA_PASSWORD")
        if not password:
            raise ValueError("TACHIBANA_PASSWORD が設定されていません")
        return password

    @property
    def environment(self) -> str:
        """環境（prod/demo）を取得する"""
        env = self.get("TACHIBANA_ENVIRONMENT", "demo")
        if env not in ["prod", "demo"]:
            raise ValueError(
                f"TACHIBANA_ENVIRONMENT は 'prod' または 'demo' である必要があります: {env}"
            )
        return env

    @property
    def auth_url(self) -> str:
        """
        認証エンドポイントURLを取得する

        Returns:
            環境に応じた認証URL
        """
        if self.environment == "prod":
            return "https://kabuka.e-shiten.jp/e_api_v4r8/auth/"
        else:
            return "https://demo-kabuka.e-shiten.jp/e_api_v4r8/auth/"

    @property
    def log_level(self) -> str:
        """ログレベルを取得する"""
        return self.get("LOG_LEVEL", "INFO")

    @property
    def report_output_dir(self) -> Path:
        """レポート出力ディレクトリを取得する"""
        output_dir = self.get("REPORT_OUTPUT_DIR", "docs")
        return self.project_root / output_dir
