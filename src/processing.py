from typing import Union

from src.widget import format_date


def filter_by_state(
    dict_list: list[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str, int]]]:
    """Функция для фильтрации списка словарей по состоянию"""
    filter_list = []
    for dictionary in dict_list:
        if dictionary["state"] == state:
            filter_list.append(dictionary)
    return filter_list


def sort_by_date(
    sort_list: list[dict[str, Union[str, int]]], revers_sort: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Функция для сортировки списка словарей по дате"""
    sorted_list = sorted(sort_list, key=lambda x: format_date(x["date"]), reverse=revers_sort)
    return sorted_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
        )
    )
