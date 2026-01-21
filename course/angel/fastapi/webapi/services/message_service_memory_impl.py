from typing import List, Optional

from course.angel.fastapi.webapi.models.message import Message
from course.angel.fastapi.webapi.services.message_service import MessageService

class MessageServiceMemoryImpl(MessageService):

    def __init__(self):
        self._messages: List[Message] = [
            Message(id=1, message="Hello World",
                    author_email="andres@gmail.com", #type: ignore
                    priority=2),
            Message(id=2, message="Section FastApi",
                    author_email=None,
                    priority=3),
            Message(id=3, message="Test message",
                    author_email="pepe@gmail.com", #type: ignore
                    priority=4),
            Message(id=4, message="FastApi with service",
                    author_email="demo@gmail.com", #type: ignore
                    priority=1),
            Message(id=5, message="Inversion of Control with Depends",
                    author_email="angel@gmail.com", #type: ignore
                    priority=5)
        ]
        self._next_message_id = 6

    def find_all(self) -> List[Message]:
        return self._messages

    def find_by_id(self, message_id: int) -> Optional[Message]:
        return next((msg for msg in self._messages if msg.id == message_id), None)

    def create_message(self, message: Message) -> Message:
        message.id = self._next_message_id
        self._messages.append(message)
        self._next_message_id += 1
        return message

    def update_message(self, message_id: int, message: Message) -> Optional[Message]:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                updated = Message(id=msg.id, message=message.message, author_email=message.author_email, priority=message.priority)
                self._messages[index] = updated
                return updated
        return None

    def delete_message(self, message_id: int) -> bool:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                self._messages.remove(msg)
                return True
        return False

