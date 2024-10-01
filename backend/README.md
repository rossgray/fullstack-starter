# backend

## Migrations

1. Start services: `make start`
2. `docker compose exec backend bash`
3. `poetry run alembic revision --autogenerate -m "todo"`
4. `poetry run alembic upgrade head`
