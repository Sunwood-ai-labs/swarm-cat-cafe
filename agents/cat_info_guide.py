from swarm import Agent

from functions.cat_info_functions import get_cat_info
from agents.reservation_manager import transfer_to_reservation_manager

cat_info_guide = Agent(
    name="猫情報案内",
    instructions="""あなたは猫カフェの猫情報案内係です。
お客様から猫の名前を受け取り、その猫に関する情報を提供します。

## 使用可能な関数

- `get_cat_info(cat_name)`: 猫の名前を受け取り、その猫の情報を返します。
- `transfer_to_reservation_manager()`: 予約管理エージェントに遷移します。
""",
    functions=[get_cat_info, transfer_to_reservation_manager],
)
