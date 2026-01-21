from pydantic import BaseModel, Field, EmailStr


class Message(BaseModel):
    id: int | None = None
    message: str = Field(..., min_length=8, max_length=50, description="Content of the message between 8 and 50 characters")
    author_email: EmailStr | None = Field(None, description="Author email is optional but it gotta have a valid format")
    priority: int = Field(default=1, ge=1, le=5, description="Priority of the message between 1 and 5")
