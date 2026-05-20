# 💸 Expense Tracker API

A simple and clean RESTful API for tracking personal expenses, built with **FastAPI**, **SQLModel**, and **SQLite**.

---

## 🚀 Features

- Create, read, update, and delete expenses
- Persistent storage using SQLite
- Auto-generated interactive API docs (Swagger UI & ReDoc)
- Data validation with Pydantic/SQLModel schemas
- Lightweight and fast — powered by FastAPI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [SQLModel](https://sqlmodel.tiangolo.com/) | ORM + data validation |
| [SQLite](https://www.sqlite.org/) | Database |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [uv](https://docs.astral.sh/uv/) | Package & project manager |

---

## 📋 Prerequisites

- Python **3.13+**
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

---

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/expense-tracker-fastapi.git
cd expense-tracker-fastapi
```

**2. Install dependencies using `uv`**

```bash
uv sync
```

**3. Run the development server**

```bash
uv run uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

---

## 📖 API Documentation

Once the server is running, visit:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints

### Expenses

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/expenses` | Get all expenses |
| `GET` | `/expense/{id}` | Get a single expense by ID |
| `POST` | `/create` | Create a new expense |
| `PUT` | `/update/{id}` | Update an existing expense |
| `DELETE` | `/expense-delete/{id}` | Delete an expense |

---

### Request & Response Examples

#### ➕ Create an Expense — `POST /create`

**Request Body:**

```json
{
  "amount": 49.99,
  "description": "Grocery shopping at Walmart",
  "category": "Food",
  "date": "2025-01-15T10:30:00"
}
```

**Response:**

```json
{
  "id": 1,
  "amount": 49.99,
  "description": "Grocery shopping at Walmart",
  "category": "Food",
  "date": "2025-01-15T10:30:00",
  "created_at": "2025-01-15T10:35:00",
  "updated_at": "2025-01-15T10:35:00"
}
```

#### ✏️ Update an Expense — `PUT /update/{id}`

**Request Body** (all fields are optional):

```json
{
  "amount": 55.00,
  "description": "Updated grocery bill"
}
```

#### 🗑️ Delete an Expense — `DELETE /expense-delete/{id}`

**Response:**

```json
{
  "message": "Todo deleted successfully"
}
```

---

## 🗂️ Project Structure

```
expense-tracker-fastapi/
├── main.py          # Application entry point and lifespan events
├── routers.py       # API route definitions
├── models.py        # SQLModel database models
├── schemas.py       # Pydantic schemas (Create, Read, Update)
├── database.py      # Database engine, session, and table setup
├── expense.db       # SQLite database file (auto-generated)
└── pyproject.toml   # Project metadata and dependencies
```

---

## 🧾 Data Model

### Expense

| Field | Type | Description |
|---|---|---|
| `id` | `int` | Auto-generated primary key |
| `amount` | `float` | Expense amount (must be > 0) |
| `description` | `str` | Short description (max 250 chars) |
| `category` | `str` | Expense category (e.g. Food, Travel) |
| `date` | `datetime` | Date of the expense |
| `created_at` | `datetime` | Auto-set on creation |
| `updated_at` | `datetime` | Auto-set on update |

---

## 📦 Dependencies

```toml
dependencies = [
    "fastapi>=0.136.1",
    "sqlmodel>=0.0.38",
    "uvicorn>=0.47.0",
]
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
