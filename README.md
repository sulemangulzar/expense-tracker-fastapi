# Expense Tracker API

A FastAPI expense tracking service with async database support and a package-based layout.

---

## Overview

This app provides CRUD operations for expenses through a REST API.
It uses SQLModel and SQLAlchemy for persistence and supports PostgreSQL via `.env` configuration.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Web framework |
| SQLModel | ORM and data validation |
| SQLAlchemy | Async engine and sessions |
| asyncpg | PostgreSQL async driver |
| Uvicorn | ASGI server |
| uv | Dependency manager |

---

## Prerequisites

- Python 3.13+
- `uv` installed (recommended)
- PostgreSQL if using production DB configuration

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/expense-tracker-fastapi.git
cd expense-tracker-fastapi
```

**2. Install dependencies**

```bash
uv sync
```

**3. Configure database settings**

Update `.env` with your database values:

```env
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345
POSTGRES_DB=fastapi
DATABASE_URL=postgresql+asyncpg://postgres:12345@localhost:5432/fastapi
```

If no PostgreSQL database is configured, the app will fall back to SQLite using `sqlite+aiosqlite:///expense.db`.

**4. Run the application**

```bash
uv run uvicorn main:app --reload
```

The service will run at `http://127.0.0.1:8000`.

---

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/expense/all` | List all expenses |
| `GET` | `/expense/{id}` | Retrieve one expense by ID |
| `POST` | `/expense/create` | Create a new expense |
| `PUT` | `/expense/update/{id}` | Update an expense |
| `DELETE` | `/expense/delete/{id}` | Delete an expense |

---

## Example Request

### Create an Expense

```json
{
  "amount": 49.99,
  "description": "Grocery shopping",
  "category": "Food",
  "date": "2025-01-15T10:30:00"
}
```

### Example Response

```json
{
  "id": 1,
  "amount": 49.99,
  "description": "Grocery shopping",
  "category": "Food",
  "date": "2025-01-15T10:30:00",
  "created_at": "2025-01-15T10:35:00+00:00",
  "updated_at": "2025-01-15T10:35:00+00:00"
}
```

---

## Project Structure

```
expense-tracker-fastapi/
├── main.py
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routers.py
│   │   └── dependencies.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── services/
│       ├── __init__.py
│       └── expenses.py
├── .env
├── .venv/
├── pyproject.toml
└── uv.lock
```

---

## Expense Model

| Field | Type | Description |
|---|---|
| `id` | `int` | Primary key |
| `amount` | `float` | Expense amount |
| `description` | `str` | Description of the expense |
| `category` | `str` | Expense category |
| `date` | `datetime` | Expense date/time |
| `created_at` | `datetime` | Auto-set on creation |
| `updated_at` | `datetime` | Auto-set on update |

---

## Notes

- Root `main.py` imports the FastAPI app from `app/main.py`.
- Database settings are loaded from `.env` and can fall back to SQLite if needed.
- The app uses async SQLAlchemy sessions and route organization under `app/api`.

---

## Dependencies

```toml
dependencies = [
    "fastapi[all]>=0.136.1",
    "pydantic>=2.13.4",
    "sqlmodel>=0.0.38",
    "uvicorn>=0.47.0",
]
```
