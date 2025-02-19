import os
import re
from typing import Any, Dict, List

from config import DATA_DIR
from src.utils import get_transaction_data


def filter_operations(list_transactions: List[Dict[str, Any | str]], search_string: str) -> List[Dict[str, Any | str]]:
    """Фильтрует операции по описанию пользователя"""
    filtered_operations = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    for operation in list_transactions:
        if "description" in operation and pattern.search(operation["description"]):
            filtered_operations.append(operation)
    return filtered_operations


def count_description(list_transactions: List[Dict[str, str | Any]], list_categories: List[str]) -> Dict[str, int]:
    """Функция для подсчета заданных категорий"""
    category_count = {}
    for category in list_categories:
        category_count[category] = 0
    for transaction in list_transactions:
        description = transaction.get("description", "").lower()
        for category in list_categories:
            pattern = re.compile(r"\b" + re.escape(category.lower()) + r"\b", re.IGNORECASE)
            if pattern.search(description):
                category_count[category] += 1
    return category_count


if __name__ == "__main__":
    path_file = os.path.join(DATA_DIR, "operations.json")
    transactions = get_transaction_data(path_file)
    string = "открытие"
    res = filter_operations(transactions, string)
    print(res)
    category = ["перевод", "покупка", "оплата"]
    res1 = count_description(transactions, category)
    print(res1)
