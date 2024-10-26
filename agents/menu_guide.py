from swarm import Agent

menu_guide = Agent(
    name="メニュー案内",
    instructions="""あなたは猫カフェのメニュー案内係です。
お客様からのリクエストに応じて、メニュー情報を提供します。

## 使用可能な関数

- `get_menu()`: メニュー情報を返します。
""",
    functions=[],
)
