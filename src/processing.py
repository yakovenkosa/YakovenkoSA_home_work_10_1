def get_sort_dict(
    list_dict: list[dict[str, str]], state: str = "EXECUTED"
) -> list[dict[str, str]]:
    """Функция, которая возвращает новый словарь"""
    new_list = []
    for ld in list_dict:
        if ld["state"] == "EXECUTED":
            new_list.append(ld)
        elif ld["state"] == "CANCELED":
            continue
    return new_list


def get_sort_list_date(list_dict: list, direction: bool = True) -> list:
    """Фенкция сортирует словари по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
