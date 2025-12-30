"""
銘柄マスターデータ取得モジュール

立花証券APIから銘柄マスターデータをダウンロードします。
GitHubサンプル（e_api_get_master_tel.py）を参考に実装
"""

import json
import urllib3
from typing import List, Dict, Any
from src.utils.logger import Logger
from src.api.auth import AuthManager


class MasterDataClient:
    """立花証券APIから銘柄マスターデータを取得するクライアント"""

    def __init__(self, auth_manager: AuthManager, logger: Logger):
        """
        マスターデータクライアントを初期化する

        Args:
            auth_manager: 認証マネージャー
            logger: ロガーオブジェクト
        """
        self.auth_manager = auth_manager
        self.logger = logger
        self.http = urllib3.PoolManager()

    def download_master_data(self) -> List[Dict[str, Any]]:
        """
        銘柄マスターデータをダウンロード

        API: CLMEventDownload
        エンドポイント: sUrlMaster（仮想URL）

        マスターデータはストリーミング形式で配信されます。
        各銘柄は1行のJSONとして返され、終端通知（CLMEventDownloadComplete）
        が送られてくるまで継続的に受信します。

        Returns:
            銘柄リスト（辞書のリスト）
            各銘柄には以下のフィールドを含む：
            - sIssueCode: 銘柄コード（4桁または5桁）
            - sIssueName: 銘柄名
            - sSizyouC: 市場コード
            - その他マスターデータ項目

        Raises:
            ValueError: マスターデータの取得に失敗した場合
        """
        # リクエストパラメータを構築
        request_params = {
            "p_no": self.auth_manager.get_next_p_no(),
            "p_sd_date": self.auth_manager._format_p_sd_date(),
            "sCLMID": "CLMEventDownload",
            "sJsonOfmt": "4",  # マスターデータは"4"推奨（引数項目名称のみ）
        }

        # URLを構築（仮想URLマスター + JSONパラメータ）
        url = f"{self.auth_manager.get_virtual_url_master()}?{json.dumps(request_params)}"

        self.logger.info("銘柄マスターデータをダウンロード中...")
        self.logger.debug(f"マスターデータURL: {url[:100]}...")

        try:
            # ストリーム形式で接続（大容量データのため）
            response = self.http.request("GET", url, preload_content=False, timeout=120)

            if response.status != 200:
                error_msg = f"マスターデータ取得失敗: HTTPステータス={response.status}"
                self.logger.error(error_msg)
                raise ValueError(error_msg)

            master_data = []
            byte_buffer = b""
            download_count = 0
            terminate_string = "CLMEventDownloadComplete"

            self.logger.info("マスターデータのストリーミング受信を開始します")
            self.logger.info("データサイズが大きいため時間がかかります（約21MB）")

            # ストリームからデータを読み込む
            for chunk in response.stream(1024):
                byte_buffer += chunk

                # JSON終端（'}'）を検出したらデータを処理
                if byte_buffer[-1:] == b"}":
                    download_count += 1

                    # Shift-JISでデコード（立花証券APIの仕様）
                    try:
                        text_data = byte_buffer.decode("shift-jis", errors="ignore")
                        data = json.loads(text_data)

                        # 終了通知をチェック
                        if data.get("sCLMID") == terminate_string:
                            self.logger.info(f"マスターデータダウンロード完了: {download_count}件")
                            self.logger.debug(f"終了通知: {data}")
                            break

                        # 通常の銘柄データを追加
                        master_data.append(data)

                        # 進捗表示（2000件ごと）
                        if download_count % 2000 == 0:
                            self.logger.info(f"ダウンロード進捗: {download_count}件")

                    except json.JSONDecodeError as e:
                        self.logger.warning(f"JSON解析エラー（スキップ）: {e}")

                    # バッファをクリア
                    byte_buffer = b""

            # ストリームを閉じる
            response.release_conn()

            if not master_data:
                error_msg = "マスターデータが空です"
                self.logger.error(error_msg)
                raise ValueError(error_msg)

            self.logger.info(f"銘柄マスターデータ取得完了: {len(master_data)}件")
            return master_data

        except urllib3.exceptions.HTTPError as e:
            error_msg = f"HTTP通信エラー: {str(e)}"
            self.logger.error(error_msg)
            raise ValueError(error_msg)

        except Exception as e:
            error_msg = f"マスターデータ取得エラー: {str(e)}"
            self.logger.error(error_msg, exc_info=True)
            raise ValueError(error_msg)
