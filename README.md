# swing-stock-screener

スウィング取引向けの株式スクリーニングレポート自動生成システム

立花証券APIを活用し、個別株のテクニカル分析を自動実行し、GitHub Pagesで日次レポートを公開します。

## [DEMO](https://hatohato25.github.io/swing-stock-screener/)

<img width="400" alt="スクリーンショット 2026-01-13 1 16 25" src="https://github.com/user-attachments/assets/b6e42994-6397-4127-b196-6a0de9045a43" />
<img width="340" alt="スクリーンショット 2026-01-13 1 16 49" src="https://github.com/user-attachments/assets/151bdc94-8e73-4858-934f-6979d8ac04ae" />

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

### 業種フィルタリング（カスタマイズ可能）

- **東証33業種から自由に選択可能**
- デフォルトではゲーム・IT関連の4業種に設定（デモ用）
  - 電気機器、その他製品、情報・通信業、サービス業
- 得意分野に絞ったスクリーニングで精度向上
- 処理時間の短縮にも貢献

### レポート生成

- レスポンシブデザインのHTMLレポート
- 6カテゴリ別のランキング表示（各Top 20）
- 日付別アーカイブ（過去レポートも閲覧可能）
- GitHub Pagesで自動公開
- **Gemini AIによる自動分析レポート**（オプション）

### 自動化

- GitHub Actionsで手動実行可能
- エラー時の自動Issue作成
- 過去レポートの自動保持（累積型デプロイ）

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
pip3 install -r requirements.txt

# または、個別にインストールする場合
pip3 install markdown>=3.5.0
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

# Gemini AI分析（オプション）
ENABLE_AI_ANALYSIS=false  # true にするとAI分析を有効化
GEMINI_API_KEY=your_gemini_api_key_here  # AI分析を有効化する場合は必須
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
- 株価データ取得: 約5分

成功すると、スクリーニング結果がコンソールに表示されます。

---

## 🤖 自動化（運用方法）

### ⚠️ 重要: 電話認証の制約について

立花証券APIは**電話認証が必須**で、認証の有効期限は**3分間のみ**です。
このため、完全自動化（cronによる無人実行）は不可能です。

現在は以下の運用方法でレポートを生成しています。

---

### 運用手順: GitHub Actions手動実行

**手順**:
1. [立花証券e支店Webサイト](https://www.e-shiten.jp/)で電話認証を実施
2. **3分以内に**以下を実行：
   - GitHubリポジトリの **Actions** タブを開く
   - **株式スクリーニング日次レポート生成** ワークフローを選択
   - **Run workflow** ボタンをクリック

**注意事項**:
- ワークフロー起動までのタイムラグがあるため、電話認証完了後すぐに実行してください
- 失敗した場合、自動的にIssueが作成されます
- 成功すると、自動的にGitHub Pagesにデプロイされます

**処理時間の目安**:
- マスターデータ取得: 約20秒
- 株価データ取得（1,000件）: 約5分
- レポート生成: 約10秒

---

## ⚙️ GitHub設定（自動デプロイ用）

### 1. GitHub Pagesの有効化

1. リポジトリページで **Settings** → **Pages** を開く
2. **Source** で以下を選択：
   - **Deploy from a branch**
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`
3. **Save** をクリック

### 2. GitHub Secretsの設定

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

### 3. レポートの確認

GitHub Actionsが成功すると、以下のURLでレポートを閲覧できます：

```
https://yourusername.github.io/swing-stock-screener/
```

**注意**: 初回デプロイには数分かかる場合があります。

---

## 📝 設定のカスタマイズ

### 対象業種の変更

[src/data/stock_filter.py](src/data/stock_filter.py)で対象業種を変更できます：

```python
# 対象業種コード（デフォルト: ゲーム・IT関連の4業種）
ALLOWED_SECTORS = {
    "3650": "電気機器",
    "3800": "その他製品",
    "5250": "情報・通信業",
    "9050": "サービス業",
}
```

**利用可能な業種コード一覧**:
- `0050`: 水産・農林業
- `1050`: 鉱業
- `2050`: 建設業
- `3050`: 食料品
- `3100`: 繊維製品
- `3150`: パルプ・紙
- `3200`: 化学
- `3250`: 医薬品
- `3300`: 石油石炭製品
- `3350`: ゴム製品
- `3400`: ガラス土石製品
- `3450`: 鉄鋼
- `3500`: 非鉄金属
- `3550`: 金属製品
- `3600`: 機械
- `3650`: 電気機器
- `3700`: 輸送用機器
- `3750`: 精密機器
- `3800`: その他製品
- `4050`: 電気・ガス業
- `5050`: 陸運業
- `5100`: 海運業
- `5150`: 空運業
- `5200`: 倉庫運輸関連
- `5250`: 情報・通信業
- `6050`: 卸売業
- `6100`: 小売業
- `7050`: 銀行業
- `7100`: 証券商品先物
- `7150`: 保険業
- `7200`: その他金融業
- `8050`: 不動産業
- `9050`: サービス業
- `9999`: その他

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

### 対象銘柄数の変更

[src/main.py](src/main.py:86)で処理する銘柄数を調整：

```python
# テストのため最初の10銘柄のみ
stock_codes = [stock["stock_code"] for stock in individual_stocks[:10]]

# 全銘柄を処理する場合
stock_codes = [stock["stock_code"] for stock in individual_stocks]
```

---

## 🤖 Gemini API連携によるレポート分析機能

スクリーニングレポートをAI（Google Gemini 2.5 Flash Preview）で自動分析し、投資判断をサポートする機能を提供します。

### 機能概要

AI分析は以下の3つの視点で提供されます：

1. **注目銘柄の選定（5銘柄程度）**
   - 複数カテゴリで検出された銘柄を優先的に評価
   - スコアが高く、RSI/MACDの組み合わせが良好な銘柄
   - それぞれの注目理由を簡潔に説明

2. **リスク評価**
   - 逆張り戦略（BB下限反転）のリスクとリターンを評価
   - ストップロス設定の推奨価格帯
   - 流動性（平均出来高）の確認ポイント

3. **投資戦略提案**
   - 短期（1-5日）、中期（1-2週間）、長期（2週間以上）の時間軸別戦略
   - 各カテゴリの特性に応じた保有期間の推奨
   - エントリー・エグジット戦略の提案

### APIキーの取得方法

1. [Google AI Studio](https://aistudio.google.com/app/apikey) にアクセス
2. Googleアカウントでログイン
3. 「Create API Key」をクリックしてAPIキーを取得
4. `.env`ファイルに`GEMINI_API_KEY`を追加

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 使用方法

#### CLI版（Phase 1: 現在利用可能）

```bash
# 最新レポートを分析
python3 -m src.analysis.analyze_report

# 特定日付のレポートを分析
python3 -m src.analysis.analyze_report --date 2025-12-30

# 結果をファイルに保存
python3 -m src.analysis.analyze_report --save
```

#### 自動化版（Phase 2: 現在利用可能）

GitHub Actionsでレポート生成時に自動的にAI分析を実行し、HTML形式で出力します。

**設定方法**:

1. **GitHub Secretsに`GEMINI_API_KEY`を追加**
   - リポジトリページで **Settings** → **Secrets and variables** → **Actions** を開く
   - **New repository secret** をクリック
   - **Name**: `GEMINI_API_KEY`
   - **Secret**: Google AI Studioで取得したAPIキー

2. **（オプション）AI分析を有効化**
   - GitHub Secretsに`ENABLE_AI_ANALYSIS`を追加
   - **Name**: `ENABLE_AI_ANALYSIS`
   - **Secret**: `true`
   - デフォルトは`false`（無効）のため、有効化する場合のみ設定が必要です

**動作確認**:
- AI分析が有効な場合、レポートページ（`index.html`）に「AI分析を見る」ボタンが表示されます
- ボタンをクリックすると、AI分析レポート（`ai_analysis.html`）が表示されます

**ローカルでの自動実行**:
```bash
# 環境変数を設定してから実行
export ENABLE_AI_ANALYSIS=true
export GEMINI_API_KEY=your_api_key_here

# メインスクリプトを実行（レポート生成後にAI分析も自動実行）
python3 -m src.main
```

### 免責事項

- この分析はAIによって生成されたものであり、情報提供のみを目的としています。
- 専門的な投資助言に代わるものではありません。
- 投資判断は必ず自己責任で行ってください。
- AI分析の精度は保証されません。銘柄の詳細なファンダメンタルズ分析、企業の業績、市場環境等を総合的に考慮することをお勧めします。
- 本分析の利用によって生じたいかなる損害についても、当方は一切の責任を負いません。

### 無料枠の制限

Google Gemini APIの無料枠は以下の通りです：

- **1分あたり**: 15リクエスト
- **1日あたり**: 1500リクエスト

1日1回のレポート生成であれば、十分に余裕があります。

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
1. **最も一般的な原因**: 電話認証が完了していない、または有効期限（3分）を過ぎた
   - 電話認証完了後、すぐにワークフローを実行してください
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

## 📄 ライセンス

このプロジェクトは個人利用を目的としています。

---

## 🙏 謝辞

- [立花証券e支店API](https://kabuka.e-shiten.jp/) - 無料で利用できる日本株API

---

**最終更新**: 2026-01-13
**プロジェクト状態**: 本番運用中
