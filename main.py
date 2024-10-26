from configs.agents import receptionist_agent
from swarm.repl import run_demo_loop

# コンテキスト変数の設定
context_variables = {
    "cafe_info": """
    営業時間: 平日 10:00-20:00, 土日祝 9:00-21:00
    住所: 東京都渋谷区猫町1-2-3
    電話番号: 03-1234-5678
    """,
    "menu_info": """
    1. ふわふわパンケーキ - ¥800
    2. にゃんこラテ - ¥600
    3. まぐろサンドイッチ - ¥750
    4. ねこねこパフェ - ¥950
    """,
    "cat_info": """
    1. ミケ (三毛猫, 3歳, メス)
    2. タマ (白猫, 5歳, オス)
    3. クロ (黒猫, 2歳, オス)
    4. チャチャ (茶トラ, 4歳, メス)
    """
}

if __name__ == "__main__":
    # デモループの実行
    run_demo_loop(receptionist_agent, context_variables=context_variables, debug=True)

# 解説：
# このスクリプトは、Swarmフレームワークを使用して対話式の猫カフェカスタマーサービスデモを実行します。
# context_variablesには猫カフェの情報、メニュー、猫の情報が含まれており、これらはエージェントが対話中に参照できます。
# run_demo_loopは、ユーザーとエージェント間の対話を管理し、receptionist_agentから始まる対話フローを実行します。
