"""
Foundation Models SDK for Python: 基本の応答例
WWDC 2026 Session 334 を参考に作成
"""
import apple_fm_sdk as fm
import asyncio


async def main() -> None:
    # システム言語モデルを取得
    model = fm.SystemLanguageModel()

    # モデルが利用可能か確認
    available, reason = model.is_available()
    if not available:
        print(f"Language model is not available: {reason}")
        return

    # セッションを開始して応答を取得
    session = fm.LanguageModelSession()
    response = await session.respond("Hello, Apple Intelligence!")
    print("=== Response ===")
    print(response.text)


if __name__ == "__main__":
    asyncio.run(main())
