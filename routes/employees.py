from fastapi import APIRouter, HTTPException
from database import employee_collection
from schemas import EmployeeCreate

router = APIRouter()

@router.post("/")
def create_employee(employee: EmployeeCreate):
    if employee_collection.find_one({"employee_id": employee.employee_id}):
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    employee_collection.insert_one(employee.dict())
    return {"message": "Employee created successfully"}

@router.get("/")
def get_employees():
    employees = list(employee_collection.find({}, {"_id": 0}))
    return employees

@router.delete("/{employee_id}")
def delete_employee(employee_id: str):
    result = employee_collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}
