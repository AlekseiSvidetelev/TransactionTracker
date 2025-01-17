import pytest

from src.widget import format_date, mask_account_card


def test_mask_account_card(account_card: list[tuple[str, str]]) -> None:
    for input_account_card, output_account_card in account_card:
        assert mask_account_card(input_account_card) == output_account_card


def test_mask_account_card_incorrect() -> None:
    with pytest.raises(ValueError):
        mask_account_card("9090")
    with pytest.raises(ValueError):
        mask_account_card("qwed23424")


@pytest.mark.parametrize(
    "date, expected_result_date",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2022-06-17T02:26:18.671407", "17.06.2022")],
)
def test_format_date(date: str, expected_result_date: str) -> None:
    assert format_date(date) == expected_result_date
    with pytest.raises(ValueError):
        format_date("2122-13-15T32:32:23.23423")  # неправильный формат даты
    with pytest.raises(ValueError):
        format_date("2122")  # неправильный тип данных
