from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session

from course.angel.fastapi.webapi.entities import Message
from course.angel.fastapi.webapi.repositories.message_repository import MessageRepository


class SqlAlchemyMessageRepository(MessageRepository):
    def __init__(self, db: Session):
        self._db = db

    def find_all(self) -> List[Message]:
        sql = select(Message).order_by(Message.id.asc())
        return list(self._db.scalars(sql).all())

    def find_by_id(self, message_id: int) -> Optional[Message]:
        return self._db.get(Message, message_id)

    def save(self, message: Message) -> Message:
        self._db.add(message)
        return message

    def delete(self, message: Message):
        self._db.delete(message)

