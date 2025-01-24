from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтра банковских операций"""
    transactions_test = filter_by_currency(transactions, "USD")
    assert next(transactions_test) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(transactions_test) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(transactions_test) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_exception_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    """Тест исключений фильтра банковских операций"""
    for transaction in filter_by_currency([], "USD"):
        with pytest.raises(ValueError):
            raise ValueError
    for transaction in filter_by_currency([{}], "USD"):
        with pytest.raises(ValueError):
            raise ValueError
    for transaction in filter_by_currency([{}], "wer"):
        with pytest.raises(ValueError):
            raise ValueError


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    """Тест описания операции из списка банковских операций"""
    description = transaction_descriptions(transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"
    for transaction in transaction_descriptions([]):
        with pytest.raises(ValueError):
            raise ValueError


def test_card_number_generator() -> None:
    """Тест генератора номеров банковских карт"""
    card_number = card_number_generator(1, 2)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    card_number_1 = card_number_generator(9999999999999995, 9999999999999999)
    assert next(card_number_1) == "9999 9999 9999 9995"
    assert next(card_number_1) == "9999 9999 9999 9996"
    assert next(card_number_1) == "9999 9999 9999 9997"
    assert next(card_number_1) == "9999 9999 9999 9998"
    assert next(card_number_1) == "9999 9999 9999 9999"


def test_exception_card_number_generator():
    """Тест исключений вывода банковских карт"""
    for card_number in card_number_generator(3, 1):
        with pytest.raises(ValueError):
             raise ValueError
    for card_number in card_number_generator(1, 1234123412341234123):
        with pytest.raises(ValueError):
            raise ValueError
    for card_number in card_number_generator(0, 1):
        with pytest.raises(ValueError):
            raise ValueError
