# schema/leave.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class LeaveRequest(BaseModel):
    employee_id: str
    start_date: date
    end_date: Optional[str] = None
    leave_type: str

class GetLeaveRequest(BaseModel):
    leave_id: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    leave_type: Optional[str] = None

class UpdateLeaveRequest(BaseModel):
    leave_id: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    leave_type: Optional[str] = None

class DeleteLeaveRequest(BaseModel):
    leave_id: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    leave_type: Optional[str] = None
