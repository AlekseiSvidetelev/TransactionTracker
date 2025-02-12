import json
import logging
import os.path
from typing import Union

from config import LOGS_DIR

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setLevel(logging.INFO)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(path_file: str) -> list[dict[str, Union[str | int]]]:
    """Получает данные о финансовых транзакциях по указанному пути до файла и возвращает список Python"""
    logger.info("Начало работы")
    try:
        if ".json" not in path_file:
            logger.info("Файл JSON не найден")
            return []
        with open(path_file, "r", encoding="utf-8") as file:
            transaction_list = json.load(file)
            if not isinstance(transaction_list, list):
                logger.info("Файл JSON не является списком")
                return []
            logger.info("Файл JSON успешно прочитан")
            return transaction_list
    except Exception as e:
        logger.error(f"Произошла ошибка {e}")
        raise Exception(f"Ошибка: {e}")


if __name__ == "__main__":
    path_file_test = r"C:\Users\svida\PycharmProjects\TransactionTracker\data\operations.json"
    get_transaction_data(path_file_test)
