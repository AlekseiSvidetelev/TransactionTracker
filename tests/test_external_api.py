from unittest.mock import patch

import pytest

from src.external_api import API_KEY, convert_sum_transactions


@patch("requests.get")
def test_convert_sum_transactions(mock_get) -> None:
    """Проверка на работу функции конвертации валюты"""
    transaction_test = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    mock_get.return_value.json.return_value = {"rates": {"EUR": 1, "RUB": 100}}
    assert convert_sum_transactions(transaction_test) == 7094618.0
    mock_get.assert_called_once_with("https://api.exchangeratesapi.io/v1/latest", params={"access_key": API_KEY})


def test_convert_sum_transactions_() -> None:
    """Тест если валюта конвертации соответствует начальной. Запрос на актуальный курс не выполняется"""
    transaction_test = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "1.0", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert convert_sum_transactions(transaction_test) == 1.0


def test_exception_convert_sum_transaction() -> None:
    """Проверка если в функцию пришли некорректные данные"""
    with pytest.raises(Exception):
        convert_sum_transactions("asd")
