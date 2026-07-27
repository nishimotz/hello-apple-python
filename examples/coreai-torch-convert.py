"""
coreai-torch: PyTorch モデルを Core AI 用 AIProgram に変換する例
WWDC 2026 Session 324/325 を参考に作成

注意: coreai-torch は WWDC 2026 で発表された概念です。
2026年7月時点では PyPI での公開・パッケージ名は未確定です。
このコードは発表内容に基づく参考構想としてご覧ください。
"""
import torch
import torch.nn as nn
import coreai.torch as coreai_torch  # 仮のパッケージ名


class MyPyTorchModel(nn.Module):
    """変換対象の最小モデル例"""
    def __init__(self) -> None:
        super().__init__()
        self.conv = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(16, 10)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)


def main() -> None:
    model = MyPyTorchModel()
    model.eval()

    # 変換用のサンプル入力
    sample_input = torch.randn(1, 3, 224, 224)

    # PyTorch モデルを Core AI 用 AIProgram に変換
    ai_program = coreai_torch.convert(
        model,
        example_inputs=(sample_input,),
        dynamic_dims={"batch": coreai_torch.Dim.unknown()}
    )

    # 保存
    ai_program.save("my_model.coreai")
    print("Saved my_model.coreai")


if __name__ == "__main__":
    main()
