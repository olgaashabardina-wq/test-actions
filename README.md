# FastAPI: тестовый бэкенд “текущее время”

## Запуск

1) Установите зависимости:

```bash
python -m pip install -r requirements.txt
```

2) Запустите сервер:

```bash
uvicorn app.main:app --reload
```

## Проверка

- `GET /` — healthcheck
- `GET /time` — текущее время сервера

Пример:

```bash
curl http://127.0.0.1:8000/time
```
