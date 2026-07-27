# WWDC 2026 Python ハンズオン教材

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

WWDC 2026 で Apple が発表した Python 関連技術（Foundation Models SDK for Python、`coreai-torch`、MLX Swift との対比など）を、ハンズオン形式で学ぶための教材リポジトリです。

## 対象者

- macOS と Python の基礎がある方
- Apple Intelligence / Core AI / MLX について概要を知りたい方
- LT 資料・勉強会ネタを探している方

## リポジトリ構成

```
hello-apple-python/
├── README.md                  # このファイル
├── LT.md                      # LT 資料（マークダウンスライド風）
├── hands-on.md                # ハンズオン手順書
├── hands-on.ipynb             # 実行用ノートブック
├── examples/
│   ├── fm-cli.sh              # fm CLI の例
│   ├── fm-sdk-basic.py        # Python SDK: 基本応答
│   ├── fm-sdk-tool.py         # Python SDK: ツール呼び出し
│   ├── fm-sdk-structured.py   # Python SDK: 構造化出力
│   ├── coreai-torch-convert.py # coreai-torch 変換例
│   └── mlx-swift-comparison.md # MLX Python vs Swift 対比
```

## 学習の流れ

1. `LT.md` を読みながら全体像を把握する
2. `hands-on.md` の手順でターミナル / ノートブックを動かす
3. `hands-on.ipynb` で Python SDK の基本を実際に試す
4. `examples/` のコードを改変して自分だけのデモを作る

## 必要環境

- macOS 26.0 以上（Apple Intelligence 対応モデル推奨）
- Python 3.10 以上
- `fm` CLI（macOS 26 以降に標準搭載）
- オプション: Swift / Xcode 26.0+（MLX Swift、Core AI 推論の実行用）

> 注意: 発表内容は WWDC 2026 時点のものです。SDK の仕様や配布方法は今後変更になる可能性があります。実際に動かす場合は Apple の公式ドキュメント・GitHub リポジトリを確認してください。

## 参考リンク

- Session 334: Build AI-powered scripts with the `fm` CLI and Python SDK
- Session 324/325: Meet Core AI / Dive into Core AI model authoring and optimization
- Session 328: Explore numerical computing in Swift with MLX
- Session 262: What’s new in Swift
- [apple/python-apple-fm-sdk](https://github.com/apple/python-apple-fm-sdk)
- [Foundation Models SDK for Python ドキュメント](https://apple.github.io/python-apple-fm-sdk/)

## ライセンス

MIT License © 2026 Takuya Nishimoto

## 作者

- **Takuya Nishimoto** ([@nishimotz](https://github.com/nishimotz))

本教材は WWDC 2026 の公開情報および [apple/python-apple-fm-sdk](https://github.com/apple/python-apple-fm-sdk) のコード例を参考に作成しています。Apple の商標・著作物は Apple Inc. に帰属します。