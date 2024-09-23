# products-app

## Requirements

- docker
- python3.12

## Запуск

- [Локально](#локально)
- [Docker](#docker)

## Локально

### Настройка проекта

#### 1. Создать виртуальное окружение

```bash
python3 -m virtualenv venv
```

#### 2. Активировать виртуальное окружение

```bash
source venv/bin/activate
```

#### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

#### 4. Накатить миграции

```bash
python shop_project/manage.py migrate
```

### Запуск

```bash
python shop_project/manage.py runserver
```

## Docker

### Настройка проекта

#### 1. Создать docker-образ

```bash
docker build -t shop_project .
```

#### 2. Запустить docker-контейнер

```bash
docker run -p 8000:8000 --name shop_project shop_project
```

#### 3. Зайти в docker-контейнер

```bash
docker exec -it shop_project /bin/bash
```

#### 4. Накатить миграции

```bash
python3 shop_project/manage.py migrate
```

### Запуск

```bash
docker run -p 8000:8000 --name shop_project shop_project
```

## Доступ

http://localhost:8000
