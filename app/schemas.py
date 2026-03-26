from typing import Optional
from pydantic import BaseModel, Field, field_validator

ALLOWED_STATUSES = {"pending", "in_progress", "done"}

class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    status: str = Field(default="pending")
    priority: int = Field(default=1, ge=1, le=3)

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        if value not in ALLOWED_STATUSES:
            raise ValueError("Status must be one of: pending, in_progress, done")
        return value
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    status: Optional[str] = None
    priority: Optional[str] = Field(default=None, ge=1, le=3)

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and value not in ALLOWED_STATUSES:
            raise ValueError("Status must be one of: pending, in_progress, done")
        return value
    

class TaskResponse(TaskBase):
    id: int

    model_config = {
        "from_attributes": True
    }