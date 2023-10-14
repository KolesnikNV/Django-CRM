# Django-CRM

============
Приложение работает на: 

1. Backend API [Django CRM](https://github.com/MicroPyramid/Django-CRM)
2. Frontend UI [React CRM](https://github.com/MicroPyramid/react-crm "React CRM")
3. Mobile app [Flutter CRM]("https://github.com/MicroPyramid/flutter-crm")

## Runcode 
1. Клонировать репозиторий
2. В корне проекта открыть файл ```Dockerfile``` и ввести в ```DJANGO_SUPERUSER_PASSWORD``` свой пароль администратора, а переменные ```--username и --email``` свой username и password (при последующих запусках можно удалить эти команды)
3. Создать файл ```.env``` (ориентироваться можно на файл ```.example.env```)
4. В корне проекта выполнить команду ```docker-compose up --build```
5. Перейти на http://0.0.0.0:8000/admin/ и начать создавать свой сайт