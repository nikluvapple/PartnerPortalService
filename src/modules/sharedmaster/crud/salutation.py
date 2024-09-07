from sqlalchemy.orm import Session
from src.modules.sharedmaster.models.salutation import Salutation

def get_salutation(db: Session):
    return db.query(Salutation).all()