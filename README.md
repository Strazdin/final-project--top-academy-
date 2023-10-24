<h2 align="center"> final-project--top-academy</h2>

### Краткое описание проекта:
Парикмахерская. Запись к парикмахеру.

### Функционал сайта:

Запись к парикмахеру с выбором даты и времени.

### Инструменты разработки

**Стек:**
- Python 3.11.0
- Django 4.2.2
- sqlite3

## Этапы разработки

##### 1) Создание проекта и приложения, базовая настройка проекта

##### 2) Делаю функционал записи к парикмахеру

##### 3) Добавляю модели барберов и услуг. Работа с ними в админке. Делаю выгрузку данных на страницу из БД

##### 4) Делаю возможность записаться к другому парикмахеру, если желаемое время уже было занято

##### заметка (решено): при удалении барбера из бд, записи к нему на услугу остается, на работу логики пока это не влияет

##### 5) Настраиваю админ-панель. Появилась возможность записать клиента через панель админа, редактировать запись (при удалении барбера удаляются все записи связанные с ним из БД, а при удалении услуги - соответствующее поле в записи оборачивается в значение NULL), а также настроил удобный поиск по записям.

## License

MIT License

Copyright (c) 2023 Strazdin Dmitriy