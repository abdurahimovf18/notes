# # # Setting up Makefile behavior
.SILENT:

# Docker Commands
up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

build:
	docker compose build

rebuild:
	$(MAKE) down
	$(MAKE) build
	$(MAKE) up

restart:
	docker compose restart app

restart-full:
	docker compose restart

# Linter/Test Commands
lint:
	uv run ruff check .

lint-fix:
	uv run ruff check . --fix

lint-fix-unsafe:
	uv run ruff check . --fix --unsafe-fixes

lint-type:
	uv run pyright

test:
	docker compose exec app uv run pytest

test-quiet:
	docker compose exec app uv run pytest -q

# Dependency Commands
sync:
	uv sync --all-groups

lock:
	uv lock

# Migration Commands
migrate-head:
	docker compose exec app uv run alembic upgrade head

migrate-base:
	docker compose exec app uv run alembic downgrade base

migrate-new:
	docker compose exec app uv run alembic stamp head

migrate-collect:
	docker compose exec app uv run alembic revision --autogenerate

migrate-up:
	docker compose exec app uv run alembic upgrade +1

migrate-down:
	docker compose exec app uv run alembic downgrade -1

# Shell Open Commands
shell:
	docker compose exec app bash

shell-db:
	docker compose exec postgres psql -U postgres -d postgres

# Tree Command
tree:
	tree > tree.txt
	