# repository/leave_repository.py
from typing import Optional

def apply_leave(employee_id: str, start_date: str, end_date: Optional[str], leave_type: str):
    # Simulate applying leave to a database
    leave_id = "generated_leave_id"  # Generate a leave ID here (e.g., UUID)
    leave_data = {
        "leave_id": leave_id,
        "employee_id": employee_id,
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type,
        "status": "pending"
    }
    # Here, add logic to insert leave_data into the database
    return leave_data

def read_leave(leave_id: str, start_date: Optional[str], end_date: Optional[str], leave_type: Optional[str]):
    # Simulate updating a leave request in the database
    read_leave = {
        "leave_id": leave_id,
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type,
        "status": "updated"
    }
    # Here, add logic to update the leave request in the database
    return read_leave

def update_leave(leave_id: str, start_date: Optional[str], end_date: Optional[str], leave_type: Optional[str]):
    # Simulate updating a leave request in the database
    updated_leave = {
        "leave_id": leave_id,
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type,
        "status": "updated"
    }
    # Here, add logic to update the leave request in the database
    return updated_leave

def delete_leave(leave_id: str, start_date: Optional[str], end_date: Optional[str], leave_type: Optional[str]):
    # Simulate updating a leave request in the database
    deleted_leave = {
        "leave_id": leave_id,
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type,
        "status": "updated"
    }
    # Here, add logic to update the leave request in the database
    return deleted_leave
