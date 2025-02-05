from unittest.mock import mock_open, patch

import pytest

from src.utils import get_transaction_data


@patch("builtins.open", mock_open(read_data='[{"id": 123, "amount": "100.00"}]'))
def test_get_transaction_data() -> None:
    """Функция для проверки как выполняется преобразования JSON файла в объект Python"""
    path_file = "mocked_file.json"
    result = get_transaction_data(path_file)
    assert result == [{"id": 123, "amount": "100.00"}]
    open.assert_called_once_with(path_file, "r", encoding="utf-8")


def test_file_not_json() -> None:
    """Функция для тестирования если указанный файл не JSON или файл не найден"""
    path_file = "mocked_file.txt"
    result = get_transaction_data(path_file)
    assert result == []


@patch("builtins.open", mock_open(read_data='{"id": 123, "amount": "100.00"}'))
def test_if_not_list() -> None:
    """Функция для проверки, что полученные данные являются списком"""
    path_file = "mocked_file.json"
    result = get_transaction_data(path_file)
    assert result == []
    open.assert_called_once_with(path_file, "r", encoding="utf-8")


@patch("builtins.open", mock_open(read_data="[{'id': 123, 'amount': '100.00'}]"))
def test_get_transaction_data_exception() -> None:
    """Функция для проверки исключений при чтении файлов"""
    path_file = "mocked_file.json"
    with pytest.raises(Exception):
        get_transaction_data(path_file)
    open.assert_called_once_with(path_file, "r", encoding="utf-8")
