from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductPackagingBase(BaseModel):
    packaging: Optional[str] = None
    pallet_size: Optional[str] = None
    packaging_dimensions: Optional[str] = None
    packaging_weight: Optional[float] = None
    target_fba_fee: Optional[float] = None
    target_fbm_fee: Optional[float] = None
    hermes_fbm_fee: Optional[float] = None
    gls_fbm_fee: Optional[float] = None

class ProductPackaging(ProductPackagingBase):
    id: int
    product_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
