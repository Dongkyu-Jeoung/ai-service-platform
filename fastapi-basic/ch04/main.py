from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.todo import router as todo_router
from database import engine, Base
# from ch03.routes.book import router as book_router

# 1. lifespan 비동기 컨텍스트 관리자 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- 서버가 켜질 때 실행될 코드 ---
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    
    yield  # 이 지점을 기준으로 앱이 실행되고 있는 동안 대기합니다.

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def welcome() -> dict:
    return {
        "message" : "welcome ch03!!"
    }

# todo 어플리케이션 개발 - CRUD
app.include_router(todo_router, tags=["TODO"])
# app.include_router(book_router, tags=["BOOK"], prefix="/book")