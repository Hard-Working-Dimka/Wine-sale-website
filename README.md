# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите библиотеки 
```
pip install -r requirements.txt.
```
Далее пользователю предоставляется выбор запуска сайта:
1. Запуск с использованием переменных окружения
2. Запуск с использованием параметров по умолчанию
3. Запуск с пользовательскими параметрами

### Запуск с использованием переменных окружения

Для запуска с использованием переменных окружения необходимо создать в каталоге с проектом файл `.env` и вставить в него следующий код:
```
EXEL_LIST_NAME = ''
EXEL_PATH_NAME = ''
```
Вставьте в переменную `EXEL_LIST_NAME` название рабочего листа exel и в переменную `EXEL_PATH_NAME` путь до exel таблицы с напитками (вставлять в кавычки). 

Перед запуском ознакомьтесь с [требованиями](#требования-к-exel-таблице) к exel таблице.

Запустите сайт командой:
```
python3 main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Запуск с использованием параметров по умолчанию

Для запуска с параметрами по умолчанию должны выполняться следующие требования.
* файл Exel находится в каталоге с проектом
* файл Exel имеет название `wine.xlsx`
* рабочий лист exel имеет название `Лист1`

Перед запуском ознакомьтесь с [требованиями](#требования-к-exel-таблице) к exel таблице.

Запустите сайт командой:
```
python3 main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Запуск с пользовательскими параметрами

Пользовательскими параметрами являются:
1. путь до Exel файла
2. название рабочего листа Exel

Параметр -p отвечает за путь до Exel файла, параметр -l за название рабочего листа Exel. 

Перед запуском ознакомьтесь с [требованиями](#требования-к-exel-таблице) к exel таблице.

Запустите сайт командой, заменив `EXEL_PATH_NAME` и `EXEL_LIST_NAME`:
```
python3 main.py -p EXEL_PATH_NAME -l EXEL_LIST_NAME
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Для подробного описания консольных аргументов, введите:
```
python3 main.py -h
```



## Требования к Exel таблице
Таблица Exel должна быть следующего формата:

| Категория | Название | Сорт | Цена | Картинка | Акция |
|:---------:|:--------:|-----:|:----:|:--------:|:-----:|
|    ...    |   ...    |  ... | ...  |   ...    |  ...  |

Столбцы 'Сорт' и 'Акция' заполнять необязательно, но присутствие названий **всех** заголовков обязательно! Так же во всех названиях заголовков необходимо соблюдать регистр на тот, что указан в шаблоне выше.

Картинки напитков должны храниться в папке`images`, а их названия в Exel таблице содержать расширение файла.
## Цели проекта

Код написан в учебных целях.
