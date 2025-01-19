from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(account_numbers: list[dict[str, Union[str, int]]]) -> None:
    """Функция для проверки маскировки номера счета"""
    for input_account_numbers, mask_account_numbers in account_numbers:
        assert get_mask_account(input_account_numbers) == mask_account_numbers
    assert get_mask_account("73654108430669958748") == "**8748"  # номер счета


def test_get_mask_account_incorrect_value() -> None:
    """Функция для проверки выпадения ошибок при несоответствии количества символов номера счета"""
    with pytest.raises(ValueError):
        get_mask_account("9090")
    with pytest.raises(ValueError):
        get_mask_account("736541084306r9958748")
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_card_number(card_numbers: list[dict[str, Union[str, int]]]) -> None:
    """Функция проверки маскировки номера карты"""
    for input_card_numbers, mask_card_numbers in card_numbers:
        assert get_mask_card_number(input_card_numbers) == mask_card_numbers
    assert get_mask_card_number("7000742189606391") == "7000 74** **** 6391"  # номер карты


def test_get_mask_card_number_incorrect_value() -> None:
    """Функция для тестирования функции если количество цифр номера карты не соответствует"""
    with pytest.raises(ValueError):
        get_mask_card_number("90902342")
    with pytest.raises(ValueError):
        get_mask_card_number("700074218960e391")
