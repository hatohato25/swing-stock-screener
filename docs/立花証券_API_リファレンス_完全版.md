# 立花証券 e支店 APIリファレンス

**元ファイル**: mfds_json_api_ref_text.html
**変換日時**: 2025-11-21

---

# e_api refference manual

<a name="ComT1"></a>
## 共通説明

<a name="ComP1"></a>
### ｅ支店・ＡＰＩ専用ＵＲＬ

| **⚠️ https://kabuka.e-shiten.jp/e_api_v4r8/（本番環境、現行バージョン）https://demo-kabuka.e-shiten.jp/e_api_v4r8/（デモ環境、現行バージョン）https://kabuka.e-shiten.jp/e_api_v4r7/（本番環境、旧バージョン、2025.11.29 廃止予定）https://demo-kabuka.e-shiten.jp/e_api_v4r7/（デモ環境、旧バージョン、2025.11.29 廃止予定）【注意事項】・現在リリースのバージョンはｅ支店・ＡＰＩ（ｖ４ｒ８）です。　旧バージョンの廃止予定等案内は立花証券・ｅ支店・ＡＰＩ専用ページ「２．リリース＆改定情報」を参照願います。・保守や機能追加等によりＵＲＬのＰｒｅｆｉｘ（e_api_v4rN 部分）を　e_api_v4rN（リビジョンＮ）またはe_api_vN（バージョンＮ）として平行リリースします。・後続版の平行リリース後６０日前後（保守作業は非営業日に実施）　旧リリース版の利用を停止（廃止）しますので、　後続版リリース後はお早めにお客様プログラムの後続版への対応をお願いいたします。・後続版リリース等の連絡は本ページ・リリース＆改定情報にてお知らせするため、　該当ページを定期的に参照願います。・本マニュアルページからのリンク資料について改定がない場合は旧バージョンのままとなります。　改定時は該当バージョンとして掲載いたしますので、最新版をご利用願います。　※改定版公開のタイミングで旧版は自動的に廃版とさせて頂きます。【デモ環境】　お客様のテスト環境としてｅ支店・デモ環境に専用環境を用意いたしました。　ご利用時間帯等につきましてはこちらを参照願います。【アクセス方法】・認証機能は　　「ｅ支店・ＡＰＩ専用ＵＲＬ/auth/?{引数}」・業務機能は　　「仮想URL（REQUEST）?{引数}」・マスタ機能は　「仮想URL（MASTER）?{引数}」・時価情報機能は「仮想URL（PRICE）?{引数}」　※{引数｝に JSON 文字列形式で要求を指定、指定項目等の説明は各機能説明を参照。　※認証機能例：「https://kabuka.e-shiten.jp/e_api_vNrN/auth/?{"p_no":"1","p_sd_date":"yyyy.mm.dd-hh:mn:ss.ttt","sCLMID":"CLMAuthLoginRequest","sPassword":"oxox","sUserId":"oxox"}」** |
| --- |
| https://kabuka.e-shiten.jp/e_api_v4r8/ |
| https://demo-kabuka.e-shiten.jp/e_api_v4r8/ |
| https://kabuka.e-shiten.jp/e_api_v4r7/ |
| https://demo-kabuka.e-shiten.jp/e_api_v4r7/ |
|  |
|  |

<a name="ComP2"></a>
### インタフェース概要

| 最初に以下資料を参照頂き本ＡＰＩの概要や構成についてご理解の上その後、必要に応じ各マニュアルをお読み下さい。立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、インタフェース概要 |
| --- |

<a name="ComP3"></a>
### ブラウザからの利用方法

| プログラム開発前にとりあえずｅ支店・ＡＰＩをブラウザで試して見たい方は以下方法で試せます。立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、ブラウザからの利用方法 |
| --- |
| 以下シート中に「基本」・・・・・・・・認証、注文入力、注文一覧「マスタ・時価」・・・・マスタ情報問合取得、 時価情報問合取得「時価配信」・・・・・・EVENT I/F を利用した時価情報配信機能の利用方法「ニュース」・・・・・・ニュース問合取得について記載しています。 |

<a name="ComP4"></a>
### 共通項目、認証機能

| 共通項目及び認証機能の使用例については以下資料を参照下さい。立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、REQUEST I/F、利用方法、データ仕様 |
| --- |

<a name="ComP5"></a>
### マスタデータ利用方法

| マスタ情報ダウンロード機能等で取得可能な各種マスタデータについては以下を参照。立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ５）、REQUEST I/F、マスタデータ利用方法ダウンロード要求で通知されるデータ項目等についてはマスタ情報ダウンロードの２．以降を参照。 |
| --- |

<a name="ComP7"></a>
### EXCEL(VBA)からの利用方法

| EXCEL(VBA)からｅ支店・ＡＰＩをご利用頂くためのサンプルモジュール（e_api.bas）及びそれを使用したEXCEL サンプルプログラムで時価情報を取得することができます。ご利用方法等は EXCEL サンプルプログラム（シート記載内容）を御覧下さい。 |
| --- |

<a name="ComT2"></a>
## 認証機能（認証I/F）

<a name="CLMAuthLoginRequest"></a>
### ログイン

#### 要求

```json
{ "sCLMID":"CLMAuthLoginRequest", "sUserId":"login", "sPassword":"pswd"}
```

| sCLMID | 機能ＩＤ | CLMAuthLoginRequest |
| --- | --- | --- |
| sUserId | ログインユーザー | e支店口座のログインＩＤ |
| sPassword | ログインパスワード | e支店口座のログインパスワード |
| **⚠️ 【注意】　アクセス方法は URL に「ｅ支店・ＡＰＩ専用ＵＲＬ/auth/?{引数}」で指定、　{引数}に JSON 文字列形式で要求を指定。　詳細は　　ｅ支店・ＡＰＩ専用ＵＲＬ　　インタフェース概要　　ブラウザからの利用方法　　共通項目、認証機能　参照。【注意】　要求または応答の項目順番については処理系により並べ替え操作されるため　JSON 仕様準拠とし保証（記載順番と一致）しない（しなくても問題ない）。　例：以下は同じ要求、または応答として処理する。　　{"項目A":"値A","項目B":"値B"}　　{"項目B":"値B","項目A":"値A"}** |  |  |

```json
{引数}
```

#### 応答

```json
{ "sCLMID":"CLMAuthLoginAck", "sResultCode":"0", "sResultText":"", "sZyoutoekiKazeiC":"1", "sSecondPasswordOmit":"1", "sLastLoginDate":"20231002075554", "sSogoKouzaKubun":"1", "sHogoAdukariKouzaKubun":"1", "sFurikaeKouzaKubun":"1", "sGaikokuKouzaKubun":"1", "sMRFKouzaKubun":"0", "sTokuteiKouzaKubunGenbutu":"2", "sTokuteiKouzaKubunSinyou":"2", "sTokuteiKouzaKubunTousin":"2", "sTokuteiHaitouKouzaKubun":"1", "sTokuteiKanriKouzaKubun":"0", "sSinyouKouzaKubun":"1", "sSakopKouzaKubun":"0", "sMMFKouzaKubun":"0", "sTyukokufKouzaKubun":"0", "sKawaseKouzaKubun":"0", "sHikazeiKouzaKubun":"0", "sKinsyouhouMidokuFlg":"0", "sUrlRequest":"https://dns-name/prefix_version/oxoxoxoxoxoxoxoxoxox/", "sUrlMaster":"https://dns-name/prefix_version/oxoxoxoxoxoxoxoxoxox/", "sUrlPrice":"https://dns-name/prefix_version/oxoxoxoxoxoxoxoxoxox/", "sUrlEvent":"https://dns-name/prefix_version/oxoxoxoxoxoxoxox/", "sUrlEventWebSocket":"wss://dns-name/prefix_version/oxoxoxoxoxoxoxox/", "sUpdateInformWebDocument":"20241001", "sUpdateInformAPISpecFunction":"20250531"}
```

| sCLMID | 機能ＩＤ | CLMAuthLoginAck |
| --- | --- | --- |
| sResultCode | 結果コード | 業務処理．エラーコード0:正常上記以外は結果コード、警告コード表参照 |
| sResultText | 結果テキスト | 「結果コード」に対応するテキスト正常:"" |
| sZyoutoekiKazeiC | 譲渡益課税区分 | 1：特定3：一般5：NISA |
| sSecondPasswordOmit | 暗証番号省略有無Ｃ | 0：無※0：固定値とする。　各注文入力において第二パスワードの入力が必須。※ｅ支店・ＡＰＩ利用の際は、e支店Webサイトより　[お客様情報]-[設定情報]-[第二暗証番号]から、　暗証番号省略を無効に設定。 |
| sLastLoginDate | 最終ログイン日時 | YYYYMMDDHHMMSS00000000000000 |
| sSogoKouzaKubun | 総合口座開設区分 | 0：未開設1：開設 |
| sHogoAdukariKouzaKubun | 保護預り口座開設区分 | 0：未開設1：開設 |
| sFurikaeKouzaKubun | 振替決済口座開設区分 | 0：未開設1：開設 |
| sGaikokuKouzaKubun | 外国口座開設区分 | 0：未開設1：開設 |
| sMRFKouzaKubun | ＭＲＦ口座開設区分 | 0：未開設1：開設 |
| sTokuteiKouzaKubunGenbutu | 特定口座区分現物 | 0：一般1：特定源泉徴収なし2：特定源泉徴収あり |
| sTokuteiKouzaKubunSinyou | 特定口座区分信用 | 0：一般1：特定源泉徴収なし2：特定源泉徴収あり |
| sTokuteiKouzaKubunTousin | 特定口座区分投信 | 0：一般1：特定源泉徴収なし2：特定源泉徴収あり |
| sTokuteiHaitouKouzaKubun | 配当特定口座区分 | 0：未開設1：開設 |
| sTokuteiKanriKouzaKubun | 特定管理口座開設区分 | 0：未開設1：開設 |
| sSinyouKouzaKubun | 信用取引口座開設区分 | 0：未開設1：開設 |
| sSakopKouzaKubun | 先物ＯＰ口座開設区分 | 0：未開設1：開設 |
| sMMFKouzaKubun | ＭＭＦ口座開設区分 | 0：未開設1：開設 |
| sTyukokufKouzaKubun | 中国Ｆ口座開設区分 | 0：未開設1：開設 |
| sKawaseKouzaKubun | 為替保証金口座開設区分 | 0：未開設1：開設 |
| sHikazeiKouzaKubun | 非課税口座開設区分 | 0：未開設1：開設※ＮＩＳＡ口座の開設有無を示す。 |
| sKinsyouhouMidokuFlg | 金商法交付書面未読フラグ | 1：未読（標準Ｗｅｂを起動し書面確認実行必須）0：既読※未読の場合、ｅ支店・ＡＰＩは利用不可のため　仮想ＵＲＬは発行されず""を設定。※既読の場合、ｅ支店・ＡＰＩは利用可能となり　仮想ＵＲＬを発行し設定。 |
| sUrlRequest | 仮想URL（REQUEST) | 業務機能　　（REQUEST I/F）仮想URL |
| sUrlMaster | 仮想URL（MASTER) | マスタ機能　（REQUEST I/F）仮想URL |
| sUrlPrice | 仮想URL（PRICE) | 時価情報機能（REQUEST I/F）仮想URL |
| sUrlEvent | 仮想URL（EVENT) | 注文約定通知（EVENT I/F）仮想URL |
| sUrlEventWebSocket | 仮想URL（EVENT-WebSocket) | 注文約定通知（EVENT I/F WebSocket版）仮想URL |
| sUpdateInformWebDocument | 交付書面更新予定日 | **⚠️ 標準Ｗｅｂの交付書面更新予定日決定後、該当日付を設定。【注意】参照** |
| sUpdateInformAPISpecFunction | ｅ支店・ＡＰＩリリース予定日 | **⚠️ ｅ支店・ＡＰＩリリース予定日決定後、該当日付を設定。【注意】参照** |
| **⚠️ 【注意】本項目は該当事象の予定日をログイン応答を利用し事前にお知らせするための項目です。お客様が開発されたプログラムでｅ支店・ＡＰＩを毎日ご利用頂いている方向けの仕組みで以下チェック「（予定日≧当日日付）ＡＮＤ（予定日！＝前回受信値（初回は空白として処理））」をプログラムに組み込むことで該当事象の予定日を自動検出することができます。交付書面更新予定日が更新された場合、予定日までに標準Ｗｅｂで書面確認を実施、ｅ支店・ＡＰＩリリース予定日が更新された場合、予定日までにＨＰにて変更内容（運用関連事項の改定、インタフェースや機能の追加変更、バージョンアップや旧バージョンの廃止など）を確認し必要な対処、対応をお客様自身で講じることで、予定日以降もｅ支店・ＡＰＩを利用継続するための通知（をする仕組み）項目です。上記チェックが日々できるよう、予定日を過ぎても（次の予定日が決まるまで）同値を応答します。予定日は当日日付より前になることはありませんが、都合により当日日付（を含む）以降の範囲で予定日が前後に変わる場合があります。** |  |  |

<a name="CLMAuthLogoutRequest"></a>
### ログアウト

#### 要求

```json
{ "sCLMID":"CLMAuthLogoutRequest"}
```

| sCLMID | 機能ＩＤ | CLMAuthLogoutRequest |
| --- | --- | --- |

#### 応答

```json
{ "sCLMID":"CLMAuthLogoutAck", "sResultCode":"0", "sResultText":""}
```

| sCLMID | 機能ＩＤ | CLMAuthLogoutAck |
| --- | --- | --- |
| sResultCode | 結果コード | CLMAuthLoginAck.sResultCode 参照 |
| sResultText | 結果テキスト | CLMAuthLoginAck.sResultText 参照 |

<a name="ComT3"></a>
## 業務機能（REQUEST I/F）

<a name="CLMKabuNewOrder"></a>
### 株式新規注文

#### 要求

```json
{ "sCLMID":"CLMKabuNewOrder", "sZyoutoekiKazeiC":"1", "sIssueCode":"8411", "sSizyouC":"00", "sBaibaiKubun":"3", "sCondition":"0", "sOrderPrice":"0", "sOrderSuryou":"100", "sGenkinShinyouKubun":"0", "sOrderExpireDay":"0", "sGyakusasiOrderType":"0", "sGyakusasiZyouken":"0", "sGyakusasiPrice":"*", "sTatebiType":"*", "sTategyokuZyoutoekiKazeiC":"*", "sSecondPassword":"pswd",＊＊＊＊以下は信用返済（建日種類＝個別指定）時の返済建玉リスト、他取引時不要＊＊＊＊ "aCLMKabuHensaiData": [  {   sTategyokuNumber:"999999",   sTatebiZyuni:"1",   sOrderSuryou:"100"  } ]}
```

| sCLMID | 機能ＩＤ | CLMKabuNewOrder |
| --- | --- | --- |
| sZyoutoekiKazeiC | 譲渡益課税区分 | 1：特定3：一般5：NISA（一般NISAの売買は2023年まで可、2024年以降は売却のみ可）6：N成長（2024年から取り扱い開始、NISA成長投資枠） |
| sIssueCode | 銘柄コード | 例:6501 |
| sSizyouC | 市場 | 00：東証 |
| sBaibaiKubun | 売買区分 | 1：売3：買5：現渡7：現引 |
| sCondition | 執行条件 | 0：指定なし2：寄付4：引け6：不成 |
| sOrderPrice | 注文値段 | *：指定なし0：成行上記以外は、注文値段 |
| sOrderSuryou | 注文株数 | 例:100 |
| sGenkinShinyouKubun | 現金信用区分 | 0：現物2：新規(制度信用6ヶ月)4：返済(制度信用6ヶ月)6：新規(一般信用6ヶ月)8：返済(一般信用6ヶ月) |
| sOrderExpireDay | 注文期日 | 0：当日上記以外は、注文期日(YYYYMMDD)[10営業日迄] |
| sGyakusasiOrderType | 逆指値注文種別 | 0：通常1：逆指値2：通常＋逆指値 |
| sGyakusasiZyouken | 逆指値条件 | 0：指定なし条件値段（トリガー価格） |
| sGyakusasiPrice | 逆指値値段 | *：指定なし0：成行上記以外は逆指値値段 |
| sTatebiType | 建日種類 | 信用返済時に指定する返済建玉順序種類指定*：指定なし（現物または新規）1：個別指定2：建日順3：単価益順4：単価損順 |
| sTategyokuZyoutoekiKazeiC | 建玉譲渡益課税区分 | 信用建玉における譲渡益課税区分（現引、現渡で使用）*：現引、現渡以外の取引1：特定3：一般 |
| sSecondPassword | 第二パスワード | 第二暗証番号（発注パスワード） |
| aCLMKabuHensaiData | 返済リスト | 信用返済（建日種類＝個別指定）時の返済建玉リスト、他取引時不要返済建玉リストとして以下３項目を配列指定する |
| sTategyokuNumber | 新規建玉番号 | 信用建玉番号（CLMShinyouTategyokuList.sOrderTategyokuNumber） |
| sTatebiZyuni | 建日順位 | 約定時返済する返済リスト内順位（１から昇順） |
| sOrderSuryou | 注文数量 | 返済建玉株数 |

#### 応答

```json
{ "sCLMID":"CLMKabuNewOrder", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sOrderNumber":"9000015", "sEigyouDay":"20221209", "sOrderUkewatasiKingaku":"140099", "sOrderTesuryou":"90", "sOrderSyouhizei":"9", "sKinri":"-", "sOrderDate":"20221209134803" }
```

| sCLMID | 機能ＩＤ | CLMKabuNewOrder |
| --- | --- | --- |
| sResultCode | 結果コード | 業務処理．エラーコード0：正常上記以外は結果コード、警告コード表参照 |
| sResultText | 結果テキスト | 「結果コード」に対応するテキスト正常:"" |
| sWarningCode | 警告コード | 業務処理．ワーニングコード0：正常上記以外は結果コード、警告コード表参照 |
| sWarningText | 警告テキスト | 「警告コード」に対応するテキスト正常:"" |
| sOrderNumber | 注文番号 | 採番（注文番号＋営業日でユニーク） |
| sEigyouDay | 営業日 | YYYYMMDD |
| sOrderUkewatasiKingaku | 注文受渡金額 | 0～9999999999999999 |
| sOrderTesuryou | 注文手数料 | 0～9999999999999999 |
| sOrderSyouhizei | 注文消費税 | 0～9999999999999999 |
| sKinri | 金利 | メモリ上のシステム市場弁済別取扱条件0～999.99999：買方金利0～999.99999：売方金利0～999.99999：買方金利（翌営業日）0～999.99999：売方金利（翌営業日）-：現物取引場合 |
| sOrderDate | 注文日時 | YYYYMMDDHHMMSS |

#### 例（各取引項目要求設定例）

<a name="CLMKabuCorrectOrder"></a>
### 株式訂正注文

#### 要求

```json
{ "sCLMID":"CLMKabuCorrectOrder", "sOrderNumber":"9000015", "sEigyouDay":"20221209", "sCondition":"0", "sOrderPrice":"0", "sOrderSuryou":"*", "sOrderExpireDay":"*", "sGyakusasiZyouken":"*", "sGyakusasiPrice":"*", "sSecondPassword":"pswd"}
```

| sCLMID | 機能ＩＤ | CLMKabuCorrectOrder |
| --- | --- | --- |
| sOrderNumber | 注文番号 | CLMKabuNewOrder.sOrderNumber |
| sEigyouDay | 営業日 | CLMKabuNewOrder.sEigyouDay |
| sCondition | 執行条件 | *：変更なし0：指定なし2：寄付4：引け6：不成 |
| sOrderPrice | 注文値段 | *：変更なし0：成行に変更訂正注文値段：指値を変更 |
| sOrderSuryou | 注文数量 | *：変更なし訂正数量：数量を変更（増株不可）※訂正数量には、内出来を含んだ数量を指定 |
| sOrderExpireDay | 注文期日 | *：変更なし0：当日変更注文期日日(YYYYMMDD)[10営業日迄] |
| sGyakusasiZyouken | 逆指値条件 | *：変更なし0：成行に変更逆指値条件：逆指値条件を変更 |
| sGyakusasiPrice | 逆指値注文値段 | *：変更なし0：成行に変更逆指値注文値段：逆指値注文値段を変更 |
| sSecondPassword | 第二パスワード | 第二暗証番号（発注パスワード） |

#### 応答

```json
{ "sCLMID":"CLMKabuCorrectOrder", "sResultCode":"0", "sResultText":"" "sOrderNumber":"9000015", "sEigyouDay":"20221209", "sOrderUkewatasiKingaku":"140099", "sOrderTesuryou":"90", "sOrderSyouhizei":"9", "sOrderDate":"20221209134803"}
```

| sCLMID | 機能ＩＤ | CLMKabuCorrectOrder |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sOrderNumber | 注文番号 | 要求設定値 |
| sEigyouDay | 営業日 | 要求設定値 |
| sOrderUkewatasiKingaku | 注文受渡金額 | 0～9999999999999999 |
| sOrderTesuryou | 注文手数料 | 0～9999999999999999 |
| sOrderSyouhizei | 注文消費税 | 0～9999999999999999 |
| sOrderDate | 注文日時 | YYYYMMDDHHMMSS |

#### 例（各取引項目要求設定例）

<a name="CLMKabuCancelOrder"></a>
### 株式取消注文

#### 要求

```json
{ "sCLMID":"CLMKabuCancelOrder", "sOrderNumber":"30000007", "sEigyouDay":"20200727", "sSecondPassword":"pswd"}
```

| sCLMID | 機能ＩＤ | CLMKabuCancelOrder |
| --- | --- | --- |
| sOrderNumber | 注文番号 | CLMKabuNewOrder.sOrderNumber |
| sEigyouDay | 営業日 | CLMKabuNewOrder.sEigyouDay |
| sSecondPassword | 第二パスワード | 第二暗証番号（発注パスワード） |

#### 応答

```json
{ "sCLMID":"CLMKabuCancelOrder", "sResultCode":"0", "sResultText":"" "sOrderNumber":"30000007", "sEigyouDay":"20200727", "sOrderUkewatasiKingaku":"140099", "sOrderDate":"20221209134803"}
```

| sCLMID | 機能ＩＤ | CLMKabuCancelOrder |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sOrderNumber | 注文番号 | 要求設定値 |
| sEigyouDay | 営業日 | 要求設定値 |
| sOrderUkewatasiKingaku | 注文受渡金額 | 0～9999999999999999 |
| sOrderDate | 注文日時 | YYYYMMDDHHMMSS |

<a name="CLMKabuCancelOrderAll"></a>
### 株式一括取消

#### 要求

```json
{ "sCLMID":"CLMKabuCancelOrderAll", "sSecondPassword":"pswd"}
```

| sCLMID | 機能ＩＤ | CLMKabuCancelOrderAll |
| --- | --- | --- |
| sSecondPassword | 第二パスワード | 第二暗証番号（発注パスワード） |

#### 応答

```json
{ "sCLMID":"CLMKabuCancelOrderAll", "sResultCode":"0", "sResultText":""}
```

| sCLMID | 機能ＩＤ | CLMKabuCancelOrderAll |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |

<a name="CLMGenbutuKabuList"></a>
### 現物保有銘柄一覧

#### 要求

```json
{ "sCLMID":"CLMGenbutuKabuList", "sIssueCode":"7201"}
```

| sCLMID | 機能ＩＤ | CLMGenbutuKabuList |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 指定あり：指定１銘柄のリスト取得（例:"7201"）指定なし：全保有銘柄のリスト取得（例:""） |
| **⚠️ 【注意】　各合計値（リスト外項目）と銘柄個別値（リスト内項目）を応答する。　リスト外項目は銘柄コードの指定に依存しない。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMGenbutuKabuList", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"7201", "sIppanGaisanHyoukagakuGoukei":"0", "sIppanGaisanHyoukaSonekiGoukei":"0", "sNisaGaisanHyoukagakuGoukei":"0", "sNisaGaisanHyoukaSonekiGoukei":"0", "sNseityouGaisanHyoukagakuGoukei":"0", "sNseityouGaisanHyoukaSonekiGoukei":"0", "sTokuteiGaisanHyoukagakuGoukei":"8315050", "sTokuteiGaisanHyoukaSonekiGoukei":"-810050", "sTotalGaisanHyoukagakuGoukei":"8315050", "sTotalGaisanHyoukaSonekiGoukei":"-810050", "aGenbutuKabuList": [  {   "sUriOrderWarningCode":"0",   "sUriOrderWarningText":"",   "sUriOrderIssueCode":"7201",   "sUriOrderZyoutoekiKazeiC":"1",   "sUriOrderZanKabuSuryou":"4200",   "sUriOrderUritukeKanouSuryou":"4200",   "sUriOrderGaisanBokaTanka":"727.0000",   "sUriOrderHyoukaTanka":"598.0000",   "sUriOrderGaisanHyoukagaku":"2511600",   "sUriOrderGaisanHyoukaSoneki":"-541800",   "sUriOrderGaisanHyoukaSonekiRitu":"-17.74",   "sSyuzituOwarine":"0",   "sZenzituHi":"0",   "sZenzituHiPer":"0",   "sUpDownFlag":"06",   "sNissyoukinKasikabuZan":"0"  } ]}
```

| sCLMID | 機能ＩＤ | CLMGenbutuKabuList |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sIppanGaisanHyoukagakuGoukei | 概算評価額合計　(一般口座残高) | 0～9999999999999999 |
| sIppanGaisanHyoukaSonekiGoukei | 概算評価損益合計(一般口座残高) | -999999999999999～9999999999999999 |
| sNisaGaisanHyoukagakuGoukei | 概算評価額合計　(NISA口座残高) | 0～9999999999999999 |
| sNisaGaisanHyoukaSonekiGoukei | 概算評価損益合計(NISA口座残高) | -999999999999999～9999999999999999 |
| sNseityouGaisanHyoukagakuGoukei | 概算評価額合計　(N成長口座残高) | 0～9999999999999999 |
| sNseityouGaisanHyoukaSonekiGoukei | 概算評価損益合計(N成長口座残高) | -999999999999999～9999999999999999 |
| sTokuteiGaisanHyoukagakuGoukei | 概算評価額合計　(特定口座残高) | 0～9999999999999999 |
| sTokuteiGaisanHyoukaSonekiGoukei | 概算評価損益合計(特定口座残高) | -999999999999999～9999999999999999 |
| sTotalGaisanHyoukagakuGoukei | 概算評価額合計　(残高合計) | 0～9999999999999999 |
| sTotalGaisanHyoukaSonekiGoukei | 概算評価損益合計(残高合計) | 0～9999999999999999 |
| aGenbutuKabuList | 現物保有リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sUriOrderWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sUriOrderWarningText | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sUriOrderIssueCode | 銘柄コード | 保有銘柄コード |
| sUriOrderZyoutoekiKazeiC | 譲渡益課税区分 | CLMKabuNewOrder.sZyoutoekiKazeiC 参照 |
| sUriOrderZanKabuSuryou | 残高株数 | 0～9999999999999 |
| sUriOrderUritukeKanouSuryou | 売付可能株数 | 0～9999999999999 |
| sUriOrderGaisanBokaTanka | 概算簿価単価 | 0.0000～999999999.9999 |
| sUriOrderHyoukaTanka | 評価単価 | 0.0000～999999999.9999 |
| sUriOrderGaisanHyoukagaku | 評価金額 | 0～9999999999999999 |
| sUriOrderGaisanHyoukaSoneki | 評価損益 | -999999999999999～9999999999999999 |
| sUriOrderGaisanHyoukaSonekiRitu | 評価損益率(%) | -999999999.99～9999999999.99 |
| sSyuzituOwarine | 前日終値 | 0.0000～999999999.9999該当値取得不可時:"" |
| sZenzituHi | 前日比 | -9999999.9999～99999999.9999該当値取得不可時:"" |
| sZenzituHiPer | 前日比(%) | -999.99～999.99該当値取得不可時:"" |
| sUpDownFlag | 騰落率Flag(%) | 以下フラグ値を設定01：+5.01 以上02：+3.01 ～+5.0003：+2.01 ～+3.0004：+1.01 ～+2.0005：+0.01 ～+1.0006：0 変化なし07：-0.01 ～-1.0008：-1.01 ～-2.0009：-2.01 ～-3.0010：-3.01 ～-5.0011：-5.01 以下前日比(%)取得不可時:"" |
| sNissyoukinKasikabuZan | 証金貸株残 | 0～9999999999999該当値取得不可時:"" |

<a name="CLMShinyouTategyokuList"></a>
### 信用建玉一覧

#### 要求

```json
{ "sCLMID":"CLMShinyouTategyokuList", "sIssueCode":"7201"}
```

| sCLMID | 機能ＩＤ | CLMShinyouTategyokuList |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 指定あり：指定１銘柄のリスト取得（例:"7201"）指定なし：全保有銘柄のリスト取得（例:""） |
| **⚠️ 【注意】　各合計値（リスト外項目）と銘柄個別値（リスト内項目）を応答する。　リスト外項目は銘柄コードの指定に依存しない。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMShinyouTategyokuList", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"7201", "sUritateDaikin":"0", "sKaitateDaikin":"70000", "sTotalDaikin":"70000", "sHyoukaSonekiGoukeiUridate":"0", "sHyoukaSonekiGoukeiKaidate":"-7783", "sTokuteiHyoukaSonekiGoukei":"-7783", "sTotalHyoukaSonekiGoukei":"-7783", "sIppanHyoukaSonekiGoukei":"0", "aShinyouTategyokuList": [  {   "sOrderWarningCode":"0",   "sOrderWarningText":"",   "sOrderTategyokuNumber":"202310160003492",   "sOrderIssueCode":"7201",   "sOrderSizyouC":"00",   "sOrderBaibaiKubun":"3",   "sOrderBensaiKubun":"26",   "sOrderZyoutoekiKazeiC":"1",   "sOrderTategyokuSuryou":"100",   "sOrderTategyokuTanka":"700.0000",   "sOrderHyoukaTanka":"622.2000",   "sOrderGaisanHyoukaSoneki":"-7783",   "sOrderGaisanHyoukaSonekiRitu":"-11.11",   "sTategyokuDaikin":"70000",   "sOrderTateTesuryou":"0",   "sOrderZyunHibu":"3",   "sOrderGyakuhibu":"0",   "sOrderKakikaeryou":"0",   "sOrderKanrihi":"0",   "sOrderKasikaburyou":"0",   "sOrderSonota":"0",   "sOrderTategyokuDay":"20231016",   "sOrderTategyokuKizituDay":"20240415",   "sTategyokuSuryou":"100",   "sOrderYakuzyouHensaiKabusu":"0",   "sOrderGenbikiGenwatasiKabusu":"0",   "sOrderOrderSuryou":"0",   "sOrderHensaiKanouSuryou":"100",   "sSyuzituOwarine":"",   "sZenzituHi":"",   "sZenzituHiPer":"",   "sUpDownFlag":""  } ]}
```

| sCLMID | 機能ＩＤ | CLMShinyouTategyokuList |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sUritateDaikin | 売建代金合計 | 0～9999999999999999 |
| sKaitateDaikin | 買建代金合計 | 0～9999999999999999 |
| sTotalDaikin | 総代金合計 | 0～9999999999999999 |
| sHyoukaSonekiGoukeiUridate | 評価損益合計_売建 | -999999999999999～9999999999999999 |
| sHyoukaSonekiGoukeiKaidate | 評価損益合計_買建 | -999999999999999～9999999999999999 |
| sTotalHyoukaSonekiGoukei | 総評価損益合計 | -999999999999999～9999999999999999 |
| sTokuteiHyoukaSonekiGoukei | 特定口座残高評価損益合計 | -999999999999999～9999999999999999 |
| sIppanHyoukaSonekiGoukei | 一般口座残高評価損益合計 | -999999999999999～9999999999999999 |
| aShinyouTategyokuList | 信用建玉リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sOrderWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sOrderWarningText | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sOrderTategyokuNumber | 建玉番号 | 保有建玉番号 |
| sOrderIssueCode | 銘柄コード | 保有銘柄コード |
| sOrderSizyouC | 市場 | 00：東証 |
| sOrderBaibaiKubun | 売買区分 | CLMKabuNewOrder.sBaibaiKubun 参照 |
| sOrderBensaiKubun | 弁済区分 | 00：なし26：制度信用6ヶ月29：制度信用無期限36：一般信用6ヶ月39：一般信用無期限 |
| sOrderZyoutoekiKazeiC | 譲渡益課税区分 | 1：特定3：一般5：NISA9：法人 |
| sOrderTategyokuSuryou | 建株数 | 0～9999999999999 |
| sOrderTategyokuTanka | 建単価 | 0.0000～999999999.9999 |
| sOrderHyoukaTanka | 評価単価 | 0.0000～999999999.9999 |
| sOrderGaisanHyoukaSoneki | 評価損益 | -999999999999999～9999999999999999 |
| sOrderGaisanHyoukaSonekiRitu | 評価損益率(%) | -999999999.99～9999999999.99 |
| sTategyokuDaikin | 建玉代金 | 0～9999999999999999 |
| sOrderTateTesuryou | 建手数料 | 0～9999999999999999 |
| sOrderZyunHibu | 順日歩 | 0～9999999999999999 |
| sOrderGyakuhibu | 逆日歩 | 0～9999999999999999 |
| sOrderKakikaeryou | 書換料 | 0～9999999999999999 |
| sOrderKanrihi | 管理費 | 0～9999999999999999 |
| sOrderKasikaburyou | 貸株料 | 0～9999999999999999 |
| sOrderSonota | その他 | 0～9999999999999999 |
| sOrderTategyokuDay | 建日 | YYYYMMDD00000000 |
| sOrderTategyokuKizituDay | 建玉期日日 | YYYYMMDD00000000：無期限 |
| sTategyokuSuryou | 建玉数量 | 0～9999999999999 |
| sOrderYakuzyouHensaiKabusu | 約定返済株数 | 0～9999999999999 |
| sOrderGenbikiGenwatasiKabusu | 現引現渡株数 | 0～9999999999999 |
| sOrderOrderSuryou | 注文中数量 | 0～9999999999999 |
| sOrderHensaiKanouSuryou | 返済可能数量 | 0～9999999999999 |
| sSyuzituOwarine | 前日終値 | 0.0000～999999999.9999該当値取得不可時:"" |
| sZenzituHi | 前日比 | -9999999.9999～99999999.9999該当値取得不可時:"" |
| sZenzituHiPer | 前日比(%) | -999.99～999.99該当値取得不可時:"" |
| sUpDownFlag | 騰落率Flag(%) | 以下フラグ値を設定01：+5.01 以上02：+3.01 ～+5.0003：+2.01 ～+3.0004：+1.01 ～+2.0005：+0.01 ～+1.0006：0 変化なし07：-0.01 ～-1.0008：-1.01 ～-2.0009：-2.01 ～-3.0010：-3.01 ～-5.0011：-5.01 以下前日比(%)取得不可時:"" |

<a name="CLMZanKaiKanougaku"></a>
### 買余力

#### 要求

```json
{ "sCLMID":"CLMZanKaiKanougaku", "sIssueCode":"", "sSizyouC":""}
```

| sCLMID | 機能ＩＤ | CLMZanKaiKanougaku |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 未使用 |
| sSizyouC | 市場 | 未使用 |
| **⚠️ 【注意】　要求項目の銘柄コード、市場は不要です。　ただし応答項目は影響を考慮し残してあります。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMZanKaiKanougaku", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"", "sSizyouC":"", "sSummaryUpdate":"202312311100", "sSummaryGenkabuKaituke":"1000000", "sSummaryNseityouTousiKanougaku":"0", "sHusokukinHasseiFlg":"0"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiKanougaku |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sSizyouC | 市場 | 要求設定値 |
| sSummaryUpdate | 更新日時 | YYYYMMDDHHMM |
| sSummaryGenkabuKaituke | 株式現物買付可能額 | 0～9999999999999999 |
| sSummaryNseityouTousiKanougaku | NISA成長投資可能額 | 0～9999999999999999 |
| sHusokukinHasseiFlg | 不足金発生フラグ | 0：未発生1：発生 |

<a name="CLMZanShinkiKanoIjiritu"></a>
### 建余力＆本日維持率

#### 要求

```json
{ "sCLMID":"CLMZanShinkiKanoIjiritu", "sIssueCode":"", "sSizyouC":""}
```

| sCLMID | 機能ＩＤ | CLMZanShinkiKanoIjiritu |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 未使用 |
| sSizyouC | 市場 | 未使用 |
| **⚠️ 【注意】　要求項目の銘柄コード、市場は不要です。　ただし応答項目は影響を考慮し残してあります。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMZanShinkiKanoIjiritu", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"", "sSizyouC":"", "sSummaryUpdate":"202312311100", "sSummarySinyouSinkidate":"1000000", "sItakuhosyoukin":"0.00", "sOisyouKakuteiFlg":"0"}
```

| sCLMID | 機能ＩＤ | CLMZanShinkiKanoIjiritu |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sSizyouC | 市場 | 要求設定値 |
| sSummaryUpdate | 更新日時 | YYYYMMDDHHMM |
| sSummarySinyouSinkidate | 信用新規建可能額 | 0～9999999999999999 |
| sItakuhosyoukin | 委託保証金率(%) | 0.00～9999999999.99 |
| sOisyouKakuteiFlg | 追証フラグ | 0：未確定1：確定 |

<a name="CLMZanUriKanousuu"></a>
### 売却可能数量

#### 要求

```json
{ "sCLMID":"CLMZanUriKanousuu", "sIssueCode":"6501"}
```

| sCLMID | 機能ＩＤ | CLMZanUriKanousuu |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 例:6501 |

#### 応答

```json
{ "sCLMID":"CLMZanUriKanousuu", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"6501", "sSummaryUpdate":"202312311100", "sZanKabuSuryouUriKanouIppan":"1000000", "sZanKabuSuryouUriKanouTokutei":"0", "sZanKabuSuryouUriKanouNisa":"0", "sZanKabuSuryouUriKanouNseityou":"0",}
```

| sCLMID | 機能ＩＤ | CLMZanUriKanousuu |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sSummaryUpdate | 更新日時 | YYYYMMDDHHMM |
| sZanKabuSuryouUriKanouIppan | 売付可能株数(一般) | 0～9999999999999 |
| sZanKabuSuryouUriKanouTokutei | 売付可能株数(特定) | 0～9999999999999 |
| sZanKabuSuryouUriKanouNisa | 売付可能株数(NISA) | 0～9999999999999 |
| sZanKabuSuryouUriKanouNseityou | 売付可能株数(N成長) | 0～9999999999999 |

<a name="CLMOrderList"></a>
### 注文一覧

#### 要求

```json
{ "sCLMID":"CLMOrderList",＊＊＊＊以下は任意指定項目、指定項目をＡＮＤ条件で検索＊＊＊＊ "sIssueCode":"8411", "sSikkouDay":"", "sOrderSyoukaiStatus":""}
```

| sCLMID | 機能ＩＤ | CLMOrderList |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 指定あり：指定１銘柄のリスト取得（例:"8411"）指定なし：全保有銘柄のリスト取得（例:""） |
| sSikkouDay | 注文執行予定日（営業日） | CLMKabuNewOrder.sEigyouDay 参照指定あり：指定１営業日のリスト取得（例:"20231018"）指定なし：全保有営業日のリスト取得（例:""） |
| sOrderSyoukaiStatus | 注文照会状態 | ""：指定なし1：未約定2：全部約定3：一部約定4：訂正取消(可能な注文）5：未約定+一部約定指定あり：指定１状態のリスト取得（例:"2"）指定なし：全保有状態のリスト取得（例:""） |
| **⚠️ 【注意】　要求項目（sCLMID 以外）は任意指定（ＡＮＤ条件）項目で、　指定項目値該当情報をリストとして応答する。　注文執行予定日（営業日）は夕方の日替処理（で翌営業日に変更）以降、　その前後（繰越前、繰越後）の情報取得に使用する。　過去の注文情報が取得できる訳ではないので注意されたい。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMOrderList", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sIssueCode":"8411", "sOrderSyoukaiStatus":"", "sSikkouDay":"", "aOrderList": [  {   "sOrderWarningCode":"0",   "sOrderWarningText":"",   "sOrderOrderNumber":"18000002",   "sOrderIssueCode":"8411",   "sOrderSizyouC":"00",   "sOrderZyoutoekiKazeiC":"1",   "sGenkinSinyouKubun":"0",   "sOrderBensaiKubun":"00",   "sOrderBaibaiKubun":"3",   "sOrderOrderSuryou":"100",   "sOrderCurrentSuryou":"0",   "sOrderOrderPrice":"2300.0000",   "sOrderCondition":"0",   "sOrderOrderPriceKubun":"2",   "sOrderGyakusasiOrderType":"0",   "sOrderGyakusasiZyouken":"0.0000",   "sOrderGyakusasiKubun":" ",   "sOrderGyakusasiPrice":"0.0000",   "sOrderTriggerType":"0",   "sOrderTatebiType":" ",   "sOrderZougen":"",   "sOrderYakuzyouSuryo":"100",   "sOrderYakuzyouPrice":"2300.0000",   "sOrderUtidekiKbn":" ",   "sOrderSikkouDay":"20231018",   "sOrderStatusCode":"10",   "sOrderStatus":"全部約定",   "sOrderYakuzyouStatus":"2",   "sOrderOrderDateTime":"20231018091407",   "sOrderOrderExpireDay":"20231031",   "sOrderKurikosiOrderFlg":"0",   "sOrderCorrectCancelKahiFlg":"1",   "sGaisanDaikin":"230187"  } ]}
```

| sCLMID | 機能ＩＤ | CLMOrderList |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sSikkouDay | 注文執行予定日 | 要求設定値 |
| sOrderSyoukaiStatus | 注文照会状態 | 要求設定値 |
| aOrderList | 注文リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sOrderWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sOrderWarningText | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sOrderOrderNumber | 注文番号 | CLMKabuNewOrder.sOrderNumber 参照 |
| sOrderIssueCode | 銘柄コード | CLMKabuNewOrder.sIssueCode 参照 |
| sOrderSizyouC | 市場 | CLMKabuNewOrder.SizyouC 参照 |
| sOrderZyoutoekiKazeiC | 譲渡益課税区分 | CLMKabuNewOrder.sZyoutoekiKazeiC 参照 |
| sGenkinSinyouKubun | 現金信用区分 | CLMKabuNewOrder.sGenkinShinyouKubun 参照 |
| sOrderBensaiKubun | 弁済区分 | 00：なし26：制度信用6ヶ月29：制度信用無期限36：一般信用6ヶ月39：一般信用無期限 |
| sOrderBaibaiKubun | 売買区分 | CLMKabuNewOrder.sBaibaiKubun 参照 |
| sOrderOrderSuryou | 注文株数 | 0～9999999999999 |
| sOrderCurrentSuryou | 有効株数 | Ｎ≦CLMKabuNewOrder.sOrderSuryou |
| sOrderOrderPrice | 注文単価 | 0.0000～999999999.9999 |
| sOrderCondition | 執行条件 | CLMKabuNewOrder.sCondition 参照 |
| sOrderOrderPriceKubun | 注文値段区分 | " "：未使用1：成行2：指値3：親注文より高い4：親注文より低い |
| sOrderGyakusasiOrderType | 逆指値注文種別 | CLMKabuNewOrder.sGyakusasiOrderType 参照 |
| sOrderGyakusasiZyouken | 逆指値条件 | 0.0000～999999999.9999 |
| sOrderGyakusasiKubun | 逆指値値段区分 | " "：未使用0：成行1：指値 |
| sOrderGyakusasiPrice | 逆指値値段 | 0.0000～999999999.9999 |
| sOrderTriggerType | トリガータイプ | 0：未トリガー（初期値）トリガー発火後は以下に遷移。1：自動2：手動発注3：手動失効 |
| sOrderTatebiType | 建日種類 | 信用返済時に指定する返済建玉順序種類指定" "：指定なし1：個別指定2：建日順3：単価益順4：単価損順 |
| sOrderZougen | リバース増減値 | 未使用 |
| sOrderYakuzyouSuryo | 成立株数 | 0～9999999999999 |
| sOrderYakuzyouPrice | 成立単価 | 0.0000～999999999.9999 |
| sOrderUtidekiKbn | 内出来区分 | " "：約定分割以外2：約定分割 |
| sOrderSikkouDay | 執行日 | YYYYMMDD |
| sOrderStatusCode | 状態コード | [通常注文]の状態0：受付未済1：未約定2：受付エラー3：訂正中4：訂正完了5：訂正失敗6：取消中7：取消完了8：取消失敗9：一部約定10：全部約定11：一部失効12：全部失効13：発注待ち14：無効15：切替注文16：切替完了17：切替注文失敗19：繰越失効20：一部障害処理21：障害処理[逆指値注文]、[通常+逆指値注文]の状態15：逆指注文(切替中)16：逆指注文(未約定)17：逆指注文(失敗)50：発注中 |
| sOrderStatus | 状態名称 | 状態コードの名称 |
| sOrderYakuzyouStatus | 約定ステータス | 0：未約定1：一部約定2：全部約定3：約定中 |
| sOrderOrderDateTime | 注文日付 | YYYYMMDDHHMMSS00000000000000 |
| sOrderOrderExpireDay | 有効期限 | YYYYMMDD00000000 |
| sOrderKurikosiOrderFlg | 繰越注文フラグ | 0：当日注文1：繰越注文2：無効 |
| sOrderCorrectCancelKahiFlg | 訂正取消可否フラグ | 0：可(取消、訂正)1：否2：一部可(取消のみ) |
| sGaisanDaikin | 概算代金 | -999999999999999～9999999999999999 |

<a name="CLMOrderListDetail"></a>
### 注文約定一覧（詳細）

#### 要求

```json
{ "sCLMID":"CLMOrderListDetail", "sOrderNumber":"18000002", "sEigyouDay":"20231018"}
```

| sCLMID | 機能ＩＤ | CLMOrderListDetail |
| --- | --- | --- |
| sOrderNumber | 注文番号 | CLMKabuNewOrder.sOrderNumber 参照 |
| sEigyouDay | 営業日 | CLMKabuNewOrder.sEigyouDay 参照 |
| **⚠️ 【注意】　要求項目は全て必須指定です。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMOrderListDetail", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sOrderNumber":"18000004", "sEigyouDay":"20231018", "sIssueCode":"8411", "sOrderSizyouC":"00", "sOrderBaibaiKubun":"1", "sGenkinSinyouKubun":"4", "sOrderBensaiKubun":"26", "sOrderCondition":"0", "sOrderOrderPriceKubun":"1", "sOrderOrderPrice":"0.0000", "sOrderOrderSuryou":"100", "sOrderCurrentSuryou":"0", "sOrderStatusCode":"10", "sOrderStatus":"全部約定", "sOrderOrderDateTime":"20231018104821", "sOrderOrderExpireDay":"00000000", "sChannel":"1", "sGenbutuZyoutoekiKazeiC":"1", "sSinyouZyoutoekiKazeiC":"1", "sGyakusasiOrderType":"0", "sGyakusasiZyouken":"0.0000", "sGyakusasiKubun":" ", "sGyakusasiPrice":"0.0000", "sTriggerType":"0", "sTriggerTime":"00000000000000", "sUkewatasiDay":"20231020", "sYakuzyouPrice":"2300.0000", "sYakuzyouSuryou":"100", "sBaiBaiDaikin":"230000", "sUtidekiKubun":" ", "sGaisanDaikin":"-11", "sBaiBaiTesuryo":"0", "sShouhizei":"0", "sTatebiType":"1", "sSizyouErrorCode":"", "sZougen":"", "sOrderAcceptTime":"20231018104942", "sOrderExpireDayLimit":"20231031", "aYakuzyouSikkouList": [  {   "sYakuzyouWarningCode":"0",   "sYakuzyouWarningText":"",   "sYakuzyouSuryou":"100",   "sYakuzyouPrice":"2300.0000",   "sYakuzyouDate":"20231018104942"  } ], "aKessaiOrderTategyokuList": [  {   "sKessaiWarningCode":"0",   "sKessaiWarningText":"",   "sKessaiTatebiZyuni":"1",   "sKessaiTategyokuDay":"20231018",   "sKessaiTategyokuPrice":"2300.0000",   "sKessaiOrderSuryo":"100",   "sKessaiYakuzyouSuryo":"100",   "sKessaiYakuzyouPrice":"2300.0000",   "sKessaiTateTesuryou":"0",   "sKessaiZyunHibu":"11",   "sKessaiGyakuhibu":"0",   "sKessaiKakikaeryou":"0",   "sKessaiKanrihi":"0",   "sKessaiKasikaburyou":"0",   "sKessaiSonota":"0",   "sKessaiSoneki":"-11"  } ]}
```

| sCLMID | 機能ＩＤ | CLMOrderListDetail |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sOrderNumber | 注文番号 | CLMKabuNewOrder.sOrderNumber 参照 |
| sEigyouDay | 営業日 | CLMKabuNewOrder.sEigyouDay 参照 |
| sIssueCode | 銘柄コード | CLMKabuNewOrder.sIssueCode 参照 |
| sOrderSizyouC | 市場 | CLMKabuNewOrder.sSizyouC 参照 |
| sOrderBaibaiKubun | 売買区分 | CLMKabuNewOrder.sBaibaiKubun 参照 |
| sGenkinSinyouKubun | 現金信用区分 | CLMKabuNewOrder.sGenkinShinyouKubun 参照 |
| sOrderBensaiKubun | 弁済区分 | CLMOrderList.sOrderBensaiKubun 参照 |
| sOrderCondition | 執行条件 | CLMKabuNewOrder.sCondition 参照 |
| sOrderOrderPriceKubun | 注文値段区分 | CLMOrderList.sOrderOrderPriceKubun 参照 |
| sOrderOrderPrice | 注文単価 | CLMOrderList.sOrderOrderPrice 参照 |
| sOrderOrderSuryou | 注文株数 | CLMOrderList.sOrderOrderSuryou 参照 |
| sOrderCurrentSuryou | 有効株数 | CLMOrderList.sOrderCurrentSuryou 参照 |
| sOrderStatusCode | 状態コード | CLMOrderList.sOrderStatusCode 参照 |
| sOrderStatus | 状態名称 | CLMOrderList.sOrderStatus 参照 |
| sOrderOrderDateTime | 注文日付 | CLMOrderList.sOrderOrderDateTime 参照 |
| sOrderOrderExpireDay | 有効期限 | CLMOrderList.sOrderOrderExpireDay 参照 |
| sChannel | チャネル | 1：標準Ｗｅｂ（PC）2：コールセンター（CC2）3：コールセンター（CC3）4：コールセンター（CC4）5：モバイル（MBL）6：リッチ（RCA）7：スマホ・タブレット（SMT）8：iPadアプリ（IPA）B：BRiSK NEXT（BRiSK）E：リッチ（RCH）F：ｅ支店・ＡＰＩ（API） |
| sGenbutuZyoutoekiKazeiC | 現物口座区分 | CLMOrderList.sOrderZyoutoekiKazeiC 参照 |
| sSinyouZyoutoekiKazeiC | 建玉口座区分 | 1：特定3：一般 |
| sGyakusasiOrderType | 逆指値注文種別 | 0：通常1：逆指値2：通常＋逆指値 |
| sGyakusasiZyouken | 逆指値条件 | 0.0000～999999999.9999 |
| sGyakusasiKubun | 逆指値値段区分 | CLMOrderList.sOrderGyakusasiKubun 参照 |
| sGyakusasiPrice | 逆指値値段 | 0.0000～999999999.9999 |
| sTriggerType | トリガータイプ | CLMOrderList.sOrderTriggerType 参照 |
| sTriggerTime | トリガー日時 | YYYYMMDDHHMMSS00000000000000 |
| sUkewatasiDay | 受渡日 | YYYYMMDD00000000 |
| sYakuzyouPrice | 約定単価 | 0.0000～999999999.9999 |
| sYakuzyouSuryou | 約定株数 | 0～9999999999999 |
| sBaiBaiDaikin | 売買代金 | 0～9999999999999999 |
| sUtidekiKubun | 内出来区分 | CLMOrderList.sOrderUtidekiKbn 参照 |
| sGaisanDaikin | 概算代金 | 0～9999999999999999 |
| sBaiBaiTesuryo | 手数料 | 0～9999999999999999 |
| sShouhizei | 消費税 | 0～9999999999999999 |
| sTatebiType | 建日種類 | CLMOrderList.sOrderTatebiType 参照 |
| sSizyouErrorCode | 取引所エラー等理由コード | ""：正常上記以外はマスタ情報ダウンロード取引所エラー等理由コード（CLMOrderErrReason）参照 |
| sZougen | リバース増減値 | 未使用 |
| sOrderAcceptTime | 取引所受付／エラー時刻 | YYYYMMDDHHMMSS00000000000000※「通常＋逆指値」の場合は、最初の通常注文の市場注文受付時刻をセット |
| sOrderExpireDayLimit | 注文失効日付 | YYYYMMDD |
| aYakuzyouSikkouList | 約定失効リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sYakuzyouWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sYakuzyouWarningText | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sYakuzyouSuryou | 約定数量 | 0～9999999999999 |
| sYakuzyouPrice | 約定価格 | 0.0000～999999999.9999 |
| sYakuzyouDate | 約定日時 | YYYYMMDDHHMMSS00000000000000 |
| aKessaiOrderTategyokuList | 決済注文建株指定リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sKessaiWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sKessaiWarningText | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sKessaiTatebiZyuni | 順位 | 0～999999999 |
| sKessaiTategyokuDay | 建日 | YYYYMMDD00000000 |
| sKessaiTategyokuPrice | 建単価 | 0.0000～999999999.9999 |
| sKessaiOrderSuryo | 返済注文株数 | 0～9999999999999 |
| sKessaiYakuzyouSuryo | 約定株数 | 0～9999999999999 |
| sKessaiYakuzyouPrice | 約定単価 | 0.0000～999999999.9999 |
| sKessaiTateTesuryou | 建手数料 | 0～9999999999999999 |
| sKessaiZyunHibu | 順日歩 | 0～9999999999999999 |
| sKessaiGyakuhibu | 逆日歩 | 0～9999999999999999 |
| sKessaiKakikaeryou | 書換料 | 0～9999999999999999 |
| sKessaiKanrihi | 管理費 | 0～9999999999999999 |
| sKessaiKasikaburyou | 貸株料 | 0～9999999999999999 |
| sKessaiSonota | その他 | 0～9999999999999999 |
| sKessaiSoneki | 決済損益/受渡代金 | -999999999999999～9999999999999999 |

<a name="CLMZanKaiSummary"></a>
### 可能額サマリー

#### 要求

```json
{ "sCLMID":"CLMZanKaiSummary"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiSummary |
| --- | --- | --- |

#### 応答

```json
{ "sCLMID":"CLMZanKaiSummary", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sUpdateDate":"202310200849", "sOisyouHasseiFlg":"0", "sOhzsKeisanDay":"", "sOhzsGenkinHosyoukin":"", "sOhzsDaiyouHyoukagaku":"", "sOhzsSasiireHosyoukin":"", "sOhzsHyoukaSoneki":"", "sOhzsSyokeihi":"", "sOhzsMiukeKessaiSon":"", "sOhzsMiukeKessaiEki":"", "sOhzsUkeireHosyoukin":"", "sOhzsTatekabuDaikin":"", "sOhzsItakuHosyoukinRitu":"", "sTatekaekinHasseiFlg":"0", "sThzNyukinKigenDay":"", "sThzSeisangaku":"", "sThzHibakariKousokukin":"", "sThzHurikaegaku":"", "sThzHituyouNyukingaku":"", "sThzKakuteiFlg":"", "sGenbutuKabuKaituke":"1144578", "sSinyouSinkidate":"26291254", "sSinyouGenbiki ":"1144578", "sHosyouKinritu":"12427.44", "sNseityouTousiKanougaku":"", "sTousinKaituke":"1144578", "sRuitouKaituke":"0", "sIPOKounyu":"1144578", "sSyukkin":"1144578", "sFusokugaku":"0", "sLargeKaidateYoryoku":"0", "sMiniKaidateYoryoku ":"0", "sLargeUridateYoryoku":"0", "sMiniUridateYoryoku":"0", "sOpKaidateYoryokyu":"0", "sSyoukokinFusokugaku":"0", "sGenbutuBaibaiDaikin":"0", "sGenbutuOrderCount":"0", "sGenbutuYakuzyouCount":"0", "sSinyouBaibaiDaikin":"0", "sSinyouOrderCount":"0", "sSinyouYakuzyouCount":"0", "sSakiBaibaiDaikin":"0", "sSakiOrderCount":"0", "sSakiYakuzyouCount":"0", "sOpBaibaiDaikin":"0", "sOpOrderCount":"0", "sOpYakuzyouCount":"0", "aHikazeiKouzaList": [  {   "sHikazeiTekiyouYear":"2023",   "sSeityouTousiKanougaku":"300000"  } ], "aOisyouHasseiZyoukyouList":"", "aHosyoukinSeikyuZyoukyouList":""}
```

| sCLMID | 機能ＩＤ | CLMZanKaiSummary |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sUpdateDate | 更新日時 | YYYYMMDDHHMM |
| sOisyouHasseiFlg | 追証発生フラグ | 1:追証　発生（追証発生状況詳細．ＯＸＯＸを設定）0:追証未発生（追証発生状況詳細．ＯＸＯＸ未設定） |
| sOhzsKeisanDay | 追証発生状況詳細.計算日 | YYYYMMDD |
| sOhzsGenkinHosyoukin | 追証発生状況詳細.現金保証金 | 0～9999999999999999 |
| sOhzsDaiyouHyoukagaku | 追証発生状況詳細.代用証券評価額 | 0～9999999999999999 |
| sOhzsSasiireHosyoukin | 追証発生状況詳細.差入保証金 | 0～9999999999999999 |
| sOhzsHyoukaSoneki | 追証発生状況詳細.評価損益 | 0～9999999999999999 |
| sOhzsSyokeihi | 追証発生状況詳細.諸経費 | 0～9999999999999999 |
| sOhzsMiukeKessaiSon | 追証発生状況詳細.未受渡決済損 | 0～9999999999999999 |
| sOhzsMiukeKessaiEki | 追証発生状況詳細.未受渡決済益 | 0～9999999999999999 |
| sOhzsUkeireHosyoukin | 追証発生状況詳細.受入保証金 | 0～9999999999999999 |
| sOhzsTatekabuDaikin | 追証発生状況詳細.建株代金 | 0～9999999999999999 |
| sOhzsItakuHosyoukinRitu | 追証発生状況詳細.委託保証金率(%) | 0～9999999999999 |
| sTatekaekinHasseiFlg | 立替金発生フラグ | 1:立替金　発生（立替金発生状況．ＯＸＯＸを設定）0:立替金未発生（立替金発生状況．ＯＸＯＸ未設定） |
| sThzNyukinKigenDay | 立替金発生状況.入金期限 | YYYYMMDD |
| sThzSeisangaku | 立替金発生状況.精算額 | 0～9999999999999999 |
| sThzHibakariKousokukin | 立替金発生状況.日計り拘束金 | 0～9999999999999999 |
| sThzHurikaegaku | 立替金発生状況.振替額 | 0～9999999999999999 |
| sThzHituyouNyukingaku | 立替金発生状況.必要入金額 | 0～9999999999999999 |
| sThzKakuteiFlg | 立替金発生状況.確定フラグ | 1:入金請求管理.計算日＜営業日0:上記外 |
| sGenbutuKabuKaituke | 株式現物買付可能額 | 0～9999999999999999 |
| sSinyouSinkidate | 信用新規建可能額 | 0～9999999999999999 |
| sSinyouGenbiki | 信用現引可能額 | 0～9999999999999999 |
| sHosyouKinritu | 委託保証金率(%) | 0～9999999999.99 |
| sNseityouTousiKanougaku | NISA成長投資可能額 | 0～9999999999999999 |
| sTousinKaituke | 投信買付可能額 | 0～9999999999999999 |
| sRuitouKaituke | MMF・中国F買付 | 0～9999999999999999 |
| sIPOKounyu | IPO購入可能額 | 0～9999999999999999 |
| sSyukkin | 出金可能額 | 0～9999999999999999 |
| sFusokugaku | 不足額(入金請求額） | 0～9999999999999999 |
| sLargeKaidateYoryoku | 先物買建 | 0～9999999999999 |
| sMiniKaidateYoryoku | OPプット売建(ミニ) | 0～9999999999999 |
| sLargeUridateYoryoku | 先物売建 | 0～9999999999999 |
| sMiniUridateYoryoku | OPコール売建(ミニ) | 0～9999999999999 |
| sOpKaidateYoryokyu | オプション新規買建 | 0～9999999999999999 |
| sSyoukokinFusokugaku | 証拠金不足額（本日請求額） | 0～9999999999999999 |
| sGenbutuBaibaiDaikin | 現物売買代金 | 0～9999999999999999 |
| sGenbutuOrderCount | 現物注文件数 | 0～9999999999999 |
| sGenbutuYakuzyouCount | 現物約定件数 | 0～9999999999999 |
| sSinyouBaibaiDaikin | 信用売買代金 | 0～9999999999999999 |
| sSinyouOrderCount | 信用注文件数 | 0～9999999999999 |
| sSinyouYakuzyouCount | 信用約定件数 | 0～9999999999999 |
| sSakiBaibaiDaikin | 先物売買代金 | 0～9999999999999999 |
| sSakiOrderCount | 先物注文件数 | 0～9999999999999 |
| sSakiYakuzyouCount | 先物約定件数 | 0～9999999999999 |
| sOpBaibaiDaikin | オプション売買代金 | 0～9999999999999999 |
| sOpOrderCount | オプション注文件数 | 0～9999999999999 |
| sOpYakuzyouCount | オプション約定件数 | 0～9999999999999 |
| aHikazeiKouzaList | 非課税口座リスト | 以下レコードを配列で設定 |
| sHikazeiTekiyouYear | 適用年（対象年） | YYYY、非課税適用年度（今年か翌年） |
| sSeityouTousiKanougaku | 成長投資可能額 | 0～999999999999999 |
| aOisyouHasseiZyoukyouList | 追証発生状況リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sOhzHasseiDay | 発生日 | YYYYMMDD |
| sOhzHosyoukinRitu | 保証金率(%) | 0～9999999999999999 |
| sOhzNyukinKigenDay | 入金期限 | YYYYMMDDHHMM |
| sOhzOisyouKingaku | 追証金額 | 0～9999999999999999 |
| sOhzKakuteiFlg | 確定フラグ | 1:入金請求管理.計算日＜営業日0:上記外 |
| sOhzHosyoukinZougen | 保証金増減 | 0～9999999999999999 |
| sOhzNyukin | 入金 | 0～9999999999999999 |
| sOhzTategyokuKessai | 建玉決済 | 0～9999999999999999 |
| sOhzKessaisonNyukin | 決済損入金 | 0～9999999999999999 |
| sOhzMikaisyouKingaku | 未解消金額 | 0～9999999999999999 |
| sOhzMikaisyouKingakuFlg | 未解消金額フラグ | 未使用 |
| aHosyoukinSeikyuZyoukyouList | 保証金請求発生状況リスト | 以下項目を配列で応答、情報が無い場合は"" |
| sHshzNyukinKigenDay | 入金期限 | 0YYYYMMDDHHMM |
| sHshzHosyoukinHasseiDay | 保証金発生日 | 0YYYYMMDDHHMM |
| sHshzHosyoukin | 保証金 | 0～9999999999999999 |
| sHshzGenkinHosyoukinHasseiDay | 現金保証金発生日 | 0YYYYMMDDHHMM |
| sHshzGenkinHosyoukin | 現金保証金 | 0～9999999999999999 |

<a name="CLMZanKaiKanougakuSuii"></a>
### 可能額推移

#### 要求

```json
{ "sCLMID":"CLMZanKaiKanougakuSuii"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiKanougakuSuii |
| --- | --- | --- |

#### 応答

```json
{ "sCLMID":"CLMZanKaiKanougakuSuii", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sUpdateDate":"202310201242", "sNearaiKubun":"0", "aKanougakuSuiiList": [  {   "sHituke":"20231020",   "sAzukariKin":"1144578",   "sHattyuZyutoukin":"0",   "sHibakariKousokukin":"0",   "sSonotaKousokukin":"0",   "sGenkinHosyoukin":"1144578",   "sDaiyouHyoukagaku":"202310200849",   "sSasiireHosyoukin":"8707818",   "sSinyouTateHyoukaSon":"8580",   "sSinyouTateHyoukaEki":"0",   "sSinyouTadeSyoukeihi":"24",   "sMiukewatasiKessaiSon":"0",   "sMiukewatasiKessaiEki":"0",   "sUkeireHosyoukin":"8699214",   "sMikessaiTateDaikin":"70000",   "sGenbikiWatasiTateDaikin":"0",   "sHituyouHosyoukin":"23100",   "sHituyouGenkinHosyoukin":"0",   "sHosyoukinYoryoku":"8676114",   "sGenkinHosyoukinYoryoku":"1144578",   "sItakuHosyoukinRitu":"12427.44",   "sHosyoukinHikidasiKousokukin":"308604",   "sHosyoukinHikidasiYoryoku":"8399214",   "sOisyouHituyouHosyoukin":"308604",   "sOisyouYoryoku":"8399214",   "sFusokugaku":"0",   "sGenbutuKaitukeKanougaku":"1144578",   "sSinyouSinkidateKanougaku":"26291254",   "sGenbikiKanougaku":"1144578",   "sTousinKaitukeKanougaku":"1144578",   "sSyukkinKanougaku":"1144578"  } ]}
```

| sCLMID | 機能ＩＤ | CLMZanKaiKanougakuSuii |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sIssueCode | 銘柄コード | 要求設定値 |
| sUpdateDate | 更新日時 | YYYYMMDDHHMM |
| sNearaiKubun | 値洗い区分 | 0:値洗い停止1:値洗い中2:値洗い終了 |
| aKanougakuSuiiList | 可能額推移リスト | 以下項目を配列で応答、情報が無い場合は""[0]:当日営業日[1]:２営業日[2]:３営業日[3]:４営業日[4]:５営業日[5]:６営業日 |
| sHituke | 日付 | YYYYMMDD |
| sAzukariKin | 預り金 | 0～9999999999999999 |
| sHattyuZyutoukin | 発注済み注文充当金 | 0～9999999999999999 |
| sHibakariKousokukin | 日計り拘束金 | 0～9999999999999999 |
| sSonotaKousokukin | その他拘束金 | 0～9999999999999999 |
| sGenkinHosyoukin | 現金保証金 | -999999999999999～9999999999999999 |
| sDaiyouHyoukagaku | 代用証券評価額 | 0～9999999999999999 |
| sSasiireHosyoukin | 差入保証金 | 0～9999999999999999 |
| sSinyouTateHyoukaSon | 信用建株 評価損 | 0～9999999999999999 |
| sSinyouTateHyoukaEki | 信用建株 評価益 | 0～9999999999999999 |
| sSinyouTadeSyoukeihi | 信用建株 諸経費 | 0～9999999999999999 |
| sMiukewatasiKessaiSon | 信用建株 未受渡決済損 | 0～9999999999999999 |
| sMiukewatasiKessaiEki | 信用建株 未受渡決済益 | 0～9999999999999999 |
| sUkeireHosyoukin | 受入保証金 | -999999999999999～9999999999999999 |
| sMikessaiTateDaikin | 未決済建株代金 | 0～9999999999999999 |
| sGenbikiWatasiTateDaikin | 現引/現渡建株代金 | 0～9999999999999999 |
| sHituyouHosyoukin | 必要保証金 | 0～9999999999999999 |
| sHituyouGenkinHosyoukin | 必要現金保証金 | 0～9999999999999999 |
| sHosyoukinYoryoku | 保証金余力 | 0～9999999999999999 |
| sGenkinHosyoukinYoryoku | 現金保証金余力 | 0～9999999999999999 |
| sItakuHosyoukinRitu | 委託保証金率(%) | -999999999.99～9999999999.99 |
| sHosyoukinHikidasiKousokukin | 保証金引出拘束金 | 0～9999999999999999 |
| sHosyoukinHikidasiYoryoku | 保証金引出余力 | 0～9999999999999999 |
| sOisyouHituyouHosyoukin | 追証必要保証金 | 0～9999999999999999 |
| sOisyouYoryoku | 追証余力 | 0～9999999999999999 |
| sFusokugaku | 追証/立替金/保証金不足額 | 0～9999999999999999 |
| sGenbutuKaitukeKanougaku | 現物株式買付可能額 | -999999999999999～9999999999999999 |
| sSinyouSinkidateKanougaku | 信用新規建可能額 | -999999999999999～9999999999999999 |
| sGenbikiKanougaku | 信用現引可能額 | -999999999999999～9999999999999999 |
| sTousinKaitukeKanougaku | 投信買付可能額、 | -999999999999999～9999999999999999 |
| sSyukkinKanougaku | 出金可能額 | -999999999999999～9999999999999999 |

<a name="CLMZanKaiGenbutuKaitukeSyousai"></a>
### 現物株式買付可能額詳細

#### 要求

```json
{ "sCLMID":"CLMZanKaiGenbutuKaitukeSyousai", "sHitukeIndex":"3"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiGenbutuKaitukeSyousai |
| --- | --- | --- |
| sHitukeIndex | 日付インデックス | 3:第4営業日4:第5営業日5:第6営業日 |

#### 応答

```json
{ "sCLMID":"CLMZanKaiGenbutuKaitukeSyousai", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sHitukeIndex":"3", "sHituke":"20231030", "sGenkinHosyoukin":"1383069", "sHosyoukinGenbutuKaitukeKanouga":"1383069", "sGenbutuKaitukeKanougaku":"1383069", "sAzukariKin":"1383069", "sHattyuZyutoukin":"0", "sHibakariKousokukin":"0", "sSonotaKousokukin":"0", "sHituyouGenkinHosyoukin":"0", "sDaiyouHyoukagaku":"7257880", "sTatekabuHyoukaSoneki":"-8940", "sTatekabuSyoukeihi":"232", "sMiukewatasiKessaiSon":"0", "sMiukewatasiKessaiEki":"0", "sUkeireHosyoukin":"8631777", "sHituyouHosyoukin":"244658", "sHosyoukinYoryoku":"8387119"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiGenbutuKaitukeSyousai |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sHitukeIndex | 日付インデックス | 要求設定値 |
| sHituke | 指定日（日付） | YYYYMMDD |
| sGenkinHosyoukin | 現金保証金 | -999999999999999～9999999999999999 |
| sHosyoukinGenbutuKaitukeKanouga | 保証金からの現物株式買付可能額 | 0～9999999999999999 |
| sGenbutuKaitukeKanougaku | 現物株式買付可能額 | -999999999999999～9999999999999999 |
| sAzukariKin | 預り金 | 0～9999999999999999 |
| sHattyuZyutoukin | 発注済み注文充当金 | 0～9999999999999999 |
| sHibakariKousokukin | 日計り拘束金 | 0～9999999999999999 |
| sSonotaKousokukin | その他拘束金 | 0～9999999999999999 |
| sHituyouGenkinHosyoukin | 必要現金保証金 | 0～9999999999999999 |
| sDaiyouHyoukagaku | 代用証券評価額 | 0～9999999999999999 |
| sTatekabuHyoukaSoneki | 建株評価損益 | -999999999999999～9999999999999999 |
| sTatekabuSyoukeihi | 建株諸経費 | 0～9999999999999999 |
| sMiukewatasiKessaiSon | 未受渡建株決済損 | 0～9999999999999999 |
| sMiukewatasiKessaiEki | 未受渡建株決済益 | 0～9999999999999999 |
| sUkeireHosyoukin | 受入保証金 | -999999999999999～9999999999999999 |
| sHituyouHosyoukin | 必要保証金 | -999999999999999～9999999999999999 |
| sHosyoukinYoryoku | 保証金余力 | -999999999999999～9999999999999999 |

<a name="CLMZanKaiSinyouSinkidateSyousai"></a>
### 信用新規建て可能額詳細

#### 要求

```json
{ "sCLMID":"CLMZanKaiSinyouSinkidateSyousai", "sHitukeIndex":"3"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiSinyouSinkidateSyousai |
| --- | --- | --- |
| sHitukeIndex | 日付インデックス | 0:第1営業日1:第2営業日2:第3営業日3:第4営業日4:第5営業日5:第6営業日 |

#### 応答

```json
{ "sCLMID":"CLMZanKaiSinyouSinkidateSyousai", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sHitukeIndex":"3", "sHituke":"20231030", "sUkeireHosyoukin":"8631777", "sHituyouHosyoukin":"244658", "sHosyoukinYoryoku":"8387119", "sHosyoukinTyousyuRitu":"33", "sSinyouSinkidateKanougaku":"25415512", "sAzukariKin":"1383069", "sHattyuZyutoukin":"0", "sSonotaKousokukin":"0", "sGenkinHosyoukin":"1383069", "sDaiyouHyoukagaku":"7257880", "sHattyuDaiyouHyoukagaku":"0", "sSasiireHosyoukin":"8640949", "sSinkiTesuryou":"0", "sHibuGyakuhibuKousokuki":"232", "sHibuGyakuhibuSyueki":"0", "sSonotaTateSyokeihi":"0", "sSinyouTadeSyoukeihi":"232", "sSinyouTateHyoukaSon":"8940", "sSinyouTateHyoukaEki":"0", "sTatekabuHyoukaSoneki":"-8940", "sMiukewatasiKessaiSon":"0", "sMiukewatasiKessaiEki":"0", "sSaiteiHituyouHosyoukin":"300000", "sHosyoukin":"244658", "sHattyuHosyoukin":"0", "sGenbikiWatasiHosyoukin":"0", "sMikessaiGenkinHosyoukin":"0", "sHattyuGenkinHosyoukin":"0", "sGenbwGenkinHosyoukin":"0", "sHituyouGenkinHosyoukin":"0", "sHosyoukinRitu":"33", "sHosyoukinIziRitu":"30", "sHosyoukinRituIziYoryoku":"8387119", "sHosyoukinIzirituIziYoryoku":"8409360", "sMikessaiTateDaikin":"741390", "sHattyuTateDaikin":"0", "sGenbikiWatasiTateDaikin":"0", "sItakuHosyoukinRitu":"1164.26", "sTouzituKessaiSon":"0", "sTouzituKessaiEki":"0", "sKessaiTotalToday":"0", "sTouzituKessaiZenHyouka":"0", "sUkewatasiTategyokuSon":"0", "sUkewatasiTategyokuEki":"0", "sKessaiTotalSiteibi":"0"}
```

| sCLMID | 機能ＩＤ | CLMZanKaiSinyouSinkidateSyousai |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sHitukeIndex | 日付インデックス | 要求設定値 |
| sHituke | 指定日（日付） | YYYYMMDD |
| sUkeireHosyoukin | 受入保証金 | -999999999999999～9999999999999999 |
| sHituyouHosyoukin | 必要保証金 | -999999999999999～9999999999999999 |
| sHosyoukinYoryoku | 保証金余力 | -999999999999999～9999999999999999 |
| sHosyoukinTyousyuRitu | 保証金徴収率(%) | 0～9999999999999 |
| sSinyouSinkidateKanougaku | 信用新規建可能額 | -999999999999999～9999999999999999 |
| sAzukariKin | 預り金 | 0～9999999999999999 |
| sHattyuZyutoukin | 発注済み注文充当金 | 0～9999999999999999 |
| sSonotaKousokukin | その他拘束金 | 0～9999999999999999 |
| sGenkinHosyoukin | 現金保証金 | -999999999999999～9999999999999999 |
| sDaiyouHyoukagaku | 代用証券評価額 | 0～9999999999999999 |
| sHattyuDaiyouHyoukagaku | 現物買発注分代用証券評価額 | 0～9999999999999999 |
| sSasiireHosyoukin | 差入保証金 | 0～9999999999999999 |
| sSinkiTesuryou | 新規建手数料 | 0～9999999999999999 |
| sHibuGyakuhibuKousokukin | 日歩・逆日歩・貸株料拘束金 | 0～9999999999999999 |
| sHibuGyakuhibuSyueki | 日歩・逆日歩収益 | 0～9999999999999999 |
| sSonotaTateSyokeihi | その他未収費用 | 0～9999999999999999 |
| sSinyouTadeSyoukeihi | 建株諸経費 | 0～9999999999999999 |
| sSinyouTateHyoukaSon | 建株評価損 | 0～9999999999999999 |
| sSinyouTateHyoukaEki | 建株評価益 | 0～9999999999999999 |
| sTatekabuHyoukaSoneki | 建株評価損益 | -999999999999999～9999999999999999 |
| sMiukewatasiKessaiSon | 未受渡建株決済損 | 0～9999999999999999 |
| sMiukewatasiKessaiEki | 未受渡建株決済益 | 0～9999999999999999 |
| sSaiteiHituyouHosyoukin | 最低必要保証金 | 0～9999999999999999 |
| sHosyoukin | 建株必要保証金 | 0～9999999999999999 |
| sHattyuHosyoukin | 発注分必要保証金 | 0～9999999999999999 |
| sGenbikiWatasiHosyoukin | 現引/現渡必要保証金 | 0～9999999999999999 |
| sMikessaiGenkinHosyoukin | 建株必要保証金（現金） | 0～9999999999999999 |
| sHattyuGenkinHosyoukin | 発注分必要保証金（現金） | 0～9999999999999999 |
| sGenbwGenkinHosyoukin | 現引/現渡必要保証金（現金） | 0～9999999999999999 |
| sHituyouGenkinHosyoukin | 必要保証金（現金） | -999999999999999～9999999999999999 |
| sHosyoukinRitu | 保証金率(%) | 0～9999999999999 |
| sHosyoukinIziRitu | 保証金維持率(%) | 0～9999999999999 |
| sHosyoukinRituIziYoryoku | 保証金率・維持余力 | -999999999999999～9999999999999999 |
| sHosyoukinIzirituIziYoryoku | 保証金維持率・維持余力 | -999999999999999～9999999999999999 |
| sMikessaiTateDaikin | 建株代金 | 0～9999999999999999 |
| sHattyuTateDaikin | 発注分建株代金 | 0～9999999999999999 |
| sGenbikiWatasiTateDaikin | 現引/現渡建株代金 | 0～9999999999999999 |
| sItakuHosyoukinRitu | 委託保証金率(%) | 0～9999999999.99 |
| sTouzituKessaiSon | 本日決済損 | 0～9999999999999999 |
| sTouzituKessaiEki | 本日決済益 | 0～9999999999999999 |
| sKessaiTotalToday | 本日決済損益合計 | 0～9999999999999999 |
| sTouzituKessaiZenHyouka | 本日決済建株の前日価格評価 | 0～9999999999999999 |
| sUkewatasiTategyokuSon | 指定日決済損 | 0～9999999999999999 |
| sUkewatasiTategyokuEki | 指定日決済益 | 0～9999999999999999 |
| sKessaiTotalSiteibi | 指定日決済損益累計 | 0～9999999999999999 |

<a name="CLMZanRealHosyoukinRitu"></a>
### リアル保証金率

#### 要求

```json
{ "sCLMID":"CLMZanRealHosyoukinRitu"}
```

| sCLMID | 機能ＩＤ | CLMZanRealHosyoukinRitu |
| --- | --- | --- |

#### 応答

```json
{ "sCLMID":"CLMZanRealHosyoukinRitu", "sResultCode":"0", "sResultText":"", "sWarningCode":"0", "sWarningText":"", "sSasiireHosyoukin":"8640949", "sHyoukaSonEki":"-9172", "sUkeireHosyoukin":"8631777", "sTateKabuDaikin":"741390", "sItakuHosyoukinRitu":"1164.26", "sOisyouHituyouHosyoukin":"309172", "sOisyouYoryoku":"8331777", "sT0SasiireHosyoukin":"8640949", "sT0HyoukaSonEki":"-9172", "sT0UkeireHosyoukin":"8631777", "sT0TateKabuDaikin":"741390", "sT0ItakuHosyoukinRitu":"1164.26", "sT0OisyouHituyouHosyoukin":"309172", "sT0OisyouYoryoku":"8331777", "sT5SasiireHosyoukin":"8640949", "sT5HyoukaSonEki":"-9172", "sT5UkeireHosyoukin":"8631777", "sT5TateKabuDaikin":"741390", "sT5ItakuHosyoukinRitu":"1164.26", "sT5OisyouHituyouHosyoukin":"309172", "sT5OisyouYoryoku":"8331777"}
```

| sCLMID | 機能ＩＤ | CLMZanRealHosyoukinRitu |
| --- | --- | --- |
| sResultCode | 結果コード | CLMKabuNewOrder.sResultCode 参照 |
| sResultText | 結果テキスト | CLMKabuNewOrder.sResultText 参照 |
| sWarningCode | 警告コード | CLMKabuNewOrder.sWarningCode 参照 |
| sWarningTexts | 警告テキスト | CLMKabuNewOrder.sWarningTexts 参照 |
| sSasiireHosyoukin | 差入保証金 | 0～9999999999999999 |
| sHyoukaSonEki | 評価損益 | 0～9999999999999999 |
| sUkeireHosyoukin | 受入保証金 | 0～9999999999999999 |
| sTateKabuDaikin | 建株代金 | -999999999999999～9999999999999999 |
| sItakuHosyoukinRitu | 委託保証金率(%) | 0～9999999999999 |
| sOisyouHituyouHosyoukin | 追証必要保証金 | 0～9999999999999999 |
| sOisyouYoryoku | 追証余力 | 0～9999999999999999 |
| sT0SasiireHosyoukin | 差入保証金 | 0～9999999999999999 |
| sT0HyoukaSonEki | 評価損益 | 0～9999999999999999 |
| sT0UkeireHosyoukin | 受入保証金 | -999999999999999～9999999999999999 |
| sT0TateKabuDaikin | 建株代金 | 0～9999999999999999 |
| sT0ItakuHosyoukinRitu | 委託保証金率(%) | 0～9999999999999 |
| sT0OisyouHituyouHosyoukin | 追証必要保証金 | 0～9999999999999999 |
| sT0OisyouYoryoku | 追証余力 | 0～9999999999999999 |
| sT5SasiireHosyoukin | 差入保証金 | 0～9999999999999999 |
| sT5HyoukaSonEki | 評価損益 | 0～9999999999999999 |
| sT5UkeireHosyoukin | 受入保証金 | -999999999999999～9999999999999999 |
| sT5TateKabuDaikin | 建株代金 | 0～9999999999999999 |
| sT5ItakuHosyoukinRitu | 委託保証金率(%) | 0～9999999999999 |
| sT5OisyouHituyouHosyoukin | 追証必要保証金 | 0～9999999999999999 |
| sT5OisyouYoryoku | 追証余力 | 0～9999999999999999 |

<a name="ComT4"></a>
## マスタ機能（REQUEST I/F）

<a name="CLMEventDownload"></a>
### マスタ情報ダウンロード

#### 要求

```json
{ "sCLMID":"CLMEventDownload",＊＊＊＊以下は任意指定項目＊＊＊＊ "sTargetCLMID":"CLMIssueMstKabu,CLMDateZyouhou"}
```

| sCLMID | 機能ＩＤ | CLMEventDownload |
| --- | --- | --- |
| sTargetCLMID | 対象機能ＩＤ | 取得したいマスタ情報の機能ＩＤをカンマ区切りで羅列する。未指定「""」時は全マスタ情報。対象機能ＩＤ：・CLMSystemStatus・CLMDateZyouhou・CLMYobine・CLMUnyouStatus・CLMUnyouStatusKabu・CLMUnyouStatusHasei・CLMIssueMstKabu・CLMIssueSizyouMstKabu・CLMIssueSizyouKiseiKabu・CLMIssueMstSak・CLMIssueMstOp・CLMIssueSizyouKiseiHasei・CLMDaiyouKakeme・CLMHosyoukinMst・CLMOrderErrReason・CLMEventDownloadComplete例："CLMIssueMstKabu,CLMDateZyouhou" |
| **⚠️ 【注意】　本要求送信後、各種マスタ情報レコードを配信する。　本要求は配信要求のため応答は返さない。　配信情報．機能ＩＤ CLMEventDownloadComplete までが　初期マスタダウンロードデータで　その後は変更情報が切断するまで配信される。　使用例の１つとして例えば株式銘柄マスタのみ取得したい場合、　sTargetCLMID に "CLMIssueMstKabu,CLMEventDownloadComplete" を指定し　CLMEventDownloadComplete を受信後切断すると株式銘柄マスタが取得できる。　配信項目中、区分値等の定義記載が無い項目値について　値が「」（空文字列）または「０」の場合、値が無い意味である。** |  |  |

#### システムステータス

```json
{ "sCLMID":"CLMSystemStatus", "sSystemStatusKey":"001", "sLoginKyokaKubun":"1", "sSystemStatus":"1", "sCreateTime":"", "sUpdateTime":"", "sUpdateNumber":"", "sDeleteFlag":"", "sDeleteTime":""}
```

| sCLMID | 機能ＩＤ | CLMSystemStatus |
| --- | --- | --- |
| sSystemStatusKey | システム状態ＫＥＹ | 001固定 |
| sLoginKyokaKubun | ログイン許可区分 | 0：不許可1：許可2：不許可(サービス時間外)9：管理者のみ可(テスト中) |
| sSystemStatus | システム状態 | 0：閉局1：開局2：一時停止 |
| sCreateTime | 作成時刻 |  |
| sUpdateTime | 更新時刻 |  |
| sUpdateNumber | 更新通番 |  |
| sDeleteFlag | 削除フラグ |  |
| sDeleteTime | 削除時刻 |  |

#### 日付情報

```json
{ "sCLMID":"CLMDateZyouhou", "sDayKey":"001", "sMaeEigyouDay_1":"20231031", "sMaeEigyouDay_2":"20231030", "sMaeEigyouDay_3":"20231027", "sTheDay":"20231101", "sYokuEigyouDay_1":"20231102", "sYokuEigyouDay_2":"20231106", "sYokuEigyouDay_3":"20231107", "sYokuEigyouDay_4":"20231108", "sYokuEigyouDay_5":"20231109", "sYokuEigyouDay_6":"20231110", "sYokuEigyouDay_7":"20231113", "sYokuEigyouDay_8":"20231114", "sYokuEigyouDay_9":"20231115", "sYokuEigyouDay_10":"20231116", "sKabuUkewatasiDay":"20231106", "sKabuKariUkewatasiDay":"20231107", "sBondUkewatasiDay":"20231106"}
```

| sCLMID | 機能ＩＤ | CLMDateZyouhou |
| --- | --- | --- |
| sDayKey | 日付ＫＥＹ | 001：当日基準002：翌日基準（夕場） |
| sMaeEigyouDay_1 | １営業日前 | YYYYMMDD |
| sMaeEigyouDay_2 | ２営業日前 | YYYYMMDD |
| sMaeEigyouDay_3 | ３営業日前 | YYYYMMDD |
| sTheDay | 当日日付 | YYYYMMDD |
| sYokuEigyouDay_1 | 翌１営業日 | YYYYMMDD |
| sYokuEigyouDay_2 | 翌２営業日 | YYYYMMDD |
| sYokuEigyouDay_3 | 翌３営業日 | YYYYMMDD |
| sYokuEigyouDay_4 | 翌４営業日 | YYYYMMDD |
| sYokuEigyouDay_5 | 翌５営業日 | YYYYMMDD |
| sYokuEigyouDay_6 | 翌６営業日 | YYYYMMDD |
| sYokuEigyouDay_7 | 翌７営業日 | YYYYMMDD |
| sYokuEigyouDay_8 | 翌８営業日 | YYYYMMDD |
| sYokuEigyouDay_9 | 翌９営業日 | YYYYMMDD |
| sYokuEigyouDay_10 | 翌１０営業日 | YYYYMMDD |
| sKabuUkewatasiDay | 株式受渡日 | YYYYMMDD |
| sKabuKariUkewatasiDay | 株式仮決受渡日 | YYYYMMDD |
| sBondUkewatasiDay | 債券受渡日 | YYYYMMDD |

#### 呼値

```json
{ "sCLMID":"CLMYobine", "sYobineTaniNumber":"101", "sTekiyouDay":"20140101", "sKizunPrice_1":"3000.000000", "sKizunPrice_2":"5000.000000", "sKizunPrice_3":"30000.000000", "sKizunPrice_4":"50000.000000", "sKizunPrice_5":"300000.000000", "sKizunPrice_6":"500000.000000", "sKizunPrice_7":"3000000.000000", "sKizunPrice_8":"5000000.000000", "sKizunPrice_9":"30000000.000000", "sKizunPrice_10":"50000000.000000", "sKizunPrice_11":"999999999.000000", "sKizunPrice_12":"0.000000", "sKizunPrice_13":"0.000000", "sKizunPrice_14":"0.000000", "sKizunPrice_15":"0.000000", "sKizunPrice_16":"0.000000", "sKizunPrice_17":"0.000000", "sKizunPrice_18":"0.000000", "sKizunPrice_19":"0.000000", "sKizunPrice_20":"0.000000", "sYobineTanka_1":"1.000000", "sYobineTanka_2":"5.000000", "sYobineTanka_3":"10.000000", "sYobineTanka_4":"50.000000", "sYobineTanka_5":"100.000000", "sYobineTanka_6":"500.000000", "sYobineTanka_7":"1000.000000", "sYobineTanka_8":"5000.000000", "sYobineTanka_9":"10000.000000", "sYobineTanka_10":"50000.000000", "sYobineTanka_11":"100000.000000", "sYobineTanka_12":"0.000000", "sYobineTanka_13":"0.000000", "sYobineTanka_14":"0.000000", "sYobineTanka_15":"0.000000", "sYobineTanka_16":"0.000000", "sYobineTanka_17":"0.000000", "sYobineTanka_18":"0.000000", "sYobineTanka_19":"0.000000", "sYobineTanka_20":"0.000000", "sDecimal_1":"0", "sDecimal_2":"0", "sDecimal_3":"0", "sDecimal_4":"0", "sDecimal_5":"0", "sDecimal_6":"0", "sDecimal_7":"0", "sDecimal_8":"0", "sDecimal_9":"0", "sDecimal_10":"0", "sDecimal_11":"0", "sDecimal_12":"0", "sDecimal_13":"0", "sDecimal_14":"0", "sDecimal_15":"0", "sDecimal_16":"0", "sDecimal_17":"0", "sDecimal_18":"0", "sDecimal_19":"0", "sDecimal_20":"0", "sCreateDate":"", "sUpdateDate":""}
```

| sCLMID | 機能ＩＤ | CLMYobine |
| --- | --- | --- |
| sYobineTaniNumber | 呼値の単位番号 | 101：株式1102：株式2103：株式3201：債券1318：日経225先物319：日経225min先物418：日経225OP |
| sTekiyouDay | 適用日 | YYYYMMDD |
| sKizunPrice_1 - sKizunPrice_20 | 基準値段1～基準値段20 | 9.999999 |
| sYobineTanka_1 - sYobineTanka_20 | 呼値単価1～呼値単価20 | 9.999999 |
| sDecimal_1 - sDecimal_20 | 小数点桁数1～小数点桁数20 | 9 |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |

#### 運用ステータス別状態

```json
{ "sCLMID":"CLMUnyouStatus", "sSystemKouzaKubun":"102", "sUnyouCategory":"01", "sUnyouUnit":"0101", "sEigyouDayC":"0", "sUnyouStatus":"001", "sTaisyouGyoumu":"04", "sGyoumuZyoutai":"001", "sCreateTime":"", "sUpdateTime":"", "sUpdateNumber":"", "sDeleteFlag":"", "sDeleteTime":"", "sEventName":"", "sMeyasuTime":""}
```

| sCLMID | 機能ＩＤ | CLMUnyouStatus |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sUnyouCategory | 運用カテゴリ | 01：株式02：派生03：派生証拠金04：累投05：投信06：IPO07：入金08：出金09：為替証拠金10：有料情報サービス11：マスタ更新12：入金請求更新 |
| sUnyouUnit | 運用単位 | 0101：株式_東証0102：株式_名証0103：株式_端株0201：OSE_日経225_先物0202：OSE_日経225_OP0301：派生証拠金_OSE0401：累投_MMF0402：累投_中国F0500：投信_全体0600：IPO_全体0700：入金_全体0800：出金_全体0900：為替証拠金_全体1000：有料情報サービス_全体1100：マスタ更新_全体1200：入金請求監視_全体 |
| sEigyouDayC | 営業日区分 | 0：営業日1：非営業日2：売買停止日 |
| sUnyouStatus | 運用ステータス | 各業務、市場等により値およびその意味が変化する000（受付停止）～900（オンライン閉局）(例)東証の株式注文における場合'000':注文受付'100':前場受付開始'120':前場立会開始'140':前場立会終了'160':前場約定通知出力終了'200':後場受付開始'220':後場受付開始'240':後場立会終了前'260':後場立会終了'280':後場約定通知出力終了'300':株式閉局'400':値洗い中'500':翌日注文受付開始'600':差分注文繰越中'700':値洗い完了'900':オンライン閉局 |
| sTaisyouGyoumu | 対象業務 | 01：評価単価02：採用値幅03：値洗い04：注文（受付）05：連続注文06：申告07：証券部応答08：派生証拠金振替09：オンライン入金10：入金連絡（銀行振込）11：現金入金（店頭入力）12：現金から為替証拠金13：為替証拠金から現金14：照会15：市場閉局16：投信注文（14：30締め）17：投信注文（15：00締め）18：余力基準19：購入辞退20：市場トリガ_約定出力21：市場トリガ_取引終了22：市場時間帯23：投信注文（14：00締め） |
| sGyoumuZyoutai | 業務別状態 | 「対象業務」に応じた業務別状態①対象業務=01(評価単価)or 02(採用値幅)の時[価格取得区分]0：時価1：マスタ②対象業務=03(値洗い)の時[値洗い処理区分]0：停止1：開始2：終了③対象業務=15(市場閉局)の時[表示区分]0：非表示1：表示④対象業務=①～③以外の時[受付状態区分]000：停止001：当日可002：翌日可 |
| sCreateTime | 作成時刻 |  |
| sUpdateTime | 更新時刻 |  |
| sUpdateNumber | 更新通番 |  |
| sDeleteFlag | 削除フラグ |  |
| sDeleteTime | 削除時刻 |  |
| sEventName | イベント名 | 運用ステータスに対する名称画面表示に使用例:　前場受付開始　前場立会終了 |
| sMeyasuTime | 目安時刻 | 運用ステータスが遷移する目安の時刻 |

#### 運用ステータス（株）

```json
{ "sCLMID":"CLMUnyouStatusKabu", "sSystemKouzaKubun":"102", "sZyouzyouSizyou":"00", "sUnyouCategory":"01", "sUnyouUnit":"0101", "sEigyouDayC":"0", "sUnyouStatus":"001", "sCreateTime":"", "sUpdateTime":"", "sUpdateNumber":"", "sDeleteFlag":"", "sDeleteTime":""}
```

| sCLMID | 機能ＩＤ | CLMUnyouStatusKabu |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sZyouzyouSizyou | 上場市場 | 00：東証 |
| sUnyouCategory | 運用カテゴリ | CLMUnyouStatus 参照 |
| sUnyouUnit | 運用単位 | CLMUnyouStatus 参照 |
| sEigyouDayC | 営業日区分 | CLMUnyouStatus 参照 |
| sUnyouStatus | 運用ステータス | CLMUnyouStatus 参照 |
| sCreateTime | 作成時刻 |  |
| sUpdateTime | 更新時刻 |  |
| sUpdateNumber | 更新通番 |  |
| sDeleteFlag | 削除フラグ |  |
| sDeleteTime | 削除時刻 |  |

#### 運用ステータス（派生）

```json
{ "sCLMID":"CLMUnyouStatusHasei", "sSystemKouzaKubun":"102", "sZyouzyouSizyou":"01", "sGensisanCode":"101", "sSyouhinType":"01", "sUnyouCategory":"01", "sUnyouUnit":"0101", "sEigyouDayC":"0", "sUnyouStatus":"001", "sCreateTime":"", "sUpdateTime":"", "sUpdateNumber":"", "sDeleteFlag":"", "sDeleteTime":""}
```

| sCLMID | 機能ＩＤ | CLMUnyouStatusHasei |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sZyouzyouSizyou | 上場市場 | 01：東証 |
| sGensisanCode | 原資産コード | CLMIssueMstSak 参照 |
| sSyouhinType | 商品種別 | 03：先物04：ＯＰ |
| sUnyouCategory | 運用カテゴリ | CLMUnyouStatus 参照 |
| sUnyouUnit | 運用単位 | CLMUnyouStatus 参照 |
| sEigyouDayC | 営業日区分 | CLMUnyouStatus 参照 |
| sUnyouStatus | 運用ステータス | CLMUnyouStatus 参照 |
| sCreateTime | 作成時刻 |  |
| sUpdateTime | 更新時刻 |  |
| sUpdateNumber | 更新通番 |  |
| sDeleteFlag | 削除フラグ |  |
| sDeleteTime | 削除時刻 |  |

#### 株式銘柄マスタ

```json
{ "sCLMID":"CLMIssueMstKabu", "sIssueCode":"1301", "sIssueName":"極 洋", "sIssueNameRyaku":"極洋", "sIssueNameKana":"キヨクヨウ", "sIssueNameEizi":"KYOKUYO", "sTokuteiF":"1", "sHikazeiC":"1", "sZyouzyouHakkouKabusu":"10928283", "sKenriotiFlag":"0", "sKenritukiSaisyuDay":"20160927", "sZyouzyouNyusatuC":"", "sNyusatuKaizyoDay":"00000000", "sNyusatuDay":"00000000", "sBaibaiTani":"100", "sBaibaiTaniYoku":"100", "sBaibaiTeisiC":"", "sHakkouKaisiDay":"00000000", "sHakkouSaisyuDay":"00000000", "sKessanC":"01", "sKessanDay":"20170328", "sZyouzyouOutouDay":"00000000", "sNiruiKizituC":"0", "sOogutiKabusu":"0", "sOogutiKingaku":"0", "sBadenpyouOutputYNC":"2", "sHosyoukinDaiyouKakeme":"80.000000", "sDaiyouHyoukaTanka":"3840.000000", "sKikoSankaC":"1", "sKarikessaiC":"", "sYusenSizyou":"00", "sMukigenC":"", "sGyousyuCode":"0050", "sGyousyuName":"水産・農林業", "sSorC":"", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":""}
```

| sCLMID | 機能ＩＤ | CLMIssueMstKabu |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 例:6501 |
| sIssueName | 銘柄名称 | 例:極 洋 |
| sIssueNameRyaku | 銘柄名略称 | 例:極洋 |
| sIssueNameKana | 銘柄名（カナ） | 例:キヨクヨウ |
| sIssueNameEizi | 銘柄名（英語表記） | 例:KYOKUYO |
| sTokuteiF | 特定口座対象Ｃ | 1：特定参加0：不参加 |
| sHikazeiC | 非課税対象Ｃ |  |
| sZyouzyouHakkouKabusu | 上場発行株数 | 9 |
| sKenriotiFlag | 権利落ちフラグ |  |
| sKenritukiSaisyuDay | 権利付最終日 |  |
| sZyouzyouNyusatuC | 上場・入札Ｃ |  |
| sNyusatuKaizyoDay | 入札解除日 |  |
| sNyusatuDay | 入札日 |  |
| sBaibaiTani | 売買単位 | 9 |
| sBaibaiTaniYoku | 売買単位(翌営業日) | 9 |
| sBaibaiTeisiC | 売買停止Ｃ | " ":通常（無）0:解除9:停止中 |
| sHakkouKaisiDay | 発行開始日 |  |
| sHakkouSaisyuDay | 発行最終日 |  |
| sKessanC | 決算Ｃ |  |
| sKessanDay | 決算日 |  |
| sZyouzyouOutouDay | 上場応答日 |  |
| sNiruiKizituC | 二類期日Ｃ |  |
| sOogutiKabusu | 大口株数 |  |
| sOogutiKingaku | 大口金額 |  |
| sBadenpyouOutputYNC | 場伝票出力有無Ｃ |  |
| sHosyoukinDaiyouKakeme | 保証金代用掛目 | 9.999999 |
| sDaiyouHyoukaTanka | 代用証券評価単価 | 9.999999 |
| sKikoSankaC | 機構参加Ｃ |  |
| sKarikessaiC | 仮決済Ｃ |  |
| sYusenSizyou | 優先市場 | 00：東証 |
| sMukigenC | 無期限対象Ｃ |  |
| sGyousyuCode | 業種コード | 0050:水産・農林業1050:鉱業2050:建設業3050:食料品3100:繊維製品3150:パルプ・紙3200:化学3250:医薬品3300:石油石炭製品3350:ゴム製品3400:ｶﾞﾗｽ土石製品3450:鉄鋼3500:非鉄金属3550:金属製品3600:機械3650:電気機器3700:輸送用機器3750:精密機器3800:その他製品4050:電気・ガス業5050:陸運業5100:海運業5150:空運業5200:倉庫運輸関連5250:情報・通信業6050:卸売業6100:小売業7050:銀行業7100:証券商品先物7150:保険業7200:その他金融業8050:不動産業9050:サービス業9999:その他 |
| sGyousyuName | 業種コード名 | sGyousyuCode 参照 |
| sSorC | ＳＯＲ対象銘柄Ｃ |  |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |

#### 株式銘柄市場マスタ

```json
{ "sCLMID":"CLMIssueSizyouMstKabu", "sIssueCode":"1301", "sZyouzyouSizyou":"00", "sSystemC":"", "sNehabaMin":"3140.000000", "sNehabaMax":"4540.000000", "sIssueKubunC":" ", "sNehabaSizyouC":"", "sSinyouC":"1", "sSinkiZyouzyouDay":"00000000", "sNehabaKigenDay":"", "sNehabaKiseiC":"", "sNehabaKiseiTi":"", "sNehabaCheckKahiC":"", "sIssueBubetuC":"1", "sZenzituOwarine":"3840.000000", "sNehabaSansyutuSizyouC":"", "sIssueKisei1C":"", "sIssueKisei2C":"", "sZyouzyouKubun":"01", "sZyouzyouHaisiDay":"00000000", "sSizyoubetuBaibaiTani":"", "sSizyoubetuBaibaiTaniYoku":"", "sYobineTaniNumber":"101", "sYobineTaniNumberYoku":"101", "sZyouhouSource":"", "sZyouhouCode":"", "sKouboPrice":"", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":""}
```

| sCLMID | 機能ＩＤ | CLMIssueSizyouMstKabu |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 例:6501 |
| sZyouzyouSizyou | 上場市場 | 00：東証 |
| sSystemC | システムＣ |  |
| sNehabaMin | 値幅下限 | 9.999999 |
| sNehabaMax | 値幅上限 | 9.999999 |
| sIssueKubunC | 銘柄区分Ｃ | "":通常（無）01:新興市場03:ETN(新興市場)04:ETN05:プロ向け市場 |
| sNehabaSizyouC | 値幅市場Ｃ |  |
| sSinyouC | 信用Ｃ | 1:貸借銘柄2:信用制度銘柄3:一般信用銘柄 |
| sSinkiZyouzyouDay | 新規上場日 | YYYYMMDD,00000000 |
| sNehabaKigenDay | 値幅期限日 |  |
| sNehabaKiseiC | 値幅規制Ｃ |  |
| sNehabaKiseiTi | 値幅規制値 |  |
| sNehabaCheckKahiC | 値幅チェック可否Ｃ |  |
| sIssueBubetuC | 銘柄部別Ｃ | 1:１部2:２部3:３部(店頭)4:４部(外国) |
| sZenzituOwarine | 前日終値 | 9.999999 |
| sNehabaSansyutuSizyouC | 値幅算出市場Ｃ |  |
| sIssueKisei1C | 銘柄規制１Ｃ |  |
| sIssueKisei2C | 銘柄規制２Ｃ |  |
| sZyouzyouKubun | 上場区分 | 00：下記以外01：東証時は「プライム」、名証時は「プレミア」、他は「一部」02：東証時は「スタンダード」、名証時は「メイン」、他は「二部」03：東証時は「プライム（外国銘柄）」、名証時は「プレミア（外国銘柄）」、他は「一部（外国銘柄）」04：東証時は「スタンダード（外国銘柄）」、名証時は「メイン（外国銘柄）」、他は「二部（外国銘柄）」07：欠番（現在QNFSデータなし)09：グロース11：グロース（外国銘柄）12：アンビシャス市場13：Q-Board（内国銘柄）14：ネクスト（内国銘柄）15：ネクスト（外国銘柄）16：（日本銀行）17：欠番（現在QNFSデータなし)18：欠番（現在QNFSデータなし)19：本則市場(外国銘柄)20：Q-Board（外国銘柄）21：TPM(国内銘柄)22：TPMF(外国銘柄) |
| sZyouzyouHaisiDay | 上場廃止日 | YYYYMMDD,00000000 |
| sSizyoubetuBaibaiTani | 売買単位 |  |
| sSizyoubetuBaibaiTaniYoku | 売買単位(翌営業日) |  |
| sYobineTaniNumber | 呼値の単位番号 | CLMYobine.sYobineTaniNumber 参照 |
| sYobineTaniNumberYoku | 呼値の単位番号(翌営業日) | CLMYobine.sYobineTaniNumber 参照 |
| sZyouhouSource | 情報系ソース |  |
| sZyouhouCode | 情報系コード |  |
| sKouboPrice | 公募価格 |  |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |

#### 株式銘柄別・市場別規制

```json
{ "sCLMID":"CLMIssueSizyouKiseiKabu", "sSystemKouzaKubun":"102", "sIssueCode":"6501", "sZyouzyouSizyou":"00", "sTeisiKubun":"1", "sGenbutuKaituke":"1", "sGenbutuKaitukeYoku":"1", "sGenbutuUrituke":"1", "sGenbutuUritukeYoku":"1", "sSeidoSinyouSinkiKaitate":"1", "sSeidoSinyouSinkiKaitateYoku":"1", "sSeidoSinyouSinkiUritate":"1", "sSeidoSinyouSinkiUritateYoku":"1", "sSeidoSinyouKaiHensai":"1", "sSeidoSinyouKaiHensaiYoku":"1", "sSeidoSinyouUriHensai":"1", "sSeidoSinyouUriHensaiYoku":"1", "sSeidoSinyouGenbiki":"1", "sSeidoSinyouGenbikiYoku":"1", "sSeidoSinyouGenwatasi":"1", "sSeidoSinyouGenwatasiYoku":"1", "sIppanSinyouSinkiKaitate":"1", "sIppanSinyouSinkiKaitateYoku":"1", "sIppanSinyouSinkiUritate":"1", "sIppanSinyouSinkiUritateYoku":"1", "sIppanSinyouKaiHensai":"1", "sIppanSinyouKaiHensaiYoku":"1", "sIppanSinyouUriHensai":"1", "sIppanSinyouUriHensaiYoku":"1", "sIppanSinyouGenbiki":"1", "sIppanSinyouGenbikiYoku":"1", "sIppanSinyouGenwatasi":"1", "sIppanSinyouGenwatasiYoku":"1", "sZizenCyouseiC":"1", "sZizenCyouseiCYoku":"1", "sSokuzituNyukinC":"1", "sSokuzituNyukinCYoku":"1", "sSokuzituNyukinKiseiDate":"20231101123000", "sSinyouSyutyuKubun":"1", "sSinyouSyutyuKubunYoku":"1", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":""}
```

| sCLMID | 機能ＩＤ | CLMIssueSizyouKiseiKabu |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sIssueCode | 銘柄コード | 例:6501 |
| sZyouzyouSizyou | 上場市場 | 00：東証 |
| sTeisiKubun | 停止区分 | 0:通常（無）1:取引禁止2:成行禁止3:端株禁止 |
| sGenbutuKaituke | 現物/買付 | sTeisiKubun 参照 |
| sGenbutuKaitukeYoku | 現物/買付（翌営業日） | sTeisiKubun 参照 |
| sGenbutuUrituke | 現物/売付 | sTeisiKubun 参照 |
| sGenbutuUritukeYoku | 現物/売付（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouSinkiKaitate | 制度信用/買建 | sTeisiKubun 参照 |
| sSeidoSinyouSinkiKaitateYoku | 制度信用/買建（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouSinkiUritate | 制度信用/売建 | sTeisiKubun 参照 |
| sSeidoSinyouSinkiUritateYoku | 制度信用/売建（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouKaiHensai | 制度信用/買返済 | sTeisiKubun 参照 |
| sSeidoSinyouKaiHensaiYoku | 制度信用/買返済（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouUriHensai | 制度信用/売返済 | sTeisiKubun 参照 |
| sSeidoSinyouUriHensaiYoku | 制度信用/売返済（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouGenbiki | 制度信用/現引 | sTeisiKubun 参照 |
| sSeidoSinyouGenbikiYoku | 制度信用/現引（翌営業日） | sTeisiKubun 参照 |
| sSeidoSinyouGenwatasi | 制度信用/現渡 | sTeisiKubun 参照 |
| sSeidoSinyouGenwatasiYoku | 制度信用/現渡（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouSinkiKaitate | 一般信用/買建 | sTeisiKubun 参照 |
| sIppanSinyouSinkiKaitateYoku | 一般信用/買建（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouSinkiUritate | 一般信用/売建 | sTeisiKubun 参照 |
| sIppanSinyouSinkiUritateYoku | 一般信用/売建（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouKaiHensai | 一般信用/買返済 | sTeisiKubun 参照 |
| sIppanSinyouKaiHensaiYoku | 一般信用/買返済（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouUriHensai | 一般信用/売返済 | sTeisiKubun 参照 |
| sIppanSinyouUriHensaiYoku | 一般信用/売返済（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouGenbiki | 一般信用/現引 | sTeisiKubun 参照 |
| sIppanSinyouGenbikiYoku | 一般信用/現引（翌営業日） | sTeisiKubun 参照 |
| sIppanSinyouGenwatasi | 一般信用/現渡 | sTeisiKubun 参照 |
| sIppanSinyouGenwatasiYoku | 一般信用/現渡（翌営業日） | sTeisiKubun 参照 |
| sZizenCyouseiC | 事前調整有無 | 0：なし（無効）1：あり（有効） |
| sZizenCyouseiCYoku | 事前調整有無（翌営業日） | sZizenCyouseiC 参照 |
| sSokuzituNyukinC | 即日入金規制有無 | sZizenCyouseiC 参照 |
| sSokuzituNyukinCYoku | 即日入金規制有無（翌営業日） | sZizenCyouseiC 参照 |
| sSokuzituNyukinKiseiDate | 即日入金規制日時 | YYYYMMDDHHMMSS,00000000000000 |
| sSinyouSyutyuKubun | 信用一極集中区分 | 0：なし1：あり2：日々公表銘柄 |
| sSinyouSyutyuKubunYoku | 信用一極集中区分（翌営業日） | sSinyouSyutyuKubun 参照 |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |

#### 先物銘柄マスタ

```json
{ "sCLMID":"CLMIssueMstSak", "sIssueCode":"160060018", "sIssueName":"日経２２５ 25年06月", "sIssueNameEizi":"NS225 2506", "sSakOpSyouhin":"18", "sGensisanKubun":"04", "sGensisanCode":"101", "sGengetu":"202506", "sZyouzyouSizyou":"01", "sTorihikiStartDay":"20180717", "sLastBaibaiDay":"20250612", "sTaniSuryou":"1", "sYobineTaniNumber":"318", "sZyouhouSource":"", "sZyouhouCode":"", "sNehabaMin":"10000.000000", "sNehabaMax":"30000.000000", "sIssueKisei1C":"", "sBaibaiTeisiC":" ", "sZenzituOwarine":"31070.000000", "sBaDenpyouOutputUmuC":"", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":""}
```

| sCLMID | 機能ＩＤ | CLMIssueMstSak |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 例:160060018 |
| sIssueName | 銘柄名 | 例:日経２２５ 25年06月 |
| sIssueNameEizi | 銘柄名（英語表記） | 例:NS225 2506 |
| sSakOpSyouhin | 先物ＯＰ商品 | 01：長期国債02：超長期国債04：中期国債05：TOPIX06：TOPIXミニ07：ミニ長期国債08：TOPIX配当指数09：S&P/TOPIX15010：株先5011：東証ｸﾞﾛｰｽ250先物15：日経平均VI16：日経30017：日経平均・配当指数18：日経22519：日経225ミニ22:ＪＰＸ日経４００先物25：オプション2530：東証電気機器株価指数31：東証輸送用機器株価指数32：東証銀行業株価指数63：TOPIXcore3064：TOPIXcore30配当69：東証REIT指数70：ハイテク指数71：フィナンシャル指数72：コンシューマー指数73：NYダウ74：CNX Nifty指数75：MSCI Japan指数76：RNプライム指数 |
| sGensisanKubun | 原資産区分 | 03：国債04：指数 |
| sGensisanCode | 原資産コード | 601：長期国債602：超長期国債604：中期国債151：TOPIX178：TOPIX配当指数112：日経平均配当指数171：TOPIXCore30179：Core30配当指数155：東証REIT指数101：日経225140：RNプライム指数144：大証NYダウ145：日経平均VI146：CNX Nifty指数 |
| sGengetu | <限月/td> | YYYYMM |
| sZyouzyouSizyou | 上場市場 | 01:東証 |
| sTorihikiStartDay | 取引開始日 | YYYYMMDD |
| sLastBaibaiDay | 最終売買日 | YYYYMMDD |
| sTaniSuryou | 単位数量 | 9 |
| sYobineTaniNumber | 呼値の単位番号 | CLMYobine.sYobineTaniNumber 参照 |
| sZyouhouSource | 情報系ソース |  |
| sZyouhouCode | 情報系コード |  |
| sNehabaMin | 値幅下限 | 9.999999 |
| sNehabaMax | 値幅上限 | 9.999999 |
| sIssueKisei1C | 銘柄規制１Ｃ |  |
| sBaibaiTeisiC | 売買停止Ｃ | CLMIssueMstKabu.sBaibaiTeisiC 参照 |
| sZenzituOwarine | 前日終値 | 9.999999 |
| sBaDenpyouOutputUmuC | 場伝票出力有無Ｃ |  |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |

#### オプション銘柄マスタ

```json
{ "sCLMID":"CLMIssueMstOp", "sIssueCode":"130030005", "sIssueName":"ＴＯＰＩＸ 2025/03 P- 2000", "sIssueNameEizi":"TPX 2503P2000", "sSakOpSyouhin":"05", "sGensisanKubun":" ", "sGensisanCode":" ", "sGengetu":"202503", "sZyouzyouSizyou":"01", "sKousiPrice":"2000.000000", "sPutCall":"5", "sTorihikiStartDay":"20230908", "sLastBaibaiDay":"20250313", "sKenrikousiLastDay":"00000000", "sTaniSuryou":"1", "sYobineTaniNumber":"405", "sZyouhouSource":"", "sZyouhouCode":"", "sNehabaMin":"0.100000", "sNehabaMax":"328.500000", "sIssueKisei1C":"", "sZenzituOwarine":"77.500000", "sZenzituRironPrice":"", "sBaDenpyouOutputUmuC":"", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":"", "sATMFlag":""}
```

| sCLMID | 機能ＩＤ | CLMIssueMstOp |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 例:130030005 |
| sIssueName | 銘柄名 | ＴＯＰＩＸ 2025/03 P- 2000 |
| sIssueNameEizi | 銘柄名（英語表記） | 例:TPX 2503P2000 |
| sSakOpSyouhin | 先物ＯＰ商品 | CLMIssueMstSak.sSakOpSyouhin 参照 |
| sGensisanKubun | 原資産区分 | CLMIssueMstSak.sGensisanKubun 参照 |
| sGensisanCode | 原資産コード | CLMIssueMstSak.sGensisanCode 参照 |
| sGengetu | <限月/td> | YYYYMM |
| sZyouzyouSizyou | 上場市場 | 01:東証 |
| sKousiPrice | 行使価格 | 9.999999 |
| sPutCall | プット・コール | 5：プット7：コール |
| sTorihikiStartDay | 取引開始日 | YYYYMMDD |
| sLastBaibaiDay | 最終売買日 | YYYYMMDD |
| sKenrikousiLastDay | 権利行使最終日 | YYYYMMDD,00000000 |
| sTaniSuryou | 単位数量 | 9 |
| sYobineTaniNumber | 呼値の単位番号 | CLMYobine.sYobineTaniNumber 参照 |
| sZyouhouSource | 情報系ソース |  |
| sZyouhouCode | 情報系コード |  |
| sNehabaMin | 値幅下限 | 9.999999 |
| sNehabaMax | 値幅上限 | 9.999999 |
| sIssueKisei1C | 銘柄規制１Ｃ |  |
| sZenzituOwarine | 前日終値 | 9.999999 |
| sZenzituRironPrice | 前日理論価格 |  |
| sBaDenpyouOutputUmuC | 場伝票出力有無Ｃ |  |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |
| sATMFlag | アットザマネーフラグ |  |

#### 派生銘柄別・市場別規制

```json
{ "sCLMID":"CLMIssueSizyouKiseiHasei", "sSystemKouzaKubun":"102", "sIssueCode":"160060018", "sZyouzyouSizyou":"01", "sTeisiKubun":"1", "sKaitate":"1", "sKaitateYoku":"1", "sUritate":"1", "sUritateYoku":"1", "sKaiHensai":"1", "sKaiHensaiYoku":"1", "sUriHensai":"1", "sUriHensaiYoku":"1", "sCreateDate":"", "sUpdateDate":"", "sUpdateNumber":""}
```

| sCLMID | 機能ＩＤ | CLMIssueSizyouKiseiHasei |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sIssueCode | 銘柄コード | 例:160060018 |
| sZyouzyouSizyou | 上場市場 | 01:東証 |
| sTeisiKubun | 停止区分 | 0：通常（無）1：取引禁止2：成行禁止3：端株禁止 |
| sKaitate | 買建 | sTeisiKubun 参照 |
| sKaitateYoku | 買建（翌営業日） | sTeisiKubun 参照 |
| sUritate | 売建 | sTeisiKubun 参照 |
| sUritateYoku | 売建（翌営業日） | sTeisiKubun 参照 |
| sKaiHensai | 買返済 | sTeisiKubun 参照 |
| sKaiHensaiYoku | 買返済（翌営業日） | sTeisiKubun 参照 |
| sUriHensai | 売返済 | sTeisiKubun 参照 |
| sUriHensaiYoku | 売返済（翌営業日） | sTeisiKubun 参照 |
| sCreateDate | 作成日時 |  |
| sUpdateDate | 更新日時 |  |
| sUpdateNumber | 更新通番 |  |

#### 代用掛目

```json
{ "sCLMID":"CLMDaiyouKakeme", "sSystemKouzaKubun":"102", "sIssueCode":"1352", "sTekiyouDay":"20220422", "sHosyokinDaiyoKakeme":"0.00", "sDeleteDay":"", "sCreateDate":"", "sUpdateNumber":"", "sUpdateDate":""}
```

| sCLMID | 機能ＩＤ | CLMDaiyouKakeme |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sIssueCode | 銘柄コード | 例:6501 |
| sTekiyouDay | 適用日 | YYYYMMDD |
| sHosyokinDaiyoKakeme | 保証金代用掛目 | 9.99999 |
| sDeleteDay | 削除日 |  |
| sCreateDate | 作成日時 |  |
| sUpdateNumber | 更新通番 |  |
| sUpdateDate | 更新日時 |  |

#### 保証金マスタ

```json
{ "sCLMID":"CLMHosyoukinMst", "sSystemKouzaKubun":"102", "sIssueCode":"1356", "sZyouzyouSizyou":"00", "sHenkouDay":"20230110", "sDaiyoHosyokinRitu":"60.000000", "sGenkinHosyokinRitu":"0.000000", "sCreateDate":"", "sUpdateNumber":"", "sUpdateDate":""}
```

| sCLMID | 機能ＩＤ | CLMHosyoukinMst |
| --- | --- | --- |
| sSystemKouzaKubun | システム口座区分 | 102：ｅ支店 |
| sIssueCode | 銘柄コード | 例:6501 |
| sZyouzyouSizyou | 上場市場 | 00：東証 |
| sHenkouDay | 変更日 | YYYYMMDD |
| sDaiyoHosyokinRitu | 代用保証金率(%) | 9.999999 |
| sGenkinHosyokinRitu | 現金保証金率(%) | 9.999999 |
| sCreateDate | 作成日時 |  |
| sUpdateNumber | 更新通番 |  |
| sUpdateDate | 更新日時 |  |

#### 取引所エラー等理由コード

```json
{ "sCLMID":"CLMOrderErrReason", "sErrReasonCode":"-110007", "sErrReasonText":"銘柄が存在しない"}
```

| sCLMID | 機能ＩＤ | CLMOrderErrReason |
| --- | --- | --- |
| sErrReasonCode | 取引所エラー等理由コード | 取引所エラー等理由コード |
| sErrReasonText | 取引所エラー等理由テキスト | 取引所エラー等理由テキスト |

#### 初期ダウンロード終了通知

```json
{ "sCLMID":"CLMEventDownloadComplete"}
```

| sCLMID | 機能ＩＤ | CLMEventDownloadComplete |
| --- | --- | --- |

<a name="CLMMfdsGetMasterData"></a>
### マスタ情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetMasterData", "sTargetCLMID":"CLMIssueMstKabu,CLMOrderErrReason", "sTargetColumn":"sIssueCode,sIssueName,sErrReasonCode,sErrReasonText"}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMasterData |
| --- | --- | --- |
| sTargetCLMID | 対象機能ＩＤ | **⚠️ 取得したいマスタ情報の機能ＩＤをカンマ区切りで羅列する。未指定「""」時は全マスタ情報。対象機能ＩＤ：・CLMIssueMstKabu・CLMIssueSizyouMstKabu・CLMIssueMstSak・CLMIssueMstOp・CLMIssueMstOther【注意１】参照・CLMIssueMstIndex【注意２】参照・CLMIssueMstFx【注意２】参照・CLMOrderErrReason・CLMDateZyouhou例："CLMIssueMstKabu,CLMOrderErrReason"** |
| sTargetColumn | 対象項目 | 各マスタ情報で取得したい項目をカンマ区切りで羅列する。未指定「""」時は全項目。例："sIssueCode,sIssueName" |
| **⚠️ 【注意】　各機能ＩＤ毎項目説明はCLMEventDownloadの２．以降を参照。　応答項目中、区分値等の定義記載が無い項目値について　値が「」（空文字列）または「０」の場合、値が無い意味である。【注意１】　マスタ情報ダウンロードには無い株価ボード、ｅ支店・ＡＰＩ独自で取り扱う　時価情報配信対象の銘柄コード、銘柄名称（それ以外の項目は無い）を取得可能。【注意２】　CLMIssueMstOther では指数＋為替（の両方）が取得できますが、　指数と為替を個別に取得できるよう新たに追加。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetMasterData", "CLMIssueMstKabu": [  {   "sIssueCode":"oxox",   "sIssueName":"oxox",  },   .   .   . ], "CLMOrderErrReason": [  {   "sErrReasonCode":"oxox",   "sErrReasonText":"oxox",  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMasterData |
| --- | --- | --- |
| CLMIssueMstKabu | 対象機能ＩＤ | 該当情報を配列で返す |
| sIssueCode | 対象項目 | 値 |
| sIssueName | 対象項目 | 値 |

<a name="CLMMfdsGetNewsHead"></a>
### ニュースヘッダー問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetNewsHead",＊＊＊＊以下は任意指定項目、指定項目をＡＮＤ条件で検索＊＊＊＊ "p_CG":"", "p_IS":"", "p_DT_FROM":"", "p_DT_TO":"", "p_REC_OFST":"", "p_REC_LIMT":""}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetNewsHead |
| --- | --- | --- |
| p_CG | カテゴリコード | 対象カテゴリコードを１つ指定 |
| p_IS | カテゴリコード | 対象銘柄コードを１つ指定する |
| p_DT_FROM | 日付（From) | ニュース日付（YYYYMMDD）範囲指定（from）N≧fromで検索 |
| p_DT_TO | 日付（To） | ニュース日付（YYYYMMDD）範囲指定（to）N≦toで検索 |
| p_REC_OFST | レコード取得位置 | レコード取得位置（デフォルト＝０、直近先頭の意味）指定条件検索後の位置 |
| p_REC_LIMT | レコード取得件数最大 | レコード取得件数最大（デフォルト＝１００）指定条件検索後の件数（最大１００） |
| **⚠️ 【注意】　機能ＩＤ以外は任意指定項目で指定項目をＡＮＤ条件で検索します。　ニュースＩＤの降（新しいデータ）順に検索します。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetNewsHead", "p_REC_MAX":"26359", "aCLMMfdsNewsHead": [  {   "p_ID":"20230512153000_OBM9789",   "p_DT":"20230512",   "p_TM":"1530",   "p_CGL":"120",   "p_GNL":"62104",   "p_ISL":"4838",   "p_HDL":"JTNDVERuZXQlM0VB...."  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetNewsHead |
| --- | --- | --- |
| p_REC_MAX | レコード件数 | 取得（検索条件に合致した全）レコード数下記配列の件数ではない |
| aCLMMfdsNewsHead | 取得リスト | 以下項目を配列で応答 |
| p_ID | ニュースＩＤ | 情報（レコード）識別用ユニーク値 |
| p_DT | ニュース日付 | **⚠️ YYYYMMDD【注意１】参照** |
| p_TM | ニュース時刻 | **⚠️ HHMMSS【注意１】参照** |
| p_CGL | ニュースカテゴリリスト | **⚠️ 複数設定時は「|」区切り【注意２】参照** |
| p_GNL | ニュースジャンルリスト | **⚠️ 複数設定時は「|」区切り【注意２】参照** |
| p_ISL | ニュース関連銘柄コードリスト | 複数設定時は「|」区切り |
| p_HDL | ニュースヘッドライン（タイトル） | ShiftJIS 日本語コード文字列を BASE64 変換し設定取得側で各デコード後利用する |
| **⚠️ 【注意】　取得レコードがあったら aCLMMfdsNewsHead に該当情報を設定します。【注意１】　ニュース関連システムの仕様でニュースＩＤ（処理順に採番される仕様）の降順にソートしたリストを応答する。　そのため、データとしてニュース日付、ニュース時刻を返すが、その順序はニュース関連システムの仕様で保証されない。【注意２】　カテゴリ及び、ジャンルについては　立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、EVENT I/F 利用方法、データ仕様、「３．（５）NS」参照。** |  |  |

<a name="CLMMfdsGetNewsBody"></a>
### ニュースボディー問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetNewsBody", "p_ID":"20230315121900_NYU8165"}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetNewsBody |
| --- | --- | --- |
| p_ID | ニュースＩＤ | 情報（レコード）識別用ユニーク値 |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetNewsBody", "p_ID":"20230315121900_NYU8165" "aCLMMfdsNewsBody": [  {   "p_ID":"20230315121900_NYU8165",   "p_DT":"20230315",   "p_TM":"121900",   "p_CGL":"110",   "p_GNL":"60010",   "p_ISL":"8070|3657|6822...",   "p_HDL":"JTNDVERuZXQlM0VB....",   "p_TX":"JTNDVERuZXQlM0VB...."  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetNewsBody |
| --- | --- | --- |
| p_ID | ニュースＩＤ | 要求設定値 |
| aCLMMfdsNewsBody | 取得リスト | 以下項目を配列で応答 |
| p_ID | ニュースＩＤ | 情報（レコード）識別用ユニーク値 |
| p_DT | ニュース日付 | **⚠️ YYYYMMDD【注意１】参照** |
| p_TM | ニュース時刻 | **⚠️ HHMMSS【注意１】参照** |
| p_CGL | ニュースカテゴリリスト | **⚠️ 複数設定時は「|」区切り【注意２】参照** |
| p_GNL | ニュースジャンルリスト | **⚠️ 複数設定時は「|」区切り【注意２】参照** |
| p_ISL | ニュース関連銘柄コードリスト | 複数設定時は「|」区切り |
| p_HDL | ニュースヘッドライン（タイトル） | ShiftJIS 日本語コード文字列を BASE64 変換し設定取得側で各デコード後利用する |
| p_TX | ニュースボディー（本文） | ShiftJIS 日本語コード文字列を BASE64 変換し設定取得側で各デコード後利用する |
| **⚠️ 【注意】　取得レコードがあったら aCLMMfdsNewsBody に該当情報を設定します。【注意１】　ニュース関連システムの仕様でニュースＩＤ（処理順に採番される仕様）の降順にソートしたリストを応答する。　そのため、データとしてニュース日付、ニュース時刻を返すが、その順序はニュース関連システムの仕様で保証されない。【注意２】　カテゴリ及び、ジャンルについては　立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、EVENT I/F 利用方法、データ仕様、「３．（５）NS」参照。** |  |  |

<a name="CLMMfdsGetIssueDetail"></a>
### 銘柄詳細情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetIssueDetail", "sTargetIssueCode":"6501,7203",}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetIssueDetail |
| --- | --- | --- |
| sTargetIssueCode | 対象銘柄コード | **⚠️ 取得したい銘柄コードをカンマ区切りで羅列【注意１】参照** |
| **⚠️ 【注意】　応答項目中、値が「」（空文字列）は値が無い意味である。【注意１】　最大１２０銘柄まで指定可能、１２０超過分は無視。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetIssueDetail", "aCLMMfdsIssueDetail": [  {   "sIssueCode":"6501",   "pBPSB":"6155.38",   "pCLOE":"2025/03/28",   "pEPSF":"131.06",   "pEXRD":"2024/06/27",   "pIDVE":"2025/09/29",   "pROEL":"10.52",   "pRPER":"30.1",   "pSPBR":"4.99",   "pSPRO":"1.54",   "pSYIE":"1.03",   "pYHPD":"2024/12/05",   "pYHPR":"4145",   "pYLPD":"2024/08/05",   "pYLPR":"2584.0"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetIssueDetail |
| --- | --- | --- |
| aCLMMfdsIssueDetail | 取得リスト | 以下項目を配列で応答 |
| sIssueCode | 対象銘柄コード | 要求設定値 |
| pBPSB | BPS（実績）／一株資産(実績最新・連結) |  |
| pCLOE | 落日（本決算）／配当権利落日 | YYYY/MM/DD |
| pEPSF | EPS（予想）／一株利益(予想・通期連結) |  |
| pEXRD | 最終落日（決算期以外） | YYYY/MM/DD |
| pIDVE | 落日（中間決算）／中間配当権利落日 | YYYY/MM/DD |
| pROEL | ROE（予想） |  |
| pRPER | PER（予想）／連結優先　PER |  |
| pSPBR | PBR（実績）／PBR(単純) |  |
| pSPRO | 株式益回り（予想）／益回り(単純) |  |
| pSYIE | 配当利回り（予想）／利回り(単純) |  |
| pYHPD | 年初来高値：更新日 | YYYY/MM/DD |
| pYHPR | 年初来高値 |  |
| pYLPD | 年初来安値：更新日 | YYYY/MM/DD |
| pYLPR | 年初来安値 |  |

<a name="CLMMfdsGetSyoukinZan"></a>
### 証金残情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetSyoukinZan", "sTargetIssueCode":"6501,7203",}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetSyoukinZan |
| --- | --- | --- |
| sTargetIssueCode | 対象銘柄コード | **⚠️ 取得したい銘柄コードをカンマ区切りで羅列【注意１】参照** |
| **⚠️ 【注意】　応答項目中、値が「」（空文字列）は値が無い意味である。【注意１】　最大１２０銘柄まで指定可能、１２０超過分は無視。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetSyoukinZan", "aCLMMfdsSyoukinZan": [  {   "sIssueCode":"6501",   "pSFC6":"24500",   "pSFD":"2024/12/30",   "pSFD6":"10.3",   "pSFF6":"239600",   "pSFG6":"21300",   "pSFKS":"2",   "pSFL6":"21900",   "pSFN6":"235900",   "pSFP6":"600",   "pSFR6":"64.75",   "pSFS6":"3700",   "pSSG6":"-3200",   "pSSL6":"0",   "pSSP6":"3200"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetSyoukinZan |
| --- | --- | --- |
| aCLMMfdsSyoukinZan | 取得リスト | 以下項目を配列で応答 |
| sIssueCode | 対象銘柄コード | 要求設定値 |
| pSFC6 | 証金差引残前日比 |  |
| pSFD | 証金更新日 | YYYY/MM/DD |
| pSFD6 | 証金回転日数 |  |
| pSFF6 | 証金融資残 |  |
| pSFG6 | 証金融資前日比 |  |
| pSFKS | 速報確報ステータス | 1:速報2:確報 |
| pSFL6 | 証金融資･新規 |  |
| pSFN6 | 証金差引残 |  |
| pSFP6 | 証金融資･返済 |  |
| pSFR6 | 貸借倍率 |  |
| pSFS6 | 証金貸株残 |  |
| pSSG6 | 証金貸株前日比 |  |
| pSSL6 | 証金貸株･新規 |  |
| pSSP6 | 証金貸株･返済 |  |

<a name="CLMMfdsGetShinyouZan"></a>
### 信用残情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetShinyouZan", "sTargetIssueCode":"6501,7203",}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetShinyouZan |
| --- | --- | --- |
| sTargetIssueCode | 対象銘柄コード | **⚠️ 取得したい銘柄コードをカンマ区切りで羅列【注意１】参照** |
| **⚠️ 【注意】　応答項目中、値が「」（空文字列）は値が無い意味である。【注意１】　最大１２０銘柄まで指定可能、１２０超過分は無視。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetShinyouZan", "aCLMMfdsShinyouZan": [  {   "sIssueCode":"6501",   "pMBB3":"1632200",   "pMBB6":"3691900",   "pMBBQ":"5324100",   "pMBC3":"-103700",   "pMBC6":"-215900",   "pMBCQ":"-319600",   "pMBD":"2024/12/20",   "pMBN3":"124600",   "pMBN6":"445800",   "pMBNQ":"570400",   "pMBR3":"5.99",   "pMBR6":"9.26",   "pMBRQ":"7.93",   "pMBS3":"272400",   "pMBS6":"398700",   "pMBSQ":"671100"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetShinyouZan |
| --- | --- | --- |
| aCLMMfdsShinyouZan | 取得リスト | 以下項目を配列で応答 |
| sIssueCode | 対象銘柄コード | 要求設定値 |
| pMBB3 | 信用残買残(一般) |  |
| pMBB6 | 信用残買残(制度) |  |
| pMBBQ | 信用残買残(合算) |  |
| pMBC3 | 信用残売残前週比(一般) |  |
| pMBC6 | 信用残売残前週比(制度) |  |
| pMBCQ | 信用残売残前週比(合算) |  |
| pMBD | 信用残日付 | YYYY/MM/DD |
| pMBN3 | 信用残買残前週比(一般) |  |
| pMBN6 | 信用残買残前週比(制度) |  |
| pMBNQ | 信用残買残前週比(合算) |  |
| pMBR3 | 信用倍率(一般) |  |
| pMBR6 | 信用倍率(制度) |  |
| pMBRQ | 信用倍率(合算) |  |
| pMBS3 | 信用残売残(一般) |  |
| pMBS6 | 信用残売残(制度) |  |
| pMBSQ | 信用残売残(合算) |  |

<a name="CLMMfdsGetHibuInfo"></a>
### 逆日歩情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetHibuInfo", "sTargetIssueCode":"6501,7203",}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetHibuInfo |
| --- | --- | --- |
| sTargetIssueCode | 対象銘柄コード | **⚠️ 取得したい銘柄コードをカンマ区切りで羅列【注意１】参照** |
| **⚠️ 【注意】　応答項目中、値が「」（空文字列）は値が無い意味である。【注意１】　最大１２０銘柄まで指定可能、１２０超過分は無視。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetHibuInfo", "aCLMMfdsHibuInfo": [  {   "sIssueCode":"6501",   "pBWRQ":"0.05"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetHibuInfo |
| --- | --- | --- |
| aCLMMfdsHibuInfo | 取得リスト | 以下項目を配列で応答 |
| sIssueCode | 対象銘柄コード | 要求設定値 |
| pBWRQ | 逆日歩 |  |

<a name="ComT5"></a>
## 時価情報機能（REQUEST I/F）

<a name="CLMMfdsGetMarketPrice"></a>
### 時価情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetMarketPrice", "sTargetIssueCode":"6501,6502,6503", "sTargetColumn":"pDPP,tDPP:T,pPRP"}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMarketPrice |
| --- | --- | --- |
| sTargetIssueCode | 対象銘柄コード | **⚠️ 取得したい銘柄コードをカンマ区切りで羅列【注意１】参照** |
| sTargetColumn | 対象情報コード | **⚠️ 取得したい情報コードをカンマ区切りで羅列【注意２】参照** |
| **⚠️ 【注意１】　最大１２０銘柄まで指定可能、１２０超過分は無視。【注意２】　情報コードについては　立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、EVENT I/F 利用方法、データ仕様　「３．（３）FD」、【情報コード一覧】記載の「型＋情報コード」を指定。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetMarketPrice", "aCLMMfdsMarketPrice": [  {   "sIssueCode":"6501",   "pDPP":"oxox",   "pPRP":"oxox",   "tDPP:T":"oxox"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMarketPrice |
| --- | --- | --- |
| aCLMMfdsMarketPrice | 取得リスト | 以下項目を配列で応答 |
| sIssueCode | 対象銘柄コード | 要求設定値 |
| pDPP | 対象情報コード | 値 |
| pPRP | 対象情報コード | 値 |
| tDPP:T | 対象情報コード | 値 |

<a name="CLMMfdsGetMarketPriceHistory"></a>
### 蓄積情報問合取得

#### 要求

```json
{ "sCLMID":"CLMMfdsGetMarketPriceHistory", "sIssueCode":"6501", "sSizyouC":"00"}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMarketPriceHistory |
| --- | --- | --- |
| sIssueCode | 銘柄コード | １要求１銘柄指定例:6501 |
| sSizyouC | 市場 | 00：東証引数省略可能（デフォルト＝東証） |
| **⚠️ 【注意】　保持データ（最大約２０年分）を日付昇順で応答します。** |  |  |

#### 応答

```json
{ "sCLMID":"CLMMfdsGetMarketPriceHistory", "sIssueCode":"6501", "sSizyouC":"00" "aCLMMfdsGetMarketPriceHistory": [  {   "sDate":"YYYYMMDD",   "pDOP":"oxox",   "pDHP":"oxox",   "pDLP":"oxox",   "pDPP":"oxox",   "pDV":"oxox",   "pDOPxK":"oxox",   "pDHPxK":"oxox",   "pDLPxK":"oxox",   "pDPPxK":"oxox",   "pDVxK":"oxox",   "pSPUO":"oxox",   "pSPUC":"oxox",   "pSPUK":"oxox"  },   .   .   . ]}
```

| sCLMID | 機能ＩＤ | CLMMfdsGetMarketPriceHistory |
| --- | --- | --- |
| sIssueCode | 銘柄コード | 要求設定値 |
| sSizyouC | 市場 | 要求設定値 |
| aCLMMfdsGetMarketPriceHistory | 取得リスト | 以下項目を配列で応答 |
| sDate | 日付 | YYYYMMDD |
| pDOP | 始値 | 該当値 |
| pDHP | 高値 | 該当値 |
| pDLP | 安値 | 該当値 |
| pDPP | 終値 | 該当値 |
| pDV | 出来高 | 該当値 |
| pDOPxK | 始値ｘ分割係数 | 分割換算係数で計算した該当値 |
| pDHPxK | 高値ｘ分割係数 | 分割換算係数で計算した該当値 |
| pDLPxK | 安値ｘ分割係数 | 分割換算係数で計算した該当値 |
| pDPPxK | 終値ｘ分割係数 | 分割換算係数で計算した該当値 |
| pDVxK | 出来高÷分割係数 | 分割換算係数で計算した該当値 |
| pSPUO | 分割前単位 | 株式分割日のみ設定 |
| pSPUC | 分割後単位 | 株式分割日のみ設定 |
| pSPUK | 分割換算係数 | 分割換算係数＝分割前単位÷分割後単位株式分割日のみ設定 |
| **⚠️ 【注意】　取得レコードがあったら aCLMMfdsGetMarketPriceHistory に該当情報を設定します。** |  |  |

<a name="ComT6"></a>
## 注文約定通知（EVENT I/F）

| 時価及び注文約定通知（EVENT I/F 利用時）については以下資料を参照下さい。　立花証券・ｅ支店・ＡＰＩ（ｖ４ｒ７）、EVENT I/F 利用方法、データ仕様 |
| --- |

<a name="ComT7"></a>
## 結果コード、警告コード表

<a name="sResultCode"></a>
### 業務機能・応答項目・結果コード、警告コードのコード一覧

| コード | 分類 | テキスト | 理由 |
| --- | --- | --- | --- |
| 10001 | ログイン | ユーザーID、パスワードに誤りがあります | ユーザＩＤ不正 |
| 10002 | ログイン | ユーザーID、パスワードに誤りがあります | パスワード不正 |
| 10003 | ログイン | ユーザータイプに誤りがあります。 | ユーザタイプ不正 |
| 10004 | ログイン | 接続に誤りがあります | チャネル不正 |
| 10005 | ログイン | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 10006 | ログイン | セッションＩＤに誤りがあります | セッションＩＤ不正 |
| 10007 | ログイン | ユーザエージェントに誤りがあります | ユーザエージェント不正 |
| 10020 | ログイン | 通信に問題があります | ダミーセッションファイル障害 |
| 10021 | ログイン | 通信に問題があります | ダミーセッションレコードなし |
| 10030 | ログイン | ログインに問題があります | ユーザー管理ファイル障害 |
| 10031 | ログイン | ログイン前に行う電話番号認証が認証されない、または、ユーザID、暗証番号をお間違えです。認証エラーおよび暗証番号ご入力間違いの合計が弊社規程回数を超えた場合、ログイン停止になります。ご注意ください。(ログイン停止の解除は、コールセンターまでお電話下さい。) | ユーザー管理レコードなし |
| 10032 | ログイン | ログインに問題があります | ユーザー管理レコード更新エラー |
| 10033 | ログイン | 電話番号認証が認証されない、ユーザID、暗証番号のご入力間違いが弊社規程回数を超えたため、現在ログイン停止中です。(ログイン停止の解除は、コールセンターまでお電話下さい。) | ユーザー管理ログインロック |
| 10034 | ログイン | ログインできません | ユーザー管理ログインＮＧ |
| 10035 | ログイン | ユーザIDか暗証番号をお間違えです。ご確認の上、再度ご入力下さい。 | ユーザー管理パスワード不一致 |
| 10036 | ログイン | ご入力された口座では当システムをご利用いただけません。ご利用のサービスをご確認ください。 | システム口座区分不一致 |
| 10037 | ログイン | システム口座区分が不正のため金商法交付ドキュメントが取得できません。 | システム口座区分不正 |
| 10038 | ログイン | ユーザIDか暗証番号をお間違えです。ご確認の上、再度ご入力下さい。 | マイページUSER管理顧客登録番号データなし |
| 10039 | ログイン | ユーザIDか暗証番号をお間違えです。ご確認の上、再度ご入力下さい。 | マイページUSER管理社員IDデータなし |
| 10040 | ログイン | システム設定ファイルで問題が発生しました | システム設定ファイル障害 |
| 10041 | ログイン | システム設定レコードがありません | システム設定レコードなし |
| 10045 | ログイン | BAD_IPファイルで問題が発生しました | BAD_IPファイル障害 |
| 10046 | ログイン | BAD_IPレコード作成でエラーが発生しました | BAD_IPレコード作成エラー |
| 10047 | ログイン | BAD_IP許可件数が制限を超えています | BAD_IP許可件数オーバー |
| 10050 | ログイン | セッション情報ファイルで問題が発生しました | セッション情報ファイル障害 |
| 10051 | ログイン | セッション情報レコードがありません | セッション情報レコードなし |
| 10052 | ログイン | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 10053 | ログイン | セッション情報レコード作成でエラーが発生しました | セッション情報レコード作成エラー |
| 10054 | ログイン | セッションＩＤ生成でエラーが発生しました | セッションＩＤ生成エラー |
| 10055 | ログイン | 顧客マスタファイルで問題が発生しました | 顧客マスタファイル障害 |
| 10056 | ログイン | 顧客マスタレコードがありません | 顧客マスタレコードなし |
| 10057 | ログイン | 社員属性ファイルで問題が発生しました | 社員属性ファイル障害 |
| 10058 | ログイン | 社員属性レコードがありません | 社員属性レコードなし |
| 10060 | ログイン | 顧客情報ファイルで問題が発生しました | 顧客情報ファイル障害 |
| 10061 | ログイン | 顧客情報レコードがありません | 顧客情報レコードなし |
| 10062 | ログイン | 顧客情報レコード更新でエラーが発生しました | 顧客情報レコード更新エラー |
| 10065 | ログイン | 口座管理ファイルで問題が発生しました | 口座管理ファイル障害 |
| 10066 | ログイン | 口座管理レコードがありません | 口座管理レコードなし |
| 10067 | ログイン | 日付情報ファイルで問題が発生しました | 日付情報ファイル障害 |
| 10068 | ログイン | 日付情報レコードがありません | 日付情報レコードなし |
| 10069 | ログイン | 翌年用口座管理ファイルで問題が発生しました | 翌年用口座管理ファイル障害 |
| 10070 | ログイン | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 10071 | ログイン | 当日日付取得でエラーが発生しました | 当日日付取得エラー |
| 10075 | ログイン | 部店管理ファイルで問題が発生しました | 部店管理ファイル障害 |
| 10076 | ログイン | 部店管理レコードがありません | 部店管理レコードなし |
| 10080 | ログイン | 情報サービス利用客ファイルに問題が発生しました | 情報サービス利用客ファイル障害 |
| 10081 | ログイン | 利用期限が切れております。引き続きご利用の場合には、証券口座ログイン後[市況・情報]-[情報サービス]からお申し込みください。 |  |
| 10082 | ログイン | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 10083 | ログイン | マネロンリスク評価ファイルに問題があります | マネロンリスク評価ファイル障害 |
| 10084 | ログイン | 電話認証制御マスタにレコードがありません。 | 電話認証制御マスタレコードなし |
| 10085 | ログイン | 電話認証電話番号マスタにデータがありません。 | 電話認証電話番号マスタレコードなし |
| 10086 | ログイン | 顧客情報にデータがありません。 | 顧客情報取得失敗 |
| 10087 | ログイン | 当社に登録の電話番号から認証電話番号へかけた後にログインしてください。 | 電話番号未登録 |
| 10088 | ログイン | 当社に登録の電話番号から認証電話番号へかけた後にログインしてください。 | 着信なし、電話認証エラー |
| 10089 | ログイン | 当社に登録の電話番号から認証電話番号へかけた後、3分以内にログインしてください。 | 制限時間内の着信なし、電話認証エラー |
| 10091 | ログイン | 対象書面の閲覧日時の取得でエラーが発生しました。改めて書面をクリックして、再表示してください。 | 交付日時取得エラー |
| 10097 | ログイン | ネットワークでエラーが発生しました | ネットワークエラー |
| 10098 | ログイン | ＤＢでエラーが発生しました | ＤＢエラー |
| 10099 | ログイン | セッションがタイムアウトしました | タイムアウト |
| 10101 | お知らせ | 選択されたメッセージは削除済みのため、表示する事ができません。 | メッセージ削除済み |
| 10102 | お知らせ | 選択されたメッセージは存在しません。 | 該当メッセージなし |
| 10103 | お知らせ | 選択されたメッセージは削除済みのため、削除する事ができません。 | メッセージ削除済み |
| 10201 | お問い合わせ | お問い合わせ内容が長すぎます。2000文字以内にしてください。 | お問い合わせ内容文字列超過 |
| 10998 | HOME | ＤＢでエラーが発生しました | ＤＢエラー |
| 10999 | HOME | セッションがタイムアウトしました | タイムアウト |
| 11001 | 株式新規注文 | 注文種別に誤りがあります | 注文種別不正 |
| 11002 | 株式新規注文 | 親注文番号に誤りがあります | 親注文番号不正 |
| 11003 | 株式新規注文 | システム口座区分に誤りがあります | システム口座区分不正 |
| 11004 | 株式新規注文 | 部店コードに誤りがあります | 部店コード不正 |
| 11005 | 株式新規注文 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 11006 | 株式新規注文 | 譲渡益課税区分に誤りがあります | 譲渡益課税区分不正 |
| 11007 | 株式新規注文 | 銘柄コードに誤りがあります | 銘柄コード不正 |
| 11008 | 株式新規注文 | 市場に誤りがあります | 市場不正 |
| 11009 | 株式新規注文 | 売買区分に誤りがあります | 売買区分不正 |
| 11010 | 株式新規注文 | 執行条件に誤りがあります | 執行条件不正 |
| 11011 | 株式新規注文 | 注文値段区分に誤りがあります | 注文値段区分不正 |
| 11012 | 株式新規注文 | 注文値段に誤りがあります | 注文値段不正 |
| 11013 | 株式新規注文 | 注文数量に誤りがあります | 注文数量不正 |
| 11014 | 株式新規注文 | 現金信用区分に誤りがあります | 現金信用区分不正 |
| 11015 | 株式新規注文 | 空売り符号に誤りがあります | 空売り符号不正 |
| 11016 | 株式新規注文 | 注文期日に誤りがあります | 注文期日不正 |
| 11017 | 株式新規注文 | 逆指値注文種別に誤りがあります | 逆指値注文種別不正 |
| 11018 | 株式新規注文 | 逆指値条件に誤りがあります | 逆指値条件不正 |
| 11019 | 株式新規注文 | 逆指値値段区分に誤りがあります | 逆指値値段区分不正 |
| 11020 | 株式新規注文 | 逆指値値段に誤りがあります | 逆指値値段不正 |
| 11021 | 株式新規注文 | 接続に誤りがあります | チャネル不正 |
| 11022 | 株式新規注文 | 接続に誤りがあります | チャネル詳細不正 |
| 11023 | 株式新規注文 | 接続に誤りがあります | ＩＰアドレス不正 |
| 11024 | 株式新規注文 | 建日種類に誤りがあります | 建日種類不正（建日種類を1：個別指定以外に指定して、返済リストに建玉を列挙した場合にも発生） |
| 11025 | 株式新規注文 | 建玉番号に誤りがあります | 建玉番号不正 |
| 11026 | 株式新規注文 | 建玉順位に誤りがあります | 建玉順位不正 |
| 11027 | 株式新規注文 | 建玉数量に誤りがあります | 建玉数量不正 |
| 11028 | 株式新規注文 | 返済数量に誤りがあります | 返済数量不正 |
| 11029 | 株式新規注文 | 第二暗証番号省略フラグに誤りがあります | 第二暗証番号省略フラグ不正 |
| 11030 | 株式新規注文 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 11031 | 株式新規注文 |  | チェックのみフラグ不正 |
| 11032 | 株式新規注文 | 不成注文に成行が指定されています | 不成注文に成行が指定されています |
| 11033 | 株式新規注文 | 注文期限を指定する場合は、執行条件は｢無条件｣を指定して下さい。 | 期限付注文執行条件エラー |
| 11034 | 株式新規注文 | 逆指値注文執行条件でエラーが発生しました | 逆指値注文執行条件エラー |
| 11035 | 株式新規注文 | 通常＋逆指値注文執行条件でエラーが発生しました | 通常＋逆指値注文執行条件エラー |
| 11036 | 株式新規注文 | 子注文に執行条件でエラーが発生しました | 子注文に執行条件エラー |
| 11037 | 株式新規注文 | 子注文に注文期限でエラーが発生しました | 子注文に注文期限エラー |
| 11039 | 株式新規注文 | 端株に指値は指定出来ない | 端株に指値は指定出来ない |
| 11040 | 株式新規注文 | 非課税口座チャネルでエラーが発生しました | 非課税口座チャネルエラー |
| 11041 | 株式新規注文 | 非課税口座取引でエラーが発生しました（現物のみ） | 非課税口座取引エラー（現物のみ） |
| 11042 | 株式新規注文 | 非課税口座執行条件でエラーが発生しました（指定なしのみ） | 非課税口座執行条件エラー（指定なしのみ） |
| 11043 | 株式新規注文 | 非課税口座値段区分でエラーが発生しました（指値のみ） | 非課税口座値段区分エラー（指値のみ） |
| 11044 | 株式新規注文 | 非課税口座注文期限でエラーが発生しました（当日中のみ） | 非課税口座注文期限エラー（当日中のみ） |
| 11045 | 株式新規注文 | 非課税口座特殊注文でエラーが発生しました（特殊注文はできません） | 非課税口座特殊注文エラー（特殊注文禁止） |
| 11046 | 株式新規注文 | 弁済区分が選択されていません | 弁済区分不正 |
| 11047 | 株式新規注文 | ｢成行｣を指定されていますが、注文単価も入力されています。指値の場合は｢指値｣に印を付けて下さい。 | 成行指値同時指定 |
| 11048 | 株式新規注文 | 通常＋逆指値値段でエラーが発生しました | 通常＋逆指値値段エラー |
| 11100 | 株式新規注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 11101 | 株式新規注文 | 運用ステータス(採用値幅)にデータがありません | 運用ステータス(採用値幅)レコードなし |
| 11102 | 株式新規注文 | 只今の時間帯は受付できません | 運用ステータス(注文).受付停止 |
| 11103 | 株式新規注文 | 日付情報にデータがありません | 日付情報レコードなし |
| 11104 | 株式新規注文 | 銘柄がありません | 銘柄マスタレコードなし |
| 11105 | 株式新規注文 | 当該銘柄は売買停止中です | 銘柄マスタ.売買停止エラー |
| 11106 | 株式新規注文 | 当該銘柄は市場に直接お取り次ぎすることができません | 銘柄マスタ.場伝票出力有無エラー |
| 11107 | 株式新規注文 | 当該銘柄はNISA口座への買付ができません | 銘柄マスタ.非課税口座エラー |
| 11108 | 株式新規注文 | 銘柄市場マスタにデータがありません | 銘柄市場マスタレコードなし |
| 11109 | 株式新規注文 | 当該銘柄は前日終値がないため成行はできません | 銘柄市場マスタ.前日終値なし(成行禁止) |
| 11110 | 株式新規注文 | 当該銘柄は上場終了しています | 銘柄市場マスタ.上場廃止日エラー |
| 11111 | 株式新規注文 | 当該銘柄は上場前です | 銘柄市場マスタ.新規上場日エラー |
| 11112 | 株式新規注文 | 当該銘柄の売買単位の整数倍の数量を入力してください | 銘柄マスタ.売買単位エラー |
| 11113 | 株式新規注文 | 当該銘柄の値幅制限内の単価を入力してください | 銘柄市場マスタ.値幅エラー |
| 11114 | 株式新規注文 |  | 銘柄市場マスタ.制度信用エラー |
| 11115 | 株式新規注文 | 当該銘柄では新規売建はお取り扱いできません | 銘柄市場マスタ.信用売建エラー |
| 11116 | 株式新規注文 | 当該銘柄ではご指定の弁済区分での新規売建はお取り扱いできません | 一般信用売建エラー |
| 11117 | 株式新規注文 | 呼値にデータがありません | 呼値レコードなし |
| 11118 | 株式新規注文 | 正しい呼値の単位で単価を入力してください | 呼値エラー |
| 11119 | 株式新規注文 | 当該銘柄の信用属性でエラーが発生しました | 銘柄市場マスタ.信用属性エラー |
| 11120 | 株式新規注文 | 注文期日でエラーが発生しました | 注文期日エラー |
| 11121 | 株式新規注文 | 逆指値段には当該銘柄の値幅制限内の単価を入力してください | 逆指値段値幅エラー |
| 11122 | 株式新規注文 | 逆指値段呼値にデータがありません | 逆指値段呼値レコードなし |
| 11123 | 株式新規注文 | 正しい呼値の単位で逆指値段を入力してください | 逆指値段呼値エラー |
| 11124 | 株式新規注文 | 執行単価が0以下です | 執行値段マイナスエラー |
| 11125 | 株式新規注文 | システム別設定にデータがありません | システム別設定レコードなし |
| 11126 | 株式新規注文 | このサービスは取り扱っておりません | システム別設定.現物未実施 |
| 11127 | 株式新規注文 | このサービスは取り扱っておりません | システム別設定.制度信用未実施 |
| 11128 | 株式新規注文 | このサービスは取り扱っておりません | システム別設定.一般信用未実施 |
| 11129 | 株式新規注文 | システム市場弁済別取扱条件にデータがありません | システム市場弁済別取扱条件レコードなし |
| 11130 | 株式新規注文 | このサービスは取り扱っておりません | サービス別取扱.現物買付取扱不可 |
| 11131 | 株式新規注文 | このサービスは取り扱っておりません | サービス別取扱.現物売付取扱不可 |
| 11132 | 株式新規注文 | このサービスは取り扱っておりません | サービス別取扱.信用新規取扱不可 |
| 11133 | 株式新規注文 | このサービスは取り扱っておりません | サービス別取扱.信用返済取扱不可 |
| 11134 | 株式新規注文 | このサービスは取り扱っておりません | サービス別取扱.現受現渡取扱不可 |
| 11135 | 株式新規注文 | 当該市場ではお取引できません | 市場別設定.取引不可 |
| 11136 | 株式新規注文 | 寄付注文はできません | 商品市場別設定.執行条件寄付不可 |
| 11137 | 株式新規注文 | 引け注文はできません | 商品市場別設定.執行条件引け不可 |
| 11138 | 株式新規注文 | 不成注文はできません | 商品市場別設定.執行条件不成不可 |
| 11139 | 株式新規注文 | 連続注文はできません | 商品市場別設定.連続注文不可 |
| 11140 | 株式新規注文 | 出来るまで注文はできません | 商品市場別設定.出来るまで注文不可 |
| 11141 | 株式新規注文 | 当該銘柄はお取引できません | 銘柄別市場別規制.停止区分取引禁止 |
| 11142 | 株式新規注文 | 当該銘柄の成行注文はできません | 銘柄別市場別規制.停止区分成行禁止 |
| 11143 | 株式新規注文 | 当該銘柄の買付の注文はできません | 銘柄別市場別規制.現物買付取引禁止 |
| 11144 | 株式新規注文 | 当該銘柄の買付の成行注文はできません | 銘柄別市場別規制.現物買付成行禁止 |
| 11145 | 株式新規注文 | 当該銘柄の売付の注文はできません | 銘柄別市場別規制.現物売付取引禁止 |
| 11146 | 株式新規注文 | 当該銘柄の売付の成行注文はできません | 銘柄別市場別規制.現物売付成行禁止 |
| 11147 | 株式新規注文 | 当該銘柄の制度信用の新規買建注文はできません | 銘柄別市場別規制.制度信用買建取引禁止 |
| 11148 | 株式新規注文 | 当該銘柄の制度信用の新規買建の成行注文はできません | 銘柄別市場別規制.制度信用買建成行禁止 |
| 11149 | 株式新規注文 | 当該銘柄の制度信用の新規売建注文はできません | 銘柄別市場別規制.制度信用売建取引禁止 |
| 11150 | 株式新規注文 | 当該銘柄の制度信用の新規売建の成行注文はできません | 銘柄別市場別規制.制度信用売建成行禁止 |
| 11151 | 株式新規注文 | 当該銘柄の制度信用の買返済注文はできません | 銘柄別市場別規制.制度信用買返済取引禁止 |
| 11152 | 株式新規注文 | 当該銘柄の制度信用の買返済の成行注文はできません | 銘柄別市場別規制.制度信用買返済成行禁止 |
| 11153 | 株式新規注文 | 当該銘柄の制度信用の売返済注文はできません | 銘柄別市場別規制.制度信用売返済取引禁止 |
| 11154 | 株式新規注文 | 当該銘柄の制度信用の売返済の成行注文はできません | 銘柄別市場別規制.制度信用売返済成行禁止 |
| 11155 | 株式新規注文 | 当該銘柄の一般信用の新規買建注文はできません | 銘柄別市場別規制.一般信用買建取引禁止 |
| 11156 | 株式新規注文 | 当該銘柄の一般信用の新規買建の成行注文はできません | 銘柄別市場別規制.一般信用買建成行禁止 |
| 11157 | 株式新規注文 | 当該銘柄の一般信用の新規売建注文はできません | 銘柄別市場別規制.一般信用売建取引禁止 |
| 11158 | 株式新規注文 | 当該銘柄の一般信用の新規売建の成行注文はできません | 銘柄別市場別規制.一般信用売建成行禁止 |
| 11159 | 株式新規注文 | 当該銘柄の一般信用の買返済注文はできません | 銘柄別市場別規制.一般信用買返済取引禁止 |
| 11160 | 株式新規注文 | 当該銘柄の一般信用の買返済の成行注文はできません | 銘柄別市場別規制.一般信用買返済成行禁止 |
| 11161 | 株式新規注文 | 当該銘柄の一般信用の売返済注文はできません | 銘柄別市場別規制.一般信用売返済取引禁止 |
| 11162 | 株式新規注文 | 当該銘柄の一般信用の売返済の成行注文はできません | 銘柄別市場別規制.一般信用売返済成行禁止 |
| 11163 | 株式新規注文 | 当該銘柄の事前調整取引はできません | 銘柄別市場別規制.事前調整取引禁止 |
| 11164 | 株式新規注文 | 当該銘柄の即日入金取引はできません | 銘柄別市場別規制.即日入金取引禁止 |
| 11165 | 株式新規注文 | 当該銘柄の即日入金取引の成行注文はできません | 銘柄別市場別規制.即日入金取引成行禁止 |
| 11166 | 株式新規注文 | 当該銘柄の制度信用の現渡注文はできません | 銘柄別市場別規制.制度信用現渡取引禁止 |
| 11167 | 株式新規注文 | 当該銘柄の制度信用の現引注文はできません | 銘柄別市場別規制.制度信用現引取引禁止 |
| 11168 | 株式新規注文 | 当該銘柄の一般信用の現渡注文はできません | 銘柄別市場別規制.一般信用現渡済取引禁止 |
| 11169 | 株式新規注文 | 当該銘柄の一般信用の現引注文はできません | 銘柄別市場別規制.一般信用現引取引禁止 |
| 11170 | 株式新規注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 11171 | 株式新規注文 | 市場別設定レコードがありません | 市場別設定レコードなし |
| 11172 | 株式新規注文 | 商品市場別設定レコードがありません | 商品市場別設定レコードなし |
| 11173 | 株式新規注文 | 当該銘柄の即日入金取引の期限付き注文はできません | 銘柄別市場別規制.即日入金期限付き注文禁止 |
| 11174 | 株式新規注文 | 当該銘柄では特定口座でのお取り扱いはできません | 銘柄マスタ.特定口座対象Ｃエラー |
| 11175 | 株式新規注文 | 上場投信信託（ETF）は、上場日当日の８：００頃より、ご注文の入力が可能となります | 銘柄市場マスタ.値幅ゼロ |
| 11176 | 株式新規注文 | 当該銘柄の端株買付の注文はできません | 銘柄別市場別規制.端株買付取引禁止 |
| 11177 | 株式新規注文 | 当該銘柄の端株売付の注文はできません | 銘柄別市場別規制.端株売付取引禁止 |
| 11245 | 株式新規注文 | システム状態にデータがありません | システム状態レコードなし |
| 11246 | 株式新規注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 11247 | 株式新規注文 | システムが受付可能時間外です。 | システム状態.閉局 |
| 11288 | 株式新規注文 | 子注文同一銘柄でエラーが発生しました | 子注文同一銘柄エラー |
| 11289 | 株式新規注文 | 子注文件数が制限を超えています | 子注文件数オーバー |
| 11299 | 株式新規注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 11300 | 株式新規注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 11301 | 株式新規注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 11302 | 株式新規注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 11303 | 株式新規注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 11304 | 株式新規注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 11305 | 株式新規注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 11306 | 株式新規注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 11307 | 株式新規注文 | 特定口座が未開設です | 口座管理.特定口座未開設 |
| 11308 | 株式新規注文 | NISA口座が未開設です | 口座管理.非課税口座未開設 |
| 11309 | 株式新規注文 | 信用口座が未開設です | 口座管理.信用口座未開設 |
| 11310 | 株式新規注文 | 外国口座が未開設です | 口座管理.外国口座未開設 |
| 11311 | 株式新規注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 11312 | 株式新規注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 11313 | 株式新規注文 | インサイダファイルに問題があります | インサイダファイル障害 |
| 11314 | 株式新規注文 | 当該注文はインサイダー情報に基づく注文ではない同意が無い為受付できません | インサイダチェックエラー |
| 11315 | 株式新規注文 | 特定投資家契約マスタファイルに問題があります | 特定投資家契約マスタファイル障害 |
| 11316 | 株式新規注文 | 特定投資家契約マスタチェックでエラーが発生しました | 特定投資家契約マスタチェックエラー |
| 11317 | 株式新規注文 | 金商法交付書面ファイルに問題があります | 金商法交付書面ファイル障害 |
| 11318 | 株式新規注文 | 金商法交付書面(当日分)ファイルに問題があります | 金商法交付書面(当日更新分)ファイル障害 |
| 11319 | 株式新規注文 | 金商法交付書面チェックでエラーが発生しました | 金商法交付書面チェックエラー |
| 11320 | 株式新規注文 | 顧客銘柄別取引停止ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 11321 | 株式新規注文 | 顧客銘柄別取引停止にデータがありません | 顧客銘柄別取引停止レコードなし |
| 11322 | 株式新規注文 | お客様の当該銘柄における現物買付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物買付停止 |
| 11323 | 株式新規注文 | お客様の当該銘柄における現物売付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物売付停止 |
| 11324 | 株式新規注文 | お客様の当該銘柄における信用新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規買建停止 |
| 11325 | 株式新規注文 | お客様の当該銘柄における信用新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規売建停止 |
| 11326 | 株式新規注文 | お客様の当該銘柄における信用買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用買返済停止 |
| 11327 | 株式新規注文 | お客様の当該銘柄における信用売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用売返済停止 |
| 11328 | 株式新規注文 | お客様の当該銘柄における信用現引のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現引停止 |
| 11329 | 株式新規注文 | お客様の当該銘柄における信用現渡のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現渡停止 |
| 11340 | 株式新規注文 | 市場別特殊執行注文取扱停止ファイルに問題があります | 市場別特殊執行注文取扱停止ファイル障害 |
| 11341 | 株式新規注文 | 当該市場での逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.逆指値停止 |
| 11342 | 株式新規注文 | 当該市場での通常＋逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.通常＋逆指値停止 |
| 11343 | 株式新規注文 | 商品別特殊執行注文取扱停止ファイルに問題があります | 商品別特殊執行注文取扱停止ファイル障害 |
| 11344 | 株式新規注文 | 逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.逆指値停止 |
| 11345 | 株式新規注文 | 通常＋逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.通常＋逆指値停止 |
| 11346 | 株式新規注文 | 銘柄別特殊執行注文取扱停止ファイルに問題があります | 銘柄別特殊執行注文取扱停止ファイル障害 |
| 11347 | 株式新規注文 | 当該銘柄は逆指値注文はできません | 銘柄別特殊執行注文取扱停止.逆指値停止 |
| 11348 | 株式新規注文 | 当該銘柄は通常＋逆指値はできません | 銘柄別特殊執行注文取扱停止.通常＋逆指値停止 |
| 11349 | 株式新規注文 | 当該銘柄は特殊執行注文はできません | 銘柄別特殊執行注文取扱停止.特殊執行注文不可 |
| 11350 | 株式新規注文 | ハードリミット市場別ファイルに問題があります | ハードリミット市場別ファイル障害 |
| 11351 | 株式新規注文 | ハードリミット市場別にデータがありません | ハードリミット市場別レコードなし |
| 11352 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合1 |
| 11353 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合2 |
| 11354 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合3 |
| 11355 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合4 |
| 11356 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合5 |
| 11360 | 株式新規注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 11361 | 株式新規注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 11362 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買上限 |
| 11363 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売上限 |
| 11364 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 11365 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 11366 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 11367 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 11368 | 株式新規注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 11369 | 株式新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 11370 | 株式新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 11371 | 株式新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 11372 | 株式新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 11380 | 株式新規注文 | 注文できません。個別ファイルに問題があります | ソフトリミット個別ファイル障害 |
| 11381 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買上限 |
| 11382 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売上限 |
| 11383 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 11384 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 11385 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 11386 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 11387 | 株式新規注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 11388 | 株式新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 11389 | 株式新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 11390 | 株式新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 11391 | 株式新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 11400 | 株式新規注文 | 注文できません。通常ファイルに問題があります | ソフトリミット通常ファイル障害 |
| 11401 | 株式新規注文 | 注文できません。通常ファイルにデータがありません | ソフトリミット通常レコードなし |
| 11402 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買上限 |
| 11403 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売上限 |
| 11404 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 11405 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 11406 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 11407 | 株式新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 11408 | 株式新規注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 11409 | 株式新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 11410 | 株式新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 11411 | 株式新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 11412 | 株式新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 11415 | 株式新規注文 | 空売り注文はできません | 空売り規制(注文不可) |
| 11416 | 株式新規注文 | 空売り成行注文はできません | 空売り規制(成行不可) |
| 11417 | 株式新規注文 | 空売り期限付き注文はできません | 空売り規制(期限付き不可) |
| 11420 | 株式新規注文 | 買付可能額が不足しています | 買付可能額不足 |
| 11421 | 株式新規注文 | 売付可能数量が不足しています | 売付可能数量不足 |
| 11422 | 株式新規注文 | 新規建余力は、%s 円です。ご注文に対して現金保証金が、%s 円不足しています。 | 信用新規建可能額不足 |
| 11423 | 株式新規注文 | 現引可能額が不足しています | 現引可能額不足 |
| 11424 | 株式新規注文 | この注文単価では%s株までしか入力できません | 売付可能数量不足 |
| 11425 | 株式新規注文 | この注文単価ではこの注文株数は入力は出来ません | 売付可能数量不足 |
| 11426 | 株式新規注文 | この銘柄は日計りの対象となっているため、現在売付可能株数は%s株となります。ご注文された%s株を発注するためには、お預かり金が%s円不足しております。 | 売付可能数量不足 |
| 11427 | 株式新規注文 | この銘柄は日計りの対象となっているため、余力が不足します。 | 売付可能数量不足 |
| 11428 | 株式新規注文 | 増担保の現金必要保証金が不足します。 | 現金必要保証金不足 |
| 11429 | 株式新規注文 | 信用新規建可能額が不足しています | 信用新規建可能額不足 |
| 11430 | 株式新規注文 | 現在、この銘柄の買付可能額は、%s 円です。%s 円不足しているため、このご注文はお受けできません。(日計り取引銘柄等、銘柄によっては可能額の算出方法が異なるケースがあります。) | 買付可能額不足 |
| 11440 | 株式新規注文 | 非課税口座管理ファイルに問題があります | 非課税口座管理ファイル障害 |
| 11441 | 株式新規注文 | 非課税口座管理にデータがありません | 非課税口座管理レコードなし |
| 11442 | 株式新規注文 | 非課税口座管理更新でエラーが発生しました | 非課税口座管理更新エラー |
| 11443 | 株式新規注文 | 非課税口座可能額が不足しています | 非課税口座可能額不足 |
| 11450 | 株式新規注文 | 顧客手数料ファイルに問題があります | 顧客手数料ファイル障害 |
| 11451 | 株式新規注文 |  | 顧客手数料レコードなし |
| 11460 | 株式新規注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 11461 | 株式新規注文 |  | 手数料マスタレコードなし |
| 11470 | 株式新規注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 11471 | 株式新規注文 |  | 課税率マスタレコードなし |
| 11480 | 株式新規注文 | 保管顧客課税別ファイルに問題があります | 保管顧客課税別ファイル障害 |
| 11481 | 株式新規注文 | 選択した口座区分がお預かり銘柄と不一致のため、このご注文はお受けできません。 | 保管顧客課税別にデータがありません |
| 11482 | 株式新規注文 | 売付可能な株数が不足しているため、このご注文はお受けできません。売却可能株数や注文一覧画面をご確認ください。 | 保管顧客課税別にデータがありません |
| 11483 | 株式新規注文 | 保管顧客課税別にデータ作成でエラーが発生しました | 保管顧客課税別レコード作成エラー |
| 11484 | 株式新規注文 | 保管顧客課税別のデータ更新でエラーが発生しました | 保管顧客課税別レコード更新エラー |
| 11490 | 株式新規注文 | 信用建玉明細ファイルに問題があります | 信用建玉明細ファイル障害 |
| 11491 | 株式新規注文 | 信用建玉明細にデータがありません | 信用建玉明細レコードなし |
| 11492 | 株式新規注文 | 信用建玉明細有効数量がありません | 信用建玉明細有効数量なし |
| 11493 | 株式新規注文 | 信用建玉明細のデータ更新でエラーが発生しました | 信用建玉明細レコード更新エラー |
| 11494 | 株式新規注文 | 信用建玉残ファイルに問題があります | 信用建玉残ファイル障害 |
| 11495 | 株式新規注文 | 信用建玉残にデータがありません | 信用建玉残レコードなし |
| 11496 | 株式新規注文 | 信用建玉残にデータ作成でエラーが発生しました | 信用建玉残レコード作成エラー |
| 11497 | 株式新規注文 | 信用建玉残のデータ更新でエラーが発生しました | 信用建玉残レコード更新エラー |
| 11500 | 株式新規注文 | 顧客金銭ファイルに問題があります | 顧客金銭ファイル障害 |
| 11501 | 株式新規注文 | 顧客金銭にデータがありません | 顧客金銭レコードなし |
| 11502 | 株式新規注文 | 顧客拘束金ファイルに問題があります | 顧客拘束金ファイル障害 |
| 11503 | 株式新規注文 | 顧客拘束金にデータがありません | 顧客拘束金レコードなし |
| 11504 | 株式新規注文 |  | 顧客拘束金レコードレコード作成エラー |
| 11505 | 株式新規注文 |  | 顧客拘束金レコード更新エラー |
| 11509 | 株式新規注文 | 保証金率取得でエラーが発生しました | 保証金率取得エラー |
| 11510 | 株式新規注文 | 代用掛目ファイルに問題があります | 代用掛目ファイル障害 |
| 11511 | 株式新規注文 | 日付情報ファイルに問題があります | 日付情報ファイル障害 |
| 11512 | 株式新規注文 | 保管顧客別残ファイルに問題があります | 保管顧客別残ファイル障害 |
| 11513 | 株式新規注文 | 保管顧客別残にデータがありません | 保管顧客別残レコードなし |
| 11514 | 株式新規注文 | 保管顧客別残にデータ作成でエラーが発生しました | 保管顧客別残レコード作成エラー |
| 11515 | 株式新規注文 | 保管顧客別残のデータ更新でエラーが発生しました | 保管顧客別残レコード更新エラー |
| 11516 | 株式新規注文 | 保証金推移ファイルに問題があります | 保証金推移ファイル障害 |
| 11517 | 株式新規注文 | 保証金推移にデータがありません | 保証金推移レコードなし |
| 11518 | 株式新規注文 | 保証金推移にデータ作成でエラーが発生しました | 保証金推移レコード作成エラー |
| 11519 | 株式新規注文 | 保証金推移のデータ更新でエラーが発生しました | 保証金推移レコード更新エラー |
| 11520 | 株式新規注文 | 顧客当日取引情報ファイルに問題があります | 顧客当日取引情報ファイル障害 |
| 11521 | 株式新規注文 | 顧客当日取引情報にデータがありません | 顧客当日取引情報レコードなし |
| 11522 | 株式新規注文 | 顧客当日取引情報にデータ作成でエラーが発生しました | 顧客当日取引情報レコード作成エラー |
| 11523 | 株式新規注文 | 顧客当日取引情報のデータ更新でエラーが発生しました | 顧客当日取引情報レコード更新エラー |
| 11524 | 株式新規注文 | 差金決済管理明細ファイルに問題があります | 差金決済管理明細ファイル障害 |
| 11525 | 株式新規注文 | 差金決済管理明細にデータがありません | 差金決済管理明細レコードなし |
| 11526 | 株式新規注文 | 差金決済管理明細にデータ作成でエラーが発生しました | 差金決済管理明細レコード作成エラー |
| 11527 | 株式新規注文 | 差金決済管理明細のデータ更新でエラーが発生しました | 差金決済管理明細レコード更新エラー |
| 11530 | 株式新規注文 | 譲渡益台帳ファイルに問題が発生しました | 譲渡益台帳ファイル障害 |
| 11531 | 株式新規注文 | 譲渡益台帳レコードがありません | 譲渡益台帳レコードなし |
| 11532 | 株式新規注文 | 譲渡益台帳レコード作成でエラーが発生しました | 譲渡益台帳レコード作成エラー |
| 11534 | 株式新規注文 | 譲渡益台帳レコード更新でエラーが発生しました | 譲渡益台帳レコード更新エラー |
| 11600 | 株式新規注文 | 注文番号（株式）ファイルに問題があります | 注文番号（株式）ファイル障害 |
| 11601 | 株式新規注文 | 注文番号（株式）にデータがありません | 注文番号（株式）レコードなし |
| 11602 | 株式新規注文 | 建玉番号（株式）ファイルに問題があります | 建玉番号（株式）ファイル障害 |
| 11603 | 株式新規注文 | 建玉番号（株式）にデータがありません | 建玉番号（株式）レコードなし |
| 11604 | 株式新規注文 | 親注文株式サマリファイルに問題があります | 親注文株式サマリファイル障害 |
| 11605 | 株式新規注文 | 親注文株式サマリにデータがありません | 親注文株式サマリレコードなし |
| 11606 | 株式新規注文 | 親注文株式サマリ有効数量がありません | 親注文株式サマリ有効数量なし |
| 11607 | 株式新規注文 | 親注文株式サマリ数量を超えています | 親注文株式サマリ数量オーバー |
| 11608 | 株式新規注文 |  | 親注文株式サマリレコード更新エラー |
| 11609 | 株式新規注文 | 株式サマリファイルに問題があります | 株式サマリファイル障害 |
| 11610 | 株式新規注文 | 株式サマリにデータがありません | 株式サマリレコードなし |
| 11611 | 株式新規注文 | 株式サマリにデータ作成でエラーが発生しました | 株式サマリレコード作成エラー |
| 11612 | 株式新規注文 | 株式サマリのデータ更新でエラーが発生しました | 株式サマリレコード更新エラー |
| 11613 | 株式新規注文 | 株式明細ファイルに問題があります | 株式明細ファイル障害 |
| 11614 | 株式新規注文 | 株式明細にデータがありません | 株式明細レコードなし |
| 11615 | 株式新規注文 | 株式明細更新でエラーが発生しました | 株式明細更新エラー |
| 11616 | 株式新規注文 | 株式明細にデータ作成でエラーが発生しました | 株式明細レコード作成エラー |
| 11617 | 株式新規注文 | 株式注文約定履歴ファイルに問題があります | 株式注文約定履歴ファイル障害 |
| 11618 | 株式新規注文 | 株式注文約定履歴作成でエラーが発生しました | 株式注文約定履歴作成エラー |
| 11621 | 株式新規注文 | 株式返済予約ファイルに問題があります | 株式返済予約ファイル障害 |
| 11622 | 株式新規注文 | 株式返済予約にデータがありません | 株式返済予約レコードなし |
| 11623 | 株式新規注文 | 株式返済予約にデータ作成でエラーが発生しました | 株式返済予約レコード作成エラー |
| 11624 | 株式新規注文 | 株式返済予約のデータ更新でエラーが発生しました | 株式返済予約レコード更新エラー |
| 11625 | 株式新規注文 | 株式返済明細ファイルに問題があります | 株式返済明細ファイル障害 |
| 11626 | 株式新規注文 | 株式返済明細にデータがありません | 株式返済明細レコードなし |
| 11627 | 株式新規注文 | 株式返済明細にデータ作成でエラーが発生しました | 株式返済明細レコード作成エラー |
| 11628 | 株式新規注文 | 株式返済明細のデータ更新でエラーが発生しました | 株式返済明細レコード更新エラー |
| 11640 | 株式新規注文 | 株式約定失効ファイルに問題があります | 株式約定失効ファイル障害 |
| 11641 | 株式新規注文 | 株式約定失効にデータがありません | 株式約定失効レコードなし |
| 11642 | 株式新規注文 | 株式約定失効にデータ作成でエラーが発生しました | 株式約定失効レコード作成エラー |
| 11643 | 株式新規注文 | 株式約定失効のデータ更新でエラーが発生しました | 株式約定失効レコード更新エラー |
| 11645 | 株式新規注文 | システム別設定ファイルに問題があります | システム別設定ファイル障害 |
| 11646 | 株式新規注文 | 銘柄マスタ（株式）ファイルに問題があります | 銘柄マスタ（株式）ファイル障害 |
| 11647 | 株式新規注文 | 銘柄市場マスタ（株式）ファイルに問題があります | 銘柄市場マスタ（株式）ファイル障害 |
| 11648 | 株式新規注文 | 銘柄別・市場別規制（株式）ファイルに問題があります | 銘柄別・市場別規制（株式）ファイル障害 |
| 11700 | 株式新規注文 | 運用ステータス(申告)にデータがありません | 運用ステータス(申告)レコードなし |
| 11701 | 株式新規注文 | 只今の時間帯は受付できません | 運用ステータス(申告).受付停止 |
| 11702 | 株式新規注文 | 運用ステータス(連続注文)にデータがありません | 運用ステータス(連続注文)レコードなし |
| 11703 | 株式新規注文 | 只今の時間帯は受付できません | 運用ステータス(連続注文).受付停止 |
| 11800 | 株式新規注文 | 余力制御ファイルに問題があります | 余力制御ファイル障害 |
| 11802 | 株式新規注文 | お客様のお取引を停止させていただいております | 余力制御.取引停止 |
| 11803 | 株式新規注文 | お客様の信用新規建のお取引を停止させていただいております | 余力制御.信用新規建停止 |
| 11806 | 株式新規注文 | お客様のその他商品買付のお取引を停止させていただいております | 余力制御.その他商品買付停止 |
| 11807 | 株式新規注文 | 追証で未入金があります | 余力制御.追証未入金あり |
| 11808 | 株式新規注文 | お客様の現引、現渡のお取引を停止させていただいております | 余力制御.現引現渡停止 |
| 11810 | 株式新規注文 | 二階建チェックファイルに問題があります | 二階建チェックファイル障害 |
| 11811 | 株式新規注文 | 二階建チェックでエラーが発生しました | 二階建チェックエラー |
| 11820 | 株式新規注文 | この銘柄には増担保規制が適用されております。増担保ファイルに問題があります。 | 増担保ファイル障害 |
| 11821 | 株式新規注文 | この銘柄には増担保規制が適用されております。規制銘柄新規建余力は、%s円です。ご注文に対して現金保証金が、%s円不足しています。 | 増担保現金チェックエラー |
| 11822 | 株式新規注文 | この銘柄には増担保規制が適用されております。規制銘柄新規建余力は、%s円です。ご注文に対して現金保証金が、%s円不足しています。 | 増担保現金チェックエラー |
| 11823 | 株式新規注文 | この銘柄には増担保規制が適用されております。ご注文に対して現金保証金が不足しています。 | 増担保現金チェックエラー |
| 11824 | 株式新規注文 | この銘柄には増担保規制が適用されております。規制銘柄新規建余力が不足しています。 | 増担保保証金チェックエラー |
| 11825 | 株式新規注文 | ご注文に対して現金保証金が不足しています。 | 増担保現金チェックエラー |
| 11826 | 株式新規注文 | 新規建余力は0円です。(最低保証金割れ) | 最低保証金割れエラー |
| 11830 | 株式新規注文 | 一極集中ファイル障害 | 一極集中ファイル障害 |
| 11831 | 株式新規注文 | 一極集中銘柄規制に抵触します。 | 一極集中チェックエラー |
| 11832 | 株式新規注文 | 保証金率チェックファイル障害 | 保証金率チェックファイル障害 |
| 11833 | 株式新規注文 | 当社運用規制の為、注文は受付られません | 保証金率チェックエラー |
| 11834 | 株式新規注文 | NISA注文抑止チェックファイル障害 | NISA買付注文抑止チェックファイル障害 |
| 11835 | 株式新規注文 | ＮＩＳＡロールオーバー期間の為、買付注文停止中です。 | NISA買付注文抑止チェックエラー |
| 11836 | 株式新規注文 | NISA注文抑止チェックファイル障害 | NISA売付注文抑止チェックファイル障害 |
| 11837 | 株式新規注文 | ＮＩＳＡロールオーバー期間の為、対象年のお預りがある銘柄の売付注文停止中です。 | NISA売付注文抑止チェックエラー |
| 11900 | 株式新規注文 | 現物買付可能額取得でエラーが発生しました | 現物買付可能額取得エラー |
| 11901 | 株式新規注文 | 差金決済売付可能数量取得でエラーが発生しました | 差金決済売付可能数量取得エラー |
| 11902 | 株式新規注文 | 信用新規建可能額取得でエラーが発生しました | 信用新規建可能額取得エラー |
| 11903 | 株式新規注文 | 現引可能額取得でエラーが発生しました | 現引可能額取得エラー |
| 11904 | 株式新規注文 | 日計り拘束金取得でエラーが発生しました | 日計り拘束金取得エラー |
| 11991 | 株式新規注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 11992 | 株式新規注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 11993 | 株式新規注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 11994 | 株式新規注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 11997 | 株式新規注文 | ネットでエラーが発生しました | ネットエラー |
| 11998 | 株式新規注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 11999 | 株式新規注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 12001 | 株式訂正注文 | 注文番号に誤りがあります | 注文番号不正 |
| 12002 | 株式訂正注文 | 営業日に誤りがあります | 営業日不正 |
| 12003 | 株式訂正注文 | 市場に誤りがあります | 市場不正 |
| 12004 | 株式訂正注文 | 執行条件訂正フラグに誤りがあります | 執行条件訂正フラグ不正 |
| 12005 | 株式訂正注文 | 執行条件に誤りがあります | 執行条件不正 |
| 12006 | 株式訂正注文 | 注文値段訂正フラグに誤りがあります | 注文値段訂正フラグ不正 |
| 12007 | 株式訂正注文 | 注文値段区分に誤りがあります | 注文値段区分不正 |
| 12008 | 株式訂正注文 | 注文値段に誤りがあります | 注文値段不正 |
| 12009 | 株式訂正注文 | 注文数量訂正フラグに誤りがあります | 注文数量訂正フラグ不正 |
| 12010 | 株式訂正注文 | 注文数量に誤りがあります | 注文数量不正 |
| 12011 | 株式訂正注文 | 注文期日訂正フラグに誤りがあります | 注文期日訂正フラグ不正 |
| 12012 | 株式訂正注文 | 注文期日訂正フラグに誤りがあります | 注文期日訂正フラグ不正 |
| 12013 | 株式訂正注文 | 逆指値値段条件訂正フラグに誤りがあります | 逆指値値段条件訂正フラグ不正 |
| 12014 | 株式訂正注文 | 逆指値条件に誤りがあります | 逆指値条件不正 |
| 12015 | 株式訂正注文 | 逆指値値段区分訂正フラグに誤りがあります | 逆指値値段区分訂正フラグ不正 |
| 12016 | 株式訂正注文 | 逆指値値段区分に誤りがあります | 逆指値値段区分不正 |
| 12017 | 株式訂正注文 | 逆指値値段に誤りがあります | 逆指値値段不正 |
| 12018 | 株式訂正注文 | 接続チャネルに誤りがあります | チャネル不正 |
| 12019 | 株式訂正注文 | 接続チャネル詳細に誤りがあります | チャネル詳細不正 |
| 12020 | 株式訂正注文 | オペレータに誤りがあります | オペレータ不正 |
| 12021 | 株式訂正注文 | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 12022 | 株式訂正注文 | 第二暗証番号省略フラグに誤りがあります | 第二暗証番号省略フラグ不正 |
| 12023 | 株式訂正注文 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 12024 | 株式訂正注文 |  | チェックのみフラグ不正 |
| 12032 | 株式訂正注文 | 不成注文に成行が指定されています | 不成注文に成行が指定されています |
| 12033 | 株式訂正注文 | 期限付き注文に執行条件の訂正はできません。 | 期限付注文執行条件エラー |
| 12034 | 株式訂正注文 | トリガー前の逆指値注文の執行条件は訂正できません。 | 逆指値注文執行条件エラー |
| 12035 | 株式訂正注文 | トリガー前の通常＋逆指値注文の執行条件は訂正できません。 | 通常＋逆指値注文執行条件エラー |
| 12036 | 株式訂正注文 | 子注文に執行条件でエラーが発生しました | 子注文に執行条件エラー |
| 12037 | 株式訂正注文 | 子注文に注文期限でエラーが発生しました | 子注文に注文期限エラー |
| 12039 | 株式訂正注文 | 端株に指値は指定できません | 端株に指値は指定出来ない |
| 12040 | 株式訂正注文 | ｢成行｣を指定されていますが、注文単価も入力されています。指値の場合は｢指値｣に印を付けて下さい。 | 成行指値同時指定 |
| 12042 | 株式訂正注文 | 非課税口座執行条件で無条件以外のエラーが発生しました | 非課税口座執行条件エラー（指定なしのみ） |
| 12043 | 株式訂正注文 | 非課税口座値段区分でエラーが発生しました（指値のみ） | 非課税口座値段区分エラー（指値のみ） |
| 12044 | 株式訂正注文 | 非課税口座注文期限でエラーが発生しました（当日中のみ） | 非課税口座注文期限エラー（当日中のみ） |
| 12048 | 株式訂正注文 | 通常＋逆指値値段でエラーが発生しました | 通常＋逆指値値段エラー |
| 12050 | 株式訂正注文 | 通常注文の逆指値条件は訂正できません。 | 通常注文逆指値条件エラー |
| 12051 | 株式訂正注文 | 通常注文の逆指値注文値段は訂正できません。 | 通常注文逆指値注文値段エラー |
| 12052 | 株式訂正注文 | トリガー前の逆指値注文の注文値段は訂正できません。 | 逆指値注文値段エラー |
| 12053 | 株式訂正注文 | トリガー前の通常＋逆指値注文の注文値段は訂正できません。 | 通常＋逆指値注文値段エラー |
| 12110 | 株式訂正注文 | 執行条件変更がありません | 執行条件変更なし |
| 12111 | 株式訂正注文 | 注文数量変更がありません | 注文数量変更なし |
| 12112 | 株式訂正注文 | 注文値段変更がありません | 注文値段変更なし |
| 12113 | 株式訂正注文 | 注文期日変更がありません | 注文期日変更なし |
| 12114 | 株式訂正注文 | 逆指値条件変更がありません | 逆指値条件変更なし |
| 12115 | 株式訂正注文 |  | 逆指値注文値段変更なし |
| 12116 | 株式訂正注文 | 変更項目がありません | 変更項目なし |
| 12120 | 株式訂正注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 12121 | 株式訂正注文 | 運用ステータス(採用値幅)にデータがありません | 運用ステータス(採用値幅)レコードなし |
| 12122 | 株式訂正注文 | 只今の時間帯は受付できません | 運用ステータス(注文).受付停止 |
| 12130 | 株式訂正注文 | 日付情報にデータがありません | 日付情報レコードなし |
| 12140 | 株式訂正注文 | 銘柄マスタにデータがありません | 銘柄マスタレコードなし |
| 12151 | 株式訂正注文 | 銘柄市場マスタにデータがありません | 銘柄市場マスタレコードなし |
| 12152 | 株式訂正注文 | 銘柄市場マスタ.前日終値がありません | 銘柄市場マスタ.前日終値なし |
| 12153 | 株式訂正注文 | 当該銘柄の売買単位の整数倍の数量を入力してください | 銘柄マスタ.売買単位エラー |
| 12154 | 株式訂正注文 | 当該銘柄の値幅制限内の単価を入力してください | 銘柄市場マスタ.値幅エラー |
| 12160 | 株式訂正注文 | 呼値にデータがありません | 呼値レコードなし |
| 12161 | 株式訂正注文 | 正しい呼値の単位で単価を入力してください | 呼値エラー |
| 12170 | 株式訂正注文 | 数量の増加はできません | 増株訂正エラー |
| 12180 | 株式訂正注文 | 注文期日でエラーが発生しました | 注文期日エラー |
| 12191 | 株式訂正注文 | 逆指値段には当該銘柄の値幅制限内の単価を入力してください | 逆指値段値幅エラー |
| 12192 | 株式訂正注文 | 逆指値段呼値にデータがありません | 逆指値段呼値レコードなし |
| 12193 | 株式訂正注文 | 正しい呼値の単位で逆指値段を入力してください | 逆指値段呼値エラー |
| 12194 | 株式訂正注文 | 執行単価が0以下です | 執行値段マイナスエラー |
| 12199 | 株式訂正注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 12200 | 株式訂正注文 | このサービスは取り扱っておりません | サービス別取扱.現物訂正取扱不可 |
| 12201 | 株式訂正注文 | このサービスは取り扱っておりません | サービス別取扱.信用訂正取扱不可 |
| 12209 | 株式訂正注文 | 商品市場別設定レコードがありません | 商品市場別設定レコードなし |
| 12210 | 株式訂正注文 | 数量と値段の同時訂正はできません | 商品市場別設定.同時訂正不可 |
| 12211 | 株式訂正注文 | 寄付への訂正はできません | 商品市場別設定.執行条件寄付不可 |
| 12212 | 株式訂正注文 | 引けへの訂正はできません | 商品市場別設定.執行条件引け不可 |
| 12213 | 株式訂正注文 | 不成への訂正はできません | 商品市場別設定.執行条件不成不可 |
| 12214 | 株式訂正注文 | 連続注文の訂正はできません | 商品市場別設定.連続注文不可 |
| 12215 | 株式訂正注文 | 出来るまで注文の訂正はできません | 商品市場別設定.出来るまで注文不可 |
| 12220 | 株式訂正注文 | 当該銘柄はお取引できません | 銘柄別市場別規制.停止区分取引禁止 |
| 12221 | 株式訂正注文 | 当該銘柄の現物買付の成行注文はできません | 銘柄別市場別規制.現物買付成行禁止 |
| 12222 | 株式訂正注文 | 当該銘柄の現物売付の成行注文はできません | 銘柄別市場別規制.現物売付成行禁止 |
| 12223 | 株式訂正注文 | 当該銘柄の制度信用の新規買建の成行注文はできません | 銘柄別市場別規制.制度信用買建成行禁止 |
| 12224 | 株式訂正注文 | 当該銘柄の制度信用の新規売建の成行注文はできません | 銘柄別市場別規制.制度信用売建成行禁止 |
| 12225 | 株式訂正注文 | 当該銘柄の制度信用の買返済の成行注文はできません | 銘柄別市場別規制.制度信用買返済成行禁止 |
| 12226 | 株式訂正注文 | 当該銘柄の制度信用の売返済の成行注文はできません | 銘柄別市場別規制.制度信用売返済成行禁止 |
| 12227 | 株式訂正注文 | 当該銘柄の一般信用の新規買建の成行注文はできません | 銘柄別市場別規制.一般信用買建成行禁止 |
| 12228 | 株式訂正注文 | 当該銘柄の一般信用の新規売建の成行注文はできません | 銘柄別市場別規制.一般信用売建成行禁止 |
| 12229 | 株式訂正注文 | 当該銘柄の一般信用の買返済の成行注文はできません | 銘柄別市場別規制.一般信用買返済成行禁止 |
| 12230 | 株式訂正注文 | 当該銘柄の一般信用の売返済の成行注文はできません | 銘柄別市場別規制.一般信用売返済成行禁止 |
| 12240 | 株式訂正注文 | 当該銘柄の即日入金取引の成行注文はできません | 銘柄別市場別規制.即日入金取引成行禁止 |
| 12241 | 株式訂正注文 | 空売り注文は成行に訂正できません | 空売り注文成行訂正エラー |
| 12245 | 株式訂正注文 | システム状態.データがありません | システム状態レコードなし |
| 12246 | 株式訂正注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 12247 | 株式訂正注文 | システムが受付可能時間外です。 | システム状態.閉局 |
| 12290 | 株式訂正注文 | 注文処理中です | 注文処理中 |
| 12291 | 株式訂正注文 | 訂正中です。時間を置いてからお試し下さい。 | 訂正中 |
| 12292 | 株式訂正注文 | 取消中です | 取消中 |
| 12293 | 株式訂正注文 | 失効済みです | 失効済み |
| 12294 | 株式訂正注文 | 約定済みです | 約定済み |
| 12295 | 株式訂正注文 | 取消済みです | 取消済み |
| 12296 | 株式訂正注文 | トリガー発動済みです | トリガー発動済み |
| 12297 | 株式訂正注文 | 強制決済中ですので、この操作はできません | 強制決済中 |
| 12298 | 株式訂正注文 | 訂正数量に誤りがあります | 訂正数量エラー |
| 12299 | 株式訂正注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 12300 | 株式訂正注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 12301 | 株式訂正注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 12302 | 株式訂正注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 12303 | 株式訂正注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 12304 | 株式訂正注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 12305 | 株式訂正注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 12306 | 株式訂正注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 12307 | 株式訂正注文 | 口座管理.特定口座が未開設です | 口座管理.特定口座未開設 |
| 12308 | 株式訂正注文 | 口座管理.非課税口座が未開設です | 口座管理.非課税口座未開設 |
| 12309 | 株式訂正注文 | 口座管理.信用口座が未開設です | 口座管理.信用口座未開設 |
| 12311 | 株式訂正注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 12312 | 株式訂正注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 12313 | 株式訂正注文 | インサイダファイルに問題があります | インサイダファイル障害 |
| 12314 | 株式訂正注文 | 当該注文はインサイダー情報に基づく注文ではない同意が無い為受付できません | インサイダチェックエラー |
| 12315 | 株式訂正注文 | 特定投資家契約マスタファイルに問題があります | 特定投資家契約マスタファイル障害 |
| 12316 | 株式訂正注文 | 特定投資家契約マスタチェックでエラーが発生しました | 特定投資家契約マスタチェックエラー |
| 12317 | 株式訂正注文 | 金商法交付書面ファイルに問題があります | 金商法交付書面ファイル障害 |
| 12318 | 株式訂正注文 | 金商法交付書面(当日分)ファイルに問題があります | 金商法交付書面(当日分)ファイル障害 |
| 12319 | 株式訂正注文 | 金商法交付書面チェックでエラーが発生しました | 金商法交付書面チェックエラー |
| 12320 | 株式訂正注文 | 顧客銘柄別取引停止ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 12321 | 株式訂正注文 | 顧客銘柄別取引停止にデータがありません | 顧客銘柄別取引停止レコードなし |
| 12322 | 株式訂正注文 | お客様の当該銘柄における現物買付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物買付停止 |
| 12323 | 株式訂正注文 | お客様の当該銘柄における現物売付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物売付停止 |
| 12324 | 株式訂正注文 | お客様の当該銘柄における信用新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規買建停止 |
| 12325 | 株式訂正注文 | お客様の当該銘柄における信用新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規売建停止 |
| 12326 | 株式訂正注文 | お客様の当該銘柄における信用買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用買返済停止 |
| 12327 | 株式訂正注文 | お客様の当該銘柄における信用売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用売返済停止 |
| 12328 | 株式訂正注文 | お客様の当該銘柄における信用現引のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現引停止 |
| 12329 | 株式訂正注文 | お客様の当該銘柄における信用現渡のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現渡停止 |
| 12340 | 株式訂正注文 | 市場別特殊執行注文取扱停止ファイルに問題があります | 市場別特殊執行注文取扱停止ファイル障害 |
| 12341 | 株式訂正注文 | 当該市場での逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.逆指値停止 |
| 12342 | 株式訂正注文 | 当該市場での通常＋逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.通常＋逆指値停止 |
| 12343 | 株式訂正注文 | 商品別特殊執行注文取扱停止ファイルに問題があります | 商品別特殊執行注文取扱停止ファイル障害 |
| 12344 | 株式訂正注文 | 逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.逆指値停止 |
| 12345 | 株式訂正注文 | 通常＋逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.通常＋逆指値停止 |
| 12346 | 株式訂正注文 | 銘柄別特殊執行注文取扱停止ファイルに問題があります | 銘柄別特殊執行注文取扱停止ファイル障害 |
| 12347 | 株式訂正注文 | 当該銘柄は逆指値注文はできません | 銘柄別特殊執行注文取扱停止.逆指値停止 |
| 12348 | 株式訂正注文 | 当該銘柄は通常＋逆指値はできません | 銘柄別特殊執行注文取扱停止.通常＋逆指値停止 |
| 12349 | 株式訂正注文 | 当該銘柄は特殊執行注文はできません | 銘柄別特殊執行注文取扱停止.特殊執行注文不可 |
| 12350 | 株式訂正注文 | ハードリミット市場別ファイルに問題があります | ハードリミット市場別ファイル障害 |
| 12351 | 株式訂正注文 | ハードリミット市場別にデータがありません | ハードリミット市場別レコードなし |
| 12352 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合1 |
| 12353 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合2 |
| 12354 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合3 |
| 12355 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合4 |
| 12356 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合5 |
| 12360 | 株式訂正注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 12361 | 株式訂正注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 12362 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買上限 |
| 12363 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売上限 |
| 12364 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 12365 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 12366 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 12367 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 12368 | 株式訂正注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 12369 | 株式訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 12370 | 株式訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 12371 | 株式訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 12372 | 株式訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 12380 | 株式訂正注文 | 注文できません。個別ファイルに問題があります | ソフトリミット個別ファイル障害 |
| 12381 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買上限 |
| 12382 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売上限 |
| 12383 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 12384 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 12385 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 12386 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 12387 | 株式訂正注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 12388 | 株式訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 12389 | 株式訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 12390 | 株式訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 12391 | 株式訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 12400 | 株式訂正注文 | 注文できません。通常ファイルに問題があります | ソフトリミット通常ファイル障害 |
| 12401 | 株式訂正注文 | 注文できません。通常にデータがありません | ソフトリミット通常レコードなし |
| 12402 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買上限 |
| 12403 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売上限 |
| 12404 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 12405 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 12406 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 12407 | 株式訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 12408 | 株式訂正注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 12409 | 株式訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 12410 | 株式訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 12411 | 株式訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 12412 | 株式訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 12415 | 株式訂正注文 | 空売り注文はできません | 空売り規制(注文不可) |
| 12416 | 株式訂正注文 | 空売り注文は成行に訂正できません | 空売り規制(成行不可) |
| 12417 | 株式訂正注文 | 空売り期限付き注文はできません | 空売り規制(期限付き不可) |
| 12420 | 株式訂正注文 | 買付可能額が不足しています | 買付可能額不足 |
| 12421 | 株式訂正注文 | 売付可能株数が不足しているため、この後注文はお受けできません | 売付可能数量不足 |
| 12422 | 株式訂正注文 | 新規建余力は、%s 円です。ご注文に対して現金保証金が、%s 円不足しています。 | 信用新規建可能額不足 |
| 12423 | 株式訂正注文 | 現引可能額が不足しています | 現引可能額不足 |
| 12426 | 株式訂正注文 | この銘柄は日計りの対象となっているため、この訂正により、お預かり金が不足します。 | 売付可能数量不足 |
| 12428 | 株式訂正注文 | 増担保の現金必要保証金が不足します。 | 現金必要保証金不足 |
| 12429 | 株式訂正注文 | 信用新規建可能額が不足しています | 信用新規建可能額不足 |
| 12430 | 株式訂正注文 | 現在、この銘柄の買付可能額は、%s 円です。%s 円不足しているため、このご注文はお受けできません。(日計り取引銘柄等、銘柄によっては可能額の算出方法が異なるケースがあります。) | 買付可能額不足 |
| 12440 | 株式訂正注文 | 非課税口座管理ファイルに問題があります | 非課税口座管理ファイル障害 |
| 12441 | 株式訂正注文 | 非課税口座管理にデータがありません | 非課税口座管理レコードなし |
| 12442 | 株式訂正注文 | 非課税口座管理更新でエラーが発生しました | 非課税口座管理更新エラー |
| 12443 | 株式訂正注文 | 非課税口座可能額が不足しています | 非課税口座可能額不足 |
| 12450 | 株式訂正注文 | 顧客手数料ファイルに問題があります | 顧客手数料ファイル障害 |
| 12451 | 株式訂正注文 |  | 顧客手数料レコードなし |
| 12460 | 株式訂正注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 12461 | 株式訂正注文 |  | 手数料マスタレコードなし |
| 12470 | 株式訂正注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 12471 | 株式訂正注文 |  | 課税率マスタレコードなし |
| 12480 | 株式訂正注文 | 保管顧客課税別ファイルに問題があります | 保管顧客課税別ファイル障害 |
| 12481 | 株式訂正注文 | 選択した口座区分がお預かり銘柄と不一致のため、このご注文はお受けできません。 | 保管顧客課税別にデータがありません |
| 12482 | 株式訂正注文 | 売付可能な株数が不足しているため、このご注文はお受けできません。売却可能株数や注文一覧画面をご確認ください。 | 保管顧客課税別有効数量がありません |
| 12483 | 株式訂正注文 | 保管顧客課税別にデータ作成でエラーが発生しました | 保管顧客課税別レコード作成エラー |
| 12484 | 株式訂正注文 | 保管顧客課税別のデータ更新でエラーが発生しました | 保管顧客課税別レコード更新エラー |
| 12490 | 株式訂正注文 | 信用建玉明細ファイルに問題があります | 信用建玉明細ファイル障害 |
| 12491 | 株式訂正注文 | 信用建玉明細にデータがありません | 信用建玉明細レコードなし |
| 12492 | 株式訂正注文 | 信用建玉明細有効数量がありません | 信用建玉明細有効数量なし |
| 12493 | 株式訂正注文 | 信用建玉明細のデータ更新でエラーが発生しました | 信用建玉明細レコード更新エラー |
| 12494 | 株式訂正注文 | 信用建玉残ファイルに問題があります | 信用建玉残ファイル障害 |
| 12495 | 株式訂正注文 | 信用建玉残にデータがありません | 信用建玉残レコードなし |
| 12496 | 株式訂正注文 | 信用建玉残にデータ作成でエラーが発生しました | 信用建玉残レコード作成エラー |
| 12497 | 株式訂正注文 | 信用建玉残のデータ更新でエラーが発生しました | 信用建玉残レコード更新エラー |
| 12500 | 株式訂正注文 | 顧客金銭ファイルに問題があります | 顧客金銭ファイル障害 |
| 12501 | 株式訂正注文 | 顧客金銭にデータがありません | 顧客金銭レコードなし |
| 12502 | 株式訂正注文 | 顧客拘束金ファイルに問題があります | 顧客拘束金ファイル障害 |
| 12503 | 株式訂正注文 | 顧客拘束金にデータがありません | 顧客拘束金レコードなし |
| 12504 | 株式訂正注文 |  | 顧客拘束金レコードレコード作成エラー |
| 12505 | 株式訂正注文 |  | 顧客拘束金レコード更新エラー |
| 12509 | 株式訂正注文 | 保証金率取得でエラーが発生しました | 保証金率取得エラー |
| 12510 | 株式訂正注文 | 代用掛目ファイルに問題があります | 代用掛目ファイル障害 |
| 12511 | 株式訂正注文 | 日付情報ファイルに問題があります | 日付情報ファイル障害 |
| 12512 | 株式訂正注文 | 保管顧客別残ファイルに問題があります | 保管顧客別残ファイル障害 |
| 12513 | 株式訂正注文 | 保管顧客別残にデータがありません | 保管顧客別残レコードなし |
| 12514 | 株式訂正注文 | 保管顧客別残にデータ作成でエラーが発生しました | 保管顧客別残レコード作成エラー |
| 12515 | 株式訂正注文 | 保管顧客別残のデータ更新でエラーが発生しました | 保管顧客別残レコード更新エラー |
| 12516 | 株式訂正注文 | 保証金推移ファイルに問題があります | 保証金推移ファイル障害 |
| 12517 | 株式訂正注文 | 保証金推移にデータがありません | 保証金推移レコードなし |
| 12518 | 株式訂正注文 | 保証金推移にデータ作成でエラーが発生しました | 保証金推移レコード作成エラー |
| 12519 | 株式訂正注文 | 保証金推移のデータ更新でエラーが発生しました | 保証金推移レコード更新エラー |
| 12520 | 株式訂正注文 | 顧客当日取引情報ファイルに問題があります | 顧客当日取引情報ファイル障害 |
| 12521 | 株式訂正注文 | 顧客当日取引情報にデータがありません | 顧客当日取引情報レコードなし |
| 12522 | 株式訂正注文 | 顧客当日取引情報にデータ作成でエラーが発生しました | 顧客当日取引情報レコード作成エラー |
| 12523 | 株式訂正注文 | 顧客当日取引情報のデータ更新でエラーが発生しました | 顧客当日取引情報レコード更新エラー |
| 12524 | 株式訂正注文 | 差金決済管理明細ファイルに問題があります | 差金決済管理明細ファイル障害 |
| 12525 | 株式訂正注文 | 差金決済管理明細にデータがありません | 差金決済管理明細レコードなし |
| 12526 | 株式訂正注文 | 差金決済管理明細にデータ作成でエラーが発生しました | 差金決済管理明細レコード作成エラー |
| 12527 | 株式訂正注文 | 差金決済管理明細のデータ更新でエラーが発生しました | 差金決済管理明細レコード更新エラー |
| 12600 | 株式訂正注文 | 注文番号（株式）ファイルに問題があります | 注文番号（株式）ファイル障害 |
| 12601 | 株式訂正注文 | 注文番号（株式）にデータがありません | 注文番号（株式）レコードなし |
| 12602 | 株式訂正注文 | 建玉番号（株式）ファイルに問題があります | 建玉番号（株式）ファイル障害 |
| 12603 | 株式訂正注文 | 建玉番号（株式）にデータがありません | 建玉番号（株式）レコードなし |
| 12604 | 株式訂正注文 | 親注文株式サマリファイルに問題があります | 親注文株式サマリファイル障害 |
| 12605 | 株式訂正注文 | 親注文株式サマリにデータがありません | 親注文株式サマリレコードなし |
| 12606 | 株式訂正注文 | 親注文株式サマリ有効数量がありません | 親注文株式サマリ有効数量なし |
| 12607 | 株式訂正注文 | 親注文株式サマリ数量を超えています | 親注文株式サマリ数量オーバー |
| 12608 | 株式訂正注文 |  | 親注文株式サマリレコード更新エラー |
| 12609 | 株式訂正注文 | 株式サマリファイルに問題があります | 株式サマリファイル障害 |
| 12610 | 株式訂正注文 | 株式サマリにデータがありません | 株式サマリレコードなし |
| 12611 | 株式訂正注文 | 株式サマリにデータ作成でエラーが発生しました | 株式サマリレコード作成エラー |
| 12612 | 株式訂正注文 | 株式サマリのデータ更新でエラーが発生しました | 株式サマリレコード更新エラー |
| 12613 | 株式訂正注文 | 株式明細ファイルに問題があります | 株式明細ファイル障害 |
| 12614 | 株式訂正注文 | 株式明細にデータがありません | 株式明細レコードなし |
| 12615 | 株式訂正注文 | 株式明細更新でエラーが発生しました | 株式明細更新エラー |
| 12616 | 株式訂正注文 | 株式明細にデータ作成でエラーが発生しました | 株式明細レコード作成エラー |
| 12617 | 株式訂正注文 | 株式注文約定履歴ファイルに問題があります | 株式注文約定履歴ファイル障害 |
| 12618 | 株式訂正注文 | 株式注文約定履歴作成でエラーが発生しました | 株式注文約定履歴作成エラー |
| 12621 | 株式訂正注文 | 株式返済予約ファイルに問題があります | 株式返済予約ファイル障害 |
| 12622 | 株式訂正注文 | 株式返済予約にデータがありません | 株式返済予約レコードなし |
| 12623 | 株式訂正注文 | 株式返済予約にデータ作成でエラーが発生しました | 株式返済予約レコード作成エラー |
| 12624 | 株式訂正注文 | 株式返済予約のデータ更新でエラーが発生しました | 株式返済予約レコード更新エラー |
| 12625 | 株式訂正注文 | 株式返済明細ファイルに問題があります | 株式返済明細ファイル障害 |
| 12626 | 株式訂正注文 | 株式返済明細にデータがありません | 株式返済明細レコードなし |
| 12627 | 株式訂正注文 | 株式返済明細にデータ作成でエラーが発生しました | 株式返済明細レコード作成エラー |
| 12628 | 株式訂正注文 | 株式返済明細のデータ更新でエラーが発生しました | 株式返済明細レコード更新エラー |
| 12640 | 株式訂正注文 | 株式約定失効ファイルに問題があります | 株式約定失効ファイル障害 |
| 12641 | 株式訂正注文 | 株式約定失効にデータがありません | 株式約定失効レコードなし |
| 12642 | 株式訂正注文 | 株式約定失効にデータ作成でエラーが発生しました | 株式約定失効レコード作成エラー |
| 12643 | 株式訂正注文 | 株式約定失効のデータ更新でエラーが発生しました | 株式約定失効レコード更新エラー |
| 12645 | 株式訂正注文 | システム別設定ファイルに問題があります | システム別設定ファイル障害 |
| 12646 | 株式訂正注文 | 銘柄マスタ（株式）ファイルに問題があります | 銘柄マスタ（株式）ファイル障害 |
| 12647 | 株式訂正注文 | 銘柄市場マスタ（株式）ファイルに問題があります | 銘柄市場マスタ（株式）ファイル障害 |
| 12700 | 株式訂正注文 | 運用ステータス(申告)にデータがありません | 運用ステータス(申告)レコードなし |
| 12701 | 株式訂正注文 | 只今の時間帯は受付できません | 運用ステータス(申告).受付停止 |
| 12702 | 株式訂正注文 | 運用ステータス(連続注文)にデータがありません | 運用ステータス(連続注文)レコードなし |
| 12703 | 株式訂正注文 | 只今の時間帯は受付できません | 運用ステータス(連続注文).受付停止 |
| 12800 | 株式訂正注文 | 余力制御ファイルに問題があります | 余力制御ファイル障害 |
| 12802 | 株式訂正注文 | 余力制御.取引制限のため受付を停止しています | 余力制御.取引停止 |
| 12803 | 株式訂正注文 | 余力制御.取引制限のため信用新規建の受付を停止しています | 余力制御.信用新規建停止 |
| 12806 | 株式訂正注文 | 余力制御.取引制限のためその他商品買付の受付を停止しています | 余力制御.その他商品買付停止 |
| 12807 | 株式訂正注文 | 追証の未入金があるため受付できません | 余力制御.追証未入金あり |
| 12810 | 株式訂正注文 | 二階建チェックファイルに問題があります | 二階建チェックファイル障害 |
| 12811 | 株式訂正注文 | 二階建チェックでエラーが発生しました | 二階建チェックエラー |
| 12820 | 株式訂正注文 | 増担保ファイルに問題があります | 増担保ファイル障害 |
| 12821 | 株式訂正注文 | 規制銘柄新規建余力は、%s円です。ご注文に対して現金保証金が、%s円不足しています。 | 増担保現金チェックエラー |
| 12822 | 株式訂正注文 | 規制銘柄新規建余力は、%s円です。ご注文に対して現金保証金が、%s円不足しています。 | 増担保現金チェックエラー |
| 12823 | 株式訂正注文 | ご注文に対して現金保証金が不足しています。 | 増担保現金チェックエラー |
| 12824 | 株式訂正注文 | 規制銘柄新規建余力が不足しています。 | 増担保保証金チェックエラー |
| 12826 | 株式訂正注文 | 新規建余力は0円です。(最低保証金割れ) | 最低保証金割れエラー |
| 12830 | 株式訂正注文 | 一極集中ファイル障害 | 一極集中ファイル障害 |
| 12831 | 株式訂正注文 | 一極集中銘柄規制に抵触します。 | 一極集中チェックエラー |
| 12832 | 株式訂正注文 | 保証金率ファイル障害 | 保証金率ファイル障害 |
| 12833 | 株式訂正注文 | 当社運用規制の為、注文は受付られません | 保証金率チェックエラー |
| 12900 | 株式訂正注文 | 現物買付可能額取得でエラーが発生しました | 現物買付可能額取得エラー |
| 12901 | 株式訂正注文 | 差金決済売付可能数量取得でエラーが発生しました | 差金決済売付可能数量取得エラー |
| 12902 | 株式訂正注文 | 信用新規建可能額取得でエラーが発生しました | 信用新規建可能額取得エラー |
| 12903 | 株式訂正注文 | 現引可能額取得でエラーが発生しました | 現引可能額取得エラー |
| 12991 | 株式訂正注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 12992 | 株式訂正注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 12993 | 株式訂正注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 12994 | 株式訂正注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 12997 | 株式訂正注文 | ネットでエラーが発生しました | ネットエラー |
| 12998 | 株式訂正注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 12999 | 株式訂正注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 13001 | 株式取消注文 | 注文番号に誤りがあります | 注文番号不正 |
| 13002 | 株式取消注文 | 営業日に誤りがあります | 営業日不正 |
| 13018 | 株式取消注文 | 接続に誤りがあります | チャネル不正 |
| 13019 | 株式取消注文 | 接続詳細に誤りがあります | チャネル詳細不正 |
| 13020 | 株式取消注文 | オペレータに誤りがあります | オペレータ不正 |
| 13021 | 株式取消注文 | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 13022 | 株式取消注文 | 第二暗証番号省略フラグに誤りがあります | 第二暗証番号省略フラグ不正 |
| 13023 | 株式取消注文 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 13100 | 株式取消注文 | 株式サマリにデータがありません | 株式サマリレコードなし |
| 13120 | 株式取消注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 13122 | 株式取消注文 | 只今の時間帯は受付できません | 運用ステータス(注文).受付停止 |
| 13130 | 株式取消注文 | 日付情報にデータがありません | 日付情報レコードなし |
| 13199 | 株式取消注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 13200 | 株式取消注文 | このサービスは取り扱っておりません | サービス別取扱.現物取消取扱不可 |
| 13201 | 株式取消注文 | このサービスは取り扱っておりません | サービス別取扱.信用取消取扱不可 |
| 13245 | 株式取消注文 | システム状態にデータがありません | システム状態レコードなし |
| 13246 | 株式取消注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 13247 | 株式取消注文 | システムが受付可能時間外です。 | システム状態.閉局 |
| 13290 | 株式取消注文 | 注文処理中です。 | 注文処理中 |
| 13291 | 株式取消注文 | 訂正中です | 訂正中 |
| 13292 | 株式取消注文 | 取消中です | 取消中 |
| 13293 | 株式取消注文 | 失効済みです | 失効済み |
| 13294 | 株式取消注文 | 約定済みです | 約定済み |
| 13295 | 株式取消注文 | 取消済みです | 取消済み |
| 13296 | 株式取消注文 | トリガー発動済みです | トリガー発動済み |
| 13297 | 株式取消注文 | 強制決済中ですので、この操作はできません | 強制決済中 |
| 13299 | 株式取消注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 13300 | 株式取消注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 13301 | 株式取消注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 13302 | 株式取消注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 13303 | 株式取消注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 13304 | 株式取消注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 13305 | 株式取消注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 13306 | 株式取消注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 13307 | 株式取消注文 | 口座管理.特定口座が未開設です | 口座管理.特定口座未開設 |
| 13308 | 株式取消注文 | 口座管理.非課税口座が未開設です | 口座管理.非課税口座未開設 |
| 13309 | 株式取消注文 | 口座管理.信用口座が未開設です | 口座管理.信用口座未開設 |
| 13311 | 株式取消注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 13312 | 株式取消注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 13313 | 株式取消注文 | インサイダファイルに問題があります | インサイダファイル障害 |
| 13314 | 株式取消注文 | 当該注文はインサイダー情報に基づく注文ではない同意が無い為受付できません | インサイダチェックエラー |
| 13315 | 株式取消注文 | 特定投資家契約マスタファイルに問題があります | 特定投資家契約マスタファイル障害 |
| 13316 | 株式取消注文 | 特定投資家契約マスタチェックでエラーが発生しました | 特定投資家契約マスタチェックエラー |
| 13317 | 株式取消注文 | 金商法交付書面ファイルに問題があります | 金商法交付書面ファイル障害 |
| 13318 | 株式取消注文 | 金商法交付書面(当日分)ファイルに問題があります | 金商法交付書面(当日分)ファイル障害 |
| 13319 | 株式取消注文 | 金商法交付書面チェックでエラーが発生しました | 金商法交付書面チェックエラー |
| 13320 | 株式取消注文 | 顧客銘柄別取引停止ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 13321 | 株式取消注文 | 顧客銘柄別取引停止にデータがありません | 顧客銘柄別取引停止レコードなし |
| 13322 | 株式取消注文 | お客様の当該銘柄における現物買付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物買付停止 |
| 13323 | 株式取消注文 | お客様の当該銘柄における現物売付のお取引を停止させていただいております | 顧客銘柄別取引停止.現物売付停止 |
| 13324 | 株式取消注文 | お客様の当該銘柄における信用新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規買建停止 |
| 13325 | 株式取消注文 | お客様の当該銘柄における信用新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.信用新規売建停止 |
| 13326 | 株式取消注文 | お客様の当該銘柄における信用買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用買返済停止 |
| 13327 | 株式取消注文 | お客様の当該銘柄における信用売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.信用売返済停止 |
| 13328 | 株式取消注文 | お客様の当該銘柄における信用現引のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現引停止 |
| 13329 | 株式取消注文 | お客様の当該銘柄における信用現渡のお取引を停止させていただいております | 顧客銘柄別取引停止.信用現渡停止 |
| 13340 | 株式取消注文 | 市場別特殊執行注文取扱停止ファイルに問題があります | 市場別特殊執行注文取扱停止ファイル障害 |
| 13341 | 株式取消注文 | 当該市場での逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.逆指値停止 |
| 13342 | 株式取消注文 | 当該市場での通常＋逆指値注文の受付を停止しています | 市場別特殊執行注文取扱停止.通常＋逆指値停止 |
| 13343 | 株式取消注文 | 商品別特殊執行注文取扱停止ファイルに問題があります | 商品別特殊執行注文取扱停止ファイル障害 |
| 13344 | 株式取消注文 | 逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.逆指値停止 |
| 13345 | 株式取消注文 | 通常＋逆指値注文の受付を停止しています | 商品別特殊執行注文取扱停止.通常＋逆指値停止 |
| 13346 | 株式取消注文 | 銘柄別特殊執行注文取扱停止ファイルに問題があります | 銘柄別特殊執行注文取扱停止ファイル障害 |
| 13347 | 株式取消注文 | 当該銘柄は逆指値注文はできません | 銘柄別特殊執行注文取扱停止.逆指値停止 |
| 13348 | 株式取消注文 | 当該銘柄は通常＋逆指値はできません | 銘柄別特殊執行注文取扱停止.通常＋逆指値停止 |
| 13349 | 株式取消注文 | 当該銘柄は特殊執行注文はできません | 銘柄別特殊執行注文取扱停止.特殊執行注文不可 |
| 13350 | 株式取消注文 | ハードリミット市場別ファイルに問題があります | ハードリミット市場別ファイル障害 |
| 13351 | 株式取消注文 | ハードリミット市場別にデータがありません | ハードリミット市場別レコードなし |
| 13352 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合1 |
| 13353 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合2 |
| 13354 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合3 |
| 13355 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合4 |
| 13356 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット市場別.発注割合5 |
| 13360 | 株式取消注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 13361 | 株式取消注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 13362 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買上限 |
| 13363 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売上限 |
| 13364 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 13365 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 13366 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 13367 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 13368 | 株式取消注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 13369 | 株式取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 13370 | 株式取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 13371 | 株式取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 13372 | 株式取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 13380 | 株式取消注文 | 注文できません。個別ファイルに問題があります | ソフトリミット個別ファイル障害 |
| 13381 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買上限 |
| 13382 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売上限 |
| 13383 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 13384 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 13385 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 13386 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 13387 | 株式取消注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 13388 | 株式取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 13389 | 株式取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 13390 | 株式取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 13391 | 株式取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 13400 | 株式取消注文 | 注文できません。通常ファイルに問題があります | ソフトリミット通常ファイル障害 |
| 13401 | 株式取消注文 | 注文できません。通常にデータがありません | ソフトリミット通常レコードなし |
| 13402 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買上限 |
| 13403 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売上限 |
| 13404 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 13405 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 13406 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 13407 | 株式取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 13408 | 株式取消注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 13409 | 株式取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 13410 | 株式取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 13411 | 株式取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 13412 | 株式取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 13415 | 株式取消注文 | 空売り注文はできません | 空売り規制(注文不可) |
| 13416 | 株式取消注文 | 空売り成行注文はできません | 空売り規制(成行不可) |
| 13417 | 株式取消注文 | 空売り期限付き注文はできません | 空売り規制(期限付き不可) |
| 13420 | 株式取消注文 | 買付可能額が不足しています | 買付可能額不足 |
| 13421 | 株式取消注文 | 売付可能数量が不足しています | 売付可能数量不足 |
| 13422 | 株式取消注文 | 信用新規建可能額が不足しています | 信用新規建可能額不足 |
| 13423 | 株式取消注文 | 現引可能額が不足しています | 現引可能額不足 |
| 13440 | 株式取消注文 | 非課税口座管理ファイルに問題があります | 非課税口座管理ファイル障害 |
| 13441 | 株式取消注文 | 非課税口座管理にデータがありません | 非課税口座管理レコードなし |
| 13442 | 株式取消注文 | 非課税口座管理更新でエラーが発生しました | 非課税口座管理更新エラー |
| 13443 | 株式取消注文 | 非課税口座可能額が不足しています | 非課税口座可能額不足 |
| 13450 | 株式取消注文 | 顧客手数料ファイルに問題があります | 顧客手数料ファイル障害 |
| 13451 | 株式取消注文 |  | 顧客手数料レコードなし |
| 13460 | 株式取消注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 13461 | 株式取消注文 |  | 手数料マスタレコードなし |
| 13470 | 株式取消注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 13471 | 株式取消注文 |  | 課税率マスタレコードなし |
| 13480 | 株式取消注文 | 保管顧客課税別ファイルに問題があります | 保管顧客課税別ファイル障害 |
| 13481 | 株式取消注文 | 選択した口座区分がお預かり銘柄と不一致のため、このご注文はお受けできません。 | 保管顧客課税別有効数量がありません |
| 13482 | 株式取消注文 | 売り超過になります。取消できません。 | 保管顧客課税別有効数量なし |
| 13483 | 株式取消注文 | 保管顧客課税別にデータ作成でエラーが発生しました | 保管顧客課税別レコード作成エラー |
| 13484 | 株式取消注文 | 保管顧客課税別のデータ更新でエラーが発生しました | 保管顧客課税別レコード更新エラー |
| 13490 | 株式取消注文 | 信用建玉明細ファイルに問題があります | 信用建玉明細ファイル障害 |
| 13491 | 株式取消注文 | 信用建玉明細にデータがありません | 信用建玉明細レコードなし |
| 13492 | 株式取消注文 | 信用建玉明細有効数量がありません | 信用建玉明細有効数量なし |
| 13493 | 株式取消注文 | 信用建玉明細のデータ更新でエラーが発生しました | 信用建玉明細レコード更新エラー |
| 13494 | 株式取消注文 | 信用建玉残ファイルに問題があります | 信用建玉残ファイル障害 |
| 13495 | 株式取消注文 | 信用建玉残にデータがありません | 信用建玉残レコードなし |
| 13496 | 株式取消注文 | 信用建玉残にデータ作成でエラーが発生しました | 信用建玉残レコード作成エラー |
| 13497 | 株式取消注文 | 信用建玉残のデータ更新でエラーが発生しました | 信用建玉残レコード更新エラー |
| 13500 | 株式取消注文 | 顧客金銭ファイルに問題があります | 顧客金銭ファイル障害 |
| 13501 | 株式取消注文 | 顧客金銭にデータがありません | 顧客金銭レコードなし |
| 13502 | 株式取消注文 | 顧客拘束金ファイルに問題があります | 顧客拘束金ファイル障害 |
| 13503 | 株式取消注文 | 顧客拘束金にデータがありません | 顧客拘束金レコードなし |
| 13504 | 株式取消注文 |  | 顧客拘束金レコードレコード作成エラー |
| 13505 | 株式取消注文 |  | 顧客拘束金レコード更新エラー |
| 13509 | 株式取消注文 | 保証金率取得でエラーが発生しました | 保証金率取得エラー |
| 13510 | 株式取消注文 | 代用掛目ファイルに問題があります | 代用掛目ファイル障害 |
| 13511 | 株式取消注文 | 日付情報ファイルに問題があります | 日付情報ファイル障害 |
| 13512 | 株式取消注文 | 保管顧客別残ファイルに問題があります | 保管顧客別残ファイル障害 |
| 13513 | 株式取消注文 | 保管顧客別残にデータがありません | 保管顧客別残レコードなし |
| 13514 | 株式取消注文 | 保管顧客別残にデータ作成でエラーが発生しました | 保管顧客別残レコード作成エラー |
| 13515 | 株式取消注文 | 保管顧客別残のデータ更新でエラーが発生しました | 保管顧客別残レコード更新エラー |
| 13516 | 株式取消注文 | 保証金推移ファイルに問題があります | 保証金推移ファイル障害 |
| 13517 | 株式取消注文 | 保証金推移にデータがありません | 保証金推移レコードなし |
| 13518 | 株式取消注文 | 保証金推移にデータ作成でエラーが発生しました | 保証金推移レコード作成エラー |
| 13519 | 株式取消注文 | 保証金推移のデータ更新でエラーが発生しました | 保証金推移レコード更新エラー |
| 13520 | 株式取消注文 | 顧客当日取引情報ファイルに問題があります | 顧客当日取引情報ファイル障害 |
| 13521 | 株式取消注文 | 顧客当日取引情報にデータがありません | 顧客当日取引情報レコードなし |
| 13522 | 株式取消注文 | 顧客当日取引情報にデータ作成でエラーが発生しました | 顧客当日取引情報レコード作成エラー |
| 13523 | 株式取消注文 | 顧客当日取引情報のデータ更新でエラーが発生しました | 顧客当日取引情報レコード更新エラー |
| 13524 | 株式取消注文 | 差金決済管理明細ファイルに問題があります | 差金決済管理明細ファイル障害 |
| 13525 | 株式取消注文 | 差金決済管理明細にデータがありません | 差金決済管理明細レコードなし |
| 13526 | 株式取消注文 | 差金決済管理明細にデータ作成でエラーが発生しました | 差金決済管理明細レコード作成エラー |
| 13527 | 株式取消注文 | 差金決済管理明細のデータ更新でエラーが発生しました | 差金決済管理明細レコード更新エラー |
| 13530 | 株式取消注文 | 譲渡益台帳ファイルに問題が発生しました | 譲渡益台帳ファイル障害 |
| 13531 | 株式取消注文 | 譲渡益台帳レコードがありません | 譲渡益台帳レコードなし |
| 13532 | 株式取消注文 | 譲渡益台帳レコード作成でエラーが発生しました | 譲渡益台帳レコード作成エラー |
| 13534 | 株式取消注文 | 譲渡益台帳レコード更新でエラーが発生しました | 譲渡益台帳レコード更新エラー |
| 13600 | 株式取消注文 | 注文番号（株式）ファイルに問題があります | 注文番号（株式）ファイル障害 |
| 13601 | 株式取消注文 | 注文番号（株式）にデータがありません | 注文番号（株式）レコードなし |
| 13602 | 株式取消注文 | 建玉番号（株式）ファイルに問題があります | 建玉番号（株式）ファイル障害 |
| 13603 | 株式取消注文 | 建玉番号（株式）にデータがありません | 建玉番号（株式）レコードなし |
| 13604 | 株式取消注文 | 親注文株式サマリファイルに問題があります | 親注文株式サマリファイル障害 |
| 13605 | 株式取消注文 | 親注文株式サマリにデータがありません | 親注文株式サマリレコードなし |
| 13606 | 株式取消注文 | 親注文株式サマリ有効数量がありません | 親注文株式サマリ有効数量なし |
| 13607 | 株式取消注文 | 親注文株式サマリ数量を超えています | 親注文株式サマリ数量オーバー |
| 13608 | 株式取消注文 |  | 親注文株式サマリレコード更新エラー |
| 13609 | 株式取消注文 | 株式サマリファイルに問題があります | 株式サマリファイル障害 |
| 13610 | 株式取消注文 | 株式サマリにデータがありません | 株式サマリレコードなし |
| 13611 | 株式取消注文 | 株式サマリにデータ作成でエラーが発生しました | 株式サマリレコード作成エラー |
| 13612 | 株式取消注文 | 株式サマリのデータ更新でエラーが発生しました | 株式サマリレコード更新エラー |
| 13613 | 株式取消注文 | 株式明細ファイルに問題があります | 株式明細ファイル障害 |
| 13614 | 株式取消注文 | 株式明細にデータがありません | 株式明細レコードなし |
| 13615 | 株式取消注文 | 株式明細更新でエラーが発生しました | 株式明細更新エラー |
| 13616 | 株式取消注文 | 株式明細にデータ作成でエラーが発生しました | 株式明細レコード作成エラー |
| 13617 | 株式取消注文 | 株式注文約定履歴ファイルに問題があります | 株式注文約定履歴ファイル障害 |
| 13618 | 株式取消注文 | 株式注文約定履歴作成でエラーが発生しました | 株式注文約定履歴作成エラー |
| 13621 | 株式取消注文 | 株式返済予約ファイルに問題があります | 株式返済予約ファイル障害 |
| 13622 | 株式取消注文 | 株式返済予約にデータがありません | 株式返済予約レコードなし |
| 13623 | 株式取消注文 | 株式返済予約にデータ作成でエラーが発生しました | 株式返済予約レコード作成エラー |
| 13624 | 株式取消注文 | 株式返済予約のデータ更新でエラーが発生しました | 株式返済予約レコード更新エラー |
| 13625 | 株式取消注文 | 株式返済明細ファイルに問題があります | 株式返済明細ファイル障害 |
| 13626 | 株式取消注文 | 株式返済明細にデータがありません | 株式返済明細レコードなし |
| 13627 | 株式取消注文 | 株式返済明細にデータ作成でエラーが発生しました | 株式返済明細レコード作成エラー |
| 13628 | 株式取消注文 | 株式返済明細のデータ更新でエラーが発生しました | 株式返済明細レコード更新エラー |
| 13640 | 株式取消注文 | 株式約定失効ファイルに問題があります | 株式約定失効ファイル障害 |
| 13641 | 株式取消注文 | 株式約定失効にデータがありません | 株式約定失効レコードなし |
| 13642 | 株式取消注文 | 株式約定失効にデータ作成でエラーが発生しました | 株式約定失効レコード作成エラー |
| 13643 | 株式取消注文 | 株式約定失効のデータ更新でエラーが発生しました | 株式約定失効レコード更新エラー |
| 13645 | 株式取消注文 | システム別設定ファイルに問題があります | システム別設定ファイル障害 |
| 13646 | 株式取消注文 | 銘柄マスタ（株式）ファイルに問題があります | 銘柄マスタ（株式）ファイル障害 |
| 13647 | 株式取消注文 | 銘柄市場マスタ（株式）ファイルに問題があります | 銘柄市場マスタ（株式）ファイル障害 |
| 13700 | 株式取消注文 | 運用ステータス(申告)にデータがありません | 運用ステータス(申告)レコードなし |
| 13701 | 株式取消注文 | 只今の時間帯は受付できません | 運用ステータス(申告).受付停止 |
| 13702 | 株式取消注文 | 運用ステータス(連続注文)にデータがありません | 運用ステータス(連続注文)レコードなし |
| 13703 | 株式取消注文 | 只今の時間帯は受付できません | 運用ステータス(連続注文).受付停止 |
| 13800 | 株式取消注文 | 余力制御ファイルに問題があります | 余力制御ファイル障害 |
| 13802 | 株式取消注文 | 余力制御.取引停止 | 余力制御.取引停止 |
| 13803 | 株式取消注文 | 余力制御.信用新規建停止 | 余力制御.信用新規建停止 |
| 13806 | 株式取消注文 | 余力制御.その他商品買付停止 | 余力制御.その他商品買付停止 |
| 13807 | 株式取消注文 | 追証の未入金があります | 余力制御.追証未入金あり |
| 13991 | 株式取消注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 13992 | 株式取消注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 13993 | 株式取消注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 13994 | 株式取消注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 13997 | 株式取消注文 | ネットワークでエラーが発生しました | ネットエラー |
| 13998 | 株式取消注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 13999 | 株式取消注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 14001 | IPO新規申込 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 14002 | IPO新規申込 | 指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | IPO銘柄マスタに存在しない |
| 14003 | IPO新規申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 申込入力期間外 |
| 14004 | IPO新規申込 | 申告価格をお間違えです。ご確認の上改めてご入力下さい。 | 申込値段区分不正 |
| 14005 | IPO新規申込 | 入力された銘柄は現在、成行規制中となっております。 | 成行禁止 |
| 14006 | IPO新規申込 | 申告価格が仮条件を超えています。ご確認の上改めてご入力下さい。 | 値幅エラー |
| 14007 | IPO新規申込 | 申込価格欄に、数字以外の文字が入力されています。半角数字でご入力下さい。 | 申込値段不正 |
| 14008 | IPO新規申込 | 申告価格の単位をお間違えです。ご確認の上改めてご入力下さい。 | 呼値エラー |
| 14009 | IPO新規申込 | 申込数量欄に、数字以外の文字が入力されています。半角数字でご入力下さい。 | 申込数量不正 |
| 14010 | IPO新規申込 | 申告数量の単位をお間違えです。数量をご確認下さい。 | 申込単位不正 |
| 14011 | IPO新規申込 | ブックビルディングの重複申込はお受けできません。申告価格・数量を変更する場合は、訂正画面からご入力下さい。 | 申込重複 |
| 14012 | IPO新規申込 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 14013 | IPO新規申込 | 成行(ストライク・プライス)を指定されていますが、注文単価も入力されています。指値の場合は「指値」に印をつけてください。 | 成行で指値 |
| 14030 | IPO新規申込 | インサイダー取引に抵触する可能性があります。 | インサイダー取引 |
| 14031 | IPO新規申込 | 目論見書電子交付未済です。 | 目論見書不正 |
| 14090 | IPO新規申込 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 14091 | IPO新規申込 | システムが受付可能時間外です。 | システム停止 |
| 14092 | IPO新規申込 | システムが受付可能時間外です。 | 業務停止 |
| 14093 | IPO新規申込 | システムが緊急停止中です。 | 日時取得エラー |
| 14094 | IPO新規申込 | システムが緊急停止中です。 | 注文番号取得エラー |
| 14101 | IPO新規申込 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 14102 | IPO新規申込 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 14994 | IPO新規申込 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 14997 | IPO新規申込 | システムが緊急停止中です。 | ネットエラー |
| 14998 | IPO新規申込 | システムが緊急停止中です。 | ＤＢエラー |
| 14999 | IPO新規申込 | システムが緊急停止中です。 | タイムアウト |
| 15001 | IPO訂正申込 | 申告価格をお間違えです。ご確認の上改めてご入力下さい。 | 注文値段訂正フラグ不正 |
| 15002 | IPO訂正申込 | 申告価格をお間違えです。ご確認の上改めてご入力下さい。 | 注文値段区分不正 |
| 15003 | IPO訂正申込 | 申告価格をお間違えです。ご確認の上改めてご入力下さい。 | ％指定に成行を指定した |
| 15004 | IPO訂正申込 | 入力された銘柄は現在、成行規制中となっております。 | 成行禁止 |
| 15005 | IPO訂正申込 | 申告価格が仮条件を超えています。ご確認の上改めてご入力下さい。 | 値幅エラー |
| 15006 | IPO訂正申込 | 申込価格欄に、数字以外の文字が入力されています。半角数字でご入力下さい。 | 指値不正 |
| 15007 | IPO訂正申込 | 申告価格の単位をお間違えです。ご確認の上改めてご入力下さい。 | 呼値エラー |
| 15008 | IPO訂正申込 | 申告価格をお間違えです。ご確認の上改めてご入力下さい。 | 注文数量訂正フラグ不正 |
| 15009 | IPO訂正申込 | 申告数量の単位をお間違えです。数量をご確認下さい。 | 注文数量不正 |
| 15010 | IPO訂正申込 | 申告数量の単位をお間違えです。数量をご確認下さい。 | 単位数量エラー |
| 15011 | IPO訂正申込 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 15012 | IPO訂正申込 | 成行(ストライク・プライス)を指定されていますが、注文単価も入力されています。指値の場合は「指値」に印をつけてください。 | 成行で指値 |
| 15030 | IPO訂正申込 | 顧客登録番号が間違っています | 顧客登録Ｎ不一致 |
| 15040 | IPO訂正申込 | いずれの項目も訂正されておりません。訂正内容をご確認下さい。 | 変更項目なし |
| 15050 | IPO訂正申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 有効な申し込みが存在しない |
| 15051 | IPO訂正申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 当選済み |
| 15052 | IPO訂正申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 申込入力期間外 |
| 15090 | IPO訂正申込 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 15091 | IPO訂正申込 | システムが受付可能時間外です。 | システム停止 |
| 15092 | IPO訂正申込 | システムが受付可能時間外です。 | 業務停止 |
| 15094 | IPO訂正申込 | システムが緊急停止中です。 | 注文番号取得エラー |
| 15095 | IPO訂正申込 | システムが緊急停止中です。 | IPO銘柄マスタ取得エラー |
| 15101 | IPO訂正申込 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 15102 | IPO訂正申込 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 15994 | IPO新規申込 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 15997 | IPO訂正申込 | システムが緊急停止中です。 | ネットエラー |
| 15998 | IPO訂正申込 | システムが緊急停止中です。 | ＤＢエラー |
| 15999 | IPO訂正申込 | システムが緊急停止中です。 | タイムアウト |
| 16011 | IPO取消申込 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 16030 | IPO取消申込 | 顧客登録番号が間違っています | 顧客登録Ｎ不一致 |
| 16050 | IPO取消申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 有効な申し込みが存在しない |
| 16051 | IPO取消申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 当選済み |
| 16052 | IPO取消申込 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 申込入力期間外 |
| 16090 | IPO取消申込 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 16091 | IPO取消申込 | システムが受付可能時間外です。 | システム停止 |
| 16092 | IPO取消申込 | システムが受付可能時間外です。 | 業務停止 |
| 16095 | IPO取消申込 | システムが緊急停止中です。 | IPO銘柄マスタ取得エラー |
| 16101 | IPO取消申込 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 16102 | IPO取消申込 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 16994 | IPO取消申込 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 16997 | IPO取消申込 | システムが緊急停止中です。 | ネットエラー |
| 16998 | IPO取消申込 | システムが緊急停止中です。 | ＤＢエラー |
| 16999 | IPO取消申込 | システムが緊急停止中です。 | タイムアウト |
| 17011 | IPO申告辞退 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 17030 | IPO申告辞退 | 顧客登録番号が間違っています | 顧客登録Ｎ不一致 |
| 17050 | IPO申告辞退 | 現在、こちらの銘柄のブックビルディングは受付停止中です。 | 有効な申し込みが存在しない |
| 17051 | IPO申告辞退 | この銘柄のブックビルディングお申し込みは、誠に残念ながら落選となりました。 | 当選していない |
| 17052 | IPO申告辞退 | 現在は購入/辞退受付期間ではありません。受付期間をご確認下さい。 | 購入/辞退申込期間外 |
| 17090 | IPO申告辞退 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 17091 | IPO申告辞退 | システムが受付可能時間外です。 | システム停止 |
| 17092 | IPO申告辞退 | システムが受付可能時間外です。 | 業務停止 |
| 17093 | IPO申告辞退 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 17095 | IPO申告辞退 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | IPO銘柄マスタ取得エラー |
| 17099 | IPO申告辞退 | システムが緊急停止中です。 | IPO拘束金の解放に失敗 |
| 17101 | IPO申告辞退 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 17102 | IPO申告辞退 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 17994 | IPO申告辞退 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 17997 | IPO申告辞退 | システムが緊急停止中です。 | ネットエラー |
| 17998 | IPO申告辞退 | システムが緊急停止中です。 | ＤＢエラー |
| 17999 | IPO申告辞退 | システムが緊急停止中です。 | タイムアウト |
| 18001 | 株式 | 当該注文は、インサイダー情報（非公開の重要事実）に基づく注文ではございません。 | インサイダー |
| 18002 | 株式 | もうすぐ本日の取引が終了します。 | 市場閉局警告表示 |
| 18003 | 株式 | 当該銘柄は上場廃止が決定しました。 | 上場廃止 |
| 19000 | 概算簿価単価変更 | 概算簿価単価の登録は完了しました。 | 概算簿価単価登録完了 |
| 19001 | 概算簿価単価変更 | 変更後概算簿価単価がに誤りがありますな値になっています。 | 概算簿価単価不正 |
| 19997 | 概算簿価単価変更 | ネットでエラーが発生しました | ネットエラー |
| 19998 | 概算簿価単価変更 | ＤＢでエラーが発生しました | ＤＢエラー |
| 19999 | 概算簿価単価変更 | タイムアウトしました | タイムアウト |
| 21001 | 派生新規注文 | 営業日に誤りがあります | 営業日不正 |
| 21002 | 派生新規注文 | 注文種別に誤りがあります | 注文種別不正 |
| 21003 | 派生新規注文 | 親注文番号に誤りがあります | 親注文番号不正 |
| 21004 | 派生新規注文 | システム口座区分に誤りがあります | システム口座区分不正 |
| 21005 | 派生新規注文 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 21006 | 派生新規注文 | 商品種別に誤りがあります | 商品種別不正 |
| 21007 | 派生新規注文 | 銘柄コードに誤りがあります | 銘柄コード不正 |
| 21008 | 派生新規注文 | 売買区分に誤りがあります | 売買区分不正 |
| 21009 | 派生新規注文 | 執行条件に誤りがあります | 執行条件不正 |
| 21010 | 派生新規注文 | 執行数量条件に誤りがあります | 執行数量条件不正 |
| 21011 | 派生新規注文 | 注文値段区分に誤りがあります | 注文値段区分不正 |
| 21012 | 派生新規注文 | 注文値段に誤りがあります | 注文値段不正 |
| 21013 | 派生新規注文 | 注文数量に誤りがあります | 注文数量不正 |
| 21014 | 派生新規注文 | 取引区分に誤りがあります | 取引区分不正 |
| 21015 | 派生新規注文 | 注文期日に誤りがあります | 注文期日不正 |
| 21016 | 派生新規注文 | 逆指値注文種別に誤りがあります | 逆指値注文種別不正 |
| 21017 | 派生新規注文 | 逆指値条件に誤りがあります | 逆指値条件不正 |
| 21018 | 派生新規注文 | 逆指値値段区分に誤りがあります | 逆指値値段区分不正 |
| 21019 | 派生新規注文 | 逆指値値段に誤りがあります | 逆指値値段不正 |
| 21020 | 派生新規注文 | 接続に誤りがあります | チャネル不正 |
| 21021 | 派生新規注文 | 接続詳細に誤りがあります | チャネル詳細不正 |
| 21022 | 派生新規注文 | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 21023 | 派生新規注文 | 建日種類に誤りがあります | 建日種類不正 |
| 21024 | 派生新規注文 | 建玉番号に誤りがあります | 建玉番号不正 |
| 21025 | 派生新規注文 | 建玉順位に誤りがあります | 建玉順位不正 |
| 21026 | 派生新規注文 | 建玉数量に誤りがあります | 建玉数量不正 |
| 21027 | 派生新規注文 | 返済数量に誤りがあります | 返済数量不正 |
| 21028 | 派生新規注文 | 不成注文に成行が指定されています | 不成注文に成行が指定されている |
| 21029 | 派生新規注文 | 期限付き注文に執行条件が指定されています | 期限付き注文に執行条件が指定されている |
| 21030 | 派生新規注文 |  | 逆指値注文の執行条件指定が不正 |
| 21031 | 派生新規注文 |  | 逆指値注文の執行条件指定が不正 |
| 21032 | 派生新規注文 | 子注文に執行条件が指定されています | 子注文に執行条件が指定されている |
| 21033 | 派生新規注文 | 子注文に注文期限が指定されています | 子注文に注文期限が指定されている |
| 21034 | 派生新規注文 | ｢成行｣を指定されていますが、注文単価も入力されています。指値の場合は｢指値｣に印を付けて下さい。 | 成行指値同時指定 |
| 21100 | 派生新規注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 21101 | 派生新規注文 | 運用ステータス(採用値幅)にデータがありません | 運用ステータス(採用値幅)レコードなし |
| 21102 | 派生新規注文 | 只今の時間帯は受付できません | 運用ステータス.受付停止中 |
| 21103 | 派生新規注文 | 日付情報にデータがありません | 日付情報レコードなし |
| 21104 | 派生新規注文 | 先物銘柄マスタにデータがありません | 先物銘柄マスタレコードなし |
| 21105 | 派生新規注文 | オプション銘柄マスタにデータがありません | オプション銘柄マスタレコードなし |
| 21106 | 派生新規注文 | 当該銘柄は市場に直接お取り次ぎすることができません | 銘柄マスタ.場伝票出力有無エラー |
| 21107 | 派生新規注文 | 当該銘柄は取引開始前です | 銘柄マスタ.取引開始日エラー |
| 21108 | 派生新規注文 | 当該銘柄は取引を終了しています | 銘柄マスタ.最終売買日エラー |
| 21109 | 派生新規注文 | 当該銘柄の売買単位の整数倍の数量を入力してください | 銘柄マスタ.売買単位エラー |
| 21110 | 派生新規注文 | 当該銘柄の値幅制限内の単価を入力してください | 値幅エラー |
| 21111 | 派生新規注文 | 呼値にデータがありません | 呼値レコードなし |
| 21112 | 派生新規注文 | 正しい呼値の単位で単価を入力してください | 呼値エラー |
| 21113 | 派生新規注文 | 派生商品マスタにデータがありません | 派生商品マスタレコードなし |
| 21114 | 派生新規注文 | 注文期日でエラーが発生しました | 注文期日エラー |
| 21115 | 派生新規注文 | 逆指条件値幅でエラーが発生しました | 逆指条件値幅エラー |
| 21116 | 派生新規注文 | 逆指条件呼値にデータがありません | 逆指条件呼値レコードなし |
| 21117 | 派生新規注文 | 逆指条件呼値でエラーが発生しました | 逆指条件呼値エラー |
| 21118 | 派生新規注文 | システム別設定にデータがありません | システム別設定レコードなし |
| 21119 | 派生新規注文 | このサービスは取り扱っておりません | システム別設定.先物未実施 |
| 21120 | 派生新規注文 | このサービスは取り扱っておりません | システム別設定.オプション未実施 |
| 21121 | 派生新規注文 | 市場別設定にデータがありません | 市場別設定レコードなし |
| 21122 | 派生新規注文 | 当該市場ではお取引できません | 市場別設定.取引不可 |
| 21123 | 派生新規注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 21124 | 派生新規注文 | このサービスは取り扱っておりません | サービス別取扱.先物新規取扱不可 |
| 21125 | 派生新規注文 | このサービスは取り扱っておりません | サービス別取扱.先物返済取扱不可 |
| 21126 | 派生新規注文 | このサービスは取り扱っておりません | サービス別取扱.オプション新規取扱不可 |
| 21127 | 派生新規注文 | このサービスは取り扱っておりません | サービス別取扱.オプション返済取扱不可 |
| 21128 | 派生新規注文 | 商品市場別設定にデータがありません | 商品市場別設定レコードなし |
| 21129 | 派生新規注文 | 買建成行注文はできません | 商品市場別設定.成行買建不可 |
| 21130 | 派生新規注文 | 売建成行注文はできません | 商品市場別設定.成行売建不可 |
| 21131 | 派生新規注文 | 返済成行注文はできません | 商品市場別設定.成行返済不可 |
| 21132 | 派生新規注文 | 寄付注文はできません | 商品市場別設定.執行条件寄付不可 |
| 21133 | 派生新規注文 | 引け注文はできません | 商品市場別設定.執行条件引け不可 |
| 21134 | 派生新規注文 | 不成注文はできません | 商品市場別設定.執行条件不成不可 |
| 21135 | 派生新規注文 | 連続注文はできません | 商品市場別設定.連続注文不可 |
| 21136 | 派生新規注文 | 出来るまで注文はできません | 商品市場別設定.出来るまで注文不可 |
| 21137 | 派生新規注文 | 当該銘柄はお取引できません | 銘柄別市場別規制.停止区分取引禁止 |
| 21138 | 派生新規注文 | 当該銘柄の成行注文はできません | 銘柄別市場別規制.停止区分成行禁止 |
| 21139 | 派生新規注文 | 当該銘柄の新規買建の注文はできません | 銘柄別市場別規制.買建取引禁止 |
| 21140 | 派生新規注文 | 当該銘柄の新規買建の成行注文はできません | 銘柄別市場別規制.買建成行禁止 |
| 21141 | 派生新規注文 | 当該銘柄の新規売建注文はできません | 銘柄別市場別規制.売建取引禁止 |
| 21142 | 派生新規注文 | 当該銘柄の新規売建の成行注文はできません | 銘柄別市場別規制.売建成行禁止 |
| 21143 | 派生新規注文 | 当該銘柄の買返済注文はできません | 銘柄別市場別規制.買返済取引禁止 |
| 21144 | 派生新規注文 | 当該銘柄の買返済の成行注文はできません | 銘柄別市場別規制.買返済成行禁止 |
| 21145 | 派生新規注文 | 当該銘柄の売返済注文はできません | 銘柄別市場別規制.売返済取引禁止 |
| 21146 | 派生新規注文 | 当該銘柄の売返済の成行注文はできません | 銘柄別市場別規制.売返済成行禁止 |
| 21225 | 派生新規注文 | SPAＮパラメータにデータがありません | SPANパラメータレコードなし |
| 21245 | 派生新規注文 | システム状態にデータがありません | システム状態レコードなし |
| 21246 | 派生新規注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 21247 | 派生新規注文 | システムが受付可能時間外です。 | システム状態.閉局 |
| 21250 | 派生新規注文 | 派生証拠金不足額ファイルに問題があります | 派生証拠金不足額ファイル障害 |
| 21251 | 派生新規注文 | 派生証拠金振替ファイルに問題があります | 派生証拠金振替ファイル障害 |
| 21252 | 派生新規注文 | 証拠金振替設定ファイルに問題があります | 証拠金振替設定ファイル障害 |
| 21253 | 派生新規注文 | 証拠金振替設定ファイルに問題があります | 証拠金振替設定ファイル障害 |
| 21254 | 派生新規注文 | SPAＮ証拠金ファイルに問題があります | SPAN証拠金ファイル障害 |
| 21256 | 派生新規注文 | 原資産マスタにデータがありません | 原資産マスタレコードなし |
| 21257 | 派生新規注文 | 運用ステータスにデータがありません(評価単価) | 運用ステータスレコードなし(評価単価) |
| 21258 | 派生新規注文 | 余力がありません | 余力なし |
| 21262 | 派生新規注文 | 運用ステータスにデータがありません(照会) | 運用ステータスレコードなし(照会) |
| 21290 | 派生新規注文 | 注文処理中です | 注文処理中 |
| 21291 | 派生新規注文 | 訂正中です | 訂正中 |
| 21292 | 派生新規注文 | 取消中です | 取消中 |
| 21293 | 派生新規注文 | 失効済みです | 失効済み |
| 21294 | 派生新規注文 | 約定済みです | 約定済み |
| 21295 | 派生新規注文 | 取消済みです | 取消済み |
| 21296 | 派生新規注文 | トリガー発動済みです | トリガー発動済み |
| 21297 | 派生新規注文 | 強制決済中ですので、この操作はできません | 強制決済中 |
| 21299 | 派生新規注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 21300 | 派生新規注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 21301 | 派生新規注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 21302 | 派生新規注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 21303 | 派生新規注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 21304 | 派生新規注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 21305 | 派生新規注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 21306 | 派生新規注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 21310 | 派生新規注文 | 口座管理.先物オプション口座未開設 | 口座管理.先物オプション口座未開設 |
| 21311 | 派生新規注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 21312 | 派生新規注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 21317 | 派生新規注文 | 契約締結前交付書面ファイルに問題があります | 契約締結前交付書面ファイル障害 |
| 21318 | 派生新規注文 | 契約締結前交付書面(当日更新ＴＲＸ)ファイルに問題があります | 契約締結前交付書面(当日更新ＴＲＸ)ファイル障害 |
| 21319 | 派生新規注文 | 契約締結前交付書面チェックでエラーが発生しました | 契約締結前交付書面チェックエラー |
| 21320 | 派生新規注文 | 顧客銘柄別取引停止ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 21321 | 派生新規注文 | 顧客銘柄別取引停止にデータがありません | 顧客銘柄別取引停止レコードなし |
| 21330 | 派生新規注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規買停止 |
| 21331 | 派生新規注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規売停止 |
| 21332 | 派生新規注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済買停止 |
| 21333 | 派生新規注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済売停止 |
| 21334 | 派生新規注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規買停止 |
| 21335 | 派生新規注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規売停止 |
| 21336 | 派生新規注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済買停止 |
| 21337 | 派生新規注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済売停止 |
| 21360 | 派生新規注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 21361 | 派生新規注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 21364 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 21365 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 21366 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 21367 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 21368 | 派生新規注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 21369 | 派生新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 21370 | 派生新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 21371 | 派生新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 21372 | 派生新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 21380 | 派生新規注文 | 注文できません。個別ソフトリミットファイルに問題があります | ソフトリミット個別ファイル障害 |
| 21383 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 21384 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 21385 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 21386 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 21387 | 派生新規注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 21388 | 派生新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 21389 | 派生新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 21390 | 派生新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 21391 | 派生新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 21400 | 派生新規注文 | 注文できません。通常ソフトリミットファイルに問題があります | ソフトリミット通常ファイル障害 |
| 21401 | 派生新規注文 | 注文できません。通常ソフトリミットファイルにデータがありません | ソフトリミット通常レコードなし |
| 21404 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 21405 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 21406 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 21407 | 派生新規注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 21408 | 派生新規注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 21409 | 派生新規注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 21410 | 派生新規注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 21411 | 派生新規注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 21412 | 派生新規注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 21460 | 派生新規注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 21461 | 派生新規注文 |  | 手数料マスタレコードなし |
| 21470 | 派生新規注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 21471 | 派生新規注文 |  | 課税率マスタレコードなし |
| 21700 | 派生新規注文 | 派生証拠金残ファイルに問題があります | 派生証拠金残ファイル障害 |
| 21701 | 派生新規注文 | 派生証拠金残にデータがありません | 派生証拠金残レコードなし |
| 21702 | 派生新規注文 | 派生証拠金残のデータ更新でエラーが発生しました | 派生証拠金残レコード更新エラー |
| 21703 | 派生新規注文 | 注文番号（派生）ファイルに問題があります | 注文番号（派生）ファイル障害 |
| 21704 | 派生新規注文 | 注文番号（派生）にデータがありません | 注文番号（派生）レコードなし |
| 21705 | 派生新規注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 21706 | 派生新規注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 21707 | 派生新規注文 | 派生建玉残にデータ作成でエラーが発生しました | 派生建玉残レコード作成エラー |
| 21708 | 派生新規注文 | 派生建玉残のデータ更新でエラーが発生しました | 派生建玉残レコード更新エラー |
| 21709 | 派生新規注文 | 派生建玉明細ファイルに問題があります | 派生建玉明細ファイル障害 |
| 21710 | 派生新規注文 | 派生建玉明細にデータがありません | 派生建玉明細レコードなし |
| 21711 | 派生新規注文 | 派生建玉明細に有効数量がありません | 派生建玉明細有効数量なし |
| 21712 | 派生新規注文 | 派生建玉明細のデータ更新でエラーが発生しました | 派生建玉明細レコード更新エラー |
| 21713 | 派生新規注文 | 派生返済予約ファイルに問題があります | 派生返済予約ファイル障害 |
| 21714 | 派生新規注文 | 派生返済予約にデータ作成でエラーが発生しました | 派生返済予約レコード作成エラー |
| 21715 | 派生新規注文 | 派生サマリファイルに問題があります | 派生サマリファイル障害 |
| 21716 | 派生新規注文 | 派生サマリにデータがありません | 派生サマリレコードなし |
| 21717 | 派生新規注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 21718 | 派生新規注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 21719 | 派生新規注文 | 派生明細ファイルに問題があります | 派生明細ファイル障害 |
| 21720 | 派生新規注文 | 派生明細にデータがありません | 派生明細レコードなし |
| 21721 | 派生新規注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 21722 | 派生新規注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 21723 | 派生新規注文 | 派生注文約定履歴ファイルに問題があります | 派生注文約定履歴ファイル障害 |
| 21724 | 派生新規注文 | 派生注文約定履歴にデータ作成でエラーが発生しました | 派生注文約定履歴レコード作成エラー |
| 21804 | 派生新規注文 | お客様の先物、オプションの新規建注文を停止させていただいております | 余力制御.先物ＯＰ新規建停止 |
| 21807 | 派生新規注文 | 追証で未入金があります | 余力制御.追証未入金あり |
| 21991 | 派生新規注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 21992 | 派生新規注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 21993 | 派生新規注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 21994 | 派生新規注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 21997 | 派生新規注文 |  | ネットエラー |
| 21998 | 派生新規注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 21999 | 派生新規注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 22001 | 派生訂正注文 | 注文番号に誤りがあります | 注文番号不正 |
| 22003 | 派生訂正注文 | 執行条件訂正フラグに誤りがあります | 執行条件訂正フラグ不正 |
| 22004 | 派生訂正注文 | 執行条件に誤りがあります | 執行条件不正 |
| 22005 | 派生訂正注文 | 注文値段訂正フラグに誤りがあります | 注文値段訂正フラグ不正 |
| 22006 | 派生訂正注文 | 注文値段区分に誤りがあります | 注文値段区分不正 |
| 22007 | 派生訂正注文 | 注文値段に誤りがあります | 注文値段不正 |
| 22008 | 派生訂正注文 | 注文数量訂正フラグに誤りがあります | 注文数量訂正フラグ不正 |
| 22009 | 派生訂正注文 | 注文数量に誤りがあります | 注文数量不正 |
| 22010 | 派生訂正注文 | 注文期日訂正フラグに誤りがあります | 注文期日訂正フラグ不正 |
| 22011 | 派生訂正注文 | 注文期日訂正フラグに誤りがあります | 注文期日訂正フラグ不正 |
| 22012 | 派生訂正注文 | 逆指値値段条件訂正フラグに誤りがあります | 逆指値値段条件訂正フラグ不正 |
| 22013 | 派生訂正注文 | 逆指値条件に誤りがあります | 逆指値条件不正 |
| 22014 | 派生訂正注文 | 逆指値値段区分訂正フラグに誤りがあります | 逆指値値段区分訂正フラグ不正 |
| 22015 | 派生訂正注文 | 逆指値値段区分に誤りがあります | 逆指値値段区分不正 |
| 22016 | 派生訂正注文 | 逆指値値段に誤りがあります | 逆指値値段不正 |
| 22017 | 派生訂正注文 | 接続に誤りがあります | チャネル不正 |
| 22018 | 派生訂正注文 | 接続詳細に誤りがあります | チャネル詳細不正 |
| 22019 | 派生訂正注文 | オペレータに誤りがあります | オペレータ不正 |
| 22020 | 派生訂正注文 | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 22022 | 派生訂正注文 | 第二暗証番号省略フラグに誤りがあります | 第二暗証番号省略フラグ不正 |
| 22023 | 派生訂正注文 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 22024 | 派生訂正注文 |  | チェックのみフラグ不正 |
| 22032 | 派生訂正注文 | 不成注文に成行が指定されています | 不成注文に成行が指定されている |
| 22033 | 派生訂正注文 | 期限付注文執行条件でエラーが発生しました | 期限付注文執行条件エラー |
| 22034 | 派生訂正注文 | 逆指値注文執行条件でエラーが発生しました | 逆指値注文執行条件エラー |
| 22035 | 派生訂正注文 | 通常＋逆指値注文執行条件でエラーが発生しました | 通常＋逆指値注文執行条件エラー |
| 22036 | 派生訂正注文 | 子注文に執行条件でエラーが発生しました | 子注文に執行条件エラー |
| 22037 | 派生訂正注文 | 子注文に注文期限でエラーが発生しました | 子注文に注文期限エラー |
| 22038 | 派生訂正注文 | ｢成行｣を指定されていますが、注文単価も入力されています。指値の場合は｢指値｣に印を付けて下さい。 | 成行指値同時指定 |
| 22108 | 派生訂正注文 | 成行指値変更でエラーが発生しました | 成行指値変更エラー |
| 22109 | 派生訂正注文 | 指値成行変更でエラーが発生しました | 指値成行変更エラー |
| 22110 | 派生訂正注文 | 執行条件変更がありません | 執行条件変更なし |
| 22111 | 派生訂正注文 | 注文数量変更がありません | 注文数量変更なし |
| 22112 | 派生訂正注文 | 注文値段変更がありません | 注文値段変更なし |
| 22113 | 派生訂正注文 | 注文期日変更がありません | 注文期日変更なし |
| 22114 | 派生訂正注文 | 逆指値条件変更がありません | 逆指値条件変更なし |
| 22115 | 派生訂正注文 |  | 逆指値注文値段変更なし |
| 22116 | 派生訂正注文 | 変更項目がありません | 変更項目なし |
| 22120 | 派生訂正注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 22121 | 派生訂正注文 | 運用ステータス(採用値幅)にデータがありません | 運用ステータス(採用値幅)レコードなし |
| 22122 | 派生訂正注文 | 只今の時間帯は受付できません | 運用ステータス(注文).受付停止 |
| 22130 | 派生訂正注文 | 日付情報にデータがありません | 日付情報レコードなし |
| 22140 | 派生訂正注文 | 銘柄マスタにデータがありません | 銘柄マスタレコードなし |
| 22153 | 派生訂正注文 | 当該銘柄の売買単位の整数倍の数量を入力してください | 銘柄マスタ.売買単位エラー |
| 22154 | 派生訂正注文 | 当該銘柄の値幅制限内の単価を入力してください | 銘柄市場マスタ.値幅エラー |
| 22160 | 派生訂正注文 | 呼値にデータがありません | 呼値レコードなし |
| 22161 | 派生訂正注文 | 正しい呼値の単位で単価を入力してください | 呼値エラー |
| 22170 | 派生訂正注文 | 数量の増加はできません | 増株訂正エラー |
| 22180 | 派生訂正注文 | 注文期日でエラーが発生しました | 注文期日エラー |
| 22191 | 派生訂正注文 | 逆指値段には当該銘柄の値幅制限内の単価を入力してください | 逆指値段値幅エラー |
| 22192 | 派生訂正注文 | 逆指値段呼値にデータがありません | 逆指値段呼値レコードなし |
| 22193 | 派生訂正注文 | 正しい呼値の単位で逆指値段を入力してください | 逆指値段呼値エラー |
| 22199 | 派生訂正注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 22200 | 派生訂正注文 | このサービスは取り扱っておりません | サービス別取扱.先物訂正取扱不可 |
| 22201 | 派生訂正注文 | このサービスは取り扱っておりません | サービス別取扱.オプション訂正取扱不可 |
| 22209 | 派生訂正注文 | 商品市場別設定レコードがありません | 商品市場別設定レコードなし |
| 22210 | 派生訂正注文 | 数量と値段の同時訂正はできません | 商品市場別設定.同時訂正不可 |
| 22211 | 派生訂正注文 | 寄付への訂正はできません | 商品市場別設定.執行条件寄付不可 |
| 22212 | 派生訂正注文 | 引けへの訂正はできません | 商品市場別設定.執行条件引け不可 |
| 22213 | 派生訂正注文 | 不成への訂正はできません | 商品市場別設定.執行条件不成不可 |
| 22214 | 派生訂正注文 | 連続注文の訂正はできません | 商品市場別設定.連続注文不可 |
| 22215 | 派生訂正注文 | 出来るまで注文の訂正はできません | 商品市場別設定.出来るまで注文不可 |
| 22220 | 派生訂正注文 | 当該銘柄の成行注文はできません | 銘柄別市場別規制.停止区分成行禁止 |
| 22221 | 派生訂正注文 | 当該銘柄の新規買建の成行注文はできません | 銘柄別市場別規制.買建成行禁止 |
| 22222 | 派生訂正注文 | 当該銘柄の新規売建の成行注文はできません | 銘柄別市場別規制.売建成行禁止 |
| 22223 | 派生訂正注文 | 当該銘柄の買返済の成行注文はできません | 銘柄別市場別規制.買返済成行禁止 |
| 22224 | 派生訂正注文 | 当該銘柄の売返済の成行注文はできません | 銘柄別市場別規制.売返済成行禁止 |
| 22225 | 派生訂正注文 | SPANパラメータにデータがありません | SPANパラメータレコードなし |
| 22245 | 派生訂正注文 | システム状態にデータがありません | システム状態レコードなし |
| 22246 | 派生訂正注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 22247 | 派生訂正注文 | システムが受付可能時間外です。 | システム状態.閉局 |
| 22250 | 派生訂正注文 | 派生証拠金不足額ファイルに問題があります | 派生証拠金不足額ファイル障害 |
| 22251 | 派生訂正注文 | 派生証拠金振替ファイルに問題があります | 派生証拠金振替ファイル障害 |
| 22252 | 派生訂正注文 | 証拠金振替設定ファイルに問題があります | 証拠金振替設定ファイル障害 |
| 22253 | 派生訂正注文 | 証拠金振替設定ファイルに問題があります | 証拠金振替設定ファイル障害 |
| 22254 | 派生訂正注文 | SPAN証拠金ファイルに問題があります | SPAN証拠金ファイル障害 |
| 22256 | 派生訂正注文 | 原資産マスタにデータがありません | 原資産マスタレコードなし |
| 22257 | 派生訂正注文 | 運用ステータスにデータがありません(評価単価) | 運用ステータスレコードなし(評価単価) |
| 22258 | 派生訂正注文 | 余力がありません | 余力なし |
| 22259 | 派生訂正注文 | 派生商品マスタにデータがありません | 派生商品マスタレコードなし |
| 22260 | 派生訂正注文 | 先物銘柄マスタにデータがありません | 先物銘柄マスタレコードなし |
| 22261 | 派生訂正注文 | オプション銘柄マスタにデータがありません | オプション銘柄マスタレコードなし |
| 22262 | 派生訂正注文 | 運用ステータスにデータがありません(照会) | 運用ステータスレコードなし(照会) |
| 22290 | 派生訂正注文 | 注文処理中です | 注文処理中 |
| 22291 | 派生訂正注文 | 訂正中です | 訂正中 |
| 22292 | 派生訂正注文 | 取消中です | 取消中 |
| 22293 | 派生訂正注文 | 失効済みです | 失効済み |
| 22294 | 派生訂正注文 | 約定済みです | 約定済み |
| 22295 | 派生訂正注文 | 取消済みです | 取消済み |
| 22296 | 派生訂正注文 | トリガー発動済みです | トリガー発動済み |
| 22297 | 派生訂正注文 | 強制決済中ですので、この操作はできません | 強制決済中 |
| 22298 | 派生訂正注文 | 訂正数量でエラーが発生しました | 訂正数量エラー |
| 22299 | 派生訂正注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 22300 | 派生訂正注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 22301 | 派生訂正注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 22302 | 派生訂正注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 22303 | 派生訂正注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 22304 | 派生訂正注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 22305 | 派生訂正注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 22306 | 派生訂正注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 22310 | 派生訂正注文 | 口座管理.先物オプション口座が未開設です | 口座管理.先物オプション口座未開設 |
| 22311 | 派生訂正注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 22312 | 派生訂正注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 22317 | 派生訂正注文 | 契約締結前交付書面ファイルに問題があります | 契約締結前交付書面ファイル障害 |
| 22318 | 派生訂正注文 | 契約締結前交付書面(当日更新ＴＲＸ)ファイルに問題があります | 契約締結前交付書面(当日更新ＴＲＸ)ファイル障害 |
| 22319 | 派生訂正注文 | 契約締結前交付書面チェックでエラーが発生しました | 契約締結前交付書面チェックエラー |
| 22320 | 派生訂正注文 | 顧客銘柄別取引制限ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 22321 | 派生訂正注文 | 顧客銘柄別取引制限にデータがありません | 顧客銘柄別取引停止レコードなし |
| 22330 | 派生訂正注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規買停止 |
| 22331 | 派生訂正注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規売停止 |
| 22332 | 派生訂正注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済買停止 |
| 22333 | 派生訂正注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済売停止 |
| 22334 | 派生訂正注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規買停止 |
| 22335 | 派生訂正注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規売停止 |
| 22336 | 派生訂正注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済買停止 |
| 22337 | 派生訂正注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済売停止 |
| 22360 | 派生訂正注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 22361 | 派生訂正注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 22364 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 22365 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 22366 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 22367 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 22368 | 派生訂正注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 22369 | 派生訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 22370 | 派生訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 22371 | 派生訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 22372 | 派生訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 22380 | 派生訂正注文 | 注文できません。個別ソフトリミットファイルに問題があります | ソフトリミット個別ファイル障害 |
| 22383 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 22384 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 22385 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 22386 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 22387 | 派生訂正注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 22388 | 派生訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 22389 | 派生訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 22390 | 派生訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 22391 | 派生訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 22400 | 派生訂正注文 | 注文できません。通常ソフトリミットファイルに問題があります | ソフトリミット通常ファイル障害 |
| 22401 | 派生訂正注文 | 注文できません。通常ソフトリミットにデータがありません | ソフトリミット通常レコードなし |
| 22404 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 22405 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 22406 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 22407 | 派生訂正注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 22408 | 派生訂正注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 22409 | 派生訂正注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 22410 | 派生訂正注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 22411 | 派生訂正注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 22412 | 派生訂正注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 22460 | 派生訂正注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 22461 | 派生訂正注文 |  | 手数料マスタレコードなし |
| 22470 | 派生訂正注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 22471 | 派生訂正注文 |  | 課税率マスタレコードなし |
| 22700 | 派生訂正注文 | 派生証拠金残ファイルに問題があります | 派生証拠金残ファイル障害 |
| 22701 | 派生訂正注文 | 派生証拠金残にデータがありません | 派生証拠金残レコードなし |
| 22702 | 派生訂正注文 | 派生証拠金残のデータ更新でエラーが発生しました | 派生証拠金残レコード更新エラー |
| 22703 | 派生訂正注文 | 注文番号（派生）ファイルに問題があります | 注文番号（派生）ファイル障害 |
| 22704 | 派生訂正注文 | 注文番号（派生）にデータがありません | 注文番号（派生）レコードなし |
| 22705 | 派生訂正注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 22706 | 派生訂正注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 22707 | 派生訂正注文 | 派生建玉残にデータ作成でエラーが発生しました | 派生建玉残レコード作成エラー |
| 22708 | 派生訂正注文 | 派生建玉残のデータ更新でエラーが発生しました | 派生建玉残レコード更新エラー |
| 22709 | 派生訂正注文 | 派生建玉明細ファイルに問題があります | 派生建玉明細ファイル障害 |
| 22710 | 派生訂正注文 | 派生建玉明細にデータがありません | 派生建玉明細レコードなし |
| 22711 | 派生訂正注文 | 派生建玉明細有効数量がありません | 派生建玉明細有効数量なし |
| 22712 | 派生訂正注文 | 派生建玉明細のデータ更新でエラーが発生しました | 派生建玉明細レコード更新エラー |
| 22713 | 派生訂正注文 | 派生返済予約ファイルに問題があります | 派生返済予約ファイル障害 |
| 22714 | 派生訂正注文 | 派生返済予約にデータ作成でエラーが発生しました | 派生返済予約レコード作成エラー |
| 22715 | 派生訂正注文 | 派生サマリファイルに問題があります | 派生サマリファイル障害 |
| 22716 | 派生訂正注文 | 派生サマリにデータがありません | 派生サマリレコードなし |
| 22717 | 派生訂正注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 22718 | 派生訂正注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 22719 | 派生訂正注文 | 派生明細ファイルに問題があります | 派生明細ファイル障害 |
| 22720 | 派生訂正注文 | 派生明細にデータがありません | 派生明細レコードなし |
| 22721 | 派生訂正注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 22722 | 派生訂正注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 22723 | 派生訂正注文 | 派生注文約定履歴ファイルに問題があります | 派生注文約定履歴ファイル障害 |
| 22724 | 派生訂正注文 | 派生注文約定履歴にデータ作成でエラーが発生しました | 派生注文約定履歴レコード作成エラー |
| 22804 | 派生訂正注文 | お客様の先物、オプションの新規建注文を停止させていただいております | 余力制御.先物ＯＰ新規建停止 |
| 22807 | 派生訂正注文 | 追証で未入金があります | 余力制御.追証未入金あり |
| 22991 | 派生訂正注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 22992 | 派生訂正注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 22993 | 派生訂正注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 22994 | 派生訂正注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 22997 | 派生訂正注文 | ネットでエラーが発生しました | ネットエラー |
| 22998 | 派生訂正注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 22999 | 派生訂正注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 23001 | 派生訂正注文 | 注文番号に誤りがあります | 注文番号不正 |
| 23017 | 派生訂正注文 | チャネルに誤りがあります | チャネル不正 |
| 23018 | 派生訂正注文 | チャネル詳細に誤りがあります | チャネル詳細不正 |
| 23019 | 派生訂正注文 | オペレータに誤りがあります | オペレータ不正 |
| 23020 | 派生訂正注文 | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 23022 | 派生訂正注文 | 第二暗証番号省略フラグに誤りがあります | 第二暗証番号省略フラグ不正 |
| 23023 | 派生訂正注文 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 23120 | 派生取消注文 | 運用ステータス(注文)にデータがありません | 運用ステータス(注文)レコードなし |
| 23122 | 派生取消注文 | 只今の時間帯は受付できません | 運用ステータス(注文).受付停止 |
| 23199 | 派生取消注文 | サービス別取扱レコードがありません | サービス別取扱レコードなし |
| 23200 | 派生取消注文 | このサービスは取り扱っておりません | サービス別取扱.先物取消取扱不可 |
| 23201 | 派生取消注文 | このサービスは取り扱っておりません | サービス別取扱.オプション取消取扱不可 |
| 23245 | 派生取消注文 | システム状態にデータがありません | システム状態レコードなし |
| 23246 | 派生取消注文 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 23247 | 派生取消注文 | システム状態.サービス停止中です | 注文処理中 |
| 23290 | 派生取消注文 | 注文処理中です | 注文処理中 |
| 23291 | 派生取消注文 | 訂正中です | 訂正中 |
| 23292 | 派生取消注文 | 取消中です | 取消中 |
| 23293 | 派生取消注文 | 失効済みです | 失効済み |
| 23294 | 派生取消注文 | 約定済みです | 約定済み |
| 23295 | 派生取消注文 | 取消済みです | 取消済み |
| 23296 | 派生取消注文 | トリガー発動済みです | トリガー発動済み |
| 23297 | 派生取消注文 | 強制決済中ですので、この操作はできません | 強制決済中 |
| 23299 | 派生取消注文 | 顧客マスタファイルに問題があります | 顧客マスタファイル障害 |
| 23300 | 派生取消注文 | 顧客マスタにデータがありません | 顧客マスタレコードなし |
| 23301 | 派生取消注文 | 顧客マスタ.精算理由でエラーが発生しました | 顧客マスタ.精算理由エラー |
| 23302 | 派生取消注文 | 顧客情報ファイルに問題があります | 顧客情報ファイル障害 |
| 23303 | 派生取消注文 | 顧客情報にデータがありません | 顧客情報レコードなし |
| 23304 | 派生取消注文 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 23305 | 派生取消注文 | 口座管理ファイルに問題があります | 口座管理ファイル障害 |
| 23306 | 派生取消注文 | 口座管理にデータがありません | 口座管理レコードなし |
| 23310 | 派生取消注文 | 口座管理.先物オプション口座未開設 | 口座管理.先物オプション口座未開設 |
| 23311 | 派生取消注文 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 23312 | 派生取消注文 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 23317 | 派生取消注文 | 契約締結前交付書面ファイルに問題があります | 契約締結前交付書面ファイル障害 |
| 23318 | 派生取消注文 | 契約締結前交付書面(当日更新ＴＲＸ)ファイルに問題があります | 契約締結前交付書面(当日更新ＴＲＸ)ファイル障害 |
| 23319 | 派生取消注文 | 契約締結前交付書面チェックでエラーが発生しました | 契約締結前交付書面チェックエラー |
| 23320 | 派生取消注文 | 顧客銘柄別取引制限ファイルに問題があります | 顧客銘柄別取引停止ファイル障害 |
| 23321 | 派生取消注文 | 顧客銘柄別取引制限にデータがありません | 顧客銘柄別取引停止レコードなし |
| 23330 | 派生取消注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規買停止 |
| 23331 | 派生取消注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.先物新規売停止 |
| 23332 | 派生取消注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済買停止 |
| 23333 | 派生取消注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.先物返済売停止 |
| 23334 | 派生取消注文 | お客様の当該銘柄における新規買建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規買停止 |
| 23335 | 派生取消注文 | お客様の当該銘柄における新規売建のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ新規売停止 |
| 23336 | 派生取消注文 | お客様の当該銘柄における買返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済買停止 |
| 23337 | 派生取消注文 | お客様の当該銘柄における売返済のお取引を停止させていただいております | 顧客銘柄別取引停止.ＯＰ返済売停止 |
| 23360 | 派生取消注文 | ハードリミットファイルに問題があります | ハードリミットファイル障害 |
| 23361 | 派生取消注文 | ハードリミットにデータがありません | ハードリミットレコードなし |
| 23364 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買新規上限 |
| 23365 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売新規上限 |
| 23366 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量買返済上限 |
| 23367 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ハードリミット.発注数量売返済上限 |
| 23368 | 派生取消注文 | 発注金額が弊社規定の制限を越えています | ハードリミット.発注金額上限 |
| 23369 | 派生取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総数量上限 |
| 23370 | 派生取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.売建玉総数量上限 |
| 23371 | 派生取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉総金額上限 |
| 23372 | 派生取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ハードリミット.建玉銘柄総金額上限 |
| 23380 | 派生取消注文 | 注文できません。個別ソフトリミットファイルに問題があります | ソフトリミット個別ファイル障害 |
| 23383 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買新規上限 |
| 23384 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売新規上限 |
| 23385 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量買返済上限 |
| 23386 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット個別.発注数量売返済上限 |
| 23387 | 派生取消注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット個別.発注金額上限 |
| 23388 | 派生取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総数量上限 |
| 23389 | 派生取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.売建玉総数量上限 |
| 23390 | 派生取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉総金額上限 |
| 23391 | 派生取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット個別.建玉銘柄総金額上限 |
| 23400 | 派生取消注文 | 注文できません。通常ソフトリミットファイルに問題があります | ソフトリミット通常ファイル障害 |
| 23401 | 派生取消注文 | 注文できません。通常ソフトリミットにデータがありません | ソフトリミット通常レコードなし |
| 23404 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買新規上限 |
| 23405 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売新規上限 |
| 23406 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量買返済上限 |
| 23407 | 派生取消注文 | 発注数量が弊社規定の制限を越えています | ソフトリミット通常.発注数量売返済上限 |
| 23408 | 派生取消注文 | 発注金額が弊社規定の制限を越えています | ソフトリミット通常.発注金額上限 |
| 23409 | 派生取消注文 | 建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総数量上限 |
| 23410 | 派生取消注文 | 売建玉の総数量(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.売建玉総数量上限 |
| 23411 | 派生取消注文 | 建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉総金額上限 |
| 23412 | 派生取消注文 | 当該銘柄の建玉の総金額(既存分＋今回ご注文分)が弊社規定の制限を越えています | ソフトリミット通常.建玉銘柄総金額上限 |
| 23460 | 派生取消注文 | 手数料マスタファイルに問題があります | 手数料マスタファイル障害 |
| 23461 | 派生取消注文 |  | 手数料マスタレコードなし |
| 23470 | 派生取消注文 | 課税率マスタファイルに問題があります | 課税率マスタファイル障害 |
| 23471 | 派生取消注文 |  | 課税率マスタレコードなし |
| 23700 | 派生取消注文 | 派生証拠金残ファイルに問題があります | 派生証拠金残ファイル障害 |
| 23701 | 派生取消注文 | 派生証拠金残にデータがありません | 派生証拠金残レコードなし |
| 23702 | 派生取消注文 | 派生証拠金残のデータ更新でエラーが発生しました | 派生証拠金残レコード更新エラー |
| 23703 | 派生取消注文 | 注文番号（派生）ファイルに問題があります | 注文番号（派生）ファイル障害 |
| 23704 | 派生取消注文 | 注文番号（派生）にデータがありません | 注文番号（派生）レコードなし |
| 23705 | 派生取消注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 23706 | 派生取消注文 | 派生建玉残ファイルに問題があります | 派生建玉残ファイル障害 |
| 23707 | 派生取消注文 | 派生建玉残にデータ作成でエラーが発生しました | 派生建玉残レコード作成エラー |
| 23708 | 派生取消注文 | 派生建玉残のデータ更新でエラーが発生しました | 派生建玉残レコード更新エラー |
| 23709 | 派生取消注文 | 派生建玉明細ファイルに問題があります | 派生建玉明細ファイル障害 |
| 23710 | 派生取消注文 | 派生建玉明細にデータがありません | 派生建玉明細レコードなし |
| 23711 | 派生取消注文 | 派生建玉明細有効数量がありません | 派生建玉明細有効数量なし |
| 23712 | 派生取消注文 | 派生建玉明細のデータ更新でエラーが発生しました | 派生建玉明細レコード更新エラー |
| 23713 | 派生取消注文 | 派生返済予約ファイルに問題があります | 派生返済予約ファイル障害 |
| 23714 | 派生取消注文 | 派生返済予約にデータ作成でエラーが発生しました | 派生返済予約レコード作成エラー |
| 23715 | 派生取消注文 | 派生サマリファイルに問題があります | 派生サマリファイル障害 |
| 23716 | 派生取消注文 | 派生サマリにデータがありません | 派生サマリレコードなし |
| 23717 | 派生取消注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 23718 | 派生取消注文 | 派生サマリにデータ作成でエラーが発生しました | 派生サマリレコード作成エラー |
| 23719 | 派生取消注文 | 派生明細ファイルに問題があります | 派生明細ファイル障害 |
| 23720 | 派生取消注文 | 派生明細にデータがありません | 派生明細レコードなし |
| 23721 | 派生取消注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 23722 | 派生取消注文 | 派生明細にデータ作成でエラーが発生しました | 派生明細レコード作成エラー |
| 23723 | 派生取消注文 | 派生注文約定履歴ファイルに問題があります | 派生注文約定履歴ファイル障害 |
| 23724 | 派生取消注文 | 派生注文約定履歴にデータ作成でエラーが発生しました | 派生注文約定履歴レコード作成エラー |
| 23804 | 派生取消注文 | 余力制御.先物ＯＰ新規建の受付は停止しています | 余力制御.先物ＯＰ新規建停止 |
| 23807 | 派生取消注文 | 追証に未入金があります | 余力制御.追証未入金あり |
| 23991 | 派生取消注文 | セッション情報レコードがありません | セッション情報レコードなし |
| 23992 | 派生取消注文 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 23993 | 派生取消注文 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 23994 | 派生取消注文 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 23997 | 派生取消注文 | ネットでエラーが発生しました | ネットエラー |
| 23998 | 派生取消注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 23999 | 派生取消注文 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 24001 | 派生先物 | もうすぐ本日の取引が終了します。 | 市場閉局警告表示 |
| 24002 | 派生オプション | もうすぐ本日の取引が終了します。 | 市場閉局警告表示 |
| 24304 | 派生一括取消 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 24980 | 派生一括取消 | 取消できる注文がありません | 取消可能注文なし |
| 24991 | 派生一括取消 | セッション情報レコードがありません | セッション情報レコードなし |
| 24992 | 派生一括取消 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 24993 | 派生一括取消 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 24994 | 派生一括取消 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 24997 | 派生一括取消 | ネットでエラーが発生しました | ネットエラー |
| 24998 | 派生一括取消 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 24999 | 派生一括取消 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 25304 | 派生一括返済 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 25980 | 派生一括返済 | 返済できる建玉がありません | 返済可能建玉なし |
| 25991 | 派生一括返済 | セッション情報レコードがありません | セッション情報レコードなし |
| 25992 | 派生一括返済 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 25993 | 派生一括返済 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 25994 | 派生一括返済 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 25997 | 派生一括返済 | ネットでエラーが発生しました | ネットエラー |
| 25998 | 派生一括返済 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 25999 | 派生一括返済 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 31001 | 投信 | 売買区分に誤りがあります | 売買区分不正 |
| 31002 | 投信 | 譲渡益課税区分に誤りがあります | 譲渡益課税区分 |
| 31003 | 投信 | 指定区分に誤りがあります | 指定区分不正 |
| 31004 | 投信 | ご注文の数量の単位をお間違えです。ご注文数量をご確認の上、改めてご入力下さい。 | 売付方法不正 |
| 31005 | 投信 | 注文数量に誤りがあります | 注文数量不正 |
| 31006 | 投信 | 売買区分と指定区分の関係に誤りがあります | 売買区分と指定区分の関係不正 |
| 31007 | 投信 | 指定区分と注文口数の関係に誤りがあります | 指定区分と注文口数の関係不正 |
| 31008 | 投信 | 指定区分と注文金額の関係に誤りがあります | 指定区分と注文金額の関係不正 |
| 31009 | 投信 | 指定区分とマスタの関係に誤りがあります | 指定区分とマスタの関係不正 |
| 31020 | 投信 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 31021 | 投信 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 銘柄マスタに存在しない |
| 31022 | 投信 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | WEB3取扱禁止 |
| 31023 | 投信 | 当日買取引はできません | 当日買取引禁止 |
| 31024 | 投信 | 翌日買取引はできません | 翌日買取引禁止 |
| 31025 | 投信 | 当日売取引はできません | 当日売取引禁止 |
| 31026 | 投信 | 翌日売取引はできません | 翌日売取引禁止 |
| 31027 | 投信 | ご注文の数量が、買付最低単位を満たしていません。ご注文数量をご確認下さい。 | 最低口数未満 |
| 31028 | 投信 | ご注文の数量の単位をお間違えです。ご注文数量をご確認下さい。 | 単位口数エラー |
| 31029 | 投信 | ご注文の数量が、買付最低単位を満たしていません。ご注文数量をご確認下さい。 | 最低金額未満 |
| 31030 | 投信 | ご注文の数量の単位をお間違えです。ご注文数量をご確認下さい。 | 単位金額エラー |
| 31031 | 投信 | ご注文の数量が、売付最低単位を満たしていません。ご注文数量をご確認の上、改めてご入力下さい。 | 最低口数未満 |
| 31032 | 投信 | ご注文の数量の単位をお間違えです。ご注文数量をご確認の上、改めてご入力下さい。 | 単位口数エラー |
| 31033 | 投信 | 入力期間外です | 入力期間外 |
| 31034 | 投信 | ＮＩＳＡロールオーバー期間の為、買付注文停止中です。 | NISA買付注文抑止チェックエラー |
| 31035 | 投信 | NISA注文抑止チェックファイル障害 | NISA買付注文抑止チェックファイル障害 |
| 31036 | 投信 | ＮＩＳＡロールオーバー期間の為、対象年のお預りがある銘柄の売付注文停止中です。 | NISA売付注文抑止チェックエラー |
| 31037 | 投信 | NISA注文抑止チェックファイル障害 | NISA売付注文抑止チェックファイル障害 |
| 31040 | 投信 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 買付可能額不足 |
| 31041 | 投信 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 利用可能非課税枠不足 |
| 31042 | 投信 | ご注文の数量が、売付可能数量を超えています。数量をご確認の上、改めてご入力下さい。 | 残高不足 |
| 31043 | 投信 | この銘柄の目論見書が取得できません。コールセンターまでお問い合わせ下さい。 | 目論見書不正 |
| 31044 | 投信 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 31050 | 投信 | 注文が見つからない | 注文が見つからない |
| 31051 | 投信 | 注文は既に取り消し済み | 注文は既に取り消し済み |
| 31052 | 投信 | 投信保管が見つからない | 投信保管が見つからない |
| 31053 | 投信 | 可能額が不足していますので、このお申し込みはお受けできません。 | 非課税口座管理が見つからない |
| 31054 | 投信 | 可能額取得でエラーが発生しました | 可能額取得エラー |
| 31055 | 投信 | 口座管理データが見つりません | 口座管理が見つからない |
| 31080 | 投信 | 投信実施区分に誤りがあります | 投信実施区分不正 |
| 31090 | 投信 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 31091 | 投信 | システムが受付可能時間外です。 | システム停止 |
| 31092 | 投信 | システムが受付可能時間外です。 | 業務停止 |
| 31093 | 投信 | 日時取得でエラーが発生しました | 日時取得エラー |
| 31094 | 投信 | システムが緊急停止中です。 | 注文番号取得エラー |
| 31095 | 投信 | システムが緊急停止中です。 | 保管顧客別残更新エラー |
| 31096 | 投信 | システムが緊急停止中です。 | 投信保管更新エラー |
| 31097 | 投信 | システムが緊急停止中です。 | 顧客当日取引更新エラー |
| 31098 | 投信 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 海外約定日取得エラー |
| 31099 | 投信 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 受渡日取得エラー |
| 31100 | 投信 | 非課税口座管理更新でエラーが発生しました | 非課税口座管理更新エラー |
| 31101 | 投信 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 31102 | 投信 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 31103 | 投信 | お客様のお取引を停止させていただいております | 余力制御.取引停止 |
| 31104 | 投信 | お客様のその他商品買付のお取引を停止させていただいております | 余力制御.その他商品買付停止 |
| 31105 | 投信 | 追証で未入金があります | 余力制御.追証未入金あり |
| 31106 | 投信 | 余力制御ファイルに問題があります | 余力制御ファイル障害 |
| 31107 | 投信 | お客様の当該銘柄における買付のお取引を停止させていただいております | 顧客銘柄別取引停止.投信買付停止 |
| 31108 | 投信 | お客様の当該銘柄における売付のお取引を停止させていただいております | 顧客銘柄別取引停止.投信売付停止 |
| 31109 | 投信 | 顧客銘柄別取引停止ファイルに問題が発生しました | 顧客銘柄別取引停止ファイル障害 |
| 31110 | 投信 | 二階建てチェックでエラーが発生しました | 二階建てチェックエラー |
| 31111 | 投信 | 二階建てファイルに問題が発生しました | 二階建てファイル障害 |
| 31112 | 投信 | 手数料取得でエラーが発生しました | 手数料取得エラー |
| 31994 | 投信 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 31997 | 投信 | システムが緊急停止中です。 | ネットエラー |
| 31998 | 投信 | システムが緊急停止中です。 | ＤＢエラー |
| 31999 | 投信 | システムが緊急停止中です。 | タイムアウト |
| 32001 | 累投 | 売買区分に誤りがあります | 売買区分不正 |
| 32002 | 累投 | 譲渡益課税区分に誤りがあります | 譲渡益課税区分 |
| 32003 | 累投 | 指定区分に誤りがあります | 指定区分不正 |
| 32004 | 累投 | 売付方法に誤りがあります | 売付方法不正 |
| 32005 | 累投 | 注文数量に誤りがあります | 注文数量不正 |
| 32006 | 累投 | 売買区分と指定区分の関係に誤りがあります | 売買区分と指定区分の関係不正 |
| 32007 | 累投 | 指定区分と注文口数の関係に誤りがあります | 指定区分と注文口数の関係不正 |
| 32008 | 累投 | 指定区分と注文金額の関係に誤りがあります | 指定区分と注文金額の関係不正 |
| 32009 | 累投 | 指定区分とマスタの関係に誤りがあります | 指定区分とマスタの関係不正 |
| 32020 | 累投 | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 32021 | 累投 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 銘柄マスタに存在しない |
| 32022 | 累投 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | WEB3取扱禁止 |
| 32023 | 累投 | 当日買取引はできません | 当日買取引禁止 |
| 32024 | 累投 | 翌日買取引はできません | 翌日買取引禁止 |
| 32025 | 累投 | 当日売取引はできません | 当日売取引禁止 |
| 32026 | 累投 | 翌日売取引はできません | 翌日売取引禁止 |
| 32027 | 累投 | ご注文の数量が、買付最低単位を満たしていません。ご注文数量をご確認下さい。 | 最低口数未満 |
| 32028 | 累投 | ご注文の数量の単位をお間違えです。ご注文数量をご確認下さい。 | 単位口数エラー |
| 32029 | 累投 | ご注文の金額が、買付最低金額を満たしていません。ご注文金額をご確認下さい。 | 最低金額未満 |
| 32030 | 累投 | ご注文の金額の単位をお間違えです。ご注文金額をご確認下さい。 | 単位金額エラー |
| 32031 | 累投 | ご注文の数量が、売付最低単位を満たしていません。ご注文数量をご確認の上、改めてご入力下さい。 | 最低口数未満 |
| 32032 | 累投 | ご注文の数量の単位をお間違えです。ご注文数量をご確認の上、改めてご入力下さい。 | 単位口数エラー |
| 32033 | 累投 | 入力期間外です | 入力期間外 |
| 32040 | 累投 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 買付可能額不足 |
| 32041 | 累投 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 利用可能非課税枠不足 |
| 32042 | 累投 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 残高不足 |
| 32043 | 累投 | この銘柄の目論見書が取得できません。コールセンターまでお問い合わせ下さい。 | 目論見書不正 |
| 32044 | 累投 | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | パスワード不正 |
| 32050 | 累投 | 注文が見つかりません | 注文が見つからない |
| 32051 | 累投 | 注文は既に取り消し済みです | 注文は既に取り消し済み |
| 32052 | 累投 | 投信保管データが見つかりません | 投信保管が見つからない |
| 32053 | 累投 | 可能額が不足していますのため、このお申し込みはお受けできません。 | 非課税口座管理が見つからない |
| 32054 | 累投 | 可能額取得でエラーが発生しました | 可能額取得エラー |
| 32055 | 累投 | 口座管理データが見つかりません | 口座管理が見つからない |
| 32080 | 累投 | 投信実施区分に誤りがあります | 投信実施区分不正 |
| 32090 | 累投 | システムが受付可能時間外です。 | 日付情報データが存在しない |
| 32091 | 累投 | システムが受付可能時間外です。 | システム停止 |
| 32092 | 累投 | システムが受付可能時間外です。 | 業務停止 |
| 32093 | 累投 | システムが緊急停止中です。 | 日時取得エラー |
| 32094 | 累投 | システムが緊急停止中です。 | 注文番号取得エラー |
| 32095 | 累投 | システムが緊急停止中です。 | 保管顧客別残更新エラー |
| 32096 | 累投 | システムが緊急停止中です。 | 投信保管更新エラー |
| 32097 | 累投 | システムが緊急停止中です。 | 顧客当日取引更新エラー |
| 32098 | 累投 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 海外約定日取得エラー |
| 32099 | 累投 | ご指定の銘柄は、弊社ではお取扱いできません。銘柄をご確認下さい。 | 受渡日取得エラー |
| 32100 | 累投 | 非課税口座管理更新でエラーが発生しました | 非課税口座管理更新エラー |
| 32101 | 累投 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 32102 | 累投 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 32103 | 累投 | お客様のお取引を停止させていただいております | 余力制御.取引停止 |
| 32104 | 累投 | お客様のその他商品買付のお取引を停止させていただいております | 余力制御.その他商品買付停止 |
| 32105 | 累投 | 追証で未入金があります | 余力制御.追証未入金あり |
| 32106 | 累投 | 余力制御ファイルに問題が発生しました | 余力制御ファイル障害 |
| 32110 | 累投 | 二階建てチェックでエラーが発生しました | 二階建てチェックエラー |
| 32111 | 累投 | 二階建てファイルに問題が発生しました | 二階建てファイル障害 |
| 32994 | 累投 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 32997 | 累投 | システムが緊急停止中です。 | ネットエラー |
| 32998 | 累投 | システムが緊急停止中です。 | ＤＢエラー |
| 32999 | 累投 | システムが緊急停止中です。 | タイムアウト |
| 41001 | 入出金 | 顧客登録に誤りがあります | 顧客登録Ｎ |
| 41002 | 入出金 | 部店コードに誤りがあります | 部店コード |
| 41003 | 入出金 | システム口座区分に問題があります | システム口座区分 |
| 41004 | 入出金 | 第二暗証番号桁数に誤りがあります | 第二暗証番号 |
| 41005 | 入出金 | 金額に誤りがあります | 金額ゼロ |
| 41006 | 入出金 | 金額桁数でエラーが発生しました | 金額桁数 |
| 41007 | 入出金 | 市場に誤りがあります | 市場 |
| 41008 | 入出金 | 現金勘定科目に誤りがあります | 現金勘定科目 |
| 41009 | 入出金 | 金融機関コードに誤りがあります | 金融機関コード |
| 41010 | 入出金 | 営業日に誤りがあります | 営業日 |
| 41011 | 入出金 | 受渡日に誤りがあります | 受渡日 |
| 41012 | 入出金 | 商品タイプに誤りがあります | 商品タイプ |
| 41013 | 入出金 | 振替限度回数を超えています | 日付キー不正 |
| 41014 | 入出金 | 金額が入力されていません | 金額不正 |
| 41015 | 入出金 | 金額に数字以外の文字が入力されています | 金額不正 |
| 41016 | 入出金 | ポータルコード項目長でエラーが発生しました | ポータルコードエラー |
| 41017 | 入出金 | ポータルコード数値でエラーが発生しました | ポータルコードエラー |
| 41018 | 入出金 | ショップコード項目長でエラーが発生しました | ショップコードエラー |
| 41019 | 入出金 | 決済機関コード項目長でエラーが発生しました | 決済機関コード |
| 41020 | 入出金 | 決済区分項目長でエラーが発生しました | 決済区分 |
| 41021 | 入出金 | 決済受付番号項目長でエラーが発生しました | 決済受付番号 |
| 41022 | 入出金 | 決済結果区分項目値でエラーが発生しました | 決済結果区分 |
| 41023 | 入出金 | 決済結果理由コード項目長でエラーが発生しました | 決済結果理由コード |
| 41024 | 入出金 | 決済結果内容項目長でエラーが発生しました | 決済結果内容 |
| 41025 | 入出金 | 処理日項目長でエラーが発生しました | 処理日 |
| 41026 | 入出金 | 処理時刻項目長でエラーが発生しました | 処理時刻 |
| 41027 | 入出金 | 顧客カナ姓名項目長でエラーが発生しました | 顧客カナ姓名 |
| 41028 | 入出金 | 顧客カナ姓項目長でエラーが発生しました | 顧客カナ姓 |
| 41029 | 入出金 | 顧客カナ名項目長でエラーが発生しました | 顧客カナ名 |
| 41030 | 入出金 | 取引金額数値でエラーが発生しました | 取引金額 |
| 41031 | 入出金 | 取引金額項目長でエラーが発生しました | 取引金額 |
| 41032 | 入出金 | 手数料金額数値でエラーが発生しました | 手数料金額 |
| 41033 | 入出金 | 手数料金額項目長でエラーが発生しました | 手数料金額 |
| 41034 | 入出金 | 入金予定日数値でエラーが発生しました | 入金予定日 |
| 41035 | 入出金 | 入金予定日項目長でエラーが発生しました | 入金予定日 |
| 41036 | 入出金 | 商品名項目長でエラーが発生しました | 商品名 |
| 41037 | 入出金 | 備考1項目長でエラーが発生しました | 備考1 |
| 41038 | 入出金 | 備考1項目長でエラーが発生しました | 備考2 |
| 41039 | 入出金 | 備考1項目長でエラーが発生しました | 備考3 |
| 41040 | 入出金 | 取次番号数値でエラーが発生しました | 取次番号 |
| 41041 | 入出金 | 取次番号項目長でエラーが発生しました | 取次番号 |
| 41042 | 入出金 | 決済結果情報検証値項目長でエラーが発生しました | 金融機関決済決済結果情報検証値 |
| 41043 | 入出金 | 決算結果情報検証値に不整合があります | 金融機関決済決済結果情報検証値 |
| 41049 | 入出金 | 振替金額に不整合があります | 金融機関決済振替金額不整合 |
| 41050 | 入出金 | プロシージャでエラーが発生しました | プロシージャエラー |
| 41051 | 入出金 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 41052 | 入出金 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 41053 | 入出金 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 41054 | 入出金 | 顧客金銭テーブルでデータがロックされています | 顧客金銭テーブルレコードロック |
| 41055 | 入出金 | お客様の振込先口座情報が登録されておりません。恐れ入りますが、コールセンターにお電話いただきご登録情報をご確認いただくか、PC画面ログイン後から「振込先指定預貯金口座変更届」をご請求ください。 | 銀行口座送金用口座なし |
| 41056 | 入出金 | 銀行口座送金用テーブル取得でエラーが発生しました | 銀行口座送金用テーブル取得エラー |
| 41057 | 入出金 | 出金可能額取得でエラーが発生しました | 出金可能額取得エラー |
| 41058 | 入出金 | 出金可能額を超えています | 出金可能額超過エラー |
| 41059 | 入出金 | 出金予約追加でエラーが発生しました | 出金予約追加エラー |
| 41060 | 入出金 | 入金明細追加でエラーが発生しました | 入金明細追加エラー |
| 41061 | 入出金 | 出金予約テーブルがありません | 出金予約テーブルなし |
| 41062 | 入出金 | 出金予約取消更新でエラーが発生しました | 出金予約取消更新エラー |
| 41063 | 入出金 | 出金予約でカーソル例外が発生しました | 出金予約カーソル例外 |
| 41064 | 入出金 | 取消金額に不整合があります | 取消金額不整合 |
| 41065 | 入出金 | 出金金額1取得でエラーが発生しました | 出金金額1取得エラー |
| 41066 | 入出金 | 出金金額2取得でエラーが発生しました | 出金金額2取得エラー |
| 41067 | 入出金 | 出金金額3取得でエラーが発生しました | 出金金額3取得エラー |
| 41068 | 入出金 | 出金金額4取得でエラーが発生しました | 出金金額4取得エラー |
| 41069 | 入出金 | 出金金額5取得でエラーが発生しました | 出金金額5取得エラー |
| 41070 | 入出金 | 対象日に不整合があります | 対象日不整合 |
| 41071 | 入出金 | 入金条件取得でエラーが発生しました | 入金条件取得エラー |
| 41072 | 入出金 | 上限金額を超えています | 入金上限金額超過 |
| 41073 | 入出金 | 最低金額未満です | 入金下限金額未満 |
| 41074 | 入出金 | 入金単位ではありません | 入金単位額エラー |
| 41075 | 入出金 | 振替件数取得でエラーが発生しました | 振替件数取得エラー |
| 41076 | 入出金 | 本日の入金回数が上限回数を超えたためお受けできません | 入金回数超過 |
| 41077 | 入出金 | 入金合計取得でエラーが発生しました | 入金合計取得エラー |
| 41078 | 入出金 | １日の上限金額を超えています | 入金合計金額超過 |
| 41079 | 入出金 | 顧客金銭テーブル更新でエラーが発生しました | 顧客金銭テーブル更新エラー |
| 41080 | 入出金 | 受渡日(出金日)に誤りがあります | 受渡日(出金日)不正 |
| 41081 | 入出金 | 出金可能額取得でエラーが発生しました | 出金可能額取得エラー |
| 41082 | 入出金 | 金融機関決済レポート追加でエラーが発生しました | 金融機関決済レポート追加エラー |
| 41083 | 入出金 | 金融機関決済レポート取得でエラーが発生しました | 金融機関決済レポート取得エラー |
| 41084 | 入出金 | 金融機関決済レポートはロックされていますでエラーが発生しました | 金融機関決済レポートロックエラー |
| 41085 | 入出金 | 金融機関決済レポート更新でエラーが発生しました | 金融機関決済レポート更新エラー |
| 41086 | 入出金 | 金融機関決済顧客登録番号に不整合があります | 金融機関決済顧客登録番号不整合 |
| 41087 | 入出金 | 金融機関決済レポート受付番号取得でエラーが発生しました | 金融機関決済レポート受付番号取得エラー |
| 41088 | 入出金 | 顧客マスタテーブル取得でエラーが発生しました | 顧客マスタテーブル取得エラー |
| 41089 | 入出金 | 出金額の上限値を超えています | 出金額上限値エラー |
| 41090 | 入出金 | 入金取引明細はロックされていますでエラーが発生しました | 入金取引明細ロックエラー |
| 41091 | 入出金 | 入金取引明細更新でエラーが発生しました | 入金取引明細更新エラー |
| 41092 | 入出金 | 余力制御にデータ取得でエラーが発生しました | 余力制御レコード取得エラー |
| 41093 | 入出金 | お客様の出金を停止させていただいております | 余力出金停止 |
| 41094 | 入出金 | 追証で未入金があります | 余力追証未入金有り |
| 41095 | 入出金 | 出金合計値の取得に失敗しました | 出金合計値取得エラー |
| 41096 | 入出金 | 指定された受渡日の出金は既に受付済です | 同一受渡日出金レコード存在済エラー |
| 41097 | 入出金 | 二階建出金チェックでエラーが発生しました | 二階建出金チェックエラー |
| 41098 | 入出金 | 二階建出金チェックファイルに問題があります | 二階建出金チェックファイル障害 |
| 41099 | 入出金 | 問合せでエラーが発生しましたが発生しました | 問合せエラー |
| 41100 | 入出金 | 当日保証金取引レコード作成でエラーが発生しました | 当日保証金取引レコード作成エラー |
| 41101 | 入出金 | 口座管理テーブル取得でエラーが発生しました | 口座管理テーブル取得エラー |
| 41102 | 入出金 | 金融機関決済二重登録でエラーが発生しました | 金融機関決済二重登録エラー |
| 41103 | 入出金 | 余力　取引停止中です | 余力取引停止 |
| 41104 | 入出金 | 既に消込結果テーブル登録済みです | 消込結果登録済 |
| 41105 | 入出金 | 消込結果テーブル取得でエラーが発生しました | 消込結果テーブル取得エラー |
| 41111 | 入出金 | このサービスは取り扱っておりません | サービス取扱い停止(オンライン入金) |
| 41112 | 入出金 | サービス別取扱レコードがありません | サービス取扱い停止(オンライン入金)レコードなし |
| 41113 | 入出金 | このサービスは取り扱っておりません | サービス取扱い停止(出金申込/取消) |
| 41114 | 入出金 | サービス別取扱レコードがありません | サービス取扱い停止(出金申込/取消)(レコードなし) |
| 41115 | 入出金 | サービス別取扱レコードがありません | サービス取扱い停止(入金取引明細)(レコードなし) |
| 41116 | 入出金 | このサービスは取り扱っておりません | サービス取扱い停止(入金取引明細) |
| 41117 | 入出金 | システム状態レコードがありません | システム状態レコードなし |
| 41118 | 入出金 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 41119 | 入出金 | システム状態.サービス停止中です | システム状態.閉局 |
| 41120 | 入出金 | 運用ステータスレコードがありません | 運用ステータスレコードなし |
| 41121 | 入出金 | 只今の時間帯は受付できません | 受付停止 |
| 41131 | 入出金 | 日計り拘束金の更新でエラーが発生しました | 日計り拘束金 |
| 41991 | 入出金 | セッション情報レコードがありません | セッション情報レコードなし |
| 41992 | 入出金 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 41993 | 入出金 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 41994 | 入出金 | ボタンが２回以上押されたた可能性があります。 | 振替二重送信エラー |
| 41997 | 入出金 | ネットでエラーが発生しました | ネットエラー |
| 41998 | 入出金 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 41999 | 入出金 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 42001 | 証拠金振替 | 顧客登録に誤りがあります | 顧客登録Ｎ |
| 42002 | 証拠金振替 | 部店コードに誤りがあります | 部店コード |
| 42003 | 証拠金振替 | システム口座区分に誤りがあります | システム口座区分 |
| 42004 | 証拠金振替 | 第二暗証番号が正しく入力されていません | 第二暗証番号 |
| 42005 | 証拠金振替 | 振替金額を正しく入力して下さい | 振替金額ゼロ |
| 42006 | 証拠金振替 | 振替金額桁数でエラーが発生しました | 振替金額桁数 |
| 42007 | 証拠金振替 | 市場に誤りがあります | 市場 |
| 42008 | 証拠金振替 | 現金勘定科目に誤りがあります | 現金勘定科目 |
| 42009 | 証拠金振替 | 出入Ｃに誤りがあります | 出入Ｃ |
| 42010 | 証拠金振替 | 営業日に誤りがあります | 営業日 |
| 42011 | 証拠金振替 | 商品カテゴリでエラーが発生しました | 商品カテゴリ |
| 42012 | 証拠金振替 | 日付キーに誤りがあります | 日付キー不正 |
| 42013 | 証拠金振替 | 振替限度回数を超えています | 振替上限回数超過 |
| 42014 | 証拠金振替 | 口座未開設です | 口座未開設エラー |
| 42015 | 証拠金振替 | 振替金額が入力されていません | 振替金額不正 |
| 42016 | 証拠金振替 | 振替金額に数字以外の文字が入力されています | 振替金額不正 |
| 42040 | 証拠金振替 | サービス別取扱レコードがありません | サービス取扱い停止(証拠金→現金)(レコードなし) |
| 42041 | 証拠金振替 | サービス別取扱レコードがありません | サービス取扱い停止(現金→証拠金)(レコードなし) |
| 42042 | 証拠金振替 | このサービスは取り扱っておりません | サービス取扱い停止(証拠金→現金) |
| 42043 | 証拠金振替 | このサービスは取り扱っておりません | サービス取扱い停止(現金→証拠金) |
| 42044 | 証拠金振替 | システム状態レコードがありません | システム状態レコードなし |
| 42045 | 証拠金振替 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 42046 | 証拠金振替 | 只今の時間帯は受付できません | システム状態.閉局 |
| 42047 | 証拠金振替 | 運用ステータスレコードがありません | 運用ステータスレコードなし |
| 42048 | 証拠金振替 | 只今の時間帯は受付できません | 受付停止 |
| 42050 | 証拠金振替 | プロシージャでエラーが発生しました | プロシージャエラー |
| 42051 | 証拠金振替 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 42053 | 証拠金振替 | 営業日に誤りがあります | 現在日付取得エラー |
| 42054 | 証拠金振替 | 営業日に誤りがあります | 現在時刻取得エラー |
| 42055 | 証拠金振替 | 営業日に誤りがあります | 顧客金銭テーブルレコードロック |
| 42056 | 証拠金振替 | 営業日に誤りがあります | 対象日不整合 |
| 42057 | 証拠金振替 | 出入Ｃ値に誤りがあります | 出入Ｃ値不正 |
| 42058 | 証拠金振替 | 顧客金銭テーブル更新でエラーが発生しました | 顧客金銭テーブル更新エラー |
| 42059 | 証拠金振替 | 証拠金振替金額合計値取得でエラーが発生しました | 証拠金振替金額合計値取得エラー |
| 42060 | 証拠金振替 | 派生証拠金振替追加でエラーが発生しました | 派生証拠金振替追加エラー |
| 42061 | 証拠金振替 | 派生証拠金が不足しています額取得でエラーが発生しました | 派生証拠金不足額取得エラー |
| 42062 | 証拠金振替 | SI顧客テーブルでデータロックが発生しました | SI顧客テーブルレコードロック |
| 42063 | 証拠金振替 | SI顧客テーブルのデータ更新でエラーが発生しました | SI顧客テーブルレコード更新エラー |
| 42064 | 証拠金振替 | 派生証拠金残にデータ追加でエラーが発生しました | 派生証拠金残レコード追加エラー |
| 42065 | 証拠金振替 | 派生証拠金残のレコードロックでエラーが発生しました | 派生証拠金残レコードロック |
| 42066 | 証拠金振替 | 派生証拠金残更新でエラーが発生しました | 派生証拠金残更新エラー |
| 42068 | 証拠金振替 | 出金可能額取得でエラーが発生しました | 出金可能額取得エラー |
| 42069 | 証拠金振替 | 証拠金振り替え金額が、弊社規定額を超えているため、このお振り替えはお受けできません | 出金可能額超過エラー |
| 42070 | 証拠金振替 | 振替件数取得でエラーが発生しました | 振替件数取得エラー |
| 42071 | 証拠金振替 | 証拠金設定値取得でエラーが発生しました | 証拠金設定値取得エラー |
| 42072 | 証拠金振替 | 振替可能回数を超えています | 振替可能数超過エラー |
| 42073 | 証拠金振替 | 証拠金残高取得でエラーが発生しました | 証拠金残高取得エラー |
| 42074 | 証拠金振替 | 為替受付番号取得でエラーが発生しました | 為替受付番号取得エラー |
| 42075 | 証拠金振替 | 派生証拠金振替取得でエラーが発生しました | 派生証拠金振替取得エラー |
| 42076 | 証拠金振替 | 派生証拠金振替取得でエラーが発生しました | 派生証拠金振替取得エラー |
| 42082 | 証拠金振替 | 証拠金残高がが不足していますしています | 証拠金不足額エラー |
| 42083 | 証拠金振替 | 振替金額が証拠金残高を超えています | 証拠金残高エラー |
| 42094 | 証拠金振替 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 42095 | 証拠金振替 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 42096 | 証拠金振替 | 余力制御にデータ取得でエラーが発生しました | 余力制御レコード取得エラー |
| 42097 | 証拠金振替 | お客様の出金を停止させていただいております | 余力出金停止 |
| 42098 | 証拠金振替 | 追証で未入金があります | 余力追証未入金有り |
| 42099 | 証拠金振替 | 二階建出金チェックでエラーが発生しました | 二階建出金チェックエラー |
| 42100 | 証拠金振替 | 二階建出金チェックファイルに問題があります | 二階建出金チェックファイル障害 |
| 42101 | 証拠金振替 | 当日保証金取引レコード作成でエラーが発生しました | 当日保証金取引レコード作成エラー |
| 42106 | 証拠金振替 | お客様のお取引を停止させていただいております | 余力取引停止 |
| 42109 | 証拠金振替 | 日計り拘束金の更新でエラーが発生しました | 日計り拘束金 |
| 42991 | 証拠金振替 | セッション情報レコードがありません | セッション情報レコードなし |
| 42992 | 証拠金振替 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 42993 | 証拠金振替 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 42994 | 証拠金振替 | ボタンが２回以上押されたた可能性があります。 | 振替二重送信エラー |
| 42998 | 証拠金振替 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 42999 | 証拠金振替 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 43001 | 代用振替 | 顧客登録に誤りがあります | 顧客登録Ｎ |
| 43002 | 代用振替 | 部店コードに誤りがあります | 部店コード |
| 43004 | 代用振替 | 第二暗証番号が正しく入力されていません | 第二暗証番号 |
| 43005 | 代用振替 | 振替金額を正しく入力して下さい | 振替金額ゼロ |
| 43006 | 代用振替 | 振替金額桁数でエラーが発生しました | 振替金額桁数 |
| 43009 | 代用振替 | 出入Ｃデータに誤りがあります | 出入Ｃ |
| 43010 | 代用振替 | 営業日に誤りがあります | 営業日 |
| 43011 | 代用振替 | 振替限度回数を超えています | 振替上限回数超過 |
| 43012 | 代用振替 | 口座未開設でエラーが発生しました | 口座未開設エラー |
| 43013 | 代用振替 | 日付キーに誤りがあります | 日付キー不正 |
| 43014 | 代用振替 | 商品コードに誤りがあります | 商品コード不正 |
| 43040 | 代用振替 | サービス別取扱レコードがありません | サービス取扱い停止(レコードなし) |
| 43041 | 代用振替 | このサービスは取り扱っておりません | サービス取扱い停止 |
| 43042 | 代用振替 | システム状態ファイルにデータがありません | システム状態レコードなし |
| 43043 | 代用振替 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 43044 | 代用振替 | システム状態.サービス停止中です | システム状態.閉局 |
| 43045 | 代用振替 | 運用ステータスレコードがありません | 運用ステータスレコードなし |
| 43046 | 代用振替 | 只今の時間帯は受付できません | 受付停止 |
| 43050 | 代用振替 | プロシージャでエラーが発生しました | プロシージャエラー |
| 43051 | 代用振替 | 第二暗証番号に誤りがあります | 第二暗証番号不正 |
| 43053 | 代用振替 | 営業日に誤りがあります | 現在日付取得エラー |
| 43054 | 代用振替 | 営業日に誤りがあります | 現在時刻取得エラー |
| 43055 | 代用振替 | 営業日に誤りがあります | 顧客金銭テーブルレコードロック |
| 43056 | 代用振替 | 本日の受付は終了いたしました | 振替日不整合 |
| 43060 | 代用振替 | 派生証拠金振替追加でエラーが発生しました | 派生証拠金振替追加エラー |
| 43065 | 代用振替 | 派生証拠金残のレコードロックでエラーが発生しました | 派生証拠金残レコードロック |
| 43066 | 代用振替 | 派生証拠金残更新でエラーが発生しました | 派生証拠金残更新エラー |
| 43068 | 代用振替 | 出金可能額取得でエラーが発生しました | 出金可能額取得エラー |
| 43069 | 代用振替 | 出金可能額超過でエラーが発生しました | 出金可能額超過エラー |
| 43078 | 代用振替 | 振替可能口数を超えています | 振替可能数超過エラー |
| 43079 | 代用振替 | 保管顧客残のレコードロックでエラーが発生しました | 保管顧客残レコードロック |
| 43080 | 代用振替 | 保管顧客残更新でエラーが発生しました | 保管顧客残更新エラー |
| 43081 | 代用振替 | 預り証券振替追加でエラーが発生しました | 預り証券振替追加エラー |
| 43094 | 代用振替 | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 43095 | 代用振替 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 43101 | 代用振替 | 当日保証金取引レコード作成でエラーが発生しました | 当日保証金取引レコード作成エラー |
| 43102 | 代用振替 | 保証金推移追加でエラーが発生しました | 保証金推移追加エラー |
| 43103 | 代用振替 | 保証金推移レコードロックでエラーが発生しました | 保証金推移レコードロック |
| 43104 | 代用振替 | 保証金推移更新でエラーが発生しました | 保証金推移更新エラー |
| 43105 | 代用振替 | 銘柄マスタの取得でエラーが発生しました | 銘柄マスタ取得エラー |
| 43991 | 代用振替 | セッション情報レコードがありません | セッション情報レコードなし |
| 43992 | 代用振替 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 43993 | 代用振替 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 43994 | 代用振替 | ボタンが２回以上押されたた可能性があります。 | 振替二重送信エラー |
| 43998 | 代用振替 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 43999 | 代用振替 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 51001 | 各種届出書類請求 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 51002 | 各種届出書類請求 | 請求受付日時項目に誤りがあります | 請求受付日時 |
| 51003 | 各種届出書類請求 | 請求書類番号項目に誤りがあります | 請求書類N |
| 51004 | 各種届出書類請求 | 処理日時項目に誤りがあります | 処理日時 |
| 51005 | 各種届出書類請求 | 処理済C項目に誤りがあります | 処理済C |
| 51006 | 各種届出書類請求 | 宛先指定C項目に誤りがあります | 宛先指定C |
| 51007 | 各種届出書類請求 | その他備考C項目に誤りがあります | その他備考C |
| 51050 | 各種届出書類請求 | プロシージャでエラーが発生しました | プロシージャエラー |
| 51051 | 各種届出書類請求 | 第二暗証番号が一致しません | 第二暗証番号不整合 |
| 51052 | 各種届出書類請求 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 51053 | 各種届出書類請求 | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 51054 | 各種届出書類請求 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 51055 | 各種届出書類請求 | 届出請求テーブルでデータロックエラーが発生しました | 届出請求テーブルロックエラー |
| 51056 | 各種届出書類請求 | 届出請求テーブル更新でエラーが発生しました | 届出請求テーブル更新エラー |
| 51057 | 各種届出書類請求 | 届出請求テーブル追加でエラーが発生しました | 届出請求テーブル追加エラー |
| 51063 | 勤務先携帯変更 | 携帯勤務先変更申込テーブル情報取得でエラーが発生しました | 携帯勤務先変更情報取得エラー |
| 51064 | 勤務先携帯変更 | 以前ご入力いただきました携帯番号・勤務先情報変更を弊社で確認中のため、この変更申込はお受けできません。 | 携帯勤務先変更申込中 |
| 51095 | 各種届出書類請求 | 顧客情報取得でエラーが発生しました | 顧客情報取得エラー |
| 51096 | 各種届出書類請求 | 電子交付マスタ取得でエラーが発生しました | 電子交付マスタ取得エラー |
| 51097 | 各種届出書類請求 | インサイダー情報取得でエラーが発生しました | インサイダー情報取得エラー |
| 51098 | 各種届出書類請求 | 手数料番号取得でエラーが発生しました | 手数料番号取得エラー |
| 51099 | 各種届出書類請求 | 問合せでエラーが発生しましたが発生しました | 問合せエラー |
| 51991 | 各種届出書類請求 | セッション情報レコードがありません | セッション情報レコードなし |
| 51992 | 各種届出書類請求 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 51993 | 各種届出書類請求 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 51994 | 各種届出書類請求 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 51997 | 各種届出書類請求 | ネットでエラーが発生しました | ネットエラー |
| 51998 | 各種届出書類請求 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 51999 | 各種届出書類請求 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 52001 | メールアドレス変更 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 52002 | メールアドレス変更 | メールアドレス１に誤りがあります | メールアドレス１ |
| 52003 | メールアドレス変更 | 株式約定メール設定に誤りがあります | 株式約定メール設定 |
| 52004 | メールアドレス変更 | 株式未約定メール設定に誤りがあります | 株式未約定メール設定 |
| 52005 | メールアドレス変更 | 先OP約定メール設定に誤りがあります | 先OP約定メール設定 |
| 52006 | メールアドレス変更 | 先OP未約定メール設定に誤りがあります | 先OP未約定メール設定 |
| 52007 | メールアドレス変更 | パスワードが一致しません | パスワード不正 |
| 52011 | メールアドレス変更 | メールアドレス２に誤りがあります | メールアドレス２ |
| 52012 | メールアドレス変更 | 株式発注メール設定に誤りがあります | 株式発注メール設定 |
| 52013 | メールアドレス変更 | 株式訂正メール設定に誤りがあります | 株式訂正メール設定 |
| 52014 | メールアドレス変更 | 株式発注拒否メール設定に誤りがあります | 株式発注拒否メール設定 |
| 52015 | メールアドレス変更 | 株式訂正受付メール設定に誤りがあります | 株式訂正受付メール設定 |
| 52016 | メールアドレス変更 | 株式訂正拒否メール設定に誤りがあります | 株式訂正拒否メール設定 |
| 52017 | メールアドレス変更 | 株式内出来メール設定に誤りがあります | 株式内出来メール設定 |
| 52050 | メールアドレス変更 | プロシージャでエラーが発生しました | プロシージャエラー |
| 52051 | メールアドレス変更 | 第二暗証番号が一致しません | 第二暗証番号不整合 |
| 52052 | メールアドレス変更 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 52053 | メールアドレス変更 | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 52054 | メールアドレス変更 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 52055 | メールアドレス変更 | メールアドレス管理テーブルでデータロックエラーが発生しました | メールアドレス管理テーブルロックエラー |
| 52056 | メールアドレス変更 | メールアドレス管理テーブル更新でエラーが発生しました | メールアドレス管理テーブル更新エラー |
| 52057 | メールアドレス変更 | メールアドレス管理テーブル追加でエラーが発生しました | メールアドレス管理テーブル追加エラー |
| 52099 | メールアドレス変更 | 問合せでエラーが発生しましたが発生しました | 問合せエラー |
| 52991 | メールアドレス変更 | セッション情報レコードがありません | セッション情報レコードなし |
| 52992 | メールアドレス変更 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 52993 | メールアドレス変更 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 52994 | メールアドレス変更 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 52997 | メールアドレス変更 | ネットでエラーが発生しました | ネットエラー |
| 52998 | メールアドレス変更 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 52999 | メールアドレス変更 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 53001 | 手数料変更申込み | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 53002 | 手数料変更申込み | 手数料商品区分項目に誤りがあります | 手数料商品区分 |
| 53003 | 手数料変更申込み | 適用開始日項目に誤りがあります | 適用開始日 |
| 53004 | 手数料変更申込み | 手数料番号Ｏ項目に誤りがあります | 手数料ＮＯ |
| 53005 | 手数料変更申込み | 第二暗証番号が一致しません | 第二暗証番号不整合 |
| 53006 | 手数料変更申込み | その他備考C項目に誤りがあります | その他備考C |
| 53050 | 手数料変更申込み | 処理中にエラーが発生しました | プロシージャエラー |
| 53051 | 手数料変更申込み | 第二暗証番号が一致しません | 第二暗証番号不整合 |
| 53052 | 手数料変更申込み | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 53053 | 手数料変更申込み | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 53054 | 手数料変更申込み | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 53055 | 手数料変更申込み | 手数料変更申込テーブルでデータロックエラーが発生しました | 手数料変更申込テーブルロックエラー |
| 53056 | 手数料変更申込み | 手数料変更申込テーブル更新でエラーが発生しました | 手数料変更申込テーブル更新エラー |
| 53057 | 手数料変更申込み | 手数料変更申込テーブル追加でエラーが発生しました | 手数料変更申込テーブル追加エラー |
| 53058 | 手数料変更申込み | 手数料情報取得でエラーが発生しました | 手数料情報取得エラー |
| 53095 | 手数料変更申込み | 顧客情報取得でエラーが発生しました | 顧客情報取得エラー |
| 53096 | 手数料変更申込み | 営業日カレンダー取得でエラーが発生しました | 営業日カレンダー取得エラー |
| 53099 | 手数料変更申込み | 問合せでエラーが発生しましたが発生しました | 問合せエラー |
| 53991 | 手数料変更申込み | セッション情報レコードがありません | セッション情報レコードなし |
| 53992 | 手数料変更申込み | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 53993 | 手数料変更申込み | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 53994 | 手数料変更申込み | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 53997 | 手数料変更申込み | ネットでエラーが発生しました | ネットエラー |
| 53998 | 手数料変更申込み | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 53999 | 手数料変更申込み | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 54001 | ログインパスワード変更 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 54002 | ログインパスワード変更 | ログインパスワード項目に誤りがあります | ログインパスワード |
| 54003 | ログインパスワード変更 | 変更後パスワード項目に誤りがあります | 変更後パスワード |
| 54005 | ログインパスワード変更 | 変更前と変更後の暗証番号が同一です。 | 暗証番号変化なし |
| 54006 | ログインパスワード変更 | 入力された新暗証番号は、指定可能な文字種ではありません。ご確認の上、再度入力してください。 | 暗証番号要件エラー |
| 54007 | ログインパスワード変更 | 暗証番号が確認用のものと一致しておりません。 | 確認用パスワードエラー |
| 54008 | ログインパスワード変更 | 暗証番号は4桁以上で設定してください。 | パスワード長不足 |
| 54050 | ログインパスワード変更 | プロシージャでエラーが発生しました | プロシージャエラー |
| 54052 | ログインパスワード変更 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 54053 | ログインパスワード変更 | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 54054 | ログインパスワード変更 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 54055 | ログインパスワード変更 | 顧客情報テーブルはロックされていますでエラーが発生しました | 顧客情報テーブルロックエラー |
| 54056 | ログインパスワード変更 | 顧客情報テーブル更新でエラーが発生しました | 顧客情報テーブル更新エラー |
| 54057 | ログインパスワード変更 | 顧客情報テーブル追加でエラーが発生しました | 顧客情報テーブル追加エラー |
| 54060 | ログインパスワード変更 | パスワードが一致しません | パスワード不整合 |
| 54061 | ログインパスワード変更 | ログイン属性テーブル更新でエラーが発生しました | ログイン属性テーブル更新エラー |
| 54062 | ログインパスワード変更 | ログイン属性テーブル追加でエラーが発生しました | ログイン属性テーブル追加エラー |
| 54101 | ログインパスワード変更 | コールセンターからの設定変更はできません。 | コールセンターからの設定変更不可 |
| 54997 | ログインパスワード変更 | ネットでエラーが発生しました | ネットエラー |
| 54998 | ログインパスワード変更 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 54999 | ログインパスワード変更 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 55001 | 第二暗証番号変更 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 55002 | 第二暗証番号変更 | ログインパスワード項目に誤りがあります | ログインパスワード |
| 55003 | 第二暗証番号変更 | 変更後パスワード項目に誤りがあります | 変更後パスワード |
| 55005 | 第二暗証番号変更 | 変更前と変更後の暗証番号が同一です。 | 暗証番号変化なし |
| 55006 | 第二暗証番号変更 | 入力された新暗証番号は、指定可能な文字種ではありません。ご確認の上、再度入力してください。 | 暗証番号要件エラー |
| 55007 | 第二暗証番号変更 | 暗証番号が確認用のものと一致しておりません。 | 確認用パスワードエラー |
| 55008 | 第二暗証番号変更 | 暗証番号は4桁以上で設定してください。 | パスワード長不足 |
| 55050 | 第二暗証番号変更 | 処理中にエラーが発生しました | プロシージャエラー |
| 55051 | 第二暗証番号変更 | 第二暗証番号が一致しません | 第二暗証番号不整合 |
| 55052 | 第二暗証番号変更 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 55053 | 第二暗証番号変更 | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 55054 | 第二暗証番号変更 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 55055 | 第二暗証番号変更 | 顧客情報テーブルでデータロックエラーが発生しました | 顧客情報テーブルロックエラー |
| 55056 | 第二暗証番号変更 | 顧客情報テーブル更新でエラーが発生しました | 顧客情報テーブル更新エラー |
| 55057 | 第二暗証番号変更 | 顧客情報テーブル追加でエラーが発生しました | 顧客情報テーブル追加エラー |
| 55101 | 第二暗証番号変更 | コールセンターからの設定変更はできません。 | コールセンターからの設定変更不可 |
| 55997 | 第二暗証番号変更 | ネットワークでエラーが発生しました | ネットエラー |
| 55998 | 第二暗証番号変更 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 55999 | 第二暗証番号変更 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 56001 | 勤務先携帯変更 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 56002 | 勤務先携帯変更 | 自宅電話番号項目に誤りがあります | 自宅電話番号 |
| 56003 | 勤務先携帯変更 | 請求書類番号項目に誤りがあります | 携帯番号N |
| 56004 | 勤務先携帯変更 | 勤務先項目に誤りがあります | 勤務先 |
| 56005 | 勤務先携帯変更 | 勤務先郵便番号項目に誤りがあります | 勤務先郵便番号 |
| 56006 | 勤務先携帯変更 | 勤務先住所1項目に誤りがあります | 勤務先住所1 |
| 56007 | 勤務先携帯変更 | 勤務先住所2項目に誤りがあります | 勤務先住所2 |
| 56008 | 勤務先携帯変更 | 勤務先住所3項目に誤りがあります | 勤務先住所3 |
| 56009 | 勤務先携帯変更 | 勤務先電話番号項目に誤りがあります | 勤務先電話番号 |
| 56010 | 勤務先携帯変更 | 勤務先所属部署項目に誤りがあります | 勤務先所属部署 |
| 56011 | 勤務先携帯変更 | 勤務先役職目に誤りがあります | 勤務先役職 |
| 56012 | 勤務先携帯変更 | 第二暗証番号が一致しません | 第二暗証番号 |
| 56050 | 勤務先携帯変更 | 処理中にエラーが発生しました | プロシージャエラー |
| 56051 | 勤務先携帯変更 | 第二暗証番号をお間違えです。ご確認の上、再度ご入力下さい。 | 第二暗証番号不整合 |
| 56052 | 勤務先携帯変更 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 56053 | 勤務先携帯変更 | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 56054 | 勤務先携帯変更 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 56055 | 勤務先携帯変更 | 携帯勤務先変更申込テーブルはロックされていますでエラーが発生しました | 携帯勤務先変更申込テーブルロックエラー |
| 56056 | 勤務先携帯変更 | 携帯勤務先変更申込テーブル更新でエラーが発生しました | 携帯勤務先変更申込テーブル更新エラー |
| 56057 | 勤務先携帯変更 | 携帯勤務先変更申込テーブル追加でエラーが発生しました | 携帯勤務先変更申込テーブル追加エラー |
| 56059 | 勤務先携帯変更 | 顧客情報取得でエラーが発生しました | 顧客情報取得エラー |
| 56099 | 勤務先携帯変更 | 問合せでエラーが発生しましたが発生しました | 問合せエラー |
| 56101 | 勤務先携帯変更 | 入力項目はすでに登録されています | 項目データ変化なし |
| 56991 | 勤務先携帯変更 | セッション情報レコードがありません | セッション情報レコードなし |
| 56992 | 勤務先携帯変更 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 56993 | 勤務先携帯変更 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 56994 | 勤務先携帯変更 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 56997 | 勤務先携帯変更 | ネットでエラーが発生しました | ネットエラー |
| 56998 | 勤務先携帯変更 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 56999 | 勤務先携帯変更 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 57001 | 市況情報 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 57002 | 市況情報 | ログインパスワード項目に誤りがあります | ログインパスワード |
| 57010 | 市況情報 | 指定された申込期間が不正です。 | 申込期間不正 |
| 57011 | 市況情報 | 選択された情報オプションは現在サービス停止中です。 | 情報オプション停止中 |
| 57012 | 市況情報 | 残金不足のため、このお申し込みはお受けできません。 | 余力不足 |
| 57013 | 市況情報 | 顧客拘束金ファイルに問題が発生しました | 顧客拘束金ファイル障害 |
| 57014 | 市況情報 | 顧客拘束金レコード作成でエラーが発生しました | 顧客拘束金レコード作成エラー |
| 57015 | 市況情報 | 顧客拘束金レコード更新でエラーが発生しました | 顧客拘束金レコード更新エラー |
| 57016 | 市況情報 | 日付情報ファイルに問題が発生しました | 日付情報ファイル障害 |
| 57021 | 市況情報 | 有料情報サービスは現在提供されておりません。 | 有料情報サービスなし |
| 57030 | 株価ボード | 登録完了 | CSV登録処理正常終了 |
| 57031 | 株価ボード | 既に全ページ登録済みです | 登録件数超過 |
| 57032 | 株価ボード | 読込み処理を中断しました。（CSVファイルではありません） | ファイル名不正 |
| 57033 | 株価ボード | 読込み処理を中断しました。（ファイルサイズが1MBを超過） | ファイルサイズ1MB超過 |
| 57034 | 株価ボード | 読込み処理を中断しました。（空ファイル） | ファイルサイズ不正 |
| 57035 | 株価ボード | 読込み処理を中断しました。（ファイル書込み失敗） | データ書き込みエラー |
| 57036 | 株価ボード | 読込み処理を中断しました。（ファイル読込み失敗） | ファイルオープンエラー |
| 57037 | 株価ボード | 読込み処理を中断しました。（ファイルオープン失敗） | アップロードファイルオープンエラー |
| 57038 | 株価ボード | 保存した株価ボードファイルを選択してください。 | データフォーマットエラー |
| 57039 | 株価ボード | 読込み処理を中断しました。（に誤りがありますな文字） | データ不正 |
| 57040 | 株価ボード | 読込み処理を中断しました。（銘柄コードの桁数に誤りがあります） | 銘柄コード不正 |
| 57041 | 株価ボード | コールセンタモードのため登録処理を中断します。権限に関わらず、オペレータによる登録はできません。 | コールセンタモードでの登録不可 |
| 57101 | 市況情報 | 表示対象データはありません | 銘柄マスタレコードなし |
| 57102 | 市況情報 | 銘柄マスタレコードがありません | 銘柄マスタレコードなし |
| 57151 | ポートフォリオ | 同一の銘柄コード・市場・単価を持ったデータは登録できません。 | 登録銘柄重複 |
| 57161 | ポートフォリオ | 注文の概算代金が、弊社指定の上限を超えています。 | 数量指定エラー |
| 57162 | ポートフォリオ | 銘柄コードに該当が存在しません。 | 銘柄コード指定エラー |
| 57163 | ポートフォリオ | 選択した市場では上場していません。 | 市場コード指定エラー |
| 57171 | ポートフォリオ | ポートフォリオ登録処理時でエラーが発生しました。 | ポートフォリオ登録処理エラー |
| 57201 | 計算サービス | 日計り銘柄 試算処理でエラーが発生しました | 日計り試算取得処理異常 |
| 57301 | 計算サービス | 時価の取得でエラーが発生しました。手動で単価をご入力ください。 | 時価取得エラー |
| 57302 | 計算サービス | ＤＢでエラーが発生しました(顧客手数料マスタ) | ＤＢエラー(顧客手数料マスタ) |
| 57303 | 計算サービス | ＤＢでエラーが発生しました(手数料マスタ) | ＤＢエラー(手数料マスタ) |
| 57304 | 計算サービス | ＤＢでエラーが発生しました(課税率マスタ) | ＤＢエラー(課税率マスタ) |
| 57981 | 情報サービス申込 | DBでエラーが発生しました(運用ステータス) | 運用ステータス不正 |
| 57982 | 情報サービス申込 | システムが受付可能時間外です。 | システム停止 |
| 57983 | 情報サービス申込 | 只今の時間帯は受付できません | 情報サービス申込業務停止中 |
| 57984 | 情報サービス申込 | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせください。 | 支店ロック中 |
| 57991 | 市況情報 | セッション情報レコードがありません | セッション情報レコードなし |
| 57992 | 市況情報 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 57993 | 市況情報 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 57994 | 市況情報 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 57996 | 市況情報 | ネットでエラーが発生しました | 可能額取得エラー |
| 57998 | 市況情報 | ＤＢでエラーが発生しました | ＤＢエラー |
| 57999 | 市況情報 | 接続がタイムアウトで切断しました | タイムアウト |
| 58001 | 口座開設 | 顧客登録項目に誤りがあります | 顧客登録Ｎ |
| 58002 | 口座開設 | ログインパスワードに誤りがあります | ログインパスワード |
| 58011 | 口座開設 | FXログインIDが正しく生成されませんでした。 | FXログインID生成エラー |
| 58012 | 口座開設 | ユーザIDに誤りがあります | ユーザID不正 |
| 58037 | 口座開設 | システム口座区分が不正のため金商法交付ドキュメントが取得できません。 | システム口座区分不正 |
| 58101 | 口座開設 | 入力不備がありますので修正してください。(インスタンスに誤りがあります) | インスタンスエラー |
| 58102 | 口座開設 | 入力不備がありますので修正してください。(文字列長に誤りがあります) | 文字列長エラー |
| 58103 | 口座開設 | 入力不備がありますので修正してください。(数値に誤りがあります) | 数値チェックエラー |
| 58104 | 口座開設 | 入力不備がありますので修正してください。(省略不可) | NULLチェックエラー |
| 58111 | 口座開設 | 入力不備がありますので修正してください。(本人職業・内部者組合せに誤りがあります) | 本人職業・内部者組合せエラー |
| 58112 | 口座開設 | 入力不備がありますので修正してください。(世帯主職業・内部者組合せに誤りがあります) | 世帯主職業・内部者組合せエラー |
| 58113 | 口座開設 | 入力不備がありますので修正してください。(職業・収入組合せに誤りがあります) | 職業・収入組合せエラー |
| 58114 | 口座開設 | 入力不備がありますので修正してください。(振込先・配当金受取組合せに誤りがあります) | 振込先・配当金受取組合せエラー |
| 58900 | 口座開設 | 現在 口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | 総合口座開設申込中 |
| 58901 | 口座開設 | 現在 信用口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | 信用口座開設申込中 |
| 58902 | 口座開設 | 現在 先物・オプション口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | 先物・オプション口座開設申込中 |
| 58903 | 口座開設 | 現在 立花くりっく365口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | FX口座開設申込中 |
| 58904 | 口座開設 | 現在 NISA口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | NISA口座開設申込中 |
| 58905 | 口座開設 | 現在 お子さま口座の開設をお申込中のため、新たにお申し込みをお受けする事はできません。 | お子さま口座開設申込中 |
| 58950 | 住所検索 | 検索用の郵便番号は、3桁以上で入力してください。 | 郵便番号３桁未満 |
| 58951 | 住所検索 | 検索用の郵便番号には、数値を入力してください。 | 郵便番号不正 |
| 58998 | 口座開設 | ＤＢでエラーが発生しました | ＤＢエラー |
| 58999 | 口座開設 | 接続がタイムアウトで切断しました | タイムアウト |
| 59037 | 資産履歴 | システム口座区分が不正のため金商法交付ドキュメントが取得できません。 | システム口座区分不正 |
| 59101 | 資産履歴 | 既に電子交付申込中のため、新たにお申し込みをお受けする事はできません。 | 電子交付申込中 |
| 59301 | NISAロールオーバー申込 | 銘柄コードが正しくありません。 | 銘柄なし |
| 59302 | NISAロールオーバー申込 | ロールオーバー数量がありません。 | ロールオーバー数なし |
| 59303 | NISAロールオーバー申込 | 銘柄コードが正しくありません。 | 銘柄コード不正 |
| 59304 | NISAロールオーバー申込 | ロールオーバー数量が正しくありません。売買単位に則した数値を入力してください。 | ロールオーバー数不正 |
| 59305 | NISAロールオーバー申込 | すでにロールオーバー申込が行われています。再度申し込む場合は一度取り消してください。 | ロールオーバー申込重複 |
| 59306 | NISAロールオーバー申込 | ロールオーバー数量が正しくありません。1つ以上の銘柄を申し込んでください。 | ロールオーバー対象無指定 |
| 59307 | NISAロールオーバー申込 | 対象のレコードが存在しません。 | 更新対象レコードなし |
| 59308 | NISAロールオーバー申込 | 更新内容の値で既に更新されています。 | 更新済みエラー |
| 59309 | NISAロールオーバー申込 | 受付番号の取得に失敗しました。 | 受付番号不正 |
| 59991 | 資産履歴 | セッション情報レコードがありません | セッション情報レコードなし |
| 59992 | 資産履歴 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 59993 | 資産履歴 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 59994 | 資産履歴 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 59998 | 資産履歴 | ＤＢでエラーが発生しました | ＤＢエラー |
| 59999 | 資産履歴 | 接続がタイムアウトで切断しました | タイムアウト |
| 60001 | 携帯パラメータ | 銘柄選択ラジオボタンは必須入力です。 | 銘柄未選択 |
| 60002 | 携帯パラメータ | 対象注文が選択されていません。 | 注文未選択 |
| 60003 | 携帯パラメータ | 対象建玉が選択されていません。 | 建玉未選択 |
| 60004 | 携帯パラメータ | 対象商品が選択されていません。 | 先物商品 |
| 60006 | 携帯パラメータ | プット・コールを選択して下さい。 | OP区分 |
| 60007 | 携帯パラメータ | 権利行使価格が入力されていません。 | 権利行使価格 |
| 60008 | 携帯パラメータ | 取消対象とする出勤日が選択されていません。 | 対象出金日 |
| 60009 | 携帯パラメータ | 権利行使価格に誤りがあります | 権利行使価格不正 |
| 60011 | 携帯パラメータ | 銘柄コードは必須入力です | 銘柄コード不正 |
| 60012 | 携帯パラメータ | 文字数に誤りがあります | 銘柄コード不正 |
| 60013 | 携帯パラメータ | 正しく入力して下さい | 銘柄コード不正 |
| 60014 | 携帯パラメータ | ご指定の銘柄は見つかりません. | 銘柄コード不正 |
| 60015 | 携帯パラメータ | 現引現渡済の注文は訂正できません。取消を行ってから再度行ってください。 | 現引現渡訂正 |
| 60016 | 携帯パラメータ | ご指定の銘柄は、上場されておりません。 | 銘柄コード不正 |
| 60017 | 携帯パラメータ | ご指定の銘柄の買付は、弊社ではお取扱いできません | 銘柄コード不正(現物買付) |
| 60018 | 携帯パラメータ | ご指定の銘柄は、弊社ではお取扱いできません | 銘柄コード不正(信用新規) |
| 60019 | 携帯パラメータ | ご指定の銘柄の買付は、弊社ではお取扱いできません | 銘柄コード不正(現物買付) |
| 60020 | 携帯パラメータ | ご指定の銘柄は、弊社ではお取扱いできません | 銘柄コード不正(信用新規) |
| 70001 | 情報系 | ただいま当該市場の情報配信を停止しております | 配信規制 |
| 70002 | 情報系 | リアル情報に遅延が発生しています。ご注意ください。 | QNFS障害 |
| 70003 | 情報系 | 決算情報に遅延が発生しています。ご注意ください。 | JIJI障害 |
| 84304 | 株式一括取消 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 84980 | 株式一括取消 | 取消できる注文がありません | 取消可能注文なし |
| 84991 | 株式一括取消 | セッション情報レコードがありません | セッション情報レコードなし |
| 84992 | 株式一括取消 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 84993 | 株式一括取消 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 84994 | 株式一括取消 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 84997 | 株式一括取消 | ネットでエラーが発生しました | ネットエラー |
| 84998 | 株式一括取消 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 84999 | 株式一括取消 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 85304 | 株式一括返済 | 第二暗証番号が誤っています | 顧客マスタ.第二パスワード不一致 |
| 85980 | 株式一括返済 | 返済できる建玉がありません | 返済可能建玉なし |
| 85991 | 株式一括返済 | セッション情報レコードがありません | セッション情報レコードなし |
| 85992 | 株式一括返済 | セッション情報レコードファイルに問題が発生しました | セッション情報レコードファイル障害 |
| 85993 | 株式一括返済 | セッション情報レコード更新でエラーが発生しました | セッション情報レコード更新エラー |
| 85994 | 株式一括返済 | ボタンが２回以上押されたた可能性があります。注文状況照会をご確認下さい。 | 注文二重送信エラー |
| 85997 | 株式一括返済 | ネットでエラーが発生しました | ネットエラー |
| 85998 | 株式一括返済 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 85999 | 株式一括返済 | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 100001 | 管理者ログイン | 管理者コードに誤りがあります | 管理者コード不正 |
| 100002 | 管理者ログイン | パスワードが正しくありません | パスワード不正 |
| 100003 | 管理者ログイン | ユーザタイプに誤りがあります | ユーザタイプ不正 |
| 100005 | 管理者ログイン | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 100006 | 管理者ログイン | ダミーセッションＩＤに誤りがあります | ダミーセッションＩＤ不正 |
| 100020 | 管理者ログイン | ダミーセッションファイルに問題があります | ダミーセッションファイル障害 |
| 100021 | 管理者ログイン | ダミーセッションにデータがありません | ダミーセッションレコードなし |
| 100033 | 管理者ログイン | 管理者マスタログインはロックされています | 管理者マスタログインロック |
| 100034 | 管理者ログイン | 管理者マスタログインができません | 管理者マスタログインＮＧ |
| 100035 | 管理者ログイン | 管理者マスタパスワードが間違っています | 管理者マスタパスワード不一致 |
| 100040 | 管理者ログイン | システム設定ファイルに問題があります | システム設定ファイル障害 |
| 100041 | 管理者ログイン | システム設定にデータがありません | システム設定レコードなし |
| 100045 | 管理者ログイン | BAD_IPファイルに問題があります | BAD_IPファイル障害 |
| 100046 | 管理者ログイン | BAD_IPにデータ作成でエラーが発生しました | BAD_IPレコード作成エラー |
| 100047 | 管理者ログイン | BAD_IP許可件数を超えています | BAD_IP許可件数オーバー |
| 100050 | 管理者ログイン | 管理者セッション情報ファイルに問題があります | 管理者セッション情報ファイル障害 |
| 100051 | 管理者ログイン | 管理者セッション情報にデータがありません | 管理者セッション情報レコードなし |
| 100052 | 管理者ログイン | 管理者セッション情報のデータ更新でエラーが発生しました | 管理者セッション情報レコード更新エラー |
| 100053 | 管理者ログイン | 管理者セッション情報にデータ作成でエラーが発生しました | 管理者セッション情報レコード作成エラー |
| 100054 | 管理者ログイン | 管理者セッションＩＤ生成でエラーが発生しました | 管理者セッションＩＤ生成エラー |
| 100055 | 管理者ログイン | 管理者マスタファイルに問題があります | 管理者マスタファイル障害 |
| 100056 | 管理者ログイン | 管理者マスタにデータがありません | 管理者マスタレコードなし |
| 100057 | 管理者ログイン | 管理者マスタのデータ更新でエラーが発生しました | 管理者マスタレコード更新エラー |
| 100060 | 管理者ログイン | 管理者グループマスタファイルに問題があります | 管理者グループマスタファイル障害 |
| 100061 | 管理者ログイン | 管理者グループマスタにデータがありません | 管理者グループマスタレコードなし |
| 100062 | 管理者ログイン | 管理者グループマスタのデータ更新でエラーが発生しました | 管理者グループマスタレコード更新エラー |
| 100063 | 管理者ログイン | 管理者グループ権限ファイルに問題があります | 管理者グループ権限ファイル障害 |
| 100065 | 管理者ログイン | 管理者グループ権限のデータ更新でエラーが発生しました | 管理者グループ権限レコード更新エラー |
| 100070 | 管理者ログイン | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 100071 | 管理者ログイン | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 100997 | 管理者ログイン | ネットワークでエラーが発生しました | ネットワークエラー |
| 100998 | 管理者ログイン | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 101007 | メインメニュー | 参照権限でエラーが発生しました | 参照権限エラー |
| 101008 | メインメニュー | 更新権限でエラーが発生しました | 更新権限エラー |
| 101009 | メインメニュー | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 101998 | メインメニュー | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 102007 | サブメニュー | 参照権限でエラーが発生しました | 参照権限エラー |
| 102008 | サブメニュー | 更新権限でエラーが発生しました | 更新権限エラー |
| 102009 | サブメニュー | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 102010 | サブメニュー | 入力時間外です | 入力時間外 |
| 102601 | サブメニュー | サービス停止中です | 閉局中 |
| 102998 | サブメニュー | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 110002 | 顧客基本情報問合せ | パスワードが正しくありません | パスワード不正 |
| 110003 | 顧客基本情報問合せ | システム権限がありません | システム権限エラー |
| 110007 | 顧客基本情報問合せ | 参照権限でエラーが発生しました | 参照権限エラー |
| 110008 | 顧客基本情報問合せ | 更新権限でエラーが発生しました | 更新権限エラー |
| 110009 | 顧客基本情報問合せ | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 110020 | 顧客基本情報問合せ | 顧客情報取得でエラーが発生しました | 顧客情報取得エラー |
| 110021 | 顧客基本情報問合せ | ロック顧客取得でエラーが発生しました | ロック顧客取得エラー |
| 110022 | 顧客基本情報問合せ | USER管理取得でエラーが発生しました | USER管理取得エラー |
| 110023 | 顧客基本情報問合せ | インサイダー情報取得でエラーが発生しました | インサイダー情報取得エラー |
| 110024 | 顧客基本情報問合せ | 電子交付マスタ取得でエラーが発生しました | 電子交付マスタ取得エラー |
| 110030 | 顧客基本情報問合せ | 該当する顧客がありません | 該当顧客なし |
| 110401 | 顧客基本情報問合せ | 業務接続番号取得でエラーが発生しました | 業務接続番号取得エラー |
| 110998 | 顧客基本情報問合せ | ＤＢでエラーが発生しました | ＤＢエラー |
| 112002 | メッセージ機能 | パスワードが正しくありません | パスワード不正 |
| 112003 | メッセージ機能 | システム権限がありません | システム権限エラー |
| 112007 | メッセージ機能 | 参照権限でエラーが発生しました | 参照権限エラー |
| 112008 | メッセージ機能 | 更新権限でエラーが発生しました | 更新権限エラー |
| 112009 | メッセージ機能 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 112011 | プライベートインフォメーション | アップロードファイルを選択しなおしてください | アップロードファイル不正 |
| 112012 | プライベートインフォメーション | ファイルのアップロード処理が異常終了しました | ファイルアップロードエラー |
| 112013 | プライベートインフォメーション | ファイルのアップロード処理が異常終了しました | アップロードファイルオープンエラー |
| 112014 | プライベートインフォメーション | ファイルに誤ったフォーマットのレコードが存在するため、処理を中断します | アップロードファイルフォーマットエラー |
| 112020 | プライベートインフォメーション | 顧客が登録されていません | 顧客マスタレコードなし |
| 112021 | プライベートインフォメーション | プライベートインフォメーションが登録されていません | PI_マスタレコードなし |
| 112022 | プライベートインフォメーション | PI_ダイレクトが登録されていません | PI_ダイレクトレコードなし |
| 112030 | プライベートインフォメーション | PI_マスタ取得でエラーが発生しました | PI_マスタ取得SQLエラー |
| 112050 | プライベートインフォメーション | 処理でエラーが発生しました | プロシージャエラー |
| 112051 | プライベートインフォメーション | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 112052 | プライベートインフォメーション | PI_通番採番でエラーが発生しました | PI_通番採番エラー |
| 112053 | プライベートインフォメーション | PI_マスタのデータロックでエラーが発生しました | PI_マスタレコードロックエラー |
| 112054 | プライベートインフォメーション | PI_ダイレクトのデータロックでエラーが発生しました | PI_ダイレクトレコードロックエラー |
| 112056 | プライベートインフォメーション | PI_マスタにデータ作成でエラーが発生しました | PI_マスタレコード作成エラー |
| 112057 | プライベートインフォメーション | PI_表示条件のデータ作成でエラーが発生しました | PI_ダイレクトレコード作成エラー |
| 112058 | プライベートインフォメーション | PI_ダイレクトのデータ作成でエラーが発生しました | PI_ダイレクト一時テーブルレコード作成エラー |
| 112059 | プライベートインフォメーション | PI_マスタのデータ更新でエラーが発生しました | PI_マスタレコード更新エラー |
| 112061 | プライベートインフォメーション | PI_ダイレクトのデータ更新でエラーが発生しました | PI_ダイレクトレコード更新エラー |
| 112062 | プライベートインフォメーション | PI_マスタのデータ削除でエラーが発生しました | PI_マスタレコード削除エラー |
| 112064 | プライベートインフォメーション | PI_ダイレクトのデータ削除でエラーが発生しました | PI_ダイレクトレコード削除エラー |
| 112101 | メール設定 | 入力されたレコードキーは既に存在します | レコード一意制約エラー |
| 112102 | メール設定 | 入力されたレコードキーが存在しません | レコードなしエラー |
| 112201 | 連絡管理 | 入力された検索件名に誤りがあります | 検索件名不正 |
| 112202 | 連絡管理 | ダウンロードファイルのレコード件数が500件を超過しています | レコード件数超過 |
| 112401 | 連絡管理 | 業務接続番号取得でエラーが発生しました | 業務接続番号取得エラー |
| 112420 | 連絡管理 | 信用口座開設申込レコードがありません | 信用口座開設申込レコードなし |
| 112421 | 連絡管理 | 先物・オプション口座開設申込レコードがありません | 先物・オプション口座開設申込レコードなし |
| 112461 | 連絡管理 | 信用口座開設申込レコードロックでエラーが発生しました | 信用口座開設申込レコードロックエラー |
| 112465 | 連絡管理 | 先物・オプション口座開設申込レコードロックでエラーが発生しました | 先物・オプション口座開設申込レコードロックエラー |
| 112466 | 連絡管理 | 信用口座開設申込(当日)レコード作成でエラーが発生しました | 信用口座開設申込(当日)レコード作成エラー |
| 112510 | 連絡管理 | 各種届出書類請求レコードがありません | 各種届出書類請求レコードなし |
| 112520 | 連絡管理 | 各種届出書類請求レコードロックでエラーが発生しました | 各種届出書類請求レコードロックエラー |
| 112530 | 連絡管理 | 各種届出書類請求レコード更新でエラーが発生しました | 各種届出書類請求レコード更新エラー |
| 112701 | プライベートインフォメーション | 件数が500件を超えているため、ファイルを分割して、再度実行して下さい。 | レコード件数が処理限界値を越えています |
| 112702 | プライベートインフォメーション | データが重複しています | レコード重複 |
| 112703 | プライベートインフォメーション | 削除対象データが見つかりませんでした | 削除対象データなし |
| 112704 | プライベートインフォメーション | アップロードファイルのデータが正しくありません | アップロードファイルデータフォーマット不正 |
| 112705 | プライベートインフォメーション | アップロードの処理区分が正しくありません | 処理区分不正 |
| 112706 | プライベートインフォメーション | アップロード処理が全件異常終了しました | アップロード処理全件エラー |
| 112707 | プライベートインフォメーション | アップロード処理が一部異常終了しました | アップロード処理一部エラー |
| 112998 | メッセージ機能 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 113002 | 顧客勘定 | パスワードが正しくありません | パスワード不正 |
| 113007 | 顧客勘定 | 参照権限でエラーが発生しました | 参照権限エラー |
| 113008 | 顧客勘定 | 更新権限でエラーが発生しました | 更新権限エラー |
| 113009 | 顧客勘定 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 113998 | 顧客勘定 | 問合せでエラーが発生しました | ＤＢエラー |
| 114002 | 為替口座申込ステータス入力 | パスワードが正しくありません | パスワード不正 |
| 114007 | 為替口座申込ステータス入力 | 参照権限でエラーが発生しました | 参照権限エラー |
| 114008 | 為替口座申込ステータス入力 | 更新権限でエラーが発生しました | 更新権限エラー |
| 114009 | 為替口座申込ステータス入力 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 114012 | 為替口座申込ステータス入力 | 顧客登録番号に誤りがあります | 顧客登録番号不正 |
| 114013 | 為替口座申込ステータス入力 | 識別コードに誤りがあります | 識別コード不正 |
| 114014 | 為替口座申込ステータス入力 | 口座開設区分に誤りがあります | 口座開設区分不正 |
| 114050 | 為替口座申込ステータス入力 | 該当レコードが存在しません | ＦＸ口座開設申込テーブル確定レコード無し |
| 114051 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブルレコードロックでエラーが発生しました | ＦＸ口座開設申込テーブルロックエラー |
| 114052 | 為替口座申込ステータス入力 | 既に確定済です | ＦＸ口座開設申込テーブル確定済 |
| 114053 | 為替口座申込ステータス入力 | 既に当日レコードが存在している(論理矛盾) | ＦＸ口座開設申込テーブルレコード存在エラー |
| 114054 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル(当日)レコードロックでエラーが発生しました | ＦＸ口座開設申込当日レコードロックエラー |
| 114055 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル(当日)レコード更新でエラーが発生しました | ＦＸ口座開設申込当日レコード更新エラー |
| 114056 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル(当日)レコードの追加でエラーが発生しました | ＦＸ口座開設申込当日レコードインサートエラー |
| 114057 | 為替口座申込ステータス入力 | 申込採番取得でエラーが発生しました | ＦＸ口座開設申込採番取得エラー |
| 114058 | 為替口座申込ステータス入力 | でエラーが発生しましたが発生しました | ＦＸ口座開設申込その他エラー |
| 114060 | 為替口座申込ステータス入力 | 取消対象レコードが見付かりません | ＦＸ口座開設申込テーブル(取消)レコード無し |
| 114061 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル(当日)レコードロックでエラーが発生しました | ＦＸ口座開設申込テーブル(取消)確定レコードロックエラー |
| 114062 | 為替口座申込ステータス入力 | 既に確定済です | ＦＸ口座開設申込テーブル(取消)確定済 |
| 114063 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル更新でエラーが発生しました | ＦＸ口座開設申込テーブル(取消)確定レコード更新エラー |
| 114066 | 為替口座申込ステータス入力 | ＦＸ口座開設申込テーブル(取消)その他でエラーが発生しました | ＦＸ口座開設申込テーブル(取消)その他エラー |
| 114998 | 為替口座申込ステータス入力 | ＤＢでエラーが発生しました | ＤＢエラー |
| 115002 | 為替振替更新 | パスワードが正しくありません | パスワード不正 |
| 115007 | 為替振替更新 | 参照権限でエラーが発生しました | 参照権限エラー |
| 115008 | 為替振替更新 | 更新権限でエラーが発生しました | 更新権限エラー |
| 115009 | 為替振替更新 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 115011 | 為替振替更新 | 顧客登録番号に誤りがあります | 顧客登録番号不正 |
| 115012 | 為替振替更新 | 識別コードに誤りがあります | 識別コード不正 |
| 115014 | 為替振替更新 | 受付番号に誤りがあります | 受付番号 |
| 115015 | 為替振替更新 | 為替保証金口座番号に誤りがあります | 為替保証金口座番号 |
| 115016 | 為替振替更新 | 入出金番号に誤りがあります | 入出金番号 |
| 115017 | 為替振替更新 | 出入Ｃに誤りがあります | 出入Ｃ |
| 115018 | 為替振替更新 | 振替金額が0円です | 振替金額 |
| 115019 | 為替振替更新 | 振替金額に誤りがあります | 振替金額 |
| 115020 | 為替振替更新 | 振替日に誤りがあります | 振替日 |
| 115021 | 為替振替更新 | 振替ステータスに誤りがあります | 振替ステータス不正 |
| 115025 | 為替振替更新 | 指定された内容に問題が発生しました | パラメータ不正 |
| 115040 | 為替振替更新 | サービス別取扱レコードがありません | サービス取扱い停止(証拠金→現金)(レコードなし) |
| 115041 | 為替振替更新 | サービス別取扱レコードがありません | サービス取扱い停止(現金→証拠金)(レコードなし) |
| 115042 | 為替振替更新 | このサービスは取り扱っておりません | サービス取扱い停止(証拠金→現金) |
| 115043 | 為替振替更新 | このサービスは取り扱っておりません | サービス取扱い停止(現金→証拠金) |
| 115044 | 為替振替更新 | システム状態レコードがありません | システム状態レコードなし |
| 115045 | 為替振替更新 | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 115046 | 為替振替更新 | システム状態.サービス停止中です | システム状態.閉局 |
| 115047 | 為替振替更新 | 運用ステータスレコードがありません | 運用ステータスレコードなし |
| 115048 | 為替振替更新 | 只今の時間帯は受付できません | 運用ステータス.受付停止中 |
| 115050 | 為替振替更新 | 為替振替更新.その他でエラーが発生しました | その他エラー |
| 115055 | 為替振替更新 | 顧客金銭テーブルレコードロックでエラーが発生しました | 顧客金銭テーブルレコードロック |
| 115056 | 為替振替更新 | 対象日が顧客金銭テーブルと不整合です | 対象日不整合 |
| 115057 | 為替振替更新 | 入出力区分に誤りがあります | IOC値不正 |
| 115058 | 為替振替更新 | 顧客金銭テーブル更新でエラーが発生しました | 顧客金銭テーブル更新エラー |
| 115084 | 為替振替更新 | 為替証拠金追加でエラーが発生しました | 為替証拠金追加エラー |
| 115085 | 為替振替更新 | 為替証拠金テーブルに該当レコードが存在しません | 為替証拠金対象レコード無し |
| 115086 | 為替振替更新 | 為替証拠金追加でエラーが発生しました | 為替証拠金対象レコードロック |
| 115087 | 為替振替更新 | 為替証拠金更新でエラーが発生しました | 為替証拠金更新エラー |
| 115088 | 為替振替更新 | 振替ステータスに誤りがあります | 振替ステータス不正 |
| 115089 | 為替振替更新 | 為替証拠金振替または顧客マスタデータが存在しません | 為替証拠金振替または顧客マスタデータ無し |
| 115090 | 為替振替更新 | 為替証拠金振替または顧客マスタデータ取得でエラーが発生しました | 為替証拠金振替または顧客マスタ取得エラー |
| 115091 | 為替振替更新 | 対象レコードは既に削除済または決済完了済です | 為替証拠金振替レコード状態エラー |
| 115092 | 為替振替更新 | 口座管理データが存在しません | 口座管理データ無し |
| 115093 | 為替振替更新 | 口座管理データ取得でエラーが発生しました | 口座管理取得エラー |
| 115998 | 為替振替更新 | ＤＢでエラーが発生しました | ＤＢエラー |
| 116002 | 為替振替アップロード | パスワードが正しくありません | パスワード不正 |
| 116007 | 為替振替アップロード | 参照権限でエラーが発生しました | 参照権限エラー |
| 116008 | 為替振替アップロード | 更新権限でエラーが発生しました | 更新権限エラー |
| 116009 | 為替振替アップロード | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 116011 | 為替振替アップロード | 顧客登録番号に誤りがあります | 顧客登録番号不正 |
| 116012 | 為替振替アップロード | 識別コードに誤りがあります | 識別コード不正 |
| 116014 | 為替振替アップロード | 受付番号に誤りがあります | 受付番号 |
| 116015 | 為替振替アップロード | 為替保証金口座番号に誤りがあります | 為替保証金口座番号 |
| 116016 | 為替振替アップロード | 入出金番号に誤りがあります | 入出金番号 |
| 116017 | 為替振替アップロード | 出入Ｃに誤りがあります | 出入Ｃ |
| 116018 | 為替振替アップロード | 振替金額が0円です | 振替金額 |
| 116019 | 為替振替アップロード | 振替金額に誤りがあります | 振替金額 |
| 116020 | 為替振替アップロード | 振替日に誤りがあります | 振替日 |
| 116030 | 為替振替アップロード | 内部ファイルオープンでエラーが発生しました | ファイルオープンエラー |
| 116031 | 為替振替アップロード | 内部ファイル書込でエラーが発生しました | ファイル書込エラー |
| 116032 | 為替振替アップロード | 内部ファイル読込でエラーが発生しました | ファイル読込エラー |
| 116033 | 為替振替アップロード | データに誤りがあります | ファイルデータ不正 |
| 116035 | 為替振替アップロード | 1件以上の個別データでエラーが発生しました | 個別エラーあり |
| 116040 | 為替振替アップロード | サービス別取扱レコードがありません | サービス取扱い停止(証拠金→現金)(レコードなし) |
| 116041 | 為替振替アップロード | サービス別取扱レコードがありません | サービス取扱い停止(現金→証拠金)(レコードなし) |
| 116042 | 為替振替アップロード | このサービスは取り扱っておりません | サービス取扱い停止(証拠金→現金) |
| 116043 | 為替振替アップロード | このサービスは取り扱っておりません | サービス取扱い停止(現金→証拠金) |
| 116044 | 為替振替アップロード | システム状態レコードがありません | システム状態レコードなし |
| 116045 | 為替振替アップロード | システムが受付可能時間外です。 | システム状態.ログイン不許可 |
| 116046 | 為替振替アップロード | システムが受付可能時間外です。 | システム状態.閉局 |
| 116047 | 為替振替アップロード | 運用ステータスレコードがありません | 運用ステータスレコードなし |
| 116048 | 為替振替アップロード | 只今の時間帯は受付できません | 運用ステータス.受付停止中 |
| 116050 | 為替振替アップロード | その他でエラーが発生しました | その他エラー |
| 116055 | 為替振替アップロード | 顧客金銭テーブルレコードロックでエラーが発生しました | 顧客金銭テーブルレコードロック |
| 116056 | 為替振替アップロード | 対象日が顧客金銭テーブルと不整合です | 対象日不整合 |
| 116057 | 為替振替アップロード | 入出力区分に誤りがあります | IOC値不正 |
| 116058 | 為替振替アップロード | 顧客金銭テーブル更新でエラーが発生しました | 顧客金銭テーブル更新エラー |
| 116084 | 為替振替アップロード | 為替証拠金追加でエラーが発生しました | 為替証拠金追加エラー |
| 116085 | 為替振替アップロード | 為替証拠金テーブルに該当レコードが存在しません | 為替証拠金対象レコード無し |
| 116086 | 為替振替アップロード | 為替証拠金追加でエラーが発生しました | 為替証拠金対象レコードロック |
| 116087 | 為替振替アップロード | 為替証拠金更新でエラーが発生しました | 為替証拠金更新エラー |
| 116088 | 為替振替アップロード | 対象レコードは既に受付済です | 為替証拠金対象レコード結果受信済 |
| 116089 | 為替振替アップロード | 為替証拠金振替または顧客マスタデータが存在しません | 為替証拠金振替または顧客マスタデータ無し |
| 116090 | 為替振替アップロード | 為替証拠金振替または顧客マスタデータ取得でエラーが発生しました | 為替証拠金振替または顧客マスタ取得エラー |
| 116091 | 為替振替アップロード | 対象レコードは既に削除済です | 為替証拠金振替レコード削除済エラー |
| 116092 | 為替振替アップロード | 口座管理データが存在しません | 口座管理データ無し |
| 116093 | 為替振替アップロード | 口座管理データ取得でエラーが発生しました | 口座管理取得エラー |
| 116094 | 為替振替アップロード | ロック顧客ファイルに問題があります | ロック顧客ファイル障害 |
| 116095 | 為替振替アップロード | 現在、お客様の口座には、お取引制限がかかっています。コールセンターまでお問い合わせ下さい。 | ロック顧客該当エラー |
| 116096 | 為替振替アップロード | 余力制御レコード取得でエラーが発生しました | 余力制御レコード取得エラー |
| 116097 | 為替振替アップロード | 余力出金停止中です | 余力出金停止 |
| 116098 | 為替振替アップロード | 余力.追証未入金有り | 余力追証未入金有り |
| 116099 | 為替振替アップロード | 二階建出金チェックでエラーが発生しました | 二階建出金チェックエラー |
| 116100 | 為替振替アップロード | 二階建出金チェックファイルに問題が発生しました | 二階建出金チェックファイル障害 |
| 116101 | 為替振替アップロード | 当日保証金取引レコード作成でエラーが発生しました | 当日保証金取引レコード作成エラー |
| 116106 | 為替振替アップロード | 余力.取引停止 | 余力取引停止 |
| 116107 | 為替振替アップロード | 指定された入出金番号は既に登録済みです | 為替証拠金振替二重登録 |
| 116998 | 為替振替アップロード | ＤＢでエラーが発生しました | ＤＢエラー |
| 120002 | 顧客銘柄別取引停止 | パスワードが正しくありません | パスワード不正 |
| 120003 | 顧客銘柄別取引停止 | システム権限がありません | システム権限エラー |
| 120007 | 顧客銘柄別取引停止 | 参照権限でエラーが発生しました | 参照権限エラー |
| 120008 | 顧客銘柄別取引停止 | 更新権限でエラーが発生しました | 更新権限エラー |
| 120009 | 顧客銘柄別取引停止 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 120011 | 顧客銘柄別取引停止 | 商品種別に誤りがあります | 商品種別不正 |
| 120020 | 顧客銘柄別取引停止 | 顧客・銘柄別取引停止情報が登録されていません | 顧客・銘柄別取引停止レコードなし |
| 120021 | 顧客銘柄別取引停止 | 顧客が登録されていません | 顧客マスタレコードなし |
| 120022 | 顧客銘柄別取引停止 | 銘柄が登録されていません | 銘柄マスタレコードなし |
| 120030 | 顧客銘柄別取引停止 | 該当データあり | 該当データあり |
| 120050 | 顧客銘柄別取引停止 | プロシージャでエラーが発生しました | プロシージャエラー |
| 120051 | 顧客銘柄別取引停止 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 120053 | 顧客銘柄別取引停止 | 顧客・銘柄別取引停止のデータロックでエラーが発生しました | 顧客・銘柄別取引停止レコードロックエラー |
| 120054 | 顧客銘柄別取引停止 | 顧客・銘柄別取引停止のデータ作成でエラーが発生しました | 顧客・銘柄別取引停止レコード作成エラー |
| 120055 | 顧客銘柄別取引停止 | 顧客・銘柄別取引停止のデータ更新でエラーが発生しました | 顧客・銘柄別取引停止レコード更新エラー |
| 120056 | 顧客銘柄別取引停止 | 顧客・銘柄別取引停止のデータ削除でエラーが発生しました | 顧客・銘柄別取引停止レコード削除エラー |
| 120998 | 顧客銘柄別取引停止 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 121002 | 株式 銘柄条件 | パスワードが正しくありません | パスワード不正 |
| 121003 | 株式 銘柄条件 | システム権限がありません | システム権限エラー |
| 121007 | 株式 銘柄条件 | 参照権限でエラーが発生しました | 参照権限エラー |
| 121008 | 株式 銘柄条件 | 更新権限でエラーが発生しました | 更新権限エラー |
| 121009 | 株式 銘柄条件 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 121010 | 株式 銘柄条件 | 入力時間外です | 入力時間外 |
| 121012 | 株式 銘柄条件 | 実施日に誤りがあります | 実施日不正 |
| 121013 | 株式 銘柄条件 | 機能タイプ値に誤りがありますでエラーが発生しました | 機能タイプ(取引停止?値段情報)不正 |
| 121020 | 株式 銘柄条件 | 銘柄マスタ（株式）が登録されていません | 銘柄マスタ（株式）レコードなし |
| 121021 | 株式 銘柄条件 | 銘柄市場マスタ（株式）が登録されていません | 銘柄市場マスタ（株式）レコードなし |
| 121022 | 株式 銘柄条件 | 銘柄別・市場別規制（株式）が登録されていません | 銘柄別・市場別規制（株式）レコードなし |
| 121023 | 株式 銘柄条件 | システム別設定にデータがありません | システム別設定レコードなし |
| 121050 | 株式 銘柄条件 | プロシージャでエラーが発生しました | プロシージャエラー |
| 121051 | 株式 銘柄条件 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 121052 | 株式 銘柄条件 | 銘柄マスタ（株式）のレコードロックでエラーが発生しました | 銘柄マスタ（株式）レコードロックエラー |
| 121053 | 株式 銘柄条件 | 銘柄市場マスタのレコードロックでエラーが発生しました | 銘柄市場マスタレコードロックエラー |
| 121054 | 株式 銘柄条件 | 銘柄別・市場別規制のレコードロックでエラーが発生しました | 銘柄別・市場別規制レコードロックエラー |
| 121055 | 株式 銘柄条件 | 銘柄予定マスタのレコードロックでエラーが発生しました | 銘柄予定マスタレコードロックエラー |
| 121056 | 株式 銘柄条件 | 保証金マスタのレコードロックでエラーが発生しました | 保証金マスタレコードロックエラー |
| 121057 | 株式 銘柄条件 | 代用掛目のレコードロックでエラーが発生しました | 代用掛目レコードロックエラー |
| 121060 | 株式 銘柄条件 | 銘柄別・市場別規制レコード作成でエラーが発生しました | 銘柄別・市場別規制レコード作成エラー |
| 121061 | 株式 銘柄条件 | 銘柄予定マスタレコード作成でエラーが発生しました | 銘柄予定マスタレコード作成エラー |
| 121062 | 株式 銘柄条件 | 保証金マスタレコード作成でエラーが発生しました | 保証金マスタレコード作成エラー |
| 121063 | 株式 銘柄条件 | 代用掛目レコード作成でエラーが発生しました | 代用掛目レコード作成エラー |
| 121070 | 株式 銘柄条件 | 銘柄マスタ（株式）レコード更新でエラーが発生しました | 銘柄マスタ（株式）レコード更新エラー |
| 121071 | 株式 銘柄条件 | 銘柄市場マスタレコード更新でエラーが発生しました | 銘柄市場マスタレコード更新エラー |
| 121072 | 株式 銘柄条件 | 銘柄別・市場別規制レコード更新でエラーが発生しました | 銘柄別・市場別規制レコード更新エラー |
| 121073 | 株式 銘柄条件 | 銘柄予定マスタレコード更新でエラーが発生しました | 銘柄予定マスタレコード更新エラー |
| 121074 | 株式 銘柄条件 | 保証金マスタレコード更新でエラーが発生しました | 保証金マスタレコード更新エラー |
| 121075 | 株式 銘柄条件 | 代用掛目レコード更新でエラーが発生しました | 代用掛目レコード更新エラー |
| 121080 | 株式 銘柄条件 | 銘柄マスタ（株式）レコード取得でエラーが発生しました | 銘柄マスタ（株式）レコード取得エラー |
| 121081 | 株式 銘柄条件 | 銘柄市場マスタレコード取得でエラーが発生しました | 銘柄市場マスタレコード取得エラー |
| 121082 | 株式 銘柄条件 | 銘柄別・市場別規制レコード取得でエラーが発生しました | 銘柄別・市場別規制レコード取得エラー |
| 121997 | 株式 銘柄条件 | ネットワークでエラーが発生しました | ネットワークエラー |
| 121998 | 株式 銘柄条件 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 122002 | 株式 注文 | パスワードが正しくありません | パスワード不正 |
| 122003 | 株式 注文 | システム権限がありません | システム権限エラー |
| 122007 | 株式 注文 | 参照権限でエラーが発生しました | 参照権限エラー |
| 122008 | 株式 注文 | 更新権限でエラーが発生しました | 更新権限エラー |
| 122009 | 株式 注文 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 122010 | 株式 注文 | 入力時間外です | 入力時間外 |
| 122020 | 株式 注文 | 注文がありません | 該当注文なし |
| 122021 | 株式 注文 | 約定がありません | 該当約定なし |
| 122025 | 株式 注文 | 銘柄マスタ（株式）が登録されていません | 銘柄マスタ（株式）レコードなし |
| 122026 | 株式 注文 | 運用ステータス_株式にデータが登録されていません | 運用ステータス_株式レコードなし |
| 122040 | 株式 注文 | 失効数量を超えています | 失効数量オーバー |
| 122050 | 株式 注文 | プロシージャでエラーが発生しました | プロシージャエラー |
| 122060 | 株式 注文 | 出来時刻でエラーが発生しました | 出来時刻エラー |
| 122061 | 株式 注文 | 出来を超えています | 出来オーバー |
| 122090 | 株式 注文 | 運用ステータス_株式のレコードロックでエラーが発生しました | 運用ステータス_株式レコードロックエラー |
| 122091 | 株式 注文 | 運用ステータス_株式のデータ更新でエラーが発生しました | 運用ステータス_株式レコード更新エラー |
| 122092 | 株式 注文 | 運用ステータス_株式にデータ取得でエラーが発生しました | 運用ステータス_株式レコード取得エラー |
| 122121 | 株式 注文 | 該当する注文がありません | 失効対象注文該当なし |
| 122122 | 株式 注文 | 株式手動失効管理にデータがありません | 株式手動失効管理レコードなし |
| 122123 | 株式 注文 | 株式手動失効にデータがありません | 株式手動失効レコードなし |
| 122130 | 株式 注文 | 株式手動失効管理にデータ挿入でエラーが発生しました | 株式手動失効管理レコード挿入エラー |
| 122131 | 株式 注文 | 株式手動失効管理のレコードロックでエラーが発生しました | 株式手動失効管理レコードロックエラー |
| 122132 | 株式 注文 | 株式手動失効管理のデータ更新でエラーが発生しました | 株式手動失効管理レコード更新エラー |
| 122133 | 株式 注文 | 株式手動失効にデータ挿入でエラーが発生しました | 株式手動失効レコード挿入エラー |
| 122134 | 株式 注文 | 株式手動失効のレコードロックでエラーが発生しました | 株式手動失効レコードロックエラー |
| 122135 | 株式 注文 | 株式手動失効のデータ更新でエラーが発生しました | 株式手動失効レコード更新エラー |
| 122199 | 株式 注文 | 処理スレッドの構成でエラーが発生しました | スレッド構成エラー |
| 122301 | 株式 注文 | 注文アップロード管理にデータがありません | 注文アップロード管理レコード無し |
| 122302 | 株式 注文 | 注文アップロード管理のレコードロックでエラーが発生しました | 注文アップロード管理レコードロック |
| 122303 | 株式 注文 | 注文アップロード管理にデータ挿入でエラーが発生しました | 注文アップロード管理レコード挿入 |
| 122304 | 株式 注文 | 注文アップロード管理のデータ更新でエラーが発生しました | 注文アップロード管理レコード更新 |
| 122305 | 株式 注文 | 注文アップロード管理のデータ取得でエラーが発生しました | 注文アップロード管理レコード取得 |
| 122306 | 株式 注文 | 注文アップロードにデータがありません | 注文アップロードレコード無し |
| 122307 | 株式 注文 | 注文アップロードのレコードロックでエラーが発生しました | 注文アップロードレコードロック |
| 122308 | 株式 注文 | 注文アップロードにデータ挿入でエラーが発生しました | 注文アップロードレコード挿入 |
| 122309 | 株式 注文 | 注文アップロードのデータ更新でエラーが発生しました | 注文アップロードレコード更新 |
| 122310 | 株式 注文 | 注文アップロードのデータ取得でエラーが発生しました | 注文アップロードレコード取得 |
| 122350 | 株式 注文 | 商品種別に誤りがあります | 商品種別不正 |
| 122351 | 株式 注文 | 処理区分に誤りがあります | 処理区分不正 |
| 122352 | 株式 注文 | 市場コードに誤りがあります | 市場コード不正 |
| 122353 | 株式 注文 | 売買区分に誤りがあります | 売買区分不正 |
| 122354 | 株式 注文 | 建日種類に誤りがあります | 建日種類不正 |
| 122355 | 株式 注文 | 現金信用区分と弁済区分で矛盾があります | 現金信用区分と弁済区分で矛盾 |
| 122356 | 株式 注文 | 建玉がありません | 建玉なし |
| 122601 | 株式 注文 | 株式閉局 | 株式閉局 |
| 122997 | 株式 注文 | ネットワークでエラーが発生しました | ネットワークエラー |
| 122998 | 株式 注文 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 123002 | 投資信託・累積投資 | パスワードが正しくありません | パスワード不正 |
| 123007 | 投資信託・累積投資 | 参照権限でエラーが発生しました | 参照権限エラー |
| 123008 | 投資信託・累積投資 | 更新権限でエラーが発生しました | 更新権限エラー |
| 123009 | 投資信託・累積投資 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 123020 | 投資信託 銘柄条件 | 銘柄マスタ(投信)にデータがありません | 銘柄マスタ(投信)レコードなし |
| 123050 | 投資信託・累積投資 | プロシージャでエラーが発生しました | プロシージャエラー |
| 123051 | 投資信託・累積投資 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 123052 | 投資信託 銘柄条件 | 銘柄マスタ（投信）のレコードロックでエラーが発生しました | 銘柄マスタ（投信）レコードロックエラー |
| 123053 | 投資信託 銘柄条件 | 銘柄マスタ（投信）のデータ更新でエラーが発生しました | 銘柄マスタ（投信）レコード更新エラー |
| 123054 | 投資信託 銘柄条件 | 銘柄マスタ（投信）のデータ取得でエラーが発生しました | 銘柄マスタ（投信）レコード取得エラー |
| 123120 | 投資信託 海外市場カレンダー | 海外市場カレンダー（投信）レコードがありません | 海外市場カレンダー（投信）レコードなし |
| 123152 | 投資信託 海外市場カレンダー | 海外市場カレンダー（投信）のレコードロックでエラーが発生しました | 海外市場カレンダー（投信）レコードロックエラー |
| 123153 | 投資信託 海外市場カレンダー | 海外市場カレンダー（投信）のデータ更新でエラーが発生しました | 海外市場カレンダー（投信）レコード更新エラー |
| 123231 | 投資信託 注文 | 取扱銘柄(投信)取得でエラーが発生しました | 取扱銘柄(投信)取得エラー |
| 123232 | 投資信託 注文 | 取扱銘柄(累投)取得でエラーが発生しました | 取扱銘柄(累投)取得エラー |
| 123320 | 投資信託 銘柄マスタ | 銘柄マスタ(累投)にデータがありません | 銘柄マスタ(累投)レコードなし |
| 123352 | 投資信託 銘柄マスタ | 銘柄マスタ（累投）のレコードロックでエラーが発生しました | 銘柄マスタ（累投）レコードロックエラー |
| 123353 | 投資信託 銘柄マスタ | 銘柄マスタ（累投）のデータ更新でエラーが発生しました | 銘柄マスタ（累投）レコード更新エラー |
| 123354 | 投資信託 銘柄マスタ | 銘柄マスタ（累投）にデータ取得でエラーが発生しました | 銘柄マスタ（累投）レコード取得エラー |
| 123998 | 投資信託・累積投資 | ＤＢでエラーが発生しました | ＤＢエラー |
| 124002 | 先物・ＯＰ | パスワードが正しくありません | パスワード不正 |
| 124003 | 先物・ＯＰ | システム口座区分に誤りがあります | システム口座区分不正 |
| 124007 | 先物・ＯＰ | 参照権限でエラーが発生しました | 参照権限エラー |
| 124008 | 先物・ＯＰ | 更新権限でエラーが発生しました | 更新権限エラー |
| 124009 | 先物・ＯＰ | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 124012 | 先物・ＯＰ | 実施日に誤りがあります | 実施日不正 |
| 124020 | 先物・ＯＰ | 注文がありません | 注文なし |
| 124021 | 先物・ＯＰ | 約定がありません | 約定なし |
| 124026 | 先物・ＯＰ | 運用ステータス_派生にデータが登録されていません | 運用ステータス_派生レコードなし |
| 124040 | 先物・ＯＰ | 失効数量を超えています | 失効数量オーバー |
| 124050 | 先物・ＯＰ | プロシージャでエラーが発生しました | プロシージャエラー |
| 124051 | 先物・ＯＰ | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 124060 | 先物・ＯＰ | 出来時刻でエラーが発生しました | 出来時刻エラー |
| 124061 | 先物・ＯＰ | 出来を超えています | 出来オーバー |
| 124090 | 先物・ＯＰ | 運用ステータス_派生のレコードロックでエラーが発生しました | 運用ステータス_派生レコードロックエラー |
| 124091 | 先物・ＯＰ | 運用ステータス_派生のデータ更新でエラーが発生しました | 運用ステータス_派生レコード更新エラー |
| 124092 | 先物・ＯＰ | 運用ステータス_派生のデータ取得でエラーが発生しました | 運用ステータス_派生レコード取得エラー |
| 124120 | 先物・ＯＰ | 銘柄が登録されていません | 銘柄マスタ（ＯＰ）該当なし |
| 124121 | 先物・ＯＰ | 該当する建玉がありません | 派生建玉明細該当なし |
| 124122 | 先物・ＯＰ | 行使割当管理にデータがありません | 行使割当管理レコードなし |
| 124123 | 先物・ＯＰ | 行使割当にデータがありません | 行使割当レコードなし |
| 124124 | 先物・ＯＰ | SQ日の該当日ではありません | 当日がSQ日でない |
| 124125 | 先物・ＯＰ | 対象の建玉が処理済みです | 対象の建玉が処理済み |
| 124130 | 先物・ＯＰ | 行使割当管理のデータ挿入でエラーが発生しました | 行使割当管理レコード挿入エラー |
| 124131 | 先物・ＯＰ | 行使割当管理のレコードロックでエラーが発生しました | 行使割当管理レコードロックエラー |
| 124132 | 先物・ＯＰ | 行使割当管理のデータ更新でエラーが発生しました | 行使割当管理レコード更新エラー |
| 124133 | 先物・ＯＰ | 行使割当管理レコード取得でエラーが発生しました | 行使割当管理レコード取得エラー |
| 124135 | 先物・ＯＰ | 行使割当レコード挿入でエラーが発生しました | 行使割当レコード挿入エラー |
| 124136 | 先物・ＯＰ | 行使割当レコードロックでエラーが発生しました | 行使割当レコードロックエラー |
| 124137 | 先物・ＯＰ | 行使割当レコード更新でエラーが発生しました | 行使割当レコード更新エラー |
| 124138 | 先物・ＯＰ | 行使割当レコード取得でエラーが発生しました | 行使割当レコード取得エラー |
| 124180 | 先物・ＯＰ | 内部ファイルオープンでエラーが発生しました | ファイルオープンエラー |
| 124181 | 先物・ＯＰ | 内部ファイル書込でエラーが発生しました | ファイル書込エラー |
| 124182 | 先物・ＯＰ | 内部ファイル読込でエラーが発生しました | ファイル読込エラー |
| 124183 | 先物・ＯＰ | ファイルデータが不正です | ファイルデータ不正 |
| 124184 | 先物・ＯＰ | ファイルサイズを1M以下にしてください | ファイルサイズ上限オーバー |
| 124185 | 先物・ＯＰ | ＣＳＶファイルのヘッダー項目数が不正です | ヘッダー項目数不正 |
| 124186 | 先物・ＯＰ | ＣＳＶファイルの行項目数が不正です | 行項目数不正 |
| 124187 | 先物・ＯＰ | ＣＳＶファイルの値が不正です | パラメータ不正 |
| 124199 | 先物・ＯＰ | 処理スレッドの構成でエラーが発生しました | スレッド構成エラー |
| 124220 | 先物・ＯＰ | 銘柄マスタ(先物)が登録されていません | 銘柄マスタ（先物）レコードなし |
| 124221 | 先物・ＯＰ | 銘柄マスタ(ＯＰ)が登録されていません | 銘柄マスタ（ＯＰ）レコードなし |
| 124250 | 先物・ＯＰ | 銘柄別・市場別規制（派生商品）レコードロックでエラーが発生しました | 銘柄別・市場別規制（派生商品）レコードロックエラー |
| 124251 | 先物・ＯＰ | 銘柄別・市場別規制（派生商品）レコード作成でエラーが発生しました | 銘柄別・市場別規制（派生商品）レコード作成エラー |
| 124252 | 先物・ＯＰ | 銘柄別・市場別規制（派生商品）レコード更新でエラーが発生しました | 銘柄別・市場別規制（派生商品）レコード更新エラー |
| 124253 | 先物・ＯＰ | 銘柄別・市場別規制（派生商品）レコード取得でエラーが発生しました | 銘柄別・市場別規制（派生商品）レコード取得エラー |
| 124260 | 先物・ＯＰ | 銘柄予定マスタレコードロックでエラーが発生しました | 銘柄予定マスタレコードロックエラー |
| 124261 | 先物・ＯＰ | 銘柄予定マスタレコード作成でエラーが発生しました | 銘柄予定マスタレコード作成エラー |
| 124262 | 先物・ＯＰ | 銘柄予定マスタレコード更新でエラーが発生しました | 銘柄予定マスタレコード更新エラー |
| 124601 | 先物・ＯＰ | 閉局中 | 閉局中 |
| 124997 | 先物・ＯＰ | ネットワークでエラーが発生しました | ネットワークエラー |
| 124998 | 先物・ＯＰ | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 125002 | ＩＰＯ | パスワードが正しくありません | パスワード不正 |
| 125003 | ＩＰＯ | システム権限がありません | システム権限エラー |
| 125007 | ＩＰＯ | 参照権限でエラーが発生しました | 参照権限エラー |
| 125008 | ＩＰＯ | 更新権限でエラーが発生しました | 更新権限エラー |
| 125009 | ＩＰＯ | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 125020 | ＩＰＯ | 銘柄マスタ(ＩＰＯ)が登録されていません | 銘柄マスタ（ＩＰＯ）レコードなし |
| 125050 | ＩＰＯ | プロシージャでエラーが発生しました | プロシージャエラー |
| 125051 | ＩＰＯ | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 125052 | ＩＰＯ | 銘柄マスタ（ＩＰＯ）のレコードロックでエラーが発生しました | 銘柄マスタ（ＩＰＯ）レコードロックエラー |
| 125053 | ＩＰＯ | 銘柄マスタ（ＩＰＯ）のデータ作成でエラーが発生しました | 銘柄マスタ（ＩＰＯ）レコード作成エラー |
| 125054 | ＩＰＯ | 銘柄マスタ（ＩＰＯ）のデータ更新でエラーが発生しました | 銘柄マスタ（ＩＰＯ）レコード更新エラー |
| 125055 | ＩＰＯ | 銘柄マスタ（ＩＰＯ）のデータ削除でエラーが発生しました | 銘柄マスタ（ＩＰＯ）レコード削除エラー |
| 125111 | ＩＰＯ | 抽選結果種別に誤りがあります | 抽選結果種別不正 |
| 125112 | ＩＰＯ | 銘柄コードに誤りがあります | 銘柄コード不正 |
| 125113 | ＩＰＯ | 顧客登録番号に誤りがあります | 顧客登録Ｎ不正 |
| 125114 | ＩＰＯ | 抽選結果に誤りがあります | 抽選結果不正 |
| 125115 | ＩＰＯ | 当選数量に誤りがあります | 当選数量不正 |
| 125116 | ＩＰＯ | 優先順位に誤りがあります | 優先順位不正 |
| 125117 | ＩＰＯ | 部店コードに誤りがあります | 部店コード不正 |
| 125130 | ＩＰＯ | 内部ファイルオープンでエラーが発生しました | ファイルオープンエラー |
| 125131 | ＩＰＯ | 内部ファイル書込でエラーが発生しました | ファイル書込エラー |
| 125132 | ＩＰＯ | 内部ファイル読込でエラーが発生しました | ファイル読込エラー |
| 125133 | ＩＰＯ | ファイルデータに誤りがあります | ファイルデータ不正 |
| 125134 | ＩＰＯ | ファイルサイズを1M以下にしてください | ファイルサイズ上限オーバー |
| 125135 | ＩＰＯ | ＣＳＶファイルのヘッダー項目数に誤りがあります | ヘッダー項目数不正 |
| 125136 | ＩＰＯ | ＣＳＶファイルの行項目数に誤りがあります | 行項目数不正 |
| 125151 | ＩＰＯ | IPO抽選結果管理にデータ無し | IPO抽選結果管理レコード無し |
| 125152 | ＩＰＯ | IPO抽選結果管理のレコードロックでエラーが発生しました | IPO抽選結果管理レコードロックエラー |
| 125153 | ＩＰＯ | IPO抽選結果管理のデータ挿入でエラーが発生しました | IPO抽選結果管理レコード挿入エラー |
| 125154 | ＩＰＯ | IPO抽選結果管理のデータ更新でエラーが発生しました | IPO抽選結果管理レコード更新エラー |
| 125156 | ＩＰＯ | IPO抽選結果にデータ無し | IPO抽選結果レコード無し |
| 125157 | ＩＰＯ | IPO抽選結果のレコードロックでエラーが発生しました | IPO抽選結果レコードロックエラー |
| 125158 | ＩＰＯ | IPO抽選結果のデータ挿入でエラーが発生しました | IPO抽選結果レコード挿入エラー |
| 125159 | ＩＰＯ | IPO抽選結果のデータ更新でエラーが発生しました | IPO抽選結果レコード更新エラー |
| 125161 | ＩＰＯ | IPOサマリにデータ無し | IPOサマリレコード無し |
| 125162 | ＩＰＯ | IPOサマリのレコードロックでエラーが発生しました | IPOサマリレコードロックエラー |
| 125163 | ＩＰＯ | IPOサマリのデータ挿入でエラーが発生しました | IPOサマリレコード挿入エラー |
| 125164 | ＩＰＯ | IPOサマリのデータ更新でエラーが発生しました | IPOサマリレコード更新エラー |
| 125166 | ＩＰＯ | 顧客金銭にデータ無し | 顧客金銭レコード無し |
| 125167 | ＩＰＯ | 顧客金銭のレコードロックでエラーが発生しました | 顧客金銭レコードロックエラー |
| 125168 | ＩＰＯ | 顧客拘束金にデータ無し | 顧客拘束金レコード無し |
| 125169 | ＩＰＯ | 顧客拘束金のデータはレコードロックされています | 顧客拘束金レコードロック |
| 125170 | ＩＰＯ | 顧客拘束金のデータ更新でエラーが発生しました | 顧客拘束金レコード更新エラー |
| 125180 | ＩＰＯ | 重複顧客チェックでエラーが発生しました | 顧客重複エラー |
| 125181 | ＩＰＯ | 購入申込期間（当社設定）が未設定です | 購入申込期間（当社設定）未設定 |
| 125182 | ＩＰＯ | 購入申込期間が終了しています | 購入申込期間（当社設定）終了後 |
| 125183 | ＩＰＯ | 申告済みの顧客ではありません | 申告顧客なし |
| 125184 | ＩＰＯ | 購入申込単位が未設定です | 購入申込単位未設定 |
| 125185 | ＩＰＯ | 当選数量が購入申込単位の整数倍ではありません | 当選数量が購入申込単位の倍数でない |
| 125186 | ＩＰＯ | 申告数量は当選数量より小さいです | 当選数量オーバー |
| 125187 | ＩＰＯ | 申告が同一銘柄中で重複しています | 重複申告エラー |
| 125188 | ＩＰＯ | 当選結果が既に割り当てられています | 当選結果割当済 |
| 125189 | ＩＰＯ | 買付可能額がが不足しています | 買付可能額不足 |
| 125190 | ＩＰＯ | 公開価格取得でエラーが発生しました | 公開価格取得エラー |
| 125191 | ＩＰＯ | システム口座区分取得でエラーが発生しました | システム口座区分取得エラー |
| 125192 | ＩＰＯ | 可能額取得でエラーが発生しました | 可能額取得エラー |
| 125193 | ＩＰＯ | 二階建てチェックでエラーが発生しました | 二階建てチェックエラー |
| 125194 | ＩＰＯ | 二階建てチェックファイルに問題があります | 二階建てチェックファイル障害 |
| 125199 | ＩＰＯ | 処理スレッドの構成でエラーが発生しました | スレッド構成エラー |
| 125998 | ＩＰＯ | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 126002 | サービス利用 | パスワードが正しくありません | パスワード不正 |
| 126007 | サービス利用 | 参照権限でエラーが発生しました | 参照権限エラー |
| 126008 | サービス利用 | 更新権限でエラーが発生しました | 更新権限エラー |
| 126009 | サービス利用 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 126012 | サービス利用 | 残金不足です | 余力不足 |
| 126064 | サービス利用 | 顧客登録番号に対応する顧客は登録されていません | 該当顧客情報なし |
| 126070 | サービス利用 | 情報サービス利用客レコードがありません | 情報サービス利用客レコードなし |
| 126071 | サービス利用 | 顧客拘束金レコードがありません | 顧客拘束金レコードなし |
| 126075 | サービス利用 | 情報サービス利用客レコードロックでエラーが発生しました | 情報サービス利用客レコードロックエラー |
| 126076 | サービス利用 | 顧客拘束金レコードロックでエラーが発生しました | 顧客拘束金レコードロックエラー |
| 126080 | サービス利用 | 情報サービス利用客更新でエラーが発生しました | 情報サービス利用客更新エラー |
| 126081 | サービス利用 | 顧客拘束金更新でエラーが発生しました | 顧客拘束金更新エラー |
| 126090 | サービス利用 | 情報サービス利用客作成でエラーが発生しました | 情報サービス利用客作成エラー |
| 126091 | サービス利用 | 顧客拘束金作成でエラーが発生しました | 顧客拘束金作成エラー |
| 126100 | サービス利用 | 営業日カレンダーレコードがありません | 営業日カレンダーデータ無し |
| 126998 | サービス利用 | ＤＢでエラーが発生しました | ＤＢエラー |
| 127002 | 商品・取引管理 | パスワードが正しくありません | パスワード不正 |
| 127003 | 商品・取引管理 | システム権限がありません | システム権限エラー |
| 127007 | 商品・取引管理 | 参照権限でエラーが発生しました | 参照権限エラー |
| 127008 | 商品・取引管理 | 更新権限でエラーが発生しました | 更新権限エラー |
| 127009 | 商品・取引管理 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 127025 | 商品・取引管理_注文約定件数照会 | 該当する注文約定件数集計データがありません | 注文約定件数集計該当なし |
| 127301 | 商品・取引管理_特殊注文 | 処理済み | 処理済み |
| 127302 | 商品・取引管理_特殊注文 | 有効注文数量がありません | 有効注文数量なし |
| 127304 | 商品・取引管理_特殊注文 | 受付未済 | 受付未済 |
| 127305 | 商品・取引管理_特殊注文 | 訂正取消中 | 訂正取消中 |
| 127306 | 商品・取引管理_特殊注文 | 対象レコードがありません | 対象レコードなし |
| 127601 | 商品・取引管理_手数料訂正 | 株式閉局 | 株式閉局 |
| 127602 | 商品・取引管理_手数料訂正 | 未約定でエラーが発生しました | 未約定エラー |
| 127603 | 商品・取引管理_手数料訂正 | 未全出来でエラーが発生しました | 未全出来エラー |
| 127604 | 商品・取引管理_手数料訂正 | 手数料マスタレコードがありません | 手数料マスタレコードなし |
| 127605 | 商品・取引管理_手数料訂正 | 総合手数料マスタレコードがありません | 総合手数料マスタレコードなし |
| 127720 | 商品・取引管理_ザラバ新規建停止 | システム状態レコードがありません | システム状態レコードなし |
| 127721 | 商品・取引管理_ザラバ新規建停止 | システム状態レコードロックでエラーが発生しました | システム状態レコードロックエラー |
| 127722 | 商品・取引管理_ザラバ新規建停止 | システム状態レコード更新でエラーが発生しました | システム状態レコード更新エラー |
| 127731 | 商品・取引管理_ザラバ新規建停止 | システム設定レコードロックでエラーが発生しました | システム設定レコードロックエラー |
| 127732 | 商品・取引管理_ザラバ新規建停止 | システム設定レコード更新でエラーが発生しました | システム設定レコード更新エラー |
| 127998 | 商品・取引管理 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 128003 | 手数料管理 | システム権限がありません | システム権限エラー |
| 128020 | 手数料管理 | 該当する手数料申込がありません | 手数料変更申込なし |
| 128998 | 手数料管理 | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 130002 | お知らせ | パスワードが正しくありません | パスワード不正 |
| 130003 | お知らせ | システム権限がありません | システム権限エラー |
| 130007 | お知らせ | 参照権限でエラーが発生しました | 参照権限エラー |
| 130008 | お知らせ | 更新権限でエラーが発生しました | 更新権限エラー |
| 130009 | お知らせ | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 130020 | お知らせ | お知らせにデータがありません | お知らせレコードなし |
| 130050 | お知らせ | プロシージャでエラーが発生しました | プロシージャエラー |
| 130051 | お知らせ | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 130052 | お知らせ | お知らせ通番採番でエラーが発生しました | お知らせ通番採番エラー |
| 130053 | お知らせ | お知らせのレコードロックでエラーが発生しました | お知らせレコードロックエラー |
| 130055 | お知らせ | お知らせにデータ作成でエラーが発生しました | お知らせレコード作成エラー |
| 130056 | お知らせ | お知らせ_リンクにデータ作成でエラーが発生しました | お知らせ_リンクレコード作成エラー |
| 130057 | お知らせ | お知らせのデータ更新でエラーが発生しました | お知らせレコード更新エラー |
| 130059 | お知らせ | お知らせにデータ削除でエラーが発生しました | お知らせレコード削除エラー |
| 130060 | お知らせ | お知らせ_リンクにデータ削除でエラーが発生しました | お知らせ_リンクレコード削除エラー |
| 130998 | お知らせ | ＤＢ接続でエラーが発生しました | ＤＢエラー |
| 140002 | 管理者・ドキュメント機能 | パスワードが正しくありません | パスワード不正 |
| 140003 | 管理者・ドキュメント機能 | システム権限がありません | システム権限エラー |
| 140007 | 管理者・ドキュメント機能 | 参照権限でエラーが発生しました | 参照権限エラー |
| 140008 | 管理者・ドキュメント機能 | 更新権限でエラーが発生しました | 更新権限エラー |
| 140009 | 管理者・ドキュメント機能 | 管理者グループ権限が設定されていません | 管理者グループ権限レコードなし |
| 140011 | 電子交付 | アップロードファイルを選択しなおしてください | アップロードファイル不正 |
| 140012 | 電子交付 | ファイルのアップロード処理が異常終了しました | ファイルアップロードエラー |
| 140013 | 電子交付 | ファイルのアップロード処理が異常終了しました | アップロードファイルオープンエラー |
| 140014 | 電子交付 | ファイルにに誤りがありますにデータが存在するため、処理を中断します | アップロードファイルフォーマットエラー |
| 140015 | 電子交付 | NFS上のファイルオープンに失敗しました | ターゲットファイルオープンエラー |
| 140016 | 電子交付 | NFS上のファイル書込みに失敗しました | ターゲットファイル書込みエラー |
| 140017 | 電子交付 | NFS上に同じ名前のファイルが存在するため、処理を中断します | NFS上に同名ファイルあり |
| 140021 | 電子交付 | 入力された種別コードは既に存在します | 種別コード　一意制約エラー |
| 140022 | 電子交付 | 電子鳩種別マスタ更新テーブル失敗 | 電子鳩ドキュメント種別マスタ更新エラー |
| 140023 | 電子交付 | 関連するドキュメントコードが存在するため削除できません | 電子鳩ドキュメント種別削除不可 |
| 140031 | 電子交付 | 入力されたドキュメントコードは既に存在します | ドキュメントコード_一意制約エラー |
| 140032 | 電子交付 | 電子鳩ドキュメント管理テーブル更新失敗 | 電子鳩ドキュメント管理更新エラー |
| 140033 | 電子交付 | 関連するドキュメントが存在するため削除できません | 電子鳩ドキュメントコード削除不可 |
| 140034 | 電子交付 | 関連する銘柄が存在するため削除できません | 電子鳩ドキュメントコード削除不可 |
| 140041 | 電子交付 | 入力された銘柄コードは既に存在します | 銘柄コード_一意制約エラー |
| 140042 | 電子交付 | 電子鳩銘柄コード管理テーブル更新失敗 | 電子鳩銘柄コード管理更新エラー |
| 140051 | 電子交付 | 電子鳩ドキュメント管理テーブル更新失敗 | 電子鳩ドキュメント管理更新エラー |
| 140052 | 電子交付 | ドキュメント交付履歴にデータが存在するため削除できません | 電子鳩ドキュメント削除不可 |
| 140053 | 電子交付 | サブドキュメントが存在するため削除できません | 電子鳩ドキュメント削除不可 |
| 140054 | 電子交付 | 同一ファイル名の書面が登録済みのため、登録処理を中止します | 電子鳩ドキュメント登録済み |
| 140055 | 電子交付 | ドキュメント交付履歴にデータが存在するため変更できません | 電子鳩ドキュメント変更不可 |
| 140061 | 電子交付 | 履歴アップロードの全件でエラーが発生しました終了しました | 履歴アップロード全件エラー |
| 140062 | 電子交付 | 履歴アップロードの一部でエラーが発生しました | 履歴アップロード一部エラー |
| 140063 | 電子交付 | ファイル名に相当するドキュメントキーが存在しません | ドキュメントキー取得エラー |
| 140064 | 電子交付 | 検索条件に該当する顧客登録番号はありませんでした。 | 顧客登録番号取得エラー |
| 140065 | 電子交付 | データ／レコード内容が正しくありません | データフォーマットエラー |
| 140066 | 電子交付 | 交付履歴の削除でエラーが発生しました | 電子鳩交付履歴削除エラー |
| 140071 | 電子交付 | 電子交付変更内容に変更がありません | 電子交付変更申込内容変更なし |
| 140081 | 電子交付 | 件数が500件を超えているため、ファイルを分割して、再度実行して下さい。 | レコード件数が処理限界値を越えています |
| 140082 | 電子交付 | レコードが重複しています | レコード重複 |
| 140083 | 電子交付 | 削除対象データが見つかりませんでした | 削除対象データなし |
| 140084 | 電子交付 | アップロードファイルのデータ形式に誤りがあります。 | アップロードファイルデータフォーマット不正 |
| 140085 | 電子交付 | アップロードの処理区分が正しくありません | 処理区分不正 |
| 140086 | 電子交付 | アップロード処理が全件異常終了しました | アップロード処理全件エラー |
| 140087 | 電子交付 | アップロード処理が一部異常終了しました | アップロード処理一部エラー |
| 140088 | 電子交付 | CSVファイルを指定の上、再度実行して下さい。 | CSVファイル以外が入力されている。 |
| 140089 | 電子交付 | ファイル容量が上限を超えています。 | ファイルサイズ不正 |
| 140090 | 電子交付 | 顧客登録番号に対応する顧客は登録されていません。 | 顧客登録番号不正 |
| 140091 | 電子交付 | 重複顧客チェックでエラーが発生しました。 | 登録顧客重複 |
| 140092 | 電子交付 | 重複登録データが存在するため、登録アップロード処理を中止します。 | 登録データ重複 |
| 140093 | 電子交付 | 削除対象データが存在しないため、削除アップロード処理を中止します。 | 削除対象データなし |
| 140094 | 管理者・ドキュメント機能 | 顧客のシステム口座区分が正しくありません。 | システム口座区分エラー |
| 140100 | 電子交付 | 銘柄コードが正しくありません。 | 銘柄コード不正 |
| 140101 | 電子交付 | 登録に失敗しました。（TMPファイルオープンエラー） | TMPファイルオープンエラー |
| 140102 | 電子交付 | 登録に失敗しました。（NFSファイルオープンエラー） | NFSファイルオープンエラー |
| 140103 | 電子交付 | 既に指定の決算日の書類は登録されています。 | NFS上に同名ファイルあり |
| 140104 | 電子交付 | 登録に失敗しました。（NFSファイル書込みエラー） | NFSファイル書込みエラー |
| 140105 | 電子交付 | 登録に失敗しました。（変更対象データなし） | 変更対象データなし |
| 140106 | 電子交付 | 削除に失敗しました。（削除対象データなし） | 削除対象データなし |
| 140107 | 電子交付 | ファイルの削除に失敗しました。（DBデータ削除のみ完了） | NFSファイル削除エラー |
| 140995 | 電子交付 | 検索結果が100件を超過したため、処理を中断します。 | 検索結果100件超過 |
| 140998 | 管理者・ドキュメント機能 | ＤＢ接続接続でエラーが発生しました | ＤＢエラー |
| 150002 | システム管理 | パスワードが正しくありません | パスワード不正 |
| 150003 | システム管理 | システム権限がありません | システム権限エラー |
| 150007 | システム管理 | 参照権限でエラーが発生しました | 参照権限エラー |
| 150008 | システム管理 | 更新権限でエラーが発生しました | 更新権限エラー |
| 150020 | システム管理 | 運用ステータス定義レコードがありません | 運用ステータス定義レコード無し |
| 150021 | システム管理 | 運用ステータスレコードがありません | 運用ステータスレコード無し |
| 150050 | システム管理 | プロシージャでエラーが発生しました | プロシージャエラー |
| 150051 | システム管理 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 150060 | システム管理 | 運用ステータス定義レコードロックでエラーが発生しました | 運用ステータス定義レコードロックエラー |
| 150061 | システム管理 | 運用ステータス定義レコード挿入でエラーが発生しました | 運用ステータス定義レコード挿入エラー |
| 150062 | システム管理 | 運用ステータス定義レコード更新でエラーが発生しました | 運用ステータス定義レコード更新エラー |
| 150063 | システム管理 | 運用ステータス定義レコード削除でエラーが発生しました | 運用ステータス定義レコード削除エラー |
| 150064 | システム管理 | 運用ステータスレコードロックでエラーが発生しました | 運用ステータスレコードロックエラー |
| 150065 | システム管理 | 運用ステータスレコード更新でエラーが発生しました | 運用ステータスレコード更新エラー |
| 150170 | システム管理 | ZIP圧縮でエラーが発生しました | ZIP圧縮エラー |
| 150180 | システム管理 | 内部ファイルオープンでエラーが発生しました | ファイルオープンエラー |
| 150181 | システム管理 | 内部ファイル書込でエラーが発生しました | ファイル書込エラー |
| 150182 | システム管理 | 内部ファイル読込でエラーが発生しました | ファイル読込エラー |
| 150183 | システム管理 | ファイルデータに誤りがあります | ファイルデータ不正 |
| 150185 | システム管理 | ＣＳＶファイルのヘッダー項目数に誤りがあります | ヘッダー項目数不正 |
| 150186 | システム管理 | ＣＳＶファイルの行項目数に誤りがあります | 行項目数不正 |
| 150187 | システム管理 | ＣＳＶファイルのパラメータに誤りがあります | パラメータ不正 |
| 150199 | システム管理 | スレッド構成でエラーが発生しました | スレッド構成エラー |
| 150301 | システム管理 | 注文アップロード管理にデータがありません | 注文アップロード管理レコードなし |
| 150302 | システム管理 | 注文アップロード管理のレコードロックでエラーが発生しました | 注文アップロード管理レコードロックエラー |
| 150303 | システム管理 | 注文アップロード管理にデータ挿入でエラーが発生しました | 注文アップロード管理レコード挿入エラー |
| 150304 | システム管理 | 注文アップロード管理のデータ更新でエラーが発生しました | 注文アップロード管理レコード更新エラー |
| 150305 | システム管理 | 注文アップロード管理のデータ取得でエラーが発生しました | 注文アップロード管理レコード取得エラー |
| 150306 | システム管理 | 注文アップロードにデータがありません | 注文アップロードレコードなし |
| 150307 | システム管理 | 注文アップロードにデータ挿入でエラーが発生しました | 注文アップロードレコード挿入エラー |
| 150308 | システム管理 | 注文アップロードのレコードロックでエラーが発生しました | 注文アップロードレコードロックエラー |
| 150309 | システム管理 | 注文アップロードのデータ更新でエラーが発生しました | 注文アップロードレコード更新エラー |
| 150310 | システム管理 | 注文アップロードレコードのデータ取得でエラーが発生しました | 注文アップロードレコード取得エラー |
| 150320 | システム管理 | 顧客がありません | 顧客なし |
| 150321 | システム管理 | 銘柄がありません | 銘柄なし |
| 150350 | システム管理 | 商品種別に誤りがあります | 商品種別不正 |
| 150351 | システム管理 | 処理区分に誤りがあります | 処理区分不正 |
| 150352 | システム管理 | 市場コードに誤りがあります | 市場コード不正 |
| 150353 | システム管理 | 現金信用区分に誤りがあります | 現金信用区分不正 |
| 150354 | システム管理 | 建日種類に誤りがあります | 建日種類不正 |
| 150355 | システム管理 | 現金信用区分と弁済区分で矛盾があります | 現金信用区分と弁済区分で矛盾 |
| 150356 | システム管理 | 建玉がありません | 建玉なし |
| 150357 | システム管理 | ファイルのシステム口座区分に誤りがあります | システム口座区分不正 |
| 150401 | システム管理 | 約定アップロード管理にデータがありません | 約定アップロード管理レコードなし |
| 150402 | システム管理 | 約定アップロード管理のレコードロックでエラーが発生しました | 約定アップロード管理レコードロックエラー |
| 150403 | システム管理 | 約定アップロード管理にデータ挿入でエラーが発生しました | 約定アップロード管理レコード挿入エラー |
| 150404 | システム管理 | 約定アップロード管理のデータ更新でエラーが発生しました | 約定アップロード管理レコード更新エラー |
| 150405 | システム管理 | 約定アップロード管理のデータ取得でエラーが発生しました | 約定アップロード管理レコード取得エラー |
| 150406 | システム管理 | 約定アップロードにデータがありません | 約定アップロードレコードなし |
| 150407 | システム管理 | 約定アップロードのレコードロックでエラーが発生しました | 約定アップロードレコードロックエラー |
| 150408 | システム管理 | 約定アップロードレコードにデータ挿入でエラーが発生しました | 約定アップロードレコード挿入エラー |
| 150409 | システム管理 | 約定アップロードのデータ更新でエラーが発生しました | 約定アップロードレコード更新エラー |
| 150410 | システム管理 | 約定アップロードのデータ取得でエラーが発生しました | 約定アップロードレコード取得エラー |
| 150450 | システム管理 | 商品種別に誤りがあります | 商品種別不正 |
| 150451 | システム管理 | 追加・取消Ｃに誤りがあります | 追加・取消Ｃ不正 |
| 150460 | システム管理 | 該当顧客でエラーが発生しました | 該当顧客でエラー発生 |
| 150461 | システム管理 | 注文がありません | 注文番号不正 |
| 150997 | システム管理 | ネットでエラーが発生しました | ネットエラー |
| 150998 | システム管理 | ＤＢでエラーが発生しました | ＤＢエラー |
| 160002 | 顧客一覧 | パスワードが正しくありません | パスワード不正 |
| 160007 | 顧客一覧 | 参照権限でエラーが発生しました | 参照権限エラー |
| 160008 | 顧客一覧 | 更新権限でエラーが発生しました | 更新権限エラー |
| 160020 | 顧客一覧 | 余力制御レコードがありません | 余力制御レコード無し |
| 160050 | 顧客一覧 | プロシージャでエラーが発生しました | プロシージャエラー |
| 160051 | 顧客一覧 | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 160060 | 顧客一覧 | 余力制御レコードロックでエラーが発生しました | 余力制御レコードロックエラー |
| 160062 | 顧客一覧 | 余力制御レコード更新でエラーが発生しました | 余力制御レコード更新エラー |
| 160120 | 顧客一覧 | 該当する入金請求データがありません | 入金請求データなし |
| 160160 | 顧客一覧 | 入金請求管理レコードロックでエラーが発生しました | 入金請求管理レコードロックエラー |
| 160161 | 顧客一覧 | 入金請求管理レコード挿入でエラーが発生しました | 入金請求管理レコード挿入エラー |
| 160162 | 顧客一覧 | 入金請求管理レコード更新でエラーが発生しました | 入金請求管理レコード更新エラー |
| 160165 | 顧客一覧 | 入金請求解除レコード挿入でエラーが発生しました | 入金請求解除レコード挿入エラー |
| 160220 | 顧客一覧 | 検索条件に合致するデータはございません | ロック顧客データなし |
| 160310 | 顧客一覧 | 存在しない要求Noです | 要求NO不正 |
| 160311 | 顧客一覧 | 受付時間外です | 受付時間外 |
| 160312 | 顧客一覧 | 只今データ作成中です | データ作成中 |
| 160313 | 顧客一覧 | レポート作成処理ででエラーが発生しました | レポート作成エラー |
| 160320 | 顧客一覧 | 検索条件に合致するデータはありません | レポート検索該当データなし |
| 160997 | 顧客一覧 | ネットでエラーが発生しました | ネットエラー |
| 160998 | 顧客一覧 | ＤＢでエラーが発生しました | ＤＢエラー |
| 170000 | 特殊注文手動発注・失効 | 正常終了 | 正常終了 |
| 170001 | 特殊注文手動発注・失効 | 処理済み | 処理済み |
| 170002 | 特殊注文手動発注・失効 | 有効注文数量がありません | 有効注文数量なし |
| 170004 | 特殊注文手動発注・失効 | 受付未済 | 受付未済 |
| 170005 | 特殊注文手動発注・失効 | 訂正取消中 | 訂正取消中 |
| 170006 | 特殊注文手動発注・失効 | 対象レコードがありません | 対象レコードなし |
| 170998 | 特殊注文手動発注・失効 | ＤＢでエラーが発生しました | ＤＢエラー |
| 180001 | 銘柄登録 | 通知する種類が選択されていません | 通知種類不正 |
| 180011 | 銘柄登録 | 株価設定を入力して下さい. | 株価入力 |
| 180012 | 銘柄登録 | 入力された株価が大きすぎます.(整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 株価入力 |
| 180013 | 銘柄登録 | 入力された株価が正しくありません.(整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 株価入力 |
| 180015 | 銘柄登録 | 設定値を入力して下さい. | 設定値入力 |
| 180016 | 銘柄登録 | 入力された設定値が大きすぎます.(率の場合は100以内、円の場合は整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 設定値入力 |
| 180017 | 銘柄登録 | 入力された設定値が正しくありません.(率の場合は100以内、円の場合は整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 設定値入力 |
| 180019 | 銘柄登録 | 設定値ﾀｲﾌﾟが選択されていません. | 単位選択 |
| 180020 | 銘柄登録 | 条件区分が選択されていません. | 条件区分 |
| 180021 | 銘柄登録 | 値段区分が選択されていません. | 値段区分 |
| 180024 | 銘柄登録 | 再通知設定が選択されていません. | 再通知 |
| 180025 | 銘柄登録 | 再通知設定値を入力して下さい. | 再通知 |
| 180026 | 銘柄登録 | 再通知設定値が大きすぎます(率の場合は100以内、円の場合は整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 再通知 |
| 180027 | 銘柄登録 | 再通知設定値が正しくありません(率の場合は100以内、円の場合は整数部は8桁以内、小数は第一位までの1以上の数値を入力してください) | 再通知 |
| 180028 | 銘柄登録 | 再通知設定値ﾀｲﾌﾟが選択されていません | 再通知 |
| 180029 | 銘柄登録 | 再通知条件区分が選択されていません | 再通知 |
| 180030 | 銘柄登録 | メールアドレスが選択されていません. | メールアドレス選択 |
| 180031 | 銘柄登録 | メールアドレスのユーザ名を入力して下さい. | メールアドレスエラー |
| 180032 | 銘柄登録 | メールアドレスのユーザ名が最大桁数を超えています.(50文字以内) | メールアドレスエラー |
| 180033 | 銘柄登録 | メールアドレスのユーザ名が正しくありません. | メールアドレスエラー |
| 180036 | 銘柄登録 | メールアドレスのドメイン名を入力して下さい. | メールアドレスエラー |
| 180037 | 銘柄登録 | メールアドレスのドメイン名が最大桁数を超えています.(50文字以内) | メールアドレスエラー |
| 180038 | 銘柄登録 | メールアドレスのドメイン名が正しくありません. | メールアドレスエラー |
| 180039 | 銘柄登録 | 指定されたメールアドレスの登録が見つかりませんでした. | メールアドレスエラー |
| 180049 | 銘柄登録 | 登録数が最大数に達しています.これ以上は登録できません. | 登録数エラー |
| 180050 | 銘柄登録 | 登録情報の追加に失敗しました | 銘柄監視テーブル追加エラー |
| 180051 | 銘柄登録 | 登録情報の追加に失敗しました | 銘柄監視テーブルロックエラー |
| 180053 | 銘柄登録 | 登録情報の更新に失敗しました | 銘柄監視テーブル更新エラー |
| 180054 | 銘柄登録 | 登録情報の削除に失敗しました | 銘柄監視テーブル削除エラー |
| 180055 | 銘柄登録 | ＤＢでエラーが発生しました | ＤＢエラー |
| 180998 | 銘柄登録 | ＤＢでエラーが発生しました | ＤＢエラー |
| 200050 | ストップ約定 | プロシージャでエラーが発生しました | プロシージャエラー |
| 200051 | ストップ約定 | 現在日付取得でエラーが発生しました | 現在日付取得エラー |
| 200401 | ストップ約定 | ストップ約定管理にデータがありません | ストップ約定管理レコードなし |
| 200402 | ストップ約定 | ストップ約定管理のレコードロックでエラーが発生しました | ストップ約定管理レコードロックエラー |
| 200404 | ストップ約定 | ストップ約定管理のデータ更新でエラーが発生しました | ストップ約定管理レコード更新エラー |
| 200405 | ストップ約定 | ストップ約定管理のデータ取得でエラーが発生しました | ストップ約定管理レコード取得エラー |
| 200406 | ストップ約定 | ストップ約定詳細にデータがありません | ストップ約定詳細レコードなし |
| 200407 | ストップ約定 | ストップ約定詳細のレコードロックでエラーが発生しました | ストップ約定詳細レコードロックエラー |
| 200409 | ストップ約定 | ストップ約定詳細のデータ更新でエラーが発生しました | ストップ約定詳細レコード更新エラー |
| 200410 | ストップ約定 | ストップ約定詳細のデータ取得でエラーが発生しました | ストップ約定詳細レコード取得エラー |
| 200997 | ストップ約定 | ネットでエラーが発生しました | ネットエラー |
| 200998 | ストップ約定 | ＤＢでエラーが発生しました | ＤＢエラー |
| 900001 | オペレータログイン | オペレータコードに誤りがあります | オペレータコード不正 |
| 900002 | オペレータログイン | パスワードが正しくありません | パスワード不正 |
| 900004 | オペレータログイン | 接続に誤りがあります | チャネル不正 |
| 900005 | オペレータログイン | ＩＰアドレスに誤りがあります | ＩＰアドレス不正 |
| 900006 | オペレータログイン | ダミーセッションＩＤに誤りがあります | ダミーセッションＩＤ不正 |
| 900020 | オペレータログイン | ダミーセッションファイルに問題があります | ダミーセッションファイル障害 |
| 900021 | オペレータログイン | ダミーセッションにデータがありません | ダミーセッションレコードなし |
| 900030 | オペレータログイン | オペレータマスタファイルに問題があります | オペレータマスタファイル障害 |
| 900031 | オペレータログイン | オペレータマスタにデータがありません | オペレータマスタレコードなし |
| 900032 | オペレータログイン | オペレータマスタのデータ更新でエラーが発生しました | オペレータマスタレコード更新エラー |
| 900033 | オペレータログイン | オペレータマスタログインはロックされています | オペレータマスタログインロック |
| 900034 | オペレータログイン | オペレータマスタログインができません | オペレータマスタログインＮＧ |
| 900035 | オペレータログイン | オペレータマスタパスワードが間違っています | オペレータマスタパスワード不一致 |
| 900036 | オペレータログイン | オペレータのシステム口座区分に誤りがあります | オペレータシステム口座区分不一致 |
| 900040 | オペレータログイン | システム設定ファイルに問題があります | システム設定ファイル障害 |
| 900041 | オペレータログイン | システム設定にデータがありません | システム設定レコードなし |
| 900045 | オペレータログイン | BAD_IPファイルに問題があります | BAD_IPファイル障害 |
| 900046 | オペレータログイン | BAD_IPにデータ作成でエラーが発生しました | BAD_IPレコード作成エラー |
| 900047 | オペレータログイン | BAD_IP許可件数を超えています | BAD_IP許可件数オーバー |
| 900050 | オペレータログイン | オペレータセッション情報ファイルに問題があります | オペレータセッション情報ファイル障害 |
| 900051 | オペレータログイン | オペレータセッション情報にデータがありません | オペレータセッション情報レコードなし |
| 900052 | オペレータログイン | オペレータセッション情報のデータ更新でエラーが発生しました | オペレータセッション情報レコード更新エラー |
| 900053 | オペレータログイン | オペレータセッション情報にデータ作成でエラーが発生しました | オペレータセッション情報レコード作成エラー |
| 900054 | オペレータログイン | オペレータセッションＩＤ生成でエラーが発生しました | オペレータセッションＩＤ生成エラー |
| 900070 | オペレータログイン | 現在時刻取得でエラーが発生しました | 現在時刻取得エラー |
| 900071 | オペレータログイン | 現在日時取得でエラーが発生しました | 現在日時取得エラー |
| 900097 | オペレータログイン | ネットワークでエラーが発生しました | ネットワークエラー |
| 900098 | オペレータログイン | ＤＢ接続接続でエラーが発生しました | ＤＢエラー |
| 900099 | オペレータログイン | サーバからの応答がありません。結果をご確認下さい。 | タイムアウト |
| 990002 | 基幹SV | システム状態.一時停止中 | システム状態＝一時停止中 |
| 990003 | 基幹SV | システム状態.サービス停止中 | システム状態＝テストモード |
| 990004 | 基幹SV | システム状態.サービス停止中 | システム状態＝メンテナンス |
| 990005 | 基幹SV | システム状態.サービス時間外 | システム状態＝サービス時間外 |
| 990006 | 基幹SV | システム状態.ログイン不許可 | システム状態＝不明 |
| 990007 | 基幹SV | システム状態.閉局 | システム状態＝閉局 |
| 990008 | 基幹SV | インサイダーにご注意ください | インサイダーにご注意ください |
| 990009 | 基幹SV | もうすぐ本日の取引が終了します。 | もうすぐ本日の取引が終了します。 |
| 991001 | 基幹SV | 注文番号に誤りがあります。 | 注文番号不正 |
| 991002 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 営業日不正 |
| 991003 | 基幹SV | 銘柄コードに誤りがあります。 | 銘柄コード不正 |
| 991004 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | システム別設定取得できず |
| 991005 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 可能額サマリ取得エラー |
| 991006 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 入金請求発生状況リスト取得エラー |
| 991007 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 注文執行予定日不正 |
| 991008 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 注文照会状態不正 |
| 991010 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 運用ステータス（株式）取得エラー |
| 991011 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 日付情報取得エラー |
| 991012 | 基幹SV | 結果が取得できませんでした | 株式サマリ取得エラー |
| 991013 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 売買単位取得エラー |
| 991014 | 基幹SV | 市場不正 | 市場不正 |
| 991015 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 運用ステータス（余力）取得ミス |
| 991016 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 可能額取得ミス |
| 991017 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 運用ステータス（値洗い）取得ミス |
| 991018 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 可能額推移取得ミス |
| 991019 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 先物運用ステータス（注文）取得ミス |
| 991020 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 先物運用ステータス（余力）取得ミス |
| 991021 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 証拠金推移取得ミス |
| 991022 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 運用ステータス（注文）取得ミス |
| 991023 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | オプション運用ステータス（注文）取得ミス |
| 991024 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 派生サマリ取得ミス |
| 991025 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 非課税口座取得ミス |
| 991032 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 運用ステータス（出金）取得エラー |
| 991033 | 基幹SV | タイムスタンプに誤りがあります。 | タイムスタンプ不正 |
| 991034 | 基幹SV | ページの有効期限切れです。 | 有効期限切れ |
| 991035 | 基幹SV | チェックのみフラグに誤りがあります。 | チェックのみフラグエラー |
| 991036 | 基幹SV | 暗証番号をお間違えです。ご確認の上再度ご入力下さい。 | 第二暗証番号エラー |
| 991037 | 基幹SV | リアル保証金率取得ミス | リアル保証金率取得ミス |
| 991038 | 基幹SV | インサイダー可否フラグ不正 | インサイダー可否フラグに誤りがあります |
| 992003 | 基幹SV | 建日、建単価等の取得に失敗しました。 | 信用建玉明細を取得できず、建玉日、建玉単価、建玉株数、譲渡益課税区分は0又は空白の初期値を使用する。 |
| 993100 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | APApiの呼び出しエラー |
| 993101 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 注文入力IF返済建玉指定ヘッダ情報不正 |
| 993102 | 基幹SV | 只今、一時的にこの業務はご利用できません。 | 信用返済注文時、返済建玉データ指定なし |
| 993103 | 基幹SV | 口座区分不一致の為、このご注文はお受けできません。 | 現引現渡注文時、返済対象建玉の譲渡益課税区分指定なし |
