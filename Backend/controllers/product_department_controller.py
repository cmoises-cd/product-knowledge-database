from sqlalchemy.orm import Session
from models.productsModel import Department as ProductDepartmentModel
from schemas.productDepartmentSchema import DepartmentBase, Department
from typing import Optional, List
from database import get_db

def create_department(db: Session, department: DepartmentBase) -> ProductDepartmentModel:
    db_department= department.model_dump()
    db_department = ProductDepartmentModel(**db_department)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def delete_department(db: Session, department_id: int) -> Optional[ProductDepartmentModel]:
    db_department = db.query(ProductDepartmentModel).filter(ProductDepartmentModel.id == department_id).first()
    if db_department:
        db.delete(db_department)
        db.commit()
        return db_department
    return None

def update_department(db: Session, department_id: int, department: DepartmentBase) -> Optional[ProductDepartmentModel]:
    db_department = db.query(ProductDepartmentModel).filter(ProductDepartmentModel.id == department_id).first()
    if db_department:
        for key, value in department.model_dump(exclude_unset=True).items():
            setattr(db_department, key, value)
        db.commit()
        db.refresh(db_department)
        return db_department
    return None