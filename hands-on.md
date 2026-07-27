# ハンズオン手順書

## ゴール

- WWDC 2026 で発表された Python 関連技術の「雰囲気」を体験する
- Foundation Models SDK for Python のコード例を実際に読み・改変する
- `fm` CLI、`coreai-torch`、MLX Swift の対比例を確認する

## 所要時間

- 全体: 約 60 分
  - イントロ: 10 分
  - fm CLI / Python SDK: 25 分
  - coreai-torch: 15 分
  - MLX Swift 対比: 10 分

## 0. 準備

1. このリポジトリをクローンまたは開く
2. Python 3.10 以上が入っていることを確認

```bash
python3 --version
```

3. 仮想環境を作っておく（任意）

```bash
python3 -m venv venv
source venv/bin/activate
```

4. （macOS 27 以降の場合）`fm` CLI が使えることを確認

```bash
fm --version
```

> **現行の macOS 26 Tahoe（Darwin 25）では `fm` CLI は利用できません（macOS 27 以降で標準搭載予定）。** CLI の例は読み物として参照し、Python SDK のコード例を中心に進めてください。

## 1. LT 資料を読む

[LT.md](LT.md) を開いて、スライド風に目を通す。

ポイント：

- Python が出てくる 3 つの場面
- `fm` CLI の例
- Foundation Models SDK for Python の API パターン
- `coreai-torch` の変換フロー
- MLX Swift の Python との対比

## 2. fm CLI を試す（実機 or 観察）

```bash
# examples/fm-cli.sh を実行可能にする
chmod +x examples/fm-cli.sh

# 内容を確認
cat examples/fm-cli.sh
```

`examples/fm-cli.sh` をターミナルで 1 行ずつ実行する。

実機がない場合は、出力を想像しながら LT.md の例を読む。

## 3. Python SDK を試す

```bash
pip install apple-fm-sdk
```

> 配布方法は今後変わる可能性あり。エラーになったら公式ドキュメントを確認。

### 3.1 基本の応答

```bash
python examples/fm-sdk-basic.py
```

内容を確認し、`prompt=` の文字列を変更して再実行する。

### 3.2 ツール呼び出し

```bash
python examples/fm-sdk-tool.py
```

`Orders.load_last_orders` は仮の関数なので、実際には自分のデータ取得処理に置き換える。

### 3.3 構造化出力

```bash
python examples/fm-sdk-structured.py
```

`ItemSuggestion` のフィールドを増やしたり、別のクラスに変えたりしてみる。

## 4. ノートブックで遊ぶ

Jupyter 環境がある場合：

```bash
pip install jupyter
jupyter notebook hands-on.ipynb
```

または VS Code で `hands-on.ipynb` を開いて実行する。

セルごとに：

1. SDK の概要を確認
2. `asyncio` を使った応例を実行
3. 構造化出力のクラスを改変
4. 簡易的な「注文履歴問い合わせツール」を作る

## 5. coreai-torch を見る

```bash
cat examples/coreai-torch-convert.py
```

ポイント：

- `coreai_torch.convert()` の引数
- `example_inputs` の役割
- `dynamic_dims` でバッチサイズを可変にする

実際に自分の PyTorch モデルがある場合は、サンプル入力を合わせて実行してみる。

## 6. MLX Swift 対比例

```bash
cat examples/mlx-swift-comparison.md
```

ポイント：

- Python 版と Swift 版で変数名・メソッド名がほぼ一致
- `mlx.core as mx` → `import MLX`
- 配列生成・四則演算の書き方を比較

挑戦：もし Swift 環境がある場合、Python の mlx-examples の簡単な例を Swift に翻訳してみる。

## 7. まとめディスカッション

ペアまたはグループで話す：

1. 自分のプロジェクトにどの技術が使えそうか？
2. Python と Swift のどちらで何を担当させたいか？
3. ハードルになりそうなポイントは？

## 8. 次のステップ

- [ ] `examples/` のコードを自分のユースケースに改変する
- [ ] LT.md を自分の言葉でアレンジする
- [ ] WWDC26 の公式動画（Session 334/324/325/328）を見る
- [ ] GitHub `apple/python-apple-fm-sdk` を watch する

## トラブルシューティング

| 症状 | 対処 |
|------|------|
| `apple-fm-sdk` が見つからない | まだ公開されていない可能性。仮実装で構造だけ確認する。 |
| `fm` コマンドがない | macOS 27 以降が必要（2026年秋リリース予定）。ハンズオンでは CLI 例の読み込みに留める。 |
| `coreai` が import できない | 現在の環境では未配布の可能性。概念理解に留める。 |
| Swift コンパイルが面倒 | Python との対比例だけ読んで、雰囲気を掴む。 |
