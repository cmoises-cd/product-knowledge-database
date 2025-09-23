from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

# Import schemas from other files
from .productPackagingSchema import ProductPackaging, ProductPackagingBase
from .productAddonSchema import ProductAddon, ProductAddonBase
from .productFeatureSchema import ProductFeature, ProductFeatureBase
from .productInclusionSchema import ProductInclusion, ProductInclusionBase
from .productAttachmentSchema import Attachment, AttachmentBase

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    status: str
    note: Optional[str] = None
    article: Optional[str] = None
    asin: Optional[str] = None
    ean: Optional[str] = None
    description: Optional[str] = None
    parentage_identifier: Optional[str] = None
    amazon_fba_sku: Optional[str] = None
    amazon_mfn_sku: Optional[str] = None
    shopify_sku: Optional[str] = None
    otto_sku: Optional[str] = None
    kaufland_sku: Optional[str] = None
    launch_date: Optional[date] = None
    sku: Optional[str] = None

class ProductCreate(ProductBase):
    pass
class ProductUpdate(ProductBase):
    name: Optional[str] = None
    status: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class Product(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True
