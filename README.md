# Backend для ХАКАТОНА

# Зависимости

- Python3
- Poetry
- Docker
- Docker-compose

# Установка

```bash
git clone git@github.com:ct-mtusi-hackathon/hackathon-backend.git
cd hackathon-backend

# Скопируйте переменные окружения
cat env_sample > .env # Изменить значения
```

# Для продакшена и фронтендера

```bash
docker-compose up --build -d
```

# Разработка

```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
hackathon migrate
```

## Запуск сервера

```bash
hackathon runserver
```
