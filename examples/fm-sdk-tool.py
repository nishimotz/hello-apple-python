"""
Foundation Models SDK for Python: ツール呼び出し例
LLM に「過去の注文を取得してもらう」架空のツールを定義するデモ
"""
import apple_fm_sdk as fm


# 架空の注文データ層
class Orders:
    @staticmethod
    async def load_last_orders(user_id: str, amount: int) -> str:
        # 実際のサービスでは DB や API 呼び出しに置き換える
        return f"User {user_id}: {amount} 件の注文履歴を返します（仮）"


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
        # LLM が生成した引数から値を取り出す
        n = args.value(int, for_property="number_orders")
        # ユーザー ID はセッション外から取得する想定
        user_id = "demo-user-123"
        return await Orders.load_last_orders(user_id=user_id, amount=n)


async def main() -> None:
    session = fm.LanguageModelSession(
        tools=[GetPastOrdersTool()],
    )
    response = await session.respond(
        "直近 5 件の注文を教えて"
    )
    print("=== Response ===")
    print(response.text)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
