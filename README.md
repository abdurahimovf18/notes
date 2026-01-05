# Notes API

Notes API is a demonstration project that implements a full CRUD system for managing notes.
The project is designed using **Clean Architecture** and **Domain-Driven Design (DDD)** principles,
with a strong focus on separation of concerns, explicit domain rules, and long-term maintainability.

Although the domain itself is simple, the implementation reflects production-grade architectural
patterns and practices commonly used in real-world backend systems.

---

## Tech Stack

The application is built using modern and widely adopted technologies:

* **Python**
* **FastAPI** — high-performance asynchronous web framework
* **PostgreSQL** — relational database
* **SQLAlchemy** — ORM and SQL toolkit
* **Alembic** — database migrations
* **RabbitMQ** — asynchronous messaging
* **Docker & Docker Compose** — containerized development environment

---

## Architecture

The project follows:

* Clean Architecture (dependency inversion and isolated domain layer)
* Domain-Driven Design (aggregates, domain errors, explicit invariants)

The codebase is explicitly separated into the following layers:

* **Domain** — core business logic and rules
* **Application** — use cases and orchestration
* **Infrastructure** — database, messaging, and external integrations
* **API** — HTTP layer and request handling

This structure makes the system easy to test, reason about, and extend.

---

## API Endpoints

### Notes

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| GET    | `/v1/notes`           | List notes              |
| POST   | `/v1/notes`           | Create a new note       |
| PATCH  | `/v1/notes`           | Update an existing note |
| DELETE | `/v1/notes/{note_id}` | Delete a note           |
| GET    | `/v1/notes/{note_id}` | Get note details        |

---

## Requirements

> ⚠️ **Important**

This project is designed to run on **Unix-based systems** (Linux or macOS).

If you are using Windows, it is strongly recommended to run the project using
**WSL (Windows Subsystem for Linux)** to ensure compatibility and smooth execution.

---

## Running the Project

### 1. Build and start services

```bash
make build up
```

### 2. Apply database migrations

```bash
make migrate-head
```

### 3. Open API documentation

Navigate to:

```text
http://localhost:8000/docs
```

You can explore and test all available endpoints using the interactive Swagger UI.

---

## Purpose

This project is built as a **demonstration and test project**.
Its main goals are to showcase:

* Clean architectural layering
* Domain-focused error handling
* Explicit use-case driven design
* Production-oriented project structure

---

## License

MIT
