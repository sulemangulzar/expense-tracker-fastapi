# Expense Tracker FastAPI

A simple Expense Tracker API built with FastAPI, SQLModel, async SQLAlchemy, PostgreSQL, and Docker Compose.

The app supports:

- User signup
- User login
- User logout
- Protected expense endpoints
- Expense CRUD
- PostgreSQL database in Docker
- Automatic table creation when the app starts

---

## Tech Stack

| Tool | Purpose |
|---|---|
| FastAPI | API framework |
| SQLModel | Models and database tables |
| SQLAlchemy Async | Async database work |
| PostgreSQL | Database |
| asyncpg | Async PostgreSQL driver |
| Docker Compose | Run PostgreSQL easily |
| uv | Python package manager |
| Uvicorn | Run the FastAPI server |
| Scalar | Alternative API documentation |

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
- pgAdmin4, DBeaver, TablePlus, or any PostgreSQL client if you want to view the DB visually

---

## Setup

### 1. Clone the repository

```bash
git clone git@github.com:sulemangulzar/expense-tracker-fastapi.git
cd expense-tracker-fastapi
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Start PostgreSQL with Docker

```bash
docker compose up -d
```

Your database runs in Docker.

Connection details:

```text
Host: localhost
Port: 5433
Database: fastapi
User: postgres
Password: postgres
```

Important:

- Docker/Postgres uses `5432` inside the container.
- Your Mac/pgAdmin connects through `5433`.

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

Or use one full database URL:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5433/fastapi
JWT_SECRET=my-secret-key
JWT_ALGORITHM=HS256
```

If `DATABASE_URL` is missing or invalid, the app builds the URL from the `POSTGRES_*` values.

---

## Run the App

```bash
uv run uvicorn main:app --reload --port 8001
```

Open the docs:

```text
Swagger: http://127.0.0.1:8001/docs
Scalar:  http://127.0.0.1:8001/scalar
```

---

## Database and pgAdmin4

The app creates tables automatically when it starts.

Tables:

- `user`
- `expense`

### Connect in pgAdmin4

Create a new server in pgAdmin4 with these values:

```text
Name: expense-tracker-fastapi
Host name/address: localhost
Port: 5433
Maintenance database: fastapi
Username: postgres
Password: postgres
```

Then refresh and open:

```text
Servers
└── expense-tracker-fastapi
    └── Databases
        └── fastapi
            └── Schemas
                └── public
                    └── Tables
                        ├── expense
                        └── user
```

If you do not see tables, right-click `Tables` and click `Refresh`.

### Check database from terminal

```bash
docker exec -it expense-tracker-fastapi psql -U postgres -d fastapi
```

Inside `psql`:

```sql
\dt
SELECT * FROM "user";
SELECT * FROM expense;
```

Exit:

```sql
\q
```

---

## Authentication Flow

1. Signup with `/signup`
2. Login with `/login`
3. Copy the `access_token`
4. In Swagger, click `Authorize`
5. Paste the token value
6. Now you can use the expense endpoints
7. Use `/logout` to invalidate the current token

Note: logout stores the logged-out token in memory. If the server restarts, that memory is cleared. This keeps the code simple for learning.

---

## API Endpoints

### User Routes

| Method | Path | Description | Login Required |
|---|---|---|---|
| `POST` | `/signup` | Create a user | No |
| `POST` | `/login` | Login and get token | No |
| `POST` | `/logout` | Logout current token | Yes |

### Expense Routes

All expense routes require login.

| Method | Path | Description | Login Required |
|---|---|---|---|
| `GET` | `/expense/all` | Get all expenses | Yes |
| `GET` | `/expense/{id}` | Get one expense | Yes |
| `POST` | `/expense/create` | Create an expense | Yes |
| `PUT` | `/expense/update/{id}` | Update an expense | Yes |
| `DELETE` | `/expense/delete/{id}` | Delete an expense | Yes |

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

### Logout

Send the token in the `Authorization` header:

```text
Authorization: Bearer token-here
```

In Swagger, click `Authorize` and paste the token value.

Response:

```json
{
  "message": "Logged out successfully"
}
```

### Create Expense

This request requires login.

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

Stop database and delete stored data:

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

Check tables:

```bash
docker exec expense-tracker-fastapi psql -U postgres -d fastapi -c "\dt"
```

---

## Beginner Notes

- You do not create the PostgreSQL server manually. Docker Compose starts it.
- You do not create tables manually. FastAPI creates them on startup.
- Use port `5433` in pgAdmin4.
- Expense endpoints return `401` if you are not logged in.
- Login gives you a token.
- Logout blocks the current token until the app restarts.


## License
- No license included yet.