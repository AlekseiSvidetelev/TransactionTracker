from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """
    функция принимаеи номер карты или счет и
    возвращать строку с замаскированными значениями
    """
    numbers_count = 0
    symbols_count = 0
    for i in card_number:
        if i.isdigit():
            numbers_count += 1
        if not i.isdigit():
            symbols_count += 1
    if numbers_count == 16:
        return f"{card_number[: symbols_count]}{get_mask_card_number(card_number[- numbers_count:])}"
    elif numbers_count == 20:
        return f"{card_number[: symbols_count]}{get_mask_account(card_number[- numbers_count:])}"


def format_date(date: str) -> str:
    """Фуккция для преобразования формата даты"""
    date_get = date[:10]
    date_format = datetime.strptime(date_get, "%Y-%m-%d")
    new_date_str = date_format.strftime("%m.%d.%Y")
    return new_date_str


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(format_date("2024-03-11T02:26:18.671407"))
