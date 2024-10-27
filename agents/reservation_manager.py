from swarm import Agent

from functions.reservation_functions import make_reservation


def transfer_to_reservation_manager():
    """予約管理エージェントに遷移します。"""
    return reservation_manager


reservation_manager = Agent(
    name="予約管理",
    instructions="""あなたは猫カフェの予約管理係です。
お客様からの予約リクエストを受け付け、予約処理を行います。

## 使用可能な関数

- `make_reservation(customer_name, datetime)`: 顧客名と日時を受け取り、予約を行います。
""",
    functions=[make_reservation],
)
