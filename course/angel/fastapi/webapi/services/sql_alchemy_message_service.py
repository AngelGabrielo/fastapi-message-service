from typing import Optional, List

from sqlalchemy.orm import Session

from course.angel.fastapi.webapi.entities.message import Message as MessageEntity
from course.angel.fastapi.webapi.models.message import Message as MessageDto
from course.angel.fastapi.webapi.repositories.message_repository import MessageRepository
from course.angel.fastapi.webapi.services.message_service import MessageService

def entity_to_dto(entity: MessageEntity) -> MessageDto:
    return MessageDto.model_validate({
        'id': entity.id,
        'message': entity.message,
        'author_email': entity.author_email,
        'priority': entity.priority
    })

class SqlAlchemyMessageService(MessageService):

    def __init__(self, repo: MessageRepository, db: Session):
        self._repo = repo
        self._db = db

    def find_all(self) -> List[MessageDto]:
        return [entity_to_dto(message_entity) for message_entity in self._repo.find_all()]

    def find_by_id(self, message_id: int) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)

        if not entity:
            return None
        return entity_to_dto(entity)

    def create_message(self, new_message: MessageDto) -> MessageDto:
        entity = MessageEntity(
            message = new_message.message,
            author_email=new_message.author_email,
            priority=new_message.priority
        )

        try:
            saved_obj = self._repo.save(entity)
            self._db.commit()
            self._db.refresh(saved_obj)
            return entity_to_dto(saved_obj)
        except Exception:
            self._db.rollback()
            raise

    def update_message(self, message_id: int, message: MessageDto) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return None
        entity.message = message.message
        entity.priority = message.priority
        entity.author_email = message.author_email

        try:
            self._db.commit()
            self._db.refresh(entity)
            return entity_to_dto(entity)
        except Exception:
            self._db.rollback()
            raise

    def delete_message(self, message_id: int) -> bool:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return False
        try:
            self._repo.delete(entity)
            self._db.commit()
            return True
        except Exception:
            self._db.rollback()
            raise