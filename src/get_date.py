from datetime import datetime


def format_date(date: str) -> str:
    """Фуккция для преобразования формата даты"""
    date_get = date[:10]
    date_format = datetime.strptime(date_get, "%Y-%m-%d")
    new_date_str = date_format.strftime("%m.%d.%Y")
    return new_date_str


if __name__ == "__main__":
    print(format_date("2024-03-11T02:26:18.671407"))
