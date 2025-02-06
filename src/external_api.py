import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")


def convert_sum_transactions(transaction: dict[str, Any], base_currency: Optional[str] = "RUB") -> float:
    try:
        convert_from = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        if transaction["operationAmount"]["currency"]["code"] == base_currency:
            return float(transaction["operationAmount"]["amount"])
        else:
            url = "https://api.exchangeratesapi.io/v1/latest"
            params = {"access_key": API_KEY}
            response = requests.get(url, params=params)
            response_join = response.json()
            amount_base_currency = (
                amount / float(response_join["rates"][convert_from]) * float(response_join["rates"][base_currency])
            )
            return round(amount_base_currency, 2)
    except Exception as e:
        raise Exception(f"Ошибка {e}")
