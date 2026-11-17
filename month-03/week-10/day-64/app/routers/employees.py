from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_employees():
    return {"employees": []}


@router.get("/{employee_id}")
def get_employee(employee_id: int):
    return {"id": employee_id}
