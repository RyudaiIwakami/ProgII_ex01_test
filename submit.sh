#githubにpushするためのスクリプト
# Usage: ./submit.sh

# 対象ファイルリスト
TARGET_FILES=(kadai1.c kadai2.c kadai3.c kadai4.c kadai5.c)

# コミットメッセージ
COMMIT_MESSAGE="kadai1-5"

# リモートリポジトリ
REMOTE_REPOSITORY="origin"

# ブランチ
BRANCH_NAME="main"

# ファイルの追加
for file in ${TARGET_FILES[@]}; do
    git add $file
done

# コミット
git commit -m "$COMMIT_MESSAGE"

# プッシュ
git push $REMOTE_REPOSITORY $BRANCH_NAME

# 終了メッセージ
echo "課題を提出しました。採点結果を確認してください。"

# 終了ステータス
exit 0
