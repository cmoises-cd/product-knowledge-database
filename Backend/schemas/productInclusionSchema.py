from pydantic import BaseModel
from typing import Optional

class ProductInclusionBase(BaseModel):
    inclusion_quantity: Optional[int] = None
    inclusion_title: Optional[str] = None

class ProductInclusion(ProductInclusionBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True
