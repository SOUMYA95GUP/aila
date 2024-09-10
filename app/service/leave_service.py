# service/leave_service.py
from datetime import date
from app.repository.leave_repository import apply_leave, update_leave,read_leave,delete_leave

def apply_for_leave(employee_id: str, start_date: date, end_date: date, leave_type: str):
    return apply_leave(employee_id, start_date, end_date, leave_type)

def read_leave_request(leave_id: str, start_date: date, end_date: date, leave_type: str):
    return read_leave(leave_id, start_date, end_date, leave_type)

def update_leave_request(leave_id: str, start_date: date, end_date: date, leave_type: str):
    return update_leave(leave_id, start_date, end_date, leave_type)

def delete_leave_request(leave_id: str, start_date: date, end_date: date, leave_type: str):
    return delete_leave(leave_id, start_date, end_date, leave_type)
