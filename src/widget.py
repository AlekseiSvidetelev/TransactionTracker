from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """
    функция принимает номер карты или счет и
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
    raise ValueError("Неверный тип данных")


def format_date(date: str) -> str:
    """Функция для преобразования формата даты"""
    if len(date) >= 10:
        date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        new_date_str = date_format.strftime("%d.%m.%Y")
        return new_date_str
    raise ValueError("Неправильный тип данных")
