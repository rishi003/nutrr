FROM python:3.12-slim

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --with main --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install --with main

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "chainlit", "run", "app.py"]