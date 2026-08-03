from fastapi import FastAPI
from ch03.routers.todo import router as todo_router
from ch03.routers.book import router as book_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message" : "welcome ch03!!"
    }

# todo 어플리케이션 개발 - CRUD
app.include_router(todo_router, tags=["TODO"])
app.include_router(book_router, tags=["BOOK"], prefix="/book")