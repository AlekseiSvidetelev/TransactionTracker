def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if len(card_number) != 16 or card_number.isdigit() is not True:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    else:
        i = 0
        part_number = []
        while True:
            part = card_number[i:i + 4]
            part_number.append(part)
            i += 4
            if i >= 16:
                break
        join_part_number = " ".join(part_number)
        return f"{join_part_number[0:7]}** **** {join_part_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    if len(account_number) != 20 or account_number.isdigit() is not True:
        raise ValueError("Номер счета должен содержать 20 цифр.")
    return f"**{account_number[-4:]}"
