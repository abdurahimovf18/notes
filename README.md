# py-starter-kit

A production-ready starter kit for Python projects.
This repository provides a clean architectural foundation for medium-sized applications, helping developers start coding immediately without spending time on project setup, tooling, and infrastructure decisions.

It implements a modular structure inspired by Domain-Driven Design (DDD) and includes batteries-included integrations for APIs, message brokers, database layers, and containerization.

## Features

* Clear, layered architecture (Domain → Application → Infrastructure → Presentation)
* Domain-Driven Design principles built into the project structure
* FastAPI integration with clean dependency modules
* FastStream setup for async event-driven consumers
* Event-bus abstraction for decoupled communication
* Unit of Work pattern implemented in kernel and infrastructure layers
* Dockerized environment for local development
* Pre-configured developer tools (Ruff, Makefile, Alembic, etc.)
* Structured configuration system using environment variables

## Included Stack

* FastAPI — HTTP API layer
* FastStream — Message broker consumers
* RabbitMQ — Event bus and async messaging
* SQLAlchemy — Database ORM
* Alembic — Migrations
* psycopg[binary] — PostgreSQL driver
* Docker & Docker Compose — Local environment setup
* Makefile — Shortcuts for running, building, and maintaining the project

## Project Structure

The project follows a clean, domain-centric layout:

```
src/
 ├── domain/                  # Domain models, events, aggregates, exceptions
 ├── application/             # Use cases, DTOs, ports, services
 ├── infrastructure/          # DB, repositories, adapters, event bus, UoW
 ├── presentation/            # API + Consumer layers
 ├── framework/               # IoC container, shared setup
 ├── config/                  # Settings, environment configuration
 └── kernel/                  # Core abstractions (DDD, UoW, event bus)
```

## Getting Started

Run the local environment:

```bash
make up
```

Run migrations:

```bash
make migrate
```

## Philosophy

This starter-kit is designed for developers who want:

* predictable project structure
* separation of concerns
* testability and maintainability
* easy onboarding to new services
* consistent architecture across multiple microservices

The template is intentionally minimal yet extensible, so you can add new modules without breaking the architectural flow.
