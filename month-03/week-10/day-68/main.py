from fastapi import APIRouter, FastAPI, status

app = FastAPI()


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_employee():
    # if 20 > 12:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="Corrupt data"
    #     )
    return {"message": "Employee created"}


app.include_router(router=router, prefix="/employees")
