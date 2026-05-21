from fastapi import APIRouter

from app.api.dependencies import ServiceDep
from app.schemas import ExpenseCreate, ExpenseRead, ExpenseUpdate

router = APIRouter(prefix="/expense")


@router.get("/all", response_model=list[ExpenseRead])
async def get_all_expenses(service: ServiceDep):
    return await service.get_all()


@router.get("/{id}", response_model=ExpenseRead)
async def get_expense(id: int, service: ServiceDep):
    return await service.get(id)


@router.post("/create", response_model=ExpenseRead)
async def create_expense(expense: ExpenseCreate, service: ServiceDep):
    return await service.add(expense)


@router.put("/update/{id}", response_model=ExpenseRead)
async def update_expense(
    id: int,
    update_schema: ExpenseUpdate,
    service: ServiceDep,
):
    return await service.update(id, update_schema)


@router.delete("/delete/{id}")
async def delete_expense(id: int, service: ServiceDep):
    return await service.delete(id)
