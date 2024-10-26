from swarm import Agent

from agents.receptionist import receptionist
from agents.cat_info_guide import cat_info_guide
from agents.menu_guide import menu_guide
from agents.reservation_manager import reservation_manager

from functions.cat_info_functions import get_cat_info
from functions.menu_functions import get_menu
from functions.reservation_functions import make_reservation

# エージェントに使用する関数を設定
receptionist.functions = [get_cat_info, get_menu, make_reservation]
cat_info_guide.functions = [get_cat_info]
menu_guide.functions = [get_menu]
reservation_manager.functions = [make_reservation]
