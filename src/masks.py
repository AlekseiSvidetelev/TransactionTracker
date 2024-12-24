def get_mask_card_number(card_number: str) -> str:
    """ Функцию маскировки номера банковской карты"""
    if len(card_number) != 16 or card_number.isdigit() is not True:
        return "Проверьте правильность ввода данных"
    else:
        i = 0
        part_number = []
        while True:
            part = card_number[i:i+4]
            part_number.append(part)
            i += 4
            if i >= 16:
                break
        join_part_number = " ".join(part_number)
        return f"{join_part_number[0:7]}** **** {join_part_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """ Функцию маскировки номера банковского счета """
    if len(account_number) != 20 or account_number.isdigit() is not True:
        return "Проверьте правильность ввода данных"
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_account("73654108430669958748"))
    print(get_mask_card_number("7000792189606391"))
