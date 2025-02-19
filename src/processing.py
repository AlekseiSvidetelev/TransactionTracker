from typing import Union


def filter_by_state(
    dict_list: list[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str, int]]]:
    """Функция для фильтрации списка словарей по состоянию"""
    filter_list = []
    for dictionary in dict_list:
        if dictionary.get("state", "") == state:
            filter_list.append(dictionary)
    return filter_list


def sort_by_date(
    sort_list: list[dict[str, Union[str, int]]], reverse: bool = False
) -> list[dict[str, Union[str, int]]]:
    """Функция для сортировки списка словарей по дате"""
    sorted_list = sorted(sort_list, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
