from fastapi import APIRouter, Depends

router = APIRouter()


def verificar_rol(rol: str):
    return {"rol": rol}


@router.get("/")
def get_employees():
    return {"employees": []}


@router.get("/admin")
def get_admin(user: dict = Depends(lambda: verificar_rol("admin"))):
    return user


@router.get("/{employee_id}")
def get_employee(employee_id: int):
    return {"id": employee_id}
