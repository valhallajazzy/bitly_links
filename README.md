# Скрипт "Преобразование ссылок и Счет кликов по ссылкам"

Данный скрипт помогает сократить ссылку, а так же посчитать количество кликов на нее 
используя сервис [bitly.com](https://bitly.com/pages/landing/bringing-us-all-a-bit-closer?gad_source=1&gclid=Cj0KCQiA35urBhDCARIsAOU7Qwncdg_Bi9AUFGTNgxNPr0voSbsbOGMp9nYTecd2ZCE9F4U1Q3iaYVcaAshvEALw_wcB) через терминал на вашем ПК. У скрипта есть 2 функции:

* При введении оригинальной ссылки скрипт ее сократит
* При введении сокращенной ссылки скрипт выведет количество кликом на эту ссылку

## Подготовка к запуску скрипта

Зарегистрируйтесь на сайте [bitly.com](https://bitly.com/pages/landing/bringing-us-all-a-bit-closer?gad_source=1&gclid=Cj0KCQiA35urBhDCARIsAOU7Qwncdg_Bi9AUFGTNgxNPr0voSbsbOGMp9nYTecd2ZCE9F4U1Q3iaYVcaAshvEALw_wcB)
и получите access token для подключения к API по ссылке [TOKEN](https://bitly.com/a/sign_in?rd=/settings/integrations)

В терминале, в корневой папке проекта создаем вирутальное окружение и устанавливаем
требуемые библиотеки:

```console
$ poetry install
```
Так же требуется в файлe .env обозначить переменную виртульного окружения (ACCESS_TOKEN)
и ввести полученный access_token для допуска к сервисному API

![Screenshot]()

## Запуск скрипта

В терминале, в корневой папке директории запустите скрипт:

```console
$ python main.py
```
![Screenshot]()