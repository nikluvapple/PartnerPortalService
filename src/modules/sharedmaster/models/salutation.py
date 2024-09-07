from sqlalchemy import Column, Integer, String, DateTime, func
from src.db.base import Base

class Salutation(Base):
    __tablename__ = "master_salutation"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    salutation_name = Column(String(100), nullable=False)