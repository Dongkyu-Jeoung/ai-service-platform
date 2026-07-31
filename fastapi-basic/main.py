from fastapi import FastAPI
from routers.hello import router as hello_router
from routers.todo import router as todo_router

app = FastAPI()         # FastAPI 서버 생성

@app.get("/")           # http://127.0.0.1:8000/       - Root
async def welcome() -> dict:      # { key : value, ... }
    return {
        "message" : "GET : welcome to FastAPI",
        "name" : "홍길동"
    }

@app.post("/")
async def welcome() -> dict:      # { key : value, ... }
    return {
        "message" : "POST : welcome to FastAPI",
        "name" : "홍길동"
    }


# tags 설정 시 swagger 화면에서 router 별로 묶어줌(그룹)
app.include_router(hello_router, tags = ["Hello"])
app.include_router(todo_router, tags = ["Todo"])