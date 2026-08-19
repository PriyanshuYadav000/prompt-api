from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers.prompts import router as prompts_router


app = FastAPI(title="AI Prompt Management API")

Base.metadata.create_all(bind=engine)

app.include_router(prompts_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}