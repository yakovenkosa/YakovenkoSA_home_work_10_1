from src.masks import mask_account, mask_card


def mask_account_card(number_string: str) -> str:
    """Функция принимает строку и маскирует номер карты или счёта"""
    if len(number_string.split()[-1]) == 16:
        new_number = mask_card(number_string.split()[-1])
        result = f"{number_string[:-16]}{new_number}"
    elif len(number_string.split()[-1]) == 20:
        new_number = mask_account(number_string.split()[-1])
        result = f"{number_string[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку с датой и форматирует её"""
    data_slise = old_data[0:10].split("-")
    result = ".".join(data_slise[::-1])
    return result
