# TransactionTracker
Проект предназначен для реализации виджета, который будет показывать последние успешные операции клиентов в личном кабинете банка.

## Установка и настройка
Для установки зависимостей и настройки проекта выполните следующие действия:

pip install -r pyprojekt.toml

## Использование функционала

### Модуль masks
Модуль содержит функции для маскировки номеров банковских карт и счетов:

get_mask_card_number(card_number): Маскирует номер банковской карты.
get_mask_account(account_number): Маскирует номер банковского счета.

### Модуль widget
Модуль содержит функции для работы с данными операций:

mask_account_card(card_number): Обрабатывает информацию о карте или счете, возвращая замаскированный номер.
get_date(date): Преобразует дату в формат ДД.ММ.ГГГГ.

### Модуль processing
Модуль содержит функции для фильтрации и сортировки данных:

filter_by_state(dict_list, state="EXECUTED"): Фильтрует операции по состоянию.
sort_by_date(sort_list, ascending=True): Сортирует операции по дате.
