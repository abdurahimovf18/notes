FROM python:3.12-slim

WORKDIR /app

COPY uv.lock pyproject.toml .python-version ./

RUN pip install --no-cache-dir uv 

RUN uv sync --group app --group tests --group linters

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "sleep infinity"]
