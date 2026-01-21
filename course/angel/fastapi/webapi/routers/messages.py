from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends, Query

from course.angel.fastapi.webapi.dependencies.message_dependencies import get_message_service
from course.angel.fastapi.webapi.models.message import Message
from course.angel.fastapi.webapi.services.message_service import MessageService

router = APIRouter()

@router.get("/", response_model=List[Message])
async def get_messages(
        service: MessageService = Depends(get_message_service)
):
    # print(f"Service's ID: {id(service)}")
    return service.find_all()

@router.get("/{message_id}", response_model=Optional[Message])
async def get_message(
        message_id: int,
        service: MessageService = Depends(get_message_service)
):
    message = service.find_by_id(message_id)
    return get_message_only(message)

@router.get("/details/", response_model=Optional[Message])
async def get_message_url_param(
        message_id: int = Query(..., ge=2),
        service: MessageService = Depends(get_message_service)
):
    message = service.find_by_id(message_id)
    return get_message_only(message)

@router.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(
        message: Message,
        service: MessageService = Depends(get_message_service)
):
    return service.create_message(message)

@router.put("/{message_id}", response_model=Optional[Message])
async def update_message(
        message_id: int,
        message: Message,
        service: MessageService = Depends(get_message_service)
):
    message_updated = service.update_message(message_id, message)
    return get_message_only(message_updated)

@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(
        message_id: int,
        service: MessageService = Depends(get_message_service)
):
    deleted = service.delete_message(message_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

def get_message_only(message: Message):
    if message is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    return message
