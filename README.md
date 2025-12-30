# swing-stock-screener

スウィング取引向けの株式スクリーニングレポート自動生成システム

立花証券APIを活用し、個別株のテクニカル分析を自動実行し、GitHub Pagesで日次レポートを公開します。

---

## 📊 機能

### スクリーニング機能

- **出来高急増検出**: 前日比2倍以上の出来高急増を検出
- **テクニカルブレイクアウト**: 25日移動平均線の上抜けを検出
- **値上がり率ランキング**: 前日比5%以上の値上がり銘柄を抽出

### テクニカル指標

- 単純移動平均（SMA）
- 指数移動平均（EMA）
- RSI（相対力指数）
- ボリンジャーバンド
- 出来高比率
- 価格変化率

### レポート生成

- レスポンシブデザインのHTMLレポート
- 3カテゴリ別のランキング表示（各Top 20）
- 日付別アーカイブ
- GitHub Pagesで自動公開

### 自動化

- GitHub Actionsで手動実行可能
- エラー時の自動Issue作成

---

## 📊 実装状況

### ✅ Phase 1: API認証方式の修正（完了 2025-12-25）
- 電話認証対応
- p_no管理機能
- 仮想URL取得（REQUEST/MASTER/PRICE）

### ✅ Phase 2: マスターデータ取得（完了 2025-12-25）
- 銘柄マスター取得（21,287件）
- 個別株フィルタリング（18,869件）
- ETF/REIT除外（100%精度）

### ✅ Phase 3: スクリーニング実装（完了 2025-12-25）
- 株価データ取得
- テクニカル指標計算（移動平均、ボリンジャーバンド、RSI、MACD）
- スクリーニング条件実装（出来高急増、ブレイクアウト、価格変動）

### 🔄 Phase 4: 成果物整理（進行中）
- ドキュメント更新
- コード整理
- テスト作成

### 📋 Phase 5: レポート生成（予定）
- HTML/Markdownレポート生成
- グラフ生成（matplotlib）

### 📋 Phase 6: 自動化（予定）
- GitHub Actions統合
- GitHub Pages公開
- 毎日自動実行

---

## 🏗️ アーキテクチャ

```
swing-stock-screener/
├── src/
│   ├── utils/          # 共通ユーティリティ
│   │   ├── config.py   # 設定管理
│   │   ├── logger.py   # ログ記録
│   │   └── calendar.py # 取引日判定
│   ├── api/            # API連携
│   │   ├── auth.py     # 認証
│   │   ├── client.py   # APIクライアント
│   │   ├── rate_limiter.py # レート制限
│   │   ├── stock_info.py   # 銘柄情報取得
│   │   └── price_volume.py # 株価・出来高取得
│   ├── data/           # データ処理
│   │   ├── validator.py # データ検証
│   │   ├── filter.py    # ETF/REIT除外
│   │   └── fetcher.py   # データ取得統合
│   ├── analysis/       # 分析機能
│   │   ├── indicators.py # テクニカル指標
│   │   └── screener.py   # スクリーニング
│   ├── report/         # レポート生成
│   │   ├── generator.py      # レポート生成
│   │   └── templates/        # HTMLテンプレート
│   │       └── index.html
│   └── main.py         # メインスクリプト
├── tests/              # テストコード
├── docs/               # 生成レポート（GitHub Pages）
├── .github/
│   └── workflows/
│       └── daily-report.yml # GitHub Actions
└── requirements.txt    # 依存パッケージ
```

---

## 🚀 セットアップ

### 必要要件

- Python 3.12以上
- 立花証券e支店の口座とAPIキー
- GitHubアカウント

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourusername/swing-stock-screener.git
cd swing-stock-screener
```

### 2. Python環境のセットアップ

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt
```

### 3. 環境変数の設定

`.env.example`をコピーして`.env`を作成：

```bash
cp .env.example .env
```

`.env`ファイルを編集：

```env
# Phase 7修正: 認証方式の変更（APIキー → ユーザーID/パスワード）
# 立花証券API設定
TACHIBANA_USER_ID=your_user_id_here
TACHIBANA_PASSWORD=your_password_here
TACHIBANA_ENVIRONMENT=demo  # prod または demo

# レポート出力先
REPORT_OUTPUT_DIR=docs

# ログレベル（DEBUG, INFO, WARNING, ERROR）
LOG_LEVEL=INFO
```

### 4. ローカルでの動作確認（電話認証が必要）

立花証券APIは**電話認証が必須**です。以下の手順で認証してから実行してください：

**手順**:
1. [立花証券e支店Webサイト](https://www.e-shiten.jp/)にログイン
2. 電話認証を実行（自動音声ガイダンスに従う）
3. **3分以内に**以下のコマンドを実行

**実行コマンド**:

```bash
# メインスクリプトを実行
python3 -m src.main
```

**処理時間の目安**:
- マスターデータ取得: 約20秒
- 個別株フィルタリング: 約1秒
- 株価データ取得（1,000件）: 約10分

成功すると、スクリーニング結果がコンソールに表示されます。

---

## 🤖 自動化（運用方法）

### ⚠️ 重要: 電話認証の制約について

立花証券APIは**電話認証が必須**で、認証の有効期限は**3分間のみ**です。
このため、完全自動化（cronによる無人実行）は不可能です。

以下の2つの運用方法から選択してください。

---

### 方式1: ローカル実行 + 自動デプロイ（推奨）

**メリット**: 確実に実行でき、GitHub Pagesへのデプロイは自動化される

**手順**:
1. [立花証券e支店Webサイト](https://www.e-shiten.jp/)にログイン
2. 電話認証を実施（自動音声ガイダンスに従う）
3. **3分以内に**以下のコマンドを実行：

```bash
# 推奨: スクリプトで自動実行
chmod +x scripts/run_daily_report.sh
./scripts/run_daily_report.sh
```

または手動で実行:
```bash
# 1. スクリーニング実行（3分以内に実行すること！）
python3 -m src.main

# 2. レポートをコミット&プッシュ
git add docs/
git commit -m "📊 日次レポート生成: $(date +'%Y-%m-%d')"
git push origin main

# 3. GitHub Actionsが自動でGitHub Pagesにデプロイ（deploy-report.yml）
```

**処理時間の目安**:
- マスターデータ取得: 約20秒
- 株価データ取得（1,000件）: 約10分
- レポート生成: 約10秒

---

### 方式2: GitHub Actions手動実行（非推奨）

**デメリット**: 電話認証のタイミング制御が困難、失敗しやすい

**手順**:
1. [立花証券e支店Webサイト](https://www.e-shiten.jp/)で電話認証を実施
2. **3分以内に**以下を実行：
   - GitHubリポジトリの **Actions** タブを開く
   - **株式スクリーニング日次レポート生成** ワークフローを選択
   - **Run workflow** ボタンをクリック

**注意事項**:
- ワークフロー起動までのタイムラグがあるため、3分以内に完了しない可能性が高い
- 失敗した場合、自動的にIssueが作成されます
- **ローカル実行（方式1）を強く推奨します**

---

### 将来的な改善案

- セッション管理機能の追加（仮想URLの永続化・自動更新）
- 立花証券APIの仕様変更を待つ（電話認証なしの照会APIの提供）
- 代替APIの検討（他の証券会社API）

---

## ⚙️ GitHub設定（自動デプロイ用）

### 1. GitHub Pagesの有効化

1. リポジトリページで **Settings** → **Pages** を開く
2. **Source** で以下を選択：
   - **Deploy from a branch**
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`
3. **Save** をクリック

### 2. GitHub Secretsの設定（オプション）

**注意**: GitHub Actions手動実行（方式2）を使用する場合のみ必要です。ローカル実行（方式1・推奨）では不要です。

<details>
<summary>GitHub Secretsの設定手順を表示</summary>

1. リポジトリページで **Settings** → **Secrets and variables** → **Actions** を開く
2. **New repository secret** をクリック
3. 以下を設定：
   - **Name**: `TACHIBANA_USER_ID`
   - **Secret**: 立花証券e支店のログインユーザーID
4. 再度 **New repository secret** をクリックし、以下を設定：
   - **Name**: `TACHIBANA_PASSWORD`
   - **Secret**: 立花証券e支店のログインパスワード
5. 再度 **New repository secret** をクリックし、以下を設定：
   - **Name**: `TACHIBANA_ENVIRONMENT`
   - **Secret**: `demo` または `prod`（初回は `demo` を推奨）

**重要**: 電話認証の制約により、GitHub Actions手動実行は失敗しやすいため、ローカル実行（方式1）を推奨します。

</details>

### 3. レポートの確認

GitHub Pagesが有効化され、ローカルからレポートをプッシュすると、以下のURLでレポートを閲覧できます：

```
https://yourusername.github.io/swing-stock-screener/
```

**注意**: 初回デプロイには数分かかる場合があります。

---

## 📝 設定のカスタマイズ

### スクリーニング条件の変更

[src/analysis/screener.py](src/analysis/screener.py)で閾値を調整できます：

```python
# 出来高急増の閾値（デフォルト: 2.0倍）
volume_result = self.volume_surge(stock_code, stock_name, ohlcv_data, threshold=2.0)

# ブレイクアウトの出来高閾値（デフォルト: 1.5倍）
breakout_result = self.technical_breakout(stock_code, stock_name, ohlcv_data, volume_threshold=1.5)

# 値上がり率の閾値（デフォルト: 5.0%）
price_change_result = self.price_change_rate_filter(stock_code, stock_name, ohlcv_data, threshold=5.0)
```

### 実行スケジュールの変更

[.github/workflows/daily-report.yml](.github/workflows/daily-report.yml)のcronを編集：

```yaml
schedule:
  # 平日朝8時(JST) = UTC 23時(前日)
  - cron: '0 23 * * 0-4'
```

### 対象銘柄数の変更

[src/main.py](src/main.py:86)で処理する銘柄数を調整：

```python
# テストのため最初の10銘柄のみ
stock_codes = [stock["stock_code"] for stock in individual_stocks[:10]]

# 全銘柄を処理する場合
stock_codes = [stock["stock_code"] for stock in individual_stocks]
```

---

## 🧪 テスト

### テストの実行

```bash
# 全テストを実行
pytest

# カバレッジ付きで実行
pytest --cov=src --cov-report=html

# 特定のテストファイルを実行
pytest tests/test_utils/test_calendar.py
```

### コード品質チェック

```bash
# Lintチェック
flake8 src/ tests/

# フォーマットチェック
black --check src/ tests/

# フォーマット適用
black src/ tests/
```

---

## 🔧 トラブルシューティング

### 認証エラーが発生する

**症状**: `❌ ログインリクエストに失敗しました`

**対処法**:
1. **電話認証を実施したか確認**（最も一般的な原因）
   - 立花証券e支店Webサイトで電話認証を実施してください
   - 認証の有効期限は3分間です
2. `.env`ファイルの設定を確認
   - `TACHIBANA_USER_ID`が正しく設定されているか
   - `TACHIBANA_PASSWORD`が正しく設定されているか
   - `TACHIBANA_ENVIRONMENT`が`demo`または`prod`になっているか
3. ネットワーク接続を確認

### レポートが生成されない

**症状**: GitHub Actionsは成功するがレポートが表示されない

**対処法**:
1. GitHub Pagesの設定を確認（`gh-pages`ブランチが選択されているか）
2. `docs/`ディレクトリにファイルが生成されているか確認
3. ブラウザのキャッシュをクリア

### GitHub Actionsが失敗する

**症状**: Actions タブでワークフローが赤色（失敗）

**対処法**:
1. **最も一般的な原因**: 電話認証が完了していない
   - GitHub Actions手動実行では電話認証のタイミング制御が困難です
   - **ローカル実行（方式1）に切り替えることを推奨します**
2. エラーログを確認
   - Actions タブ → 失敗したワークフロー → ログを確認
3. 自動作成されたIssueを確認
4. ローカルで`python3 -m src.main`を実行してエラーを特定

---

## 📈 パフォーマンス

### 現在の性能

- **処理銘柄数**: 10銘柄（テスト設定）
- **実行時間**: 未計測（全銘柄では15分以内を目標）
- **APIレート制限**: 10リクエスト/秒
- **テストカバレッジ**: 6%（calendar.pyのみ100%）

### 最適化の方向性

- API呼び出しの並列化
- データキャッシュの活用
- テストカバレッジの向上（目標80%以上）

---

## 🛡️ セキュリティ

### 重要な注意事項

- **認証情報を絶対にコミットしないこと**
  - `.env`ファイルは`.gitignore`に含まれています
  - GitHub Secretsを使用してください

- **認証方式について（Phase 7修正）**
  - ユーザーID/パスワード方式で認証します
  - 第二暗証番号は照会機能では不要です（注文機能は使用しません）
  - 初回ログイン時は金商法交付書面の確認が必要な場合があります

---

## 📚 技術スタック

- **言語**: Python 3.12.1
- **主要ライブラリ**:
  - `requests` - API通信
  - `pandas`, `numpy` - データ処理
  - `jinja2` - テンプレートエンジン
  - `jpholiday` - 日本の祝日判定
  - `pytest` - テスト
  - `flake8`, `black` - コード品質管理

---

## 🗺️ ロードマップ

### Phase 6: 品質向上（進行中）

- [x] MVP完成
- [ ] README整備
- [ ] テストカバレッジ向上（目標80%）
- [ ] パフォーマンス最適化

### 将来の拡張機能

- Chart.jsによる価格チャート表示
- テーブルソート・フィルタ機能
- 追加テクニカル指標（MACD、ストキャスティクス等）
- 信用取引情報の分析
- 板情報の分析

---

## 📄 ライセンス

このプロジェクトは個人利用を目的としています。

---

## 🙏 謝辞

- [立花証券e支店API](https://kabuka.e-shiten.jp/) - 無料で利用できる日本株API
- [jpholiday](https://github.com/Lalcs/jpholiday) - 日本の祝日ライブラリ

---

## 📞 サポート

質問や問題がある場合は、[Issues](https://github.com/yourusername/swing-stock-screener/issues)で報告してください。

---

**最終更新**: 2025-11-21
**プロジェクト状態**: MVP完成、本番運用準備中
