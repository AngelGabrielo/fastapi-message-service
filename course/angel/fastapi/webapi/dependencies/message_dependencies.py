from fastapi.params import Depends
from sqlalchemy.orm import Session

from course.angel.fastapi.webapi.config.db import SessionLocal
from course.angel.fastapi.webapi.repositories.message_repository import MessageRepository
from course.angel.fastapi.webapi.repositories.sql_alchemy_message_repository import SqlAlchemyMessageRepository
from course.angel.fastapi.webapi.services.message_service import MessageService

from course.angel.fastapi.webapi.services.sql_alchemy_message_service import SqlAlchemyMessageService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_message_repository(db: Session = Depends(get_db)) -> MessageRepository:
    return SqlAlchemyMessageRepository(db)

def get_message_service(repo: MessageRepository = Depends(get_message_repository),
                        db: Session = Depends(get_db)) -> MessageService:
    return SqlAlchemyMessageService(repo, db)