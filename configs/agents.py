from configs.tools import *
from swarm import Agent

# 受付係エージェントの指示を生成する関数
def receptionist_instructions(context_variables):
    cafe_info = context_variables.get("cafe_info", "")
    return f"""あなたは猫カフェの受付係です。お客様の質問に丁寧に答え、適切なエージェントに転送してください。
    カフェの基本情報: {cafe_info}
    メニューについての質問はメニュー案内エージェントに、
    予約に関する質問は予約管理エージェントに、
    猫についての質問は猫の情報案内エージェントに転送してください。
    それ以外の一般的な質問にはあなたが直接答えてください。"""

# 各エージェントの定義
receptionist_agent = Agent(
    name="受付係",
    instructions=receptionist_instructions,
    functions=[transfer_to_menu_guide, transfer_to_reservation_manager, transfer_to_cat_info_guide],
)

menu_guide_agent = Agent(
    name="メニュー案内",
    instructions="""あなたは猫カフェのメニュー案内担当です。
    お客様のメニューに関する質問に丁寧に答えてください。
    メニュー以外の質問には受付係エージェントに戻してください。""",
    functions=[get_menu_info, transfer_to_receptionist],
)

reservation_manager_agent = Agent(
    name="予約管理",
    instructions="""あなたは猫カフェの予約管理担当です。
    お客様の予約に関する質問や要望に丁寧に対応してください。
    予約以外の質問には受付係エージェントに戻してください。""",
    functions=[make_reservation, cancel_reservation, check_reservation, transfer_to_receptionist],
)

cat_info_guide_agent = Agent(
    name="猫の情報案内",
    instructions="""あなたは猫カフェの猫の情報案内担当です。
    お客様の猫に関する質問に丁寧に答えてください。
    猫以外の質問には受付係エージェントに戻してください。""",
    functions=[get_cat_info, transfer_to_receptionist],
)

# 解説：
# このファイルでは、猫カフェの各エージェント（受付係、メニュー案内、予約管理、猫の情報案内）を定義しています。
# 各エージェントには名前、指示（役割の説明）、使用可能な関数が設定されています。
# エージェント間の転送を管理することで、複雑な顧客サービスのフローを実現しています。
