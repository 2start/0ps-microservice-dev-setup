FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY Pipfile* ./

RUN pip install --no-cache-dir pipenv \
  && pipenv install --system --deploy

COPY . .
ENV PYTHONPATH=/app
