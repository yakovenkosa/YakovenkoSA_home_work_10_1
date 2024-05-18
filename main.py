from src.processing import get_sort_dict, get_sort_list_date
from src.widget import get_new_data, mask_account_card
from src.decorators import log

print(mask_account_card("MasterCard 7158300734726758"))

print(mask_account_card("Счет 73654108430135874305"))

print(get_new_data("2018-07-11T02:26:18.671407"))

print(
    get_sort_dict(
        [
            {
                "id": "41428829",
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {
                "id": "939719570",
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": "594226727",
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": "615064591",
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)

print(
    get_sort_list_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция вызова декоратора с файлом сохранения mylog.txt"""
    return x + y


my_function(1, 2)


@log()
def my_function_1(x, y):
    """Функция вызова декоратора без файла сохранения и вывод в консоль."""
    return x + y


my_function_1(1, 2)


@log(filename="mylog.txt")
def my_function_error(x, y):
    """Функция вызова декоратора с ошибкой и сохранение вывода в файл mylog.txt"""
    return x / y


my_function_error(1, 0)
