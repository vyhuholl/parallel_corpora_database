# **База данных параллельного подкорпуса НКРЯ** <sup>1</sup>

Параллельный подкорпус НКРЯ: http://ruscorpora.ru/new/search-para.html <br>
<br>
## **Содержание**


*  **Схема БД.txt** – описание базы данных
*  **db_init.py** – скрипт, инициализирующий базу данных
*  **db_backend.py** – код запросов к БД
*  **main.py** – веб-интерфейс на Flask
*  */data* – таблицы БД в формате csv, а также питоновские объекты, использованные при создании таблиц.
*  */templates* – шаблоны HTML.


<br>
## **Запросы к БД**

<br>

## **Запуск приложения через командную строку**


1. Склонировать репозиторий командой `git clonе`: <br>
```bash
git clone https://github.com/vyhuholl/parallel_corpora_database.git
```
2. Установить необходимые библиотеки из *requirements.txt*: <br>
```bash
pip3 install -r requirements.txt
```
3. Убедиться, что у вас установлен mysql.
4. Заменить в файле `authentification.py` `USER` и `PASSWORD` на логин и пароль от вашего MySql сервера.
5. Находясь в репозитории приложения, запустить mysql и импортировать БД под именем `parallel_corpora_db`, заменив *username* на логин от вашего MySql сервера:
```bash
mysql -u username -p parallel_coprora_db < parallel_coprora_db.sql
```
6. Находясь в репозитории приложения, запустить `main_py`:
```bash
python main.py
```
7. Открыть в браузере адрес http://127.0.0.1:5000/


<br>
<sup>1</sup> – не учитывался многоязычный раздел параллельного подкорпуса НКРЯ и подкорпус русской классики в немецких переводах.
