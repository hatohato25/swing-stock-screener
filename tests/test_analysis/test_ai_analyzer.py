"""
GeminiReportAnalyzerクラスの単体テスト

モックAPIを使用して、API呼び出しやファイル読み込みをテストします。
"""

import unittest
from unittest.mock import Mock, patch, mock_open
import requests
from pathlib import Path
import tempfile
import shutil

from src.analysis.ai_analyzer import GeminiReportAnalyzer


class TestGeminiReportAnalyzer(unittest.TestCase):
    """GeminiReportAnalyzerクラスのテストケース"""

    def setUp(self):
        """各テストメソッドの実行前に呼ばれる初期化処理"""
        self.api_key = "test_api_key_12345678"
        self.logger = Mock()
        self.analyzer = GeminiReportAnalyzer(self.api_key, self.logger)

    @patch('requests.post')
    def test_call_gemini_api_success(self, mock_post):
        """
        正常系: API呼び出しが成功し、期待通りの文字列が返る
        """
        # モックレスポンスを設定
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "テスト分析結果"
                            }
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        # テスト実行
        payload = {"test": "payload"}
        result = self.analyzer.call_gemini_api(payload)

        # アサーション
        self.assertEqual(result, "テスト分析結果")
        mock_post.assert_called_once()
        self.logger.info.assert_called()

    @patch('requests.post')
    def test_call_gemini_api_timeout(self, mock_post):
        """
        異常系: タイムアウトが発生し、TimeoutErrorが発生する
        """
        # タイムアウトを発生させる
        mock_post.side_effect = requests.exceptions.Timeout()

        # テスト実行
        payload = {"test": "payload"}

        # アサーション: TimeoutErrorが発生することを確認
        with self.assertRaises(TimeoutError):
            self.analyzer.call_gemini_api(payload)

        self.logger.error.assert_called()

    @patch('requests.post')
    def test_call_gemini_api_empty_response(self, mock_post):
        """
        異常系: 空のレスポンスが返り、ValueErrorが発生する
        """
        # 空のレスポンスを設定
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": ""
                            }
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        # テスト実行
        payload = {"test": "payload"}

        # アサーション: ValueErrorが発生することを確認
        with self.assertRaises(ValueError):
            self.analyzer.call_gemini_api(payload)

        self.logger.error.assert_called()

    @patch('requests.post')
    def test_call_gemini_api_request_exception(self, mock_post):
        """
        異常系: リクエスト例外が発生し、ValueErrorが発生する
        """
        # リクエスト例外を発生させる
        mock_post.side_effect = requests.exceptions.RequestException("Network error")

        # テスト実行
        payload = {"test": "payload"}

        # アサーション: ValueErrorが発生することを確認
        with self.assertRaises(ValueError):
            self.analyzer.call_gemini_api(payload)

        self.logger.error.assert_called()

    def test_read_latest_report_success(self):
        """
        正常系: 最新レポートを正しく読み込み、期待通りの結果が返る
        """
        # 一時ディレクトリを作成
        temp_dir = tempfile.mkdtemp()

        try:
            # テスト用のレポートファイルを作成
            test_dates = ["2025-01-01", "2025-01-02", "2025-01-03"]
            for date in test_dates:
                date_dir = Path(temp_dir) / date
                date_dir.mkdir(parents=True, exist_ok=True)
                report_path = date_dir / "README.md"
                report_path.write_text(f"# レポート {date}", encoding="utf-8")

            # テスト実行（最新は 2025-01-03）
            report_date, report_content = self.analyzer.read_latest_report(docs_dir=temp_dir)

            # アサーション
            self.assertEqual(report_date, "2025-01-03")
            self.assertEqual(report_content, "# レポート 2025-01-03")
            self.logger.info.assert_called()

        finally:
            # 一時ディレクトリを削除
            shutil.rmtree(temp_dir)

    def test_read_latest_report_not_found(self):
        """
        異常系: レポートディレクトリが存在せず、FileNotFoundErrorが発生する
        """
        # 一時ディレクトリを作成（空）
        temp_dir = tempfile.mkdtemp()

        try:
            # テスト実行
            # アサーション: FileNotFoundErrorが発生することを確認
            with self.assertRaises(FileNotFoundError):
                self.analyzer.read_latest_report(docs_dir=temp_dir)

            self.logger.error.assert_called()

        finally:
            # 一時ディレクトリを削除
            shutil.rmtree(temp_dir)

    def test_read_report_by_date_success(self):
        """
        正常系: 指定日付のレポートを正しく読み込み、期待通りの結果が返る
        """
        # 一時ディレクトリを作成
        temp_dir = tempfile.mkdtemp()

        try:
            # テスト用のレポートファイルを作成
            date = "2025-01-02"
            date_dir = Path(temp_dir) / date
            date_dir.mkdir(parents=True, exist_ok=True)
            report_path = date_dir / "README.md"
            report_path.write_text(f"# レポート {date}", encoding="utf-8")

            # テスト実行
            report_content = self.analyzer.read_report_by_date(date, docs_dir=temp_dir)

            # アサーション
            self.assertEqual(report_content, "# レポート 2025-01-02")
            self.logger.info.assert_called()

        finally:
            # 一時ディレクトリを削除
            shutil.rmtree(temp_dir)

    def test_read_report_by_date_invalid_format(self):
        """
        異常系: 日付形式が不正で、ValueErrorが発生する
        """
        # テスト実行
        # アサーション: ValueErrorが発生することを確認
        with self.assertRaises(ValueError):
            self.analyzer.read_report_by_date("2025/01/02")

        self.logger.error.assert_called()

    def test_read_report_by_date_not_found(self):
        """
        異常系: 指定日付のレポートが存在せず、FileNotFoundErrorが発生する
        """
        # 一時ディレクトリを作成（空）
        temp_dir = tempfile.mkdtemp()

        try:
            # テスト実行
            # アサーション: FileNotFoundErrorが発生することを確認
            with self.assertRaises(FileNotFoundError):
                self.analyzer.read_report_by_date("2025-01-01", docs_dir=temp_dir)

            self.logger.error.assert_called()

        finally:
            # 一時ディレクトリを削除
            shutil.rmtree(temp_dir)

    def test_generate_prompt(self):
        """
        正常系: プロンプトが正しく生成される
        """
        # テスト実行
        report_content = "# テストレポート\n\n銘柄情報..."
        payload = self.analyzer.generate_prompt(report_content)

        # アサーション
        self.assertIn("contents", payload)
        self.assertIn("systemInstruction", payload)
        self.assertIn("アナリスト", payload["systemInstruction"]["parts"][0]["text"])
        self.assertIn(report_content, payload["contents"][0]["parts"][0]["text"])

    @patch.object(GeminiReportAnalyzer, 'read_latest_report')
    @patch.object(GeminiReportAnalyzer, 'generate_prompt')
    @patch.object(GeminiReportAnalyzer, 'call_gemini_api')
    def test_analyze_without_date(self, mock_call_api, mock_gen_prompt, mock_read_latest):
        """
        正常系: 日付指定なしで分析を実行し、最新レポートが使用される
        """
        # モック設定
        mock_read_latest.return_value = ("2025-01-03", "# レポート 2025-01-03")
        mock_gen_prompt.return_value = {"test": "payload"}
        mock_call_api.return_value = "AI分析結果"

        # テスト実行
        result = self.analyzer.analyze()

        # アサーション
        mock_read_latest.assert_called_once()
        mock_gen_prompt.assert_called_once_with("# レポート 2025-01-03")
        mock_call_api.assert_called_once()
        self.assertIn("AI分析結果", result)
        self.assertIn("免責事項", result)

    @patch.object(GeminiReportAnalyzer, 'read_report_by_date')
    @patch.object(GeminiReportAnalyzer, 'generate_prompt')
    @patch.object(GeminiReportAnalyzer, 'call_gemini_api')
    def test_analyze_with_date(self, mock_call_api, mock_gen_prompt, mock_read_by_date):
        """
        正常系: 日付指定ありで分析を実行し、指定日付のレポートが使用される
        """
        # モック設定
        mock_read_by_date.return_value = "# レポート 2025-01-02"
        mock_gen_prompt.return_value = {"test": "payload"}
        mock_call_api.return_value = "AI分析結果"

        # テスト実行
        result = self.analyzer.analyze(report_date="2025-01-02")

        # アサーション
        mock_read_by_date.assert_called_once_with("2025-01-02")
        mock_gen_prompt.assert_called_once_with("# レポート 2025-01-02")
        mock_call_api.assert_called_once()
        self.assertIn("AI分析結果", result)
        self.assertIn("免責事項", result)


if __name__ == '__main__':
    unittest.main()
