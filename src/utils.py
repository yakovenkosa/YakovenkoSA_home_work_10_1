import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/itils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path: str) -> list[dict]:
    """ Функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
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
