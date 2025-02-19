import os
from collections import Counter
from typing import Any, Dict, List

from config import DATA_DIR
from src.csv_xlsx_utils import get_transaction_csv, get_transactions_xlsx
from src.filter_operations import filter_operations
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction_data
from src.widget import format_date, mask_account_card


def main() -> None:
    """ " Функция для обработки списка банковских транзакций"""
    print(
        "Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла.\n"
        "2. Получить информацию о транзакциях из CSV-файла.\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    work_file = input()
    print(f"Пользователь: {work_file}")
    transactions: List[Dict[str | Any]] = []
    if work_file == "1":
        print("Для обработки выбран JSON-файл")
        path_file = os.path.join(DATA_DIR, "operations.json")
        transactions = get_transaction_data(path_file)
    elif work_file == "2":
        print("Для обработки выбран CSV-файл")
        path_file = os.path.join(DATA_DIR, "transactions.csv")
        transactions = get_transaction_csv(path_file)
    elif work_file == "3":
        print("Для обработки выбран XLSX-файл")
        path_file = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        transactions = get_transactions_xlsx(path_file)
    else:
        return print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    filter_words = ["EXECUTED", "CANCELED", "PENDING"]
    filter_word = input().upper()
    while filter_word not in filter_words:
        print(f'Статус операции "{filter_word}" недоступен')
        filter_word = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
    print(transactions)
    # Сортировка транзакции по состоянию
    transactions = filter_by_state(transactions, filter_word)
    print(transactions)
    # Запрос сортировки по дате
    if input("Отсортировать операции по дате? Да/Нет").lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")  # Запрос на сортировку по убыванию
        reverse = False
        if input().lower() == "по убыванию":
            reverse = True
        transactions = sort_by_date(transactions, reverse)
    print(transactions)
    # Запрос на вывод транзакции в рублях
    if input("Выводить только транзакции в рублях? Да/Нет").lower() == "да":
        if work_file == "1":
            transactions = [
                transaction
                for transaction in transactions
                if "RUB" in transaction["operationAmount"]["currency"]["code"]
            ]
        elif work_file == "2" or work_file == "3":
            transactions = [transaction for transaction in transactions if "RUB" in transaction["currency_code"]]
    print(transactions)
    # Отфильтровать список транзакций по описанию
    if input("Отфильтровать список транзакций по определенному слову в описании? Да / Нет").lower() == "да":
        description_word = input("Введите описание: ").lower()
        transactions = filter_operations(transactions, description_word)
    print(transactions)
    print("Распечатываю итоговый список транзакций...")
    if transactions == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Подсчет количества операций в выборке
    count_transactions = Counter(transaction["description"] for transaction in transactions)
    for transaction_type, count in count_transactions.items():
        print(f"Операция: '{transaction_type}': {count} раз")

    # Печать итогового результата по выборкам транзакций
    for transaction in transactions:
        if work_file == "1":
            if (
                transaction.get("description") == "Открытие счета"
                or transaction.get("description") == "Открытие вклада"
            ):
                print(f"{format_date(transaction["date"])} {transaction["description"]}")
                print(f"{mask_account_card(transaction["to"])}")
                print(
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["name"]}\n"
                )
            else:
                print(f"{format_date(transaction["date"])} {transaction["description"]}")
                print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
                print(
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}\n"
                )
        elif work_file == "2" or work_file == "3":
            if (
                transaction.get("description") == "Открытие счета"
                or transaction.get("description") == "Открытие вклада"
            ):
                print(f"{format_date(transaction["date"])} {transaction["description"]}")
                print(f"{mask_account_card(transaction["to"])}")
                print(f"Сумма: {transaction["amount"]} {transaction['currency_code']}\n")
            else:
                print(f"{format_date(transaction["date"])} {transaction["description"]}")
                print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
                print(f"Сумма: {transaction["amount"]} {transaction['currency_code']}\n")


if __name__ == "__main__":
    main()
