from pydantic import BaseModel
from typing import Optional

class ProductAddonBase(BaseModel):
    addons_name:str
    addons_description: Optional[str] = None

class ProductAddonUpdate(ProductAddonBase):
    addons_name: Optional[str]

class ProductAddon(ProductAddonBase):
    id: int
    product_id: int
    
    class Config:
        orm_mode = True
