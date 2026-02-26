from fastapi import APIRouter, HTTPException
from database import attendance_collection
from schemas import AttendanceCreate

router = APIRouter()

@router.post("/")
def mark_attendance(attendance: AttendanceCreate):
    existing = attendance_collection.find_one({
        "employee_id": attendance.employee_id,
        "date": str(attendance.date)
    })

    if existing:
        raise HTTPException(status_code=400, detail="Attendance already marked for this date")

    attendance_data = attendance.dict()
    attendance_data["date"] = str(attendance_data["date"])

    attendance_collection.insert_one(attendance_data)
    return {"message": "Attendance marked"}

@router.get("/{employee_id}")
def get_attendance(employee_id: str):
    records = list(attendance_collection.find(
        {"employee_id": employee_id},
        {"_id": 0}
    ))
    return records

@router.put("/{employee_id}/{date}")
def update_attendance(employee_id: str, date: str, attendance: AttendanceCreate):
    existing_record = attendance_collection.find_one({"employee_id": employee_id, "date": date})
    if not existing_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    attendance_collection.update_one(
        {"employee_id": employee_id, "date": date},
        {"$set": attendance.dict()}
    )
    return {"message": "Attendance updated successfully"}
