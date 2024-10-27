from agents.cat_info_guide import cat_info_guide
from agents.menu_guide import menu_guide


def transfer_to_cat_info_guide():
    """猫情報案内エージェントに遷移します。"""
    return cat_info_guide


def transfer_to_menu_guide():
    """メニュー案内エージェントに遷移します。"""
    return menu_guide

# def transfer_to_reservation_manager():
#     """予約管理エージェントに遷移します。"""
#     return reservation_manager
