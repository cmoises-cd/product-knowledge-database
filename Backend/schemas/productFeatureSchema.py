from pydantic import BaseModel
from typing import Optional

class ProductFeatureBase(BaseModel):
    feature_name: Optional[str] = None
    feature_description: Optional[str] = None

class ProductFeature(ProductFeatureBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True
