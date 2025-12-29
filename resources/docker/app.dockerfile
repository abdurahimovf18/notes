FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY uv.lock pyproject.toml .python-version ./

RUN uv sync --group app --group tests

COPY . .

EXPOSE 8000

ENTRYPOINT [\
    "uv", "run", \
    "gunicorn", \
    "src.main:app", \
    "-k", "uvicorn.workers.UvicornWorker", \
    "-b", "0.0.0.0:8000" \
]
