![Static Badge](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=yellow)
![Static Badge](https://img.shields.io/badge/docker-25.0.4-blue?logo=docker)
![Static Badge](https://img.shields.io/badge/redis-7.2.4-blue?logo=redis&logoColor=red)
![Static Badge](https://img.shields.io/badge/uv-0.5.11-blue?logo=uv&logoColor=%23DE5FE9)
![Static Badge](https://img.shields.io/badge/FastAPI-0.115.6-blue?logo=fastapi&logoColor=%23009688)
![Static Badge](https://img.shields.io/badge/sqlalchemy-2.0.37-blue?logo=sqlalchemy&logoColor=%23D71F00)
![Static Badge](https://img.shields.io/badge/PostgreSQL-15.0-blue?logo=postgresql&logoColor=%234169E1)

## HUB

Хранилище созданных матриц и пользователей, имеющих доступ к их управлению

## Сборка

Для сборки приложения разработан [Dockerfile](https://github.com/awrura/hub/blob/main/docker/Dockerfile), запуск приложения осуществляется через него. **Важно**, перед запуском docker контейнера необходимо создать и заполнить `.env` файл. 
Пример файла можно посмотреть в [.env.example](https://github.com/awrura/hub/blob/main/.env.example)

## Жизненный цикл

Матрицы создаются через административный интерфейс данного сервиса, после чего, пользователю выдается некоторый `secret key` связанный с созданной матрицей. С помощью данного ключа он имеет возможность ~~активировать~~ привязать матрицу 
к своему профилю для дальнейшего использования
