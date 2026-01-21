from abc import ABC, abstractmethod
from typing import List, Optional

from course.angel.fastapi.webapi.models.message import Message


class MessageService(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
        ...
    @abstractmethod
    def find_by_id(self, message_id: int) -> Optional[Message]:
        ...
    @abstractmethod
    def create_message(self, message: Message) -> Message:
        ...
    @abstractmethod
    def update_message(self, message_id: int, message: Message) -> Optional[Message]:
        ...
    @abstractmethod
    def delete_message(self, message_id: int) -> bool:
        ...

