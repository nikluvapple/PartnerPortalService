from pydantic import BaseModel


class SalutationBase(BaseModel):
    salutation_name: str


class SalutationCreate(SalutationBase):
    pass


class Salutation(SalutationBase):
    id: int

    class Config:
        orm_mode = True
