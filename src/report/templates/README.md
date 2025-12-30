# 株式スクリーニングレポート

**日付**: {{ date }}

---

## このレポートについて

このレポートは、スウィング取引（数日〜数週間の保有期間）に適した個別株を自動抽出するものです。

テクニカル指標（移動平均線、ボリンジャーバンド、RSI、MACD等）と出来高、ファンダメンタルズ指標（PER/PBR/配当利回り/ROE）をベースに、以下5つのカテゴリで銘柄を抽出しています：

- **出来高急増**：機関投資家や大口資金の流入を示唆
- **ブレイクアウト**：トレンド転換の初動を捉える
- **BB下限反転**：逆張り戦略（売られ過ぎからの反転を狙う）
- **割安バリュー株**：厳格基準の割安株（景気後退局面に強い）
- **インフレ対応バリュー株**：緩和基準の割安株（収益性重視）

※ETF、REIT、インフラファンドは除外し、個別株のみを対象としています。

---

## スコアの見方

- **スコア算出方法**：各カテゴリで検出された銘柄群の中での相対順位に基づく0-100のスケール
- **出来高急増**：元スコア = (当日出来高 / 前日出来高) × 10
- **ブレイクアウト**：元スコア = MA乖離率 + 出来高比率
- **BB下限反転**：元スコア = BB乖離 + RSI + MACD改善 + 出来高
- **割安バリュー株**：元スコア = (15/PER)×10 + (1.5/PBR)×10 + 配当利回り×5
- **インフレ対応バリュー株**：元スコア = (25/PER)×8 + (2.5/PBR)×8 + 配当利回り×4 + ROE×2
- **解釈**：スコア20以上は要注目、30以上は強い兆候、50以上は非常に強い兆候
- **注意**：スコアは同日内の相対評価です。カテゴリ間のスコア比較も可能です

---

## スクリーニング条件

| カテゴリ | 条件 | 理由 |
|---------|------|------|
| 出来高急増 | 前日比2倍以上 | 大口資金の流入や材料の発生を示唆。流動性が高まり、価格変動の可能性が高まる |
| ブレイクアウト | 25日MA上抜け または BB上限突破 | トレンド転換の初動を捉える。上抜け時の出来高増加は信頼性が高い |
| BB下限反転 | BB下限±5%、RSI<=30、MACD改善 | 逆張り戦略。売られ過ぎからの反転を狙う。リスク高のため要注意 |
| 割安バリュー株 | PER<15倍、PBR<1.5倍、配当>=2.5% | 厳格な割安基準。業績安定企業の割安株。景気後退局面に強い |
| インフレ対応バリュー株 | PER<25倍、PBR<2.5倍、配当>=2.0%、ROE>=8.0% | インフレ環境で成長投資を行う企業。ROEで収益性を担保 |
| 共通 | 平均出来高10万株以上 | 流動性を確保し、スムーズな売買を可能にする |

---

## サマリー

- **該当銘柄数（ユニーク）**: {{ stats.total_stocks }}銘柄
- **出来高急増**: {{ stats.volume_surge_count }}銘柄
- **ブレイクアウト**: {{ stats.breakout_count }}銘柄
- **BB下限反転**: {{ stats.bb_lower_bounce_count }}銘柄
- **割安バリュー株**: {{ stats.value_conservative_count }}銘柄
- **インフレ対応バリュー株**: {{ stats.value_inflation_adjusted_count }}銘柄

---

{% if rankings.volume_surge %}
## 出来高急増ランキング（Top 20）

**目的**：前日比2倍以上の出来高を記録した銘柄。機関投資家の参入や材料の発生を示唆します。
**活用法**：出来高急増は価格変動の前兆。RSIと併せて買われ過ぎを確認しましょう。

| 順位 | 銘柄コード | 銘柄名 | 現在値 | 当日出来高 | 平均出来高(25日) | 出来高比率 | RSI | スコア |
|------|-----------|--------|--------|-----------|----------------|-----------|-----|--------|
{% for stock in rankings.volume_surge[:20] -%}
| {{ loop.index }} | {{ stock.stock_code }} | {{ stock.stock_name }} | {{ stock.details.current_price }} | {{ "{:,}".format(stock.details.current_volume) }} | {{ "{:,}".format(stock.details.avg_volume_25d) }} | {{ stock.details.volume_ratio }}倍 | {{ stock.details.rsi if stock.details.rsi else '-' }} | {{ "%.1f"|format(stock.score) }} |
{% endfor %}
---
{% endif %}

{% if rankings.breakout %}
## テクニカルブレイクアウトランキング（Top 20）

**目的**：25日移動平均線の上抜けまたはボリンジャーバンド上限突破。トレンド転換の初動を捉えます。
**活用法**：上抜け時の出来高増加が重要。MACD（ヒストグラム）がプラスなら上昇トレンドの可能性大。

| 順位 | 銘柄コード | 銘柄名 | 現在値 | 25日MA | 乖離率 | 出来高比率 | RSI | MACD | スコア |
|------|-----------|--------|--------|--------|--------|-----------|-----|------|--------|
{% for stock in rankings.breakout[:20] -%}
| {{ loop.index }} | {{ stock.stock_code }} | {{ stock.stock_name }} | {{ stock.details.current_price }} | {{ stock.details.ma_value if stock.details.ma_value else '-' }} | {{ stock.details.price_deviation if stock.details.price_deviation else '-' }}% | {{ stock.details.volume_ratio if stock.details.volume_ratio else '-' }}倍 | {{ stock.details.rsi if stock.details.rsi else '-' }} | {{ stock.details.macd_histogram if stock.details.macd_histogram else '-' }} | {{ "%.1f"|format(stock.score) }} |
{% endfor %}
---
{% endif %}

{% if rankings.bb_lower_bounce %}
## BB下限反転ランキング（Top 20）

**目的**：ボリンジャーバンド下限付近で売られ過ぎから反転の兆候がある銘柄。逆張り戦略。

**活用法**：RSI 30以下の売られ過ぎ、かつMACDヒストグラムが底を打った銘柄。リスク管理（ストップロス設定）必須。

**⚠️ 注意**：逆張り戦略のため、リスクが高いです。損切りルールを厳守してください。

| 順位 | 銘柄コード | 銘柄名 | 現在値 | BB下限 | BB乖離率 | RSI | MACD改善 | 出来高比率 | スコア |
|------|-----------|--------|--------|--------|---------|-----|---------|-----------|--------|
{% for stock in rankings.bb_lower_bounce[:20] -%}
| {{ loop.index }} | {{ stock.stock_code }} | {{ stock.stock_name }} | {{ stock.details.current_price }} | {{ "%.2f"|format(stock.details.bb_lower) }} | {{ "%.2f"|format(stock.details.bb_lower_deviation) }}% | {{ "%.2f"|format(stock.details.rsi) }} | {{ "%.2f"|format(stock.details.macd_improvement) }} | {{ "%.2f"|format(stock.details.volume_ratio) }}倍 | {{ "%.1f"|format(stock.score) }} |
{% endfor %}
---
{% endif %}

{% if rankings.value_conservative %}
## 割安バリュー株ランキング（Top 20）

**目的**：厳格な割安基準（PER < 15倍、PBR < 1.5倍、配当 >= 2.5%）で抽出された割安株。

**活用法**：業績安定企業の割安株。景気後退局面や金利低下局面に強い。配当を重視した長期保有に適しています。

**スコア計算**：(15/PER)×10 + (1.5/PBR)×10 + 配当利回り×5

| 順位 | 銘柄コード | 銘柄名 | 現在値 | PER | PBR | 配当利回り | ROE | スコア |
|------|-----------|--------|--------|-----|-----|-----------|-----|--------|
{% for stock in rankings.value_conservative[:20] -%}
| {{ loop.index }} | {{ stock.stock_code }} | {{ stock.stock_name }} | {{ stock.details.current_price }} | {{ "%.2f"|format(stock.details.per) if stock.details.per else '-' }}倍 | {{ "%.2f"|format(stock.details.pbr) if stock.details.pbr else '-' }}倍 | {{ "%.2f"|format(stock.details.dividend_yield) if stock.details.dividend_yield else '-' }}% | {{ "%.2f"|format(stock.details.roe) if stock.details.roe else '-' }}% | {{ "%.1f"|format(stock.score) }} |
{% endfor %}
---
{% endif %}

{% if rankings.value_inflation_adjusted %}
## インフレ対応バリュー株ランキング（Top 20）

**目的**：インフレ環境に適応した緩和基準（PER < 25倍、PBR < 2.5倍、配当 >= 2.0%、ROE >= 8.0%）で抽出された割安株。

**背景**：インフレ環境では企業が成長投資を行うため、一時的にPER/PBRが上昇します。ROEで収益性を担保することで、成長投資が有効に機能している企業を抽出しています。

**活用法**：インフレ継続局面や金利上昇局面に適応した銘柄選択。収益性（ROE）を重視した成長期待株。

**スコア計算**：(25/PER)×8 + (2.5/PBR)×8 + 配当利回り×4 + ROE×2

| 順位 | 銘柄コード | 銘柄名 | 現在値 | PER | PBR | 配当利回り | ROE | スコア |
|------|-----------|--------|--------|-----|-----|-----------|-----|--------|
{% for stock in rankings.value_inflation_adjusted[:20] -%}
| {{ loop.index }} | {{ stock.stock_code }} | {{ stock.stock_name }} | {{ stock.details.current_price }} | {{ "%.2f"|format(stock.details.per) if stock.details.per else '-' }}倍 | {{ "%.2f"|format(stock.details.pbr) if stock.details.pbr else '-' }}倍 | {{ "%.2f"|format(stock.details.dividend_yield) if stock.details.dividend_yield else '-' }}% | {{ "%.2f"|format(stock.details.roe) if stock.details.roe else '-' }}% | {{ "%.1f"|format(stock.score) }} |
{% endfor %}
---
{% endif %}

---

## 免責事項

- このレポートは情報提供のみを目的としており、投資推奨や投資助言を行うものではありません。
- 掲載された情報は過去のデータに基づく分析結果であり、将来の株価動向を保証するものではありません。
- 投資判断は必ず自己責任で行ってください。銘柄の詳細なファンダメンタルズ分析、企業の業績、市場環境等を総合的に考慮することをお勧めします。
- 投資にはリスクが伴います。損失が発生する可能性があることをご理解の上、適切なリスク管理を行ってください。
- 本レポートの利用によって生じたいかなる損害についても、当方は一切の責任を負いません。

---

*Generated by Swing Stock Screener*
