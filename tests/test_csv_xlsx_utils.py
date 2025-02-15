from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_xlsx_utils import get_transaction_csv, get_transactions_xlsx


def test_file_not_find() -> None:
    """Функция для тестирования если указанный файл не найден или имеет не правильное расширение"""
    path_file = "test_file.txt"
    assert get_transaction_csv(path_file) == []
    assert get_transactions_xlsx(path_file) == []


@patch("builtins.open", mock_open(read_data="id;amount\n123;100.00\n"))
def test_get_transaction_csv() -> None:
    """Функция для тестирования чтения файла CSV"""
    path_file = "mocked_file.csv"
    result = get_transaction_csv(path_file)
    assert result == [{"id": "123", "amount": "100.00"}]
    open.assert_called_once_with(path_file, encoding="utf-8")


@patch("pandas.read_excel")
def test_get_transactions_xlsx(mock_read_excel):
    """ Функция для тестирования чтения файлов XLSX """
    mock_data = pd.DataFrame({"id": [1, 2, 3], "amount": [100.00, 200.00, 300.00]})
    mock_read_excel.return_value = mock_data
    result = get_transactions_xlsx("mocked_file.xlsx")
    expected_result = [{"id": 1, "amount": 100.00}, {"id": 2, "amount": 200.00}, {"id": 3, "amount": 300.00}]
    assert result == expected_result
    mock_read_excel.assert_called_once_with("mocked_file.xlsx")
