def get_sort_dict(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция, которая возвращает новый словарь"""
    new_list = []
    for ld in list_dict:
        if ld.get("state") == state:
            new_list.append(ld)
    return new_list


def get_sort_list_date(list_dict: list, direction: bool = True) -> list:
    """Фенкция сортирует словари по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
