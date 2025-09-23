from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str

class Department(DepartmentBase):
    id: int

    class Config:
        orm_mode = True
