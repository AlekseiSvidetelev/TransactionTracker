from typing import Any, Dict, Generator, List, Optional, Union


def filter_by_currency(
    transactions_list: List[Dict[str, Any]], currency: Optional[str] = None
) -> Generator[Dict[str, Any], None, None]:
    """Функция принимает на вход список словарей, представляющих транзакции. Возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    if transactions_list == [] or currency is None or transactions_list == [{}]:
        ValueError("Список транзакций пуст")
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions: List[Dict[str, Union[str, int]]]) -> Generator[str | int]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции"""
    if not transactions:
        ValueError("Пустой список")
    else:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator[str]:
    """Функция принимает начальный и конечный номер карты и поочередно выдает номера банковских карт в диапазоне"""
    zero_card_number = "0000000000000000"
    if start_number > end_number:
        ValueError("Неверный тип данных")
    elif 0 < start_number <= 9999999999999999 and 0 < end_number <= 9999999999999999:
        quanlity_card_numbers = end_number - start_number + 1
        for num in range(quanlity_card_numbers):
            start_number_str = str(start_number)
            size = len(start_number_str)
            card_number_1 = zero_card_number[:-size] + start_number_str
            yield f"{card_number_1[:4]} {card_number_1[4:8]} {card_number_1[8:12]} {card_number_1[12:]}"
            start_number += 1
