import json
from typing import Union


def get_transaction_data(path_file: str) -> list[dict[str, Union[str | int]]]:
    """Получает данные о финансовых транзакциях по указанному пути до файла и возвращает список Python"""
    try:
        if ".json" not in path_file:
            return []
        with open(path_file, "r", encoding="utf-8") as file:
            transaction_list = json.load(file)
            if not isinstance(transaction_list, list):
                return []
            return transaction_list
    except Exception as e:
        raise Exception(f"Ошибка: {e}")
