import csv
from typing import Any

import pandas as pd


def get_transaction_csv(path_file: str) -> list[dict[str | Any, str | Any]]:
    """Функция для чтения транзакций из файла CSV"""
    try:
        if ".csv" not in path_file:
            return []
        with open(path_file, encoding="utf-8") as st_file:
            reader = csv.DictReader(st_file, delimiter=";")
            list_transactions = list(reader)
        return list_transactions
    except Exception as e:
        raise Exception(f"Ошибка {Exception} {e}")


def get_transactions_xlsx(path_file: str) -> list[dict[str | Any, str | Any]]:
    """Функция для чтения транзакций из файла xlsx"""
    try:
        if ".xlsx" not in path_file:
            return []
        df = pd.read_excel(path_file)
        nested_dict_list = df.to_dict("records")
        return nested_dict_list
    except Exception as e:
        raise Exception(f"Ошибка {Exception} {e}")


if __name__ == "__main__":
    path_file_test_csv = r"C:\Users\svida\PycharmProjects\TransactionTracker\data\transactions.csv"
    print(get_transaction_csv(path_file_test_csv))
    path_file_test_xlsx = r"C:\Users\svida\PycharmProjects\TransactionTracker\data\transactions_excel.xlsx"
    print(get_transactions_xlsx(path_file_test_xlsx))
