# LT 資料：WWDC 2026 で Python はどこに出てきた？

> タイトル案: **「Apple エコシステムにおける Python の新しい居場所」**
> 発表時間: 15 分 / ハンズオン: 30 分

---

## スライド 1：イントロダクション

### なぜ今 Python？

- WWDC 2026 の大きな流れ：**Core AI / Foundation Models / MLX Swift**
- Apple は自社エコシステムの中で Python の位置づけを強化した
- 役割分担：
  - **Swift**：アプリ実装の正面
  - **Python**：実験・評価・モデル変換の側面

---

## スライド 2：Python が出てきた 3 つの場面

| 場面 | キーワード | 用途 |
|------|-----------|------|
| 1. プロトタイピング | `fm` CLI + Foundation Models SDK for Python | プロンプト評価、スクリプト連携 |
| 2. モデル変換 | `coreai-torch` | PyTorch → Core AI 用モデル |
| 3. 数値計算の橋渡し | MLX Swift | Python mlx-examples の知見を Swift に持ち込む |

---

## スライド 3：場面 1 — `fm` CLI

### ターミナルから LLM を使う

```bash
# 対話モード
fm chat

# 単発プロンプト
fm respond "WWDC26 の Python 関連発表を3行でまとめて"

# Private Cloud Compute モデル
fm respond "複雑な正規表現を Swift で書いて" --model pcc

# 画像入力
fm respond "このスクリーンショットで何のアプリを使ってる？" \
  --image Screenshot.png --model pcc

# 構造化出力
fm schema object --name AppsIdentified --string app_names --array > schema.json
fm respond "このスクリーンショットでアクティブなアプリは？" \
  --image Screenshot.png --model pcc --schema schema.json
# => {"app_names": ["Messages", "Mail", "Calendar"]}
```

**ポイント**：Jupyter/Pandas/matplotlib など、Python エコシステムと自然に連携できる。

---

## スライド 4：場面 1 — Foundation Models SDK for Python

### インストール

```bash
pip install apple-fm-sdk
```

### 基本の応答

```python
import apple_fm_sdk as fm
import asyncio

async def main():
    model = fm.SystemLanguageModel()
    available, reason = model.is_available()
    if not available:
        print(f"not available: {reason}")
        return

    session = fm.LanguageModelSession()
    response = await session.respond("Hello")
    print(response.text)

asyncio.run(main())
```

---

## スライド 5：場面 1 — ツール呼び出し

```python
import apple_fm_sdk as fm

class GetPastOrdersTool(fm.Tool):
    name = "get_past_orders"
    description = "過去の注文を取得する"

    @fm.generable
    class Arguments:
        number_orders: int = fm.guide("取得する件数")

    @property
    def arguments_schema(self) -> fm.GenerationSchema:
        return self.Arguments.generation_schema()

    async def call(self, args: fm.GeneratedContent) -> str:
        n = args.value(int, for_property="number_orders")
        return await Orders.load_last_orders(user_id=user_id, amount=n)
```

**ポイント**：Python の型ヒント + デコレータで、LLM から呼ばせたい関数の引数を宣言する。

---

## スライド 6：場面 1 — 構造化出力

```python
import apple_fm_sdk as fm

@fm.generable
class ItemSuggestion:
    name: str = fm.guide("商品名")
    category: str = fm.guide("カテゴリ")
    reason: str = fm.guide("推薦理由")

async def suggest() -> ItemSuggestion:
    session = fm.LanguageModelSession()
    return await session.respond(
        "おすすめの食材を1つ提案して",
        generating=ItemSuggestion
    )
```

**ポイント**：Pydantic/dataclass 的なクラスで「どういう JSON を返してほしいか」を教える。

---

## スライド 7：場面 2 — `coreai-torch`

### PyTorch → Core AI

```python
import torch
import coreai.torch as coreai_torch

model = MyPyTorchModel()
sample_input = torch.randn(1, 3, 224, 224)

ai_program = coreai_torch.convert(
    model,
    example_inputs=(sample_input,),
    dynamic_dims={"batch": coreai_torch.Dim.unknown()}
)

ai_program.save("my_model.coreai")
```

### Swift 側で推論

```swift
import CoreAI

let model = try AIGraph(contentsOf: URL(fileURLWithPath: "my_model.coreai"))
let result = try model.inference(input: imageTensor)
```

**ポイント**：Python で作ったモデルを最適化・コンパイルし、Swift / Core AI ランタイムへ橋渡し。

---

## スライド 8：場面 3 — MLX Swift

### Python（MLX）

```python
import mlx.core as mx

a = mx.array([1.0, 2.0, 3.0])
b = mx.array([4.0, 5.0, 6.0])
c = a + b
print(c)  # [5.0, 7.0, 9.0]
```

### Swift（MLX Swift）

```swift
import MLX

let a = MLXArray([1.0, 2.0, 3.0])
let b = MLXArray([4.0, 5.0, 6.0])
let c = a + b
print(c)  // [5.0, 7.0, 9.0]
```

**ポイント**：API 名・概念がほぼ一致。mlx-examples の実装を Swift に移植しやすい。

---

## スライド 9：まとめ

### Python は「実験・評価・変換」の言語

- `fm` CLI + Python SDK → プロンプト評価パイプライン
- `coreai-torch` → PyTorch モデルの Apple Silicon 最適化
- MLX Swift → Python 数値計算の知見を Swift に継承

### Swift は「製品実装」の言語

- Core AI ランタイム、On-Device 推論、アプリ統合

### 今後の学び方

1. Jupyter で `apple-fm-sdk` を試す
2. 自作 PyTorch モデルを `coreai-torch` で変換する
3. mlx-examples を Swift に翻訳して比較する

---

## スライド 10：参考

- Session 334: Build AI-powered scripts with the `fm` CLI and Python SDK
- Session 324/325: Meet Core AI / Dive into Core AI model authoring and optimization
- Session 328: Explore numerical computing in Swift with MLX
- Session 262: What’s new in Swift
- github.com/apple/python-apple-fm-sdk

## ハンズオンへ

→ 次は `hands-on.md` を開いて、実際にコードを動かしましょう！
