from fastapi import FastAPI
from routes import employees, attendance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])

@app.get("/")
def root():
    return {"status": "HRMS Lite API running"}
