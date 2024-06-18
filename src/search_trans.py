import re


def search_transactions(transactions: list, search_string: str) -> dict:
    """Функция, которая фильтрует список словарей с данными о банковских операциях по заданной строке поиска."""
    filtered_transactions = []
    for transaction in transactions:
        if re.search(search_string, transaction['description'], re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def categorize_transactions(transactions: list, categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории."""
    category_counts = []
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction['description'].lower():
                category_counts[category] += 1
    return category_counts


def get_transactions_rub(transactions: list, search_key: str) ->list:
    """Функция, которая фильтрует транзакции по выбранной валюте"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result
