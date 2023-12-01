# Скрипт "Преобразователь ссылок"

Данный скрипт помогает сократить ссылку, а так же посчитать количество кликов на нее 
используя сервис [bitly.com](https://bitly.com/pages/landing/bringing-us-all-a-bit-closer?gad_source=1&gclid=Cj0KCQiA35urBhDCARIsAOU7Qwncdg_Bi9AUFGTNgxNPr0voSbsbOGMp9nYTecd2ZCE9F4U1Q3iaYVcaAshvEALw_wcB) через терминал на вашем ПК. У скрипта есть 2 функции:

* При введении оригинальной ссылки скрипт ее сократит
* При введении сокращенной ссылки скрипт выведет количество кликов по этой ссылке

## Подготовка к запуску скрипта

Зарегистрируйтесь на сайте [bitly.com](https://bitly.com/pages/landing/bringing-us-all-a-bit-closer?gad_source=1&gclid=Cj0KCQiA35urBhDCARIsAOU7Qwncdg_Bi9AUFGTNgxNPr0voSbsbOGMp9nYTecd2ZCE9F4U1Q3iaYVcaAshvEALw_wcB)
, а так же получите access token для подключения к API по ссылке [TOKEN](https://bitly.com/a/sign_in?rd=/settings/integrations)

В терминале, в корневой папке проекта создаем вирутальное окружение и устанавливаем
требуемые библиотеки:

```console
$ poetry install
```
Так же требуется в файлe .env обозначить переменную виртульного окружения (BITLY_ACCESS_TOKEN)
и ввести полученный access_token для допуска к сервисному API

![Screenshot](https://github.com/valhallajazzy/bitly_links/blob/main/pictures/ACCESS_TOKEN.png)

## Запуск скрипта

В терминале, в корневой папке директории запустите скрипт:

```console
$ python3 main.py
```
![Screenshot](https://github.com/valhallajazzy/bitly_links/blob/main/pictures/RUNNING_THE_SCRIPT.png)
