from contextlib import nullcontext as does_not_raise

import pytest

from src.decorators import log


def my_function(x, y):
    """Функция для тестирования декоратора"""
    if x < y:
        raise ValueError("Values must be greater zero")
    return x + y


@pytest.mark.parametrize(
    "x, y, expected, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (4, 5, 9, does_not_raise()),
        (7, 7, 14, does_not_raise()),
        (-1, 2, 1, pytest.raises(ValueError)),
    ],
)
@log()
def test_my_function(x, y, expected, expectation):
    """Функция для тестирования декоратора если название файла не задано и данные выводятся в консоль"""
    with expectation:
        assert my_function(x, y) == expected


@log("mylog.txt")
@pytest.mark.parametrize(
    "x, y, expected, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (4, 5, 9, does_not_raise()),
        (7, 7, 14, does_not_raise()),
        (-1, 2, 1, pytest.raises(ValueError)),
    ],
)
def test_log_with_file_name(x, y, expected, expectation):
    """Функция для тестирования декоратора если название файла задано. Название файла mylog.txt"""
    with expectation:
        assert my_function(x, y) == expected
