# api/leave.py
from fastapi import APIRouter, HTTPException
from app.schema.leave import LeaveRequest, UpdateLeaveRequest, GetLeaveRequest, DeleteLeaveRequest
from app.service.leave_service import apply_for_leave, update_leave_request,read_leave_request,delete_leave_request

router = APIRouter()

@router.post("/leave/apply")
async def apply_leave(leave_request: LeaveRequest):
    try:
        leave = apply_for_leave(leave_request.employee_id, leave_request.start_date, leave_request.end_date, leave_request.leave_type)
        return {"message": "Leave applied successfully", "leave": leave}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/leave/get")
async def get_leave(get_leave_request: GetLeaveRequest):
    try:
        read_leave = read_leave_request(get_leave_request.leave_id, get_leave_request.start_date, get_leave_request.end_date, get_leave_request.leave_type)
        return {"message": "Leave details retrieved successfully", "leave": read_leave}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/leave/update")
async def update_leave(update_request: UpdateLeaveRequest):
    try:
        updated_leave = update_leave_request(update_request.leave_id, update_request.start_date, update_request.end_date, update_request.leave_type)
        return {"message": "Leave updated successfully", "leave": updated_leave}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/leave/delete")
async def delete_leave(delete_request: DeleteLeaveRequest):
    try:
        deleted_leave = delete_leave_request(delete_request.leave_id, delete_request.start_date, delete_request.end_date, delete_request.leave_type)
        return {"message": "Leave deleted successfully", "leave": deleted_leave}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
