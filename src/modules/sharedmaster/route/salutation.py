from fastapi import APIRouter, Depends, HTTPException
from src.modules.sharedmaster.schema.salutation_dto import Salutation
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.modules.sharedmaster.crud.salutation import get_salutation as get_salutation_crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[Salutation])
def get_salutation(db: Session = Depends(get_db)):
    print("Enter route")
    return get_salutation_crud(db=db)
