FROM python:3.10-alpine

EXPOSE 8000

WORKDIR /code

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /code

RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi --without test

CMD ["poetry", "run", "uvicorn",  "fast_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
