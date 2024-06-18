import json
import logging
import pandas as pd
import csv
import os
from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)

def get_transactions(file_path: str) -> list[dict]:
    """ Функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        logger.info(f'Обращаемся к JSON-файлу и возвращаем список словарей с данными о финансовых транзакциях')
        with open(file_path, "r", encoding="utf-8") as f:
            repository = json.load(f)
            logger.info(f'Проверка файла, на что он в нём присутствуют данные')
            if isinstance(repository, list):
                logger.info(f'Возвращаем данные')
                return repository
            else:
                logger.info(f'Возвращяем пустой список, так как файл пустой, содержит не список или не найден')
                return []
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f'Ошибка при декодировании файла: {ex}')
        return []


def get_transactions_csv(file_path_csv: str)-> list[dict]:
    """Реализация функции считывания финансовых операций из CSV-файла."""
    transactions = []
    try:
        logging.info(f"Чтение CSV-файла: {file_path_csv}")
        with open(file_path_csv, "r", encoding="utf-8") as file:
            transactions_df = csv.DictReader(file, delimiter=';')
            for row in transactions_df:
                transactions.append(row)
                logging.info(f"Загружено {len(transactions)} строк из CSV-файла")
        return transactions
    except Exception as e:
        logging.error(f"Ошибка чтения CSV-файла: {e}")
        return []


def get_transactions_excel(file_path_ex: str)-> list[dict]:
    """Реализация функции считывания финансовых операций из XLSX-файла."""
    transactions = []
    try:
        with open(file_path_ex, "rb") as file_ex:
            logging.info(f"Чтение файла Excel: {file_path_ex}")
            transactions_excel = pd.read_excel(file_ex)
            if isinstance(transactions_excel, pd.DataFrame):
                list_dict = transactions_excel.to_dict("records")
                logging.info(f"Данные Excel преобразованы в список словарей: {len(list_dict)} строк")
                return list_dict
            else:
                logging.warning("Файл транзакций Excel не является DataFrame")
                return[]
    except Exception as e:
        logging.error(f"Ошибка чтения файла Excel file: {e}")
        print(f"ошибка {e}")
        return []
