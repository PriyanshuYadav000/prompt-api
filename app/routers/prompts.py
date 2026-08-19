from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Prompt
from app.schemas import PromptCreate, PromptResponse

router = APIRouter(prefix="/prompts", tags=["Prompts"])

@router.post("/",response_model=PromptResponse,status_code=status.HTTP_201_CREATED)
def create_prompt(
    prompt: PromptCreate,
    db: Session = Depends(get_db)
):
    new_prompt = Prompt(
        name=prompt.name,
        description=prompt.description,
        prompt_text=prompt.prompt_text,
        category=prompt.category,
        version=prompt.version,
        is_active=prompt.is_active
    )

    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return new_prompt

@router.get("/", response_model=list[PromptResponse])
def get_prompts(db: Session = Depends(get_db)):
    prompts = db.query(Prompt).all()
    return prompts