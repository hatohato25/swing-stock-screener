"""
レート制限管理モジュール

立花証券APIのレート制限(10リクエスト/秒)を管理します。
"""

import time
from threading import Lock
from collections import deque


class RateLimiter:
    """APIレート制限を管理するクラス"""

    def __init__(self, max_requests: int = 10, time_window: float = 1.0):
        """
        レート制限マネージャーを初期化する

        Args:
            max_requests: 時間ウィンドウあたりの最大リクエスト数
            time_window: 時間ウィンドウ(秒)
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: deque = deque()
        self.lock = Lock()

    def acquire(self) -> None:
        """
        リクエスト許可を取得する

        レート制限に達している場合は自動的に待機する
        """
        with self.lock:
            current_time = time.time()

            # 時間ウィンドウ外の古いリクエストを削除
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()

            # レート制限に達している場合は待機
            if len(self.requests) >= self.max_requests:
                # 最も古いリクエストが時間ウィンドウから外れるまで待機
                sleep_time = self.time_window - (current_time - self.requests[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    # 待機後、再度古いリクエストを削除
                    current_time = time.time()
                    while (
                        self.requests
                        and self.requests[0] <= current_time - self.time_window
                    ):
                        self.requests.popleft()

            # 現在のリクエストを記録
            self.requests.append(time.time())

    def get_wait_time(self) -> float:
        """
        次のリクエストまでの待機時間を取得する

        Returns:
            待機時間(秒)。すぐにリクエスト可能な場合は0.0
        """
        with self.lock:
            current_time = time.time()

            # 時間ウィンドウ外の古いリクエストを削除
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()

            # レート制限に達していない場合は待機不要
            if len(self.requests) < self.max_requests:
                return 0.0

            # 最も古いリクエストが時間ウィンドウから外れるまでの時間
            wait_time = self.time_window - (current_time - self.requests[0])
            return max(0.0, wait_time)

    def reset(self) -> None:
        """
        レート制限カウンターをリセットする

        主にテスト目的で使用
        """
        with self.lock:
            self.requests.clear()

    def get_current_usage(self) -> int:
        """
        現在の時間ウィンドウ内のリクエスト数を取得する

        Returns:
            現在のリクエスト数
        """
        with self.lock:
            current_time = time.time()

            # 時間ウィンドウ外の古いリクエストを削除
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()

            return len(self.requests)
