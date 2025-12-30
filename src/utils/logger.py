"""
ログ記録モジュール

アプリケーション全体のログ記録を管理します。
"""

import logging
import sys
from datetime import datetime
from pathlib import Path


class Logger:
    """ログ記録を管理するクラス"""

    def __init__(self, log_dir: str = "data/logs", name: str = "kabu-report"):
        """
        ロガーを初期化する

        Args:
            log_dir: ログファイルを保存するディレクトリ
            name: ロガー名
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # 既存のハンドラーをクリア（重複を防ぐ）
        self.logger.handlers.clear()

        self._setup_handlers()

    def _setup_handlers(self) -> None:
        """ログハンドラーを設定する"""
        # フォーマッター
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # ファイルハンドラー（日付ごとのログファイル）
        log_file = self.log_dir / f'{datetime.now().strftime("%Y-%m-%d")}.log'
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # コンソールハンドラー（標準出力）
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def set_level(self, level: str) -> None:
        """
        ログレベルを設定する

        Args:
            level: ログレベル（DEBUG, INFO, WARNING, ERROR, CRITICAL）
        """
        numeric_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.setLevel(numeric_level)
        for handler in self.logger.handlers:
            handler.setLevel(numeric_level)

    def info(self, message: str) -> None:
        """INFOレベルのログを出力する"""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """WARNINGレベルのログを出力する"""
        self.logger.warning(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """
        ERRORレベルのログを出力する

        Args:
            message: ログメッセージ
            exc_info: 例外情報を含めるかどうか
        """
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """DEBUGレベルのログを出力する"""
        self.logger.debug(message)

    def critical(self, message: str) -> None:
        """CRITICALレベルのログを出力する"""
        self.logger.critical(message)
