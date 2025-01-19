from typing import Union

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(
    dictionary_list: list[dict[str, Union[str, int]]],
    dictionary_list_expected: list[dict[str, Union[str, int]]],
    dictionary_list_expected_: list[dict[str, Union[str, int]]],
) -> None:
    """Функция для проверки фильтрации списка словарей с данными"""
    assert filter_by_state(dictionary_list, "EXECUTED") == dictionary_list_expected
    assert filter_by_state(dictionary_list) == dictionary_list_expected
    assert filter_by_state(dictionary_list, "CANCELED") == dictionary_list_expected_


def test_sort_by_date(
    dictionary_list: list[dict[str, Union[str, int]]], sorted_list_date: list[dict[str, Union[str, int]]]
) -> None:
    """Функция для сортировки списка словарей по дате"""
    assert sort_by_date(dictionary_list) == sorted_list_date


def test_sort_revers_by_date(
    dictionary_list: list[dict[str, Union[str, int]]], sorted_list_date_revers: list[dict[str, Union[str, int]]]
) -> None:
    """Функция для проверки сортировки по дате по убыванию"""
    assert sort_by_date(dictionary_list, True) == sorted_list_date_revers
    assert sort_by_date([], True) == []
