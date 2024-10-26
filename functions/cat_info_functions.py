def get_cat_info(cat_name):
    """
    猫の名前を受け取り、その猫の情報を返します。

    Args:
        cat_name (str): 猫の名前

    Returns:
        dict: 猫の情報
    """

    # 猫の情報は、データベースや外部APIから取得する想定
    cat_info = {
        "name": cat_name,
        "breed": "スコティッシュフォールド",
        "age": 3,
        "personality": "人懐っこい",
    }

    return cat_info
