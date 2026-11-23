from fastapi import APIRouter, Depends, HTTPException, status

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
    return {"employees": employees}


@router.get("/admin", status_code=status.HTTP_200_OK)
def get_admin(user: dict = admin_user_dependency):
    return user


@router.get("/{employee_id}", status_code=status.HTTP_200_OK)
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee["name"]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found."
    )
