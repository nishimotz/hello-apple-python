#!/bin/zsh
# fm CLI ハンズオン例
# 実行環境: macOS 27 以降（想定）

echo "=== 1. 対話モード ==="
fm chat

echo "=== 2. 単発プロンプト ==="
fm respond "WWDC26 の Python 関連発表を3行でまとめて"

echo "=== 3. Private Cloud Compute モデル ==="
fm respond "複雑な正規表現を Swift で書いて" --model pcc

echo "=== 4. 画像入力 ==="
fm respond "このスクリーンショットで何のアプリを使ってる？" \
  --image Screenshot.png --model pcc

echo "=== 5. 構造化出力 ==="
fm schema object --name AppsIdentified --string app_names --array > schema.json
cat schema.json
echo "---"
fm respond "このスクリーンショットでアクティブなアプリは？" \
  --image Screenshot.png --model pcc --schema schema.json
