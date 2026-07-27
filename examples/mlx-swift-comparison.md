# MLX Python vs MLX Swift 対比例

WWDC 2026 Session 328「Explore numerical computing in Swift with MLX」より、MLX Swift は Python の MLX API をミラーしている。

## 配列の生成と足し算

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

## ポイント

| Python | Swift | 意味 |
|--------|-------|------|
| `import mlx.core as mx` | `import MLX` | ライブラリ読み込み |
| `mx.array(...)` | `MLXArray(...)` | 配列生成 |
| `+` 演算子 | `+` 演算子 | 要素ごとの加算 |
| `print(c)` | `print(c)` | 結果表示 |

## なぜこれが便利なのか

- `mlx-examples`（Python）で実験したロジックを、ほぼ同じ構造で Swift に移植できる
- Apple Silicon 上でのトレーニング・推論を Swift / Core AI と組み合わせやすい
- Python 側で使った慣習（ブロードキャスト、lazy evaluation など）を引き継げる

## ハンズオン課題

1. Python で `mx.array` を使って行列積を計算する
2. 同じ計算を `MLXArray` で Swift に書き換えてみる
3. 結果が一致することを確認する
