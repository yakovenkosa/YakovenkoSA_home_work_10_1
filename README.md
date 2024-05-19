# Cерверная часть виджета банковских операций

## Описание:

Проект серверная часть виджета банковских операций - это веб-приложение на Python, которое умеет  отображать операции 
клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git

```
## Использование:

1. В файле main.py можно в передавать различные именования номеров карт и счётов.
2. Функции можно передавать дату и время банковской операции и она будет возвращать корректную дату совершения 
выбранной операции.
3. Функции можно передать список всех банковских операция, она будет возвращать список необходмых операций.
4. В проекте реализованы тесты, которые проверяют работу проекта и его модулей. Данные тесты находятся в отдельном 
пакете tests. Для их запуска необходимо воспользоваться командой pytest --cov. Если необходимо сгенерировать отчёт о 
покрытии в HTML-файле, нужно воспользоваться командой pytest --cov=src --cov-report=html .Данная программа показывает, 
какой процент кода программы был протестирован. Данный инструмент для оценки качества тестирования и выявления проблем 
в коде.
5. В проекте реализован модуль generators.py для новых функций с банковскими операциями: выдача операций с конкретной 
валютой, выдача описаний по каждой операции, и генерация новых номеров банковских карт. Реализация данных функций, так 
же выведена в модуле main.py. К модулю generators.py были написаны тесты для проверки и выявления проблем в коде.
6. В проекте реализован модуль decorators.py. Данный модуль будет логировать вызов функции и ее результат в файл или 
в консоль. Реализация функции, представлена в модуле main.py. Результат выполнения функции, независимо от выполнения её 
с ошибкой или без, записывается в текстовый документ, mylog.txt. Также реализован вывод результата в консоль. К модулю 
decorators.py были написаны тесты для проверки и выявления проблем в коде.

## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).