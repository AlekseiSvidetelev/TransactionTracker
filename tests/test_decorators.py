from contextlib import nullcontext as does_not_raise

import pytest

from src.decorators import log


@log()
def sum_arg(x: float, y: float) -> float:
    """Функция для тестирования декоратора"""
    if x == y:
        raise ValueError("'x' не должен быть равен 'y'")
    return x + y


@pytest.mark.parametrize(
    "x, y, expected, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (4, 5, 9, does_not_raise()),
        (7, 8, 15, does_not_raise()),
    ],
)
def test_my_function(x, y, expected, expectation):
    """Функция для тестирования декоратора если название файла не задано и данные выводятся в консоль"""
    with expectation:
        assert sum_arg(x, y) == expected


def test_exception(capsys):
    """Функция для тестирования исключений декоратора если название файла не задано и вывод на консоль"""
    with pytest.raises(ValueError):
        sum_arg(1, 1)
        raise ValueError("'x' не должен быть равен 'y'")
    out, err = capsys.readouterr()
    assert out == "sum_arg: error - 'x' не должен быть равен 'y'. Input: (1, 1), {}\n"
    assert err == ""


@log("mylog.txt")
def sum_arg_with_file_name(x, y):
    """Функция для тестирования декоратора"""
    if x == y:
        raise ValueError("'x' не должен быть равен 'y'")
    return x + y


@pytest.mark.parametrize(
    "x, y, expected, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (4, 5, 9, does_not_raise()),
        (7, 8, 15, does_not_raise()),
    ],
)
def test_log_with_file_name(x, y, expected, expectation):
    """Функция для тестирования декоратора если название файла задано. Название файла mylog.txt"""
    with expectation:
        assert sum_arg_with_file_name(x, y) == expected


def test_exception_(capsys):
    """Функция для тестирования исключений декоратора если название файла задано. Название файла mylog.txt"""
    with pytest.raises(ValueError):
        sum_arg_with_file_name(1, 1)
        raise ValueError("'x' не должен быть равен 'y'")
