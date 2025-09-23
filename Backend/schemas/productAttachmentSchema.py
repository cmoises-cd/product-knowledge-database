from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .productDepartmentSchema import Department

class AttachmentBase(BaseModel):
    department_id: Optional[int] = None
    file_url: Optional[str] = None
    note: Optional[str] = None

class Attachment(AttachmentBase):
    id: int
    product_id: int
    created_at: Optional[datetime] = None
    department: Optional[Department] = None
    
    class Config:
        orm_mode = True
