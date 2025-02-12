import logging
import os

from config import LOGS_DIR

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "masks.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setLevel(logging.INFO)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    logger.info("Начало работы")
    try:
        if len(card_number) != 16 or card_number.isdigit() is not True:
            raise ValueError("Номер карты должен содержать 16 цифр.")
        i = 0
        part_number = []
        while True:
            part = card_number[i:i + 4]
            part_number.append(part)
            i += 4
            if i >= 16:
                break
        join_part_number = " ".join(part_number)
        logger.info("Успешная работа программы")
        return f"{join_part_number[0:7]}** **** {join_part_number[-4:]}"
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    logger.info("Начало работы")
    try:
        if len(account_number) != 20 or account_number.isdigit() is not True:
            raise ValueError("Номер счета должен содержать 20 цифр.")
        logger.info("Успешное выполнение")
        return f"**{account_number[-4:]}"
    except Exception as e:
        logger.error(f"Ошибка: {e}")


if __name__ == "__main__":
    get_mask_card_number("1234123412341234")
    get_mask_card_number("123412412341234")
    get_mask_account("12345123451234512345")
    get_mask_account("1234513451234512345")
