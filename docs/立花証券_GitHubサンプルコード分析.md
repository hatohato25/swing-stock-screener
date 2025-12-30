# 立花証券 GitHub サンプルコード分析

## 概要

立花証券のGitHubアカウント（[e-shiten-jp](https://github.com/e-shiten-jp)）には、e支店APIを利用するための28個のサンプルリポジトリが公開されています。すべて電話認証対応で、Python（一部Excel VBA）で実装されています。

**API バージョン**: v4r7
**テスト環境**: Python 3.11.2, Debian 12
**ライセンス**: MIT

---

## 🚨 重要な共通注意事項

すべてのサンプルコードに共通する重要な警告：

> **本番環境に接続した場合、実際に注文を出せます。市場で条件が一致して約定した場合、取り消せません。**

- 利用者は自己責任で使用すること
- 利用時間外の接続時はエラーコード `"p_errno":"9"` が返される
- 著作者は一切の責任を負わない

---

## 📦 スウィング取引システムに有用なリポジトリ

### 1. 認証・ログイン

#### [e_api_login_tel.py](https://github.com/e-shiten-jp/e_api_login_tel.py)
**目的**: 電話認証後のログインと仮想URL取得

**認証フロー**:
1. 電話認証を完了する
2. 3分以内にスクリプトを実行
3. 仮想URL（1日券）を取得

**設定ファイル**: `e_api_account_info.txt`
- ユーザーID
- パスワード
- 第2パスワード
- 接続URL
- JSON形式設定

**出力ファイル**:
- `e_api_info_p_no.txt` - 現在のp_no値
- `e_api_login_response.txt` - 仮想URL（request, master, price, event の各エンドポイント）

**使用タイミング**: すべてのAPI操作の前提条件

---

### 2. マスターデータ取得

#### [e_api_get_master_tel.py](https://github.com/e-shiten-jp/e_api_get_master_tel.py)
**目的**: 銘柄マスターデータの一括ダウンロード

**取得可能なデータ**:
- 銘柄コード
- 銘柄名
- 銘柄名略称
- 銘柄名カナ
- 銘柄名英語
- 優先市場
- 業種コード

**データ制限**: 株式銘柄マスタ（CLMIssueMstKabu）では一部フィールドのみ機能

**付属機能**: `read_master.py` で営業日情報取得可能

**スウィング取引での用途**:
- 銘柄スクリーニング用マスターデータ作成
- 業種分類による絞り込み
- 銘柄名での検索・フィルタリング

---

### 3. 株価データ取得

#### [e_api_get_histrical_price_daily.py](https://github.com/e-shiten-jp/e_api_get_histrical_price_daily.py)
**目的**: 日足（ローソク足）株価データの取得

**設定パラメータ**:
- `my_sIssueCode`: 銘柄コード（通常株4桁、優先株5桁）
- `my_sSizyouC`: 市場コード（00 = 東証）
- `my_fname_output`: 出力CSVファイル名

**出力形式**: CSV（Shift-JIS エンコーディング）

**注意事項**:
- 取引時間外はエラーコード"9"を返す
- スナップショットと日足取得に対応している指数・通貨ペアはCSVファイルで文書化

**スウィング取引での用途**:
- 過去の価格トレンド分析
- テクニカル指標の計算（移動平均、ボリンジャーバンドなど）
- バックテスト用データ収集

---

#### [e_api_get_price_from_file_tel.py](https://github.com/e-shiten-jp/e_api_get_price_from_file_tel.py)
**目的**: CSVファイルから銘柄リストを読み込み、スナップショット株価を一括取得

**入力ファイル**: `price_list_in.csv`
- 1行目: 取得データ項目（`stock_code` 固定、以降は `pDPP,tDPP:T` のようなデータコード）
- 2行目以降: 銘柄コード（1行1銘柄）

**処理フロー**:
1. ファイルから銘柄リスト・取得項目を読み出し
2. APIで株価を取得
3. 結果を `price_list_out.csv` に出力

**スウィング取引での用途**:
- 監視銘柄リストの一括価格チェック
- スクリーニング条件に合致した銘柄の現在値取得
- 朝8時の自動取得処理に最適

---

### 4. リアルタイムデータ受信

#### [e_api_event_receive.py](https://github.com/e-shiten-jp/e_api_event_receive.py)
**目的**: 約定・株価変動のリアルタイムプッシュ通知受信

**主要機能**:
1. Event I/Fへの接続（仮想URL認証後）
2. 複数銘柄の同時監視（サンプルでは3銘柄）
3. 指定時間後の自動シャットダウン

**設定項目**:
- 行番号（1-120の範囲でティッカー識別）
- 銘柄コード（通常株4桁、優先株5桁）
- 市場指定（現在は東証のみ）
- 稼働時間（分単位）

**スウィング取引での用途**:
- 急騰・急落アラート
- エントリー/エグジットのタイミング通知
- ただし、スウィング取引は日次判断が主のため優先度は低い

---

#### [e_api_websocket_receive_tel.py](https://github.com/e-shiten-jp/e_api_websocket_receive_tel.py)
**目的**: WebSocketによる約定・株価プッシュ通知の受信（暫定版）

**実装特性**:
- 電話認証後の仮想URL（1日券）を使用
- Shift-JIS文字コードでデータ返却
- 設定ファイルと同一ディレクトリでの実行が必須

**エラーハンドリング**:
- 利用時間外: `"p_errno":"9"` (システム・サービス停止中)

**スウィング取引での用途**:
- event_receive.py と同様、リアルタイム監視
- WebSocket実装の参考コード

---

### 5. ニュース取得

#### [e_api_get_news_header_tel.py](https://github.com/e-shiten-jp/e_api_get_news_header_tel.py)
**目的**: ニュースヘッダー（見出し）の取得

**スウィング取引での用途**:
- 銘柄関連ニュースの確認
- 決算発表・業績修正などのイベント検出

---

#### [e_api_get_news_body_tel.py](https://github.com/e-shiten-jp/e_api_get_news_body_tel.py)
**目的**: ニュースIDを指定してニュース本文を取得

**スウィング取引での用途**:
- ヘッダーで検出したニュースの詳細取得
- ファンダメンタル分析の補助

---

## 🎯 スウィング取引システムへの適用戦略

### 必須コンポーネント

1. **認証**: `e_api_login_tel.py`
   - GitHub Actions実行前に仮想URL取得
   - 1日券のため毎日実行が必要

2. **マスターデータ**: `e_api_get_master_tel.py`
   - 定期的（週次など）にマスター更新
   - 銘柄フィルタリングの基礎データ

3. **日足データ**: `e_api_get_histrical_price_daily.py`
   - テクニカル分析用の過去データ取得
   - スクリーニング条件の計算

4. **スナップショット**: `e_api_get_price_from_file_tel.py`
   - 平日朝8時の自動実行
   - 監視銘柄リストの価格一括取得

### オプションコンポーネント

5. **ニュース**: `e_api_get_news_header_tel.py` / `e_api_get_news_body_tel.py`
   - レポートに銘柄関連ニュースを追加
   - ファンダメンタル要因の補足

6. **リアルタイム**: `e_api_event_receive.py` / `e_api_websocket_receive_tel.py`
   - スウィング取引では優先度低（日次判断が主）
   - 将来的なアラート機能で検討

---

## 📁 推奨ファイル構成

```
swing-stock-screener/
├── src/
│   ├── auth/
│   │   └── login.py          # e_api_login_tel.py を参考
│   ├── data/
│   │   ├── master.py         # e_api_get_master_tel.py を参考
│   │   ├── daily_price.py    # e_api_get_histrical_price_daily.py を参考
│   │   └── snapshot.py       # e_api_get_price_from_file_tel.py を参考
│   ├── screening/
│   │   └── filters.py        # スクリーニングロジック
│   └── report/
│       └── generator.py      # レポート生成
├── config/
│   └── e_api_account_info.txt
├── data/
│   ├── master/               # マスターデータ保存
│   ├── daily/                # 日足データ保存
│   └── watchlist.csv         # 監視銘柄リスト
└── .github/
    └── workflows/
        └── daily-screening.yml
```

---

## 🔧 実装時の注意点

### 文字コード
- API応答は **Shift-JIS** エンコーディング
- Python での処理時に `encoding='shift-jis'` を指定

### 認証の有効期限
- 仮想URLは **1日券**（翌営業日まで有効）
- GitHub Actions で毎日ログイン処理を実行

### 取引時間外のエラーハンドリング
- エラーコード `"p_errno":"9"` のハンドリング実装
- リトライロジックの追加検討

### 本番環境への接続
- **テスト時は必ずテスト環境URLを使用**
- 本番環境では実際の注文が発生する可能性

### API呼び出し頻度
- 過度なAPI呼び出しを避ける
- スロットリング・レート制限の実装を検討

---

## 📚 次のステップ

1. **サンプルコードのダウンロード**
   - 主要リポジトリをクローン
   - 認証・データ取得部分を抽出

2. **認証フローの実装**
   - `e_api_login_tel.py` をベースにログイン機能作成
   - GitHub Actions Secrets に認証情報を設定

3. **データ取得パイプラインの構築**
   - マスターデータ → 日足データ → スナップショット の順で実装
   - 各処理を独立したモジュールとして設計

4. **スクリーニングロジックの実装**
   - テクニカル指標の計算
   - フィルタリング条件の適用

5. **レポート生成とGitHub Pages公開**
   - Markdown/HTML形式でのレポート作成
   - GitHub Actions での自動公開

---

## 📝 参考リンク

- [立花証券 GitHub アカウント](https://github.com/e-shiten-jp)
- [API リファレンス完全版](../立花証券_API_リファレンス_完全版.md)
- [立花証券 e支店 公式サイト](https://e-shiten.jp/)

---

**最終更新**: 2025-11-21
**作成者**: Claude Code
