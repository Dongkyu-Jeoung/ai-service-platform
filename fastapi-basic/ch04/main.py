from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.todo import router as todo_router
from routes.book import router as book_router
from database import engine, Base

# 1. lifespan 비동기 컨텍스트 관리자 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- 서버가 켜질 때 실행될 코드 ---
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    
    yield  # 이 지점을 기준으로 앱이 실행되고 있는 동안 대기합니다.

app = FastAPI(lifespan=lifespan)

# 리액트 프론트엔드 접속 허용 : CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://172.28.144.1:5173"
    ],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(todo_router, tags=["TODO"])
app.include_router(book_router, tags=["BOOK"], prefix="/book")