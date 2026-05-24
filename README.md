# Expense Tracker FastAPI

A simple beginner-friendly Expense Tracker API built with FastAPI, SQLModel, async SQLAlchemy, and PostgreSQL.

The app supports:

- User signup
- User login
- Expense CRUD
- PostgreSQL with Docker Compose
- Automatic table creation on app startup

---

## Tech Stack

| Tool | Purpose |
|---|---|
| FastAPI | API framework |
| SQLModel | Models and database tables |
| SQLAlchemy Async | Async database connection |
| PostgreSQL | Main database |
| asyncpg | Async PostgreSQL driver |
| Docker Compose | Run PostgreSQL easily |
| uv | Python package manager |
| Uvicorn | Run FastAPI app |

---

## Project Structure

```text
expense-tracker-fastapi/
├── main.py
├── compose.yaml
├── pyproject.toml
├── uv.lock
├── README.md
└── app/
    ├── config.py
    ├── utils.py
    ├── api/
    │   └── dependencies.py
    ├── core/
    │   └── security.py
    ├── database/
    │   └── database.py
    ├── models/
    │   └── models.py
    ├── routers/
    │   ├── routers.py
    │   ├── user.py
    │   └── expenses.py
    ├── schemas/
    │   └── schemas.py
    └── services/
        ├── user.py
        └── expenses.py
```

---

## Requirements

- Python 3.13+
- uv
- Docker Desktop

---

## Setup

### 1. Clone the project

```bash
git clone git@github.com:sulemangulzar/expense-tracker-fastapi.git
cd expense-tracker-fastapi
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Start PostgreSQL

```bash
docker compose up -d
```

This starts PostgreSQL in Docker.

Database connection details:

```text
Host: localhost
Port: 5433
Database: fastapi
User: postgres
Password: postgres
```

The Docker container uses internal PostgreSQL port `5432`, but your Mac connects through port `5433`.

---

## Environment Variables

Create a `.env` file in the project root:

```env
POSTGRES_SERVER=localhost
POSTGRES_PORT=5433
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fastapi

JWT_SECRET=my-secret-key
JWT_ALGORITHM=HS256
```

You can also use one full database URL instead:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5433/fastapi
JWT_SECRET=my-secret-key
JWT_ALGORITHM=HS256
```

If `DATABASE_URL` is invalid or missing, the app builds the PostgreSQL URL from the `POSTGRES_*` values.

---

## Run the App

```bash
uv run uvicorn main:app --reload --port 8001
```

Open Swagger docs:

```text
http://127.0.0.1:8001/docs
```

---

## Database

Tables are created automatically when the app starts.

Tables:

- `user`
- `expense`

To check the database directly:

```bash
docker exec -it expense-tracker-fastapi psql -U postgres -d fastapi
```

Inside `psql`:

```sql
\dt
SELECT * FROM "user";
SELECT * FROM expense;
```

Exit `psql`:

```sql
\q
```

---

## API Endpoints

### User Routes

| Method | Path | Description |
|---|---|---|
| `POST` | `/signup` | Create a user |
| `POST` | `/login` | Login and get an access token |

### Expense Routes

| Method | Path | Description |
|---|---|---|
| `GET` | `/expense/all` | Get all expenses |
| `GET` | `/expense/{id}` | Get one expense |
| `POST` | `/expense/create` | Create an expense |
| `PUT` | `/expense/update/{id}` | Update an expense |
| `DELETE` | `/expense/delete/{id}` | Delete an expense |

---

## Request Examples

### Signup

```json
{
  "name": "Suleman",
  "email": "suleman@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "id": 1,
  "name": "Suleman",
  "email": "suleman@example.com"
}
```

### Login

```json
{
  "email": "suleman@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "token-here",
  "token_type": "bearer"
}
```

### Create Expense

```json
{
  "amount": 25.5,
  "description": "Lunch",
  "category": "Food",
  "date": "2026-05-24T12:00:00Z"
}
```

Response:

```json
{
  "id": 1,
  "amount": 25.5,
  "description": "Lunch",
  "category": "Food",
  "date": "2026-05-24T12:00:00Z",
  "created_at": "2026-05-24T14:55:22.435899Z",
  "updated_at": "2026-05-24T14:55:22.435909Z"
}
```

---

## Useful Commands

Start database:

```bash
docker compose up -d
```

Stop database:

```bash
docker compose down
```

Stop database and remove stored data:

```bash
docker compose down -v
```

Run app:

```bash
uv run uvicorn main:app --reload --port 8001
```

Check Docker logs:

```bash
docker logs expense-tracker-fastapi
```

---

## Notes for Beginners

- You do not need to create the PostgreSQL server manually. Docker Compose starts it for you.
- You do not need to create tables manually. FastAPI creates them on startup.
- If the API request succeeds, the data is saved in Docker PostgreSQL.
- Use port `5433` in DB tools like pgAdmin, DBeaver, or TablePlus.
