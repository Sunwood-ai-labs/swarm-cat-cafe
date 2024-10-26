def make_reservation(customer_name, datetime):
    """
    顧客名と日時を受け取り、予約を行います。

    Args:
        customer_name (str): 顧客名
        datetime (datetime): 予約日時

    Returns:
        str: 予約結果
    """

    # 予約処理は、データベースや外部APIに接続して行う想定
    reservation_result = f"{customer_name}様の予約を{datetime}に承りました。"

    return reservation_result
