FROM python:3.14-slim

WORKDIR /app

RUN pip install poetry==2.4.1

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi --without dev

COPY src/ ./src/

EXPOSE 8000

CMD ["uvicorn","src.api.main:app","--host","0.0.0.0","--port","8000"]

