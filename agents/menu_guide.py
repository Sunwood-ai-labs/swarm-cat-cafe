from swarm import Agent

from functions.menu_functions import get_menu
from agents.reservation_manager import transfer_to_reservation_manager

menu_guide = Agent(
    name="メニュー案内",
    instructions="""あなたは猫カフェのメニュー案内係です。
お客様からのリクエストに応じて、メニュー情報を提供します。

## 使用可能な関数

- `get_menu()`: メニュー情報を返します。
- `transfer_to_reservation_manager()`: 予約管理エージェントに遷移します。
""",
    functions=[get_menu, transfer_to_reservation_manager],
)
