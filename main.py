import os
import pandas as pd
import datetime
from src.utils import get_transactions, get_transactions_csv, get_transactions_excel
from src.processing import get_sort_dict, get_sort_list_date
from src.search_trans import get_transactions_rub
from src.search_trans import search_transactions

from typing import Any


def main() -> Any:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        selection = input("Введите выбранный номер: ")

        if selection == "1":
            print("Выбран пункт 1: Получить информацию о транзакциях из JSON-файла")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_file_path = os.path.join(current_dir, "data", 'operations.json')
            transactions = get_transactions(json_file_path)
            break
        elif selection == "2":
            print("Выбран пункт 2: Получить информацию о транзакциях из CSV-файла")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path_csv = os.path.join(current_dir, "data", "transactions.csv")
            transactions = get_transactions_csv(file_path_csv)
            break
        elif selection == "3":
            print("Выбран пункт 3: Получить информацию о транзакциях из XLSX-файла")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path_ex = os.path.join(current_dir, "data", 'transactions_excel.xlsx')
            transactions = get_transactions_excel(file_path_ex)
            break
        else:
            print("Некорректный ввод. Повторите ввод заново.")
            continue

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        select_status = input("Введите выбранный статус: ")

        if select_status.upper() == "EXECUTED":
            transactions_status = get_sort_dict(transactions, "EXECUTED")
            break
        elif select_status.upper() == "CANCELED":
            transactions_status = get_sort_dict(transactions, "CANCELED")
            break
        elif select_status.upper() == "PENDING":
            transactions_status = get_sort_dict(transactions, "PENDING")
            break
        else:
            print(f"Статус операции {select_status} недоступен. Повторите ввод заново.")
            continue

    while True:
        select_user = input("Отсортировать операции по дате? Да/Нет").lower()

        if select_user == "да":
            sort_order = input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию").lower()
            if sort_order == "по возрастанию":
                transactions_select = get_sort_list_date(transactions_status, True)
            elif sort_order == "по убыванию":
                transactions_select = get_sort_list_date(transactions_status, False)
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue

            currency = input("Выводить только рублевые тразакции? Да/Нет").lower()
            if currency == "да":
                transactions_select = get_transactions_rub(transactions, "RUB")
            elif currency == "нет":
                transactions_select = get_transactions_rub(transactions, "USD")
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue

            filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
            if filter_description == "да":
                transactions_select = search_transactions(transactions, "description")
            elif filter_description == "нет":
                transactions_select = search_transactions(transactions, "description")
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue
            break
        elif select_user == "нет":
            sort_order = input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию").lower()
            if sort_order == "по возрастанию":
                transactions_select = get_sort_list_date(transactions_status, True)
            elif sort_order == "по убыванию":
                transactions_select = get_sort_list_date(transactions_status, False)
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue

            currency = input("Выводить только рублевые тразакции? Да/Нет").lower()
            if currency == "да":
                transactions_select = get_transactions_rub(transactions, "RUB")
            elif currency == "нет":
                transactions_select = get_transactions_rub(transactions, "USD")
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue

            filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
            if filter_description == "да":
                transactions_select = search_transactions(transactions, "description")
            elif filter_description == "нет":
                transactions_select = search_transactions(transactions, "description")
            else:
                print("Некорректный ввод. Повторите ввод заново.")
                continue
            break
        else:
            print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")
            break

    return transactions_select


print(main())