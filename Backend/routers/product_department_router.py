from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from controllers import product_department_controller
from database import get_db
from schemas import productDepartmentSchema

# Initialize the router
router = APIRouter(prefix="/departments", tags=["Product Departments"])

# Create a new department
@router.post("/", response_model=productDepartmentSchema.Department)
def create_department(department: productDepartmentSchema.DepartmentBase, db: Session = Depends(get_db)):
    return product_department_controller.create_department(db, department)

# Delete a department by its ID
@router.delete("/{department_id}", response_model=productDepartmentSchema.Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return product_department_controller.delete_department(db, department_id)

# Update a department by its ID
@router.put("/{department_id}", response_model=productDepartmentSchema.Department)
def update_department(department_id: int, department: productDepartmentSchema.DepartmentBase, db: Session = Depends(get_db)):
    updated_department = product_department_controller.update_department(db, department_id, department)
    if not updated_department:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated_department