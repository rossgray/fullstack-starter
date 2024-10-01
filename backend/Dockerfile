FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc curl gnupg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# RUN pipx install poetry

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml poetry.lock alembic.ini /app/

RUN poetry install

COPY ./api /app/api
COPY ./alembic /app/alembic

CMD ["poetry", "run", "fastapi", "dev", "--host", "0.0.0.0", "api/main.py"]