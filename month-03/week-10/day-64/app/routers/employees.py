from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


def verificar_rol(rol: str):
    return {"rol": rol}


admin_user_dependency = Depends(lambda: verificar_rol("admin"))

employees = [
    {"id": 1, "name": "Josue"},
    {"id": 2, "name": "Cedrick"},
]


@router.get("/")
def get_employees():
    return {"employees": []}


@router.get("/admin")
def get_admin(user: dict = admin_user_dependency):
    return user


@router.get("/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee["name"]

    raise HTTPException(status_code=404, detail="Employee not found.")
