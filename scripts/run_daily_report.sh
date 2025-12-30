#!/bin/bash
# 日次レポート生成スクリプト（ローカル実行用）

set -e

echo "📊 株式スクリーニング日次レポート生成"
echo "=========================================="
echo ""

# 1. 電話認証の確認
echo "⚠️  電話認証を実施してください"
echo "   1. https://www.e-shiten.jp/ にログイン"
echo "   2. 電話認証を実行"
echo "   3. 3分以内にこのスクリプトを実行"
echo ""
read -p "電話認証を完了しましたか？ (y/N): " confirm

if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "❌ 中止しました"
    exit 1
fi

# 2. スクリプト実行
echo ""
echo "⏳ スクリーニング実行中..."
python3 -m src.main

# 3. Gitコミット
echo ""
echo "⏳ レポートをコミット中..."
git add docs/
git commit -m "📊 日次レポート生成: $(date +'%Y-%m-%d')" || {
    echo "変更なし"
    exit 0
}

# 4. プッシュ
echo ""
read -p "GitHub にプッシュしますか？ (y/N): " push_confirm

if [[ "$push_confirm" =~ ^[Yy]$ ]]; then
    git push
    echo "✅ 完了: GitHub Pagesに自動デプロイされます"
else
    echo "⚠️  後で手動でプッシュしてください: git push"
fi
