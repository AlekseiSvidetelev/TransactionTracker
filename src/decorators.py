import os
import time
from functools import wraps
from typing import Any, Optional

from mypy.util import os_path_join


def log(filename: Optional[str] = None) -> Any:
    """
    Декоратор с параметром который логирует время выполнения функции и результат в файл или выводит в терминал если
    имя файла не задано.
    :param filename: Название файла куда будут записываться логи в корне проекта
    """
    def decorator(func: Any) -> Any:
        """
        Декоратор который принимает и обертывает функцию
        """
        PATH_TO_FILE = os.path.dirname(os.path.dirname(__file__))

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Функция проверяет выполнение условий, время выполнения работы функции, в случае возникновения ошибок
            выводит тип ошибки.
            """
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = f"{func.__name__}: time execution - {end_time - start_time:7f}. Result: {result}"
                if filename:
                    with open(os_path_join(PATH_TO_FILE, filename), "a") as file:
                        file.write(str(log_message) + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__}: error - {str(e)}. Input: {args}, {kwargs}"
                if filename:
                    with open(os_path_join(PATH_TO_FILE, filename), "a") as file:
                        file.write(str(log_message) + "n")
                else:
                    print(log_message)
        return wrapper

    return decorator
