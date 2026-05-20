from select import select

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from database import sessionDep
from models import Expense
from schemas import ExpenseCreate, ExpenseRead, ExpenseUpdate

router = APIRouter()


@router.get("/expenses", response_model=list[ExpenseRead])
def get_all_expenses(session: sessionDep):
    expenses = session.exec(select(Expense)).all()
    return expenses


@router.get(f"/expense/{id}", response_model=ExpenseRead)
def get_expense_by_id(id: int, session: sessionDep):
    expense = session.get(Expense, id)

    if not expense:
        raise HTTPException(status_code=404, detail="Todo not found")

    return expense


@router.post("/create", response_model=ExpenseRead)
def create_espense(expense: ExpenseCreate, session: sessionDep):
    new_expense = Expense(**expense.model_dump())

    session.add(new_expense)
    session.commit()
    session.refresh(new_expense)

    return new_expense


@router.put(f"/update/{id}", response_model=ExpenseRead)
def update_todo(id: int, update_schema: ExpenseUpdate, session: sessionDep):
    expense = session.get(Expense, id)

    if not expense:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_data = expense.sqlmodel_update(update_schema)

    session.add(updated_data)
    session.commit()
    session.refresh(expense)

    return expense


@router.delete("/expense-delete/{todo_id}")
def delete_todo(id: int, session: sessionDep):
    expense = session.get(Expense, id)

    if not expense:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(expense)
    session.commit()

    return {"message": "Todo deleted successfully"}
