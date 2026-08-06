from fastapi import FastAPI
from routes.study import router as study_router

app = FastAPI()

app.include_router(study_router, tags=["study"], prefix="/study")