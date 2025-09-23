from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .productDepartmentSchema import Department

class AttachmentBase(BaseModel):
    file_url: Optional[str] = None
    note: Optional[str] = None

class AttachmentUpdate(AttachmentBase):
    pass 
class Attachment(AttachmentBase):
    id: int
    product_id: int
    created_at: Optional[datetime] = None
    department: Department
    
    class Config:
        orm_mode = True
