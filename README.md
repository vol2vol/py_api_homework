# py_api_homework
Сайт отличается от того, что был в гугл форме (приношу свои извинения).
Программа парсит сайт фабрики бетонов и сортирует названия изделий(блоков) по алфавиту. В качестве базы данных использовался sqlite, а для парсинга использовались библиотеки BeautifulSoup и requests. В main.py находится функция parser. Она считывает карточки всех строительных блоков и с помощью циклов for product in products и for url in urls вычленяют данные из карточек и добавляют в базу данных. dockerfile развёртывает контейнер. build.sh запускает docker-compose.
Буду доделывать интерфейс (телеграм бот).
