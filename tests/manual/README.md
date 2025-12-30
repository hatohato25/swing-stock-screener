# Manual Tests

このディレクトリには、手動実行用のテストスクリプトが含まれています。

## ファイル一覧

### test_api_connection.py
立花証券APIへの接続テスト。認証フロー（電話認証→ログイン→仮想URL取得）を検証します。

**実行方法**:
```bash
python3 tests/manual/test_api_connection.py
```

### test_api_data_parse.py
APIレスポンスのパース処理テスト。JSON形式のレスポンスを正しく解析できるか検証します。

**実行方法**:
```bash
python3 tests/manual/test_api_data_parse.py
```

### test_stock_info.py
銘柄情報取得APIのテスト。PER/PBR/配当利回り/ROE等の基本情報を取得できるか検証します。

**実行方法**:
```bash
python3 tests/manual/test_stock_info.py
```

### test_value_stock_api.py
バリュー株スクリーニングのテスト。複数銘柄の情報を一括取得し、スクリーニング条件を検証します。

**実行方法**:
```bash
python3 tests/manual/test_value_stock_api.py
```

## 注意事項

- これらのテストは立花証券APIに実際に接続します
- `.env`ファイルに認証情報（`TACHIBANA_USER_ID`, `TACHIBANA_PASSWORD`）を設定してください
- API制限（10リクエスト/秒）を考慮して実行してください
- 本番環境（`TACHIBANA_ENVIRONMENT=prod`）での実行には注意してください

## 自動テストとの違い

`tests/`ディレクトリ配下の自動テスト（pytest）とは異なり、これらのスクリプトは：

- API接続を伴う統合テスト
- 手動実行が前提
- デバッグ・検証目的
- CI/CDでは実行されない

自動テスト（pytest）は`tests/test_*`ディレクトリにあり、モック・スタブを使用してAPI接続なしで実行できます。
