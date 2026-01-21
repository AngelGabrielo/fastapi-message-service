from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from course.angel.fastapi.webapi.config.db import Base


class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    message: Mapped[str] = mapped_column(String(200), nullable=False)
    author_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=1)