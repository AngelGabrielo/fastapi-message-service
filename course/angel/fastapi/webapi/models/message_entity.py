from dataclasses import dataclass

@dataclass
class MessageEntity:
    id: int
    message: str
    secret: str
