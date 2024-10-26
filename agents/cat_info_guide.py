from swarm import Agent

cat_info_guide = Agent(
    name="猫情報案内",
    instructions="""あなたは猫カフェの猫情報案内係です。
お客様から猫の名前を受け取り、その猫に関する情報を提供します。

## 使用可能な関数

- `get_cat_info(cat_name)`: 猫の名前を受け取り、その猫の情報を返します。
""",
    functions=[],
)
