"""
Foundation Models SDK for Python: 構造化出力例
LLM に generable デコレータで定義したスキーマに沿った応答を返してもらう
"""
import apple_fm_sdk as fm
import asyncio


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


async def main() -> None:
    result = await suggest()
    print("=== Structured Output ===")
    print(f"name: {result.name}")
    print(f"category: {result.category}")
    print(f"reason: {result.reason}")


if __name__ == "__main__":
    asyncio.run(main())
