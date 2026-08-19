from datetime import datetime

from pydantic import BaseModel


class PromptCreate(BaseModel):
    name: str
    description: str | None = None
    prompt_text: str
    category: str
    version: int = 1
    is_active: bool = True


class PromptUpdate(BaseModel):
    name: str
    description: str | None = None
    prompt_text: str
    category: str
    version: int
    is_active: bool


class PromptResponse(BaseModel):
    id: int
    name: str
    description: str | None
    prompt_text: str
    category: str
    version: int
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }