# /todo  -  get, post, put, delete
# GET : Read / POST : Create / PUT : Update / DELETE : Delete

from fastapi import APIRouter, Path
from pydantic import BaseModel

router = APIRouter()

# Item Model
class Item(BaseModel):
    item : str
    status : str

# Todo Model
class Todo(BaseModel):
    id : int
    item : Item

# Todo list
todo_list = []

@router.get("/todo")          
async def read_todo() -> dict:      # { key : value, ... }
    return {
        "message" : "GET : hello world"
    }

@router.post("/todo")
async def create_todo(todo : Todo) -> dict:      # { key : value, ... }
    todo_list.append(todo)
    return {
        "message" : "create!",
        "todo_list" : todo_list
    }

# id 값 / 수정 내용을 받아 todo_list에서 찾아 수정
@router.put("/todo/{id}")
async def update_todo(new_item:Item, id:int = Path(..., title="id")) -> dict:      # { key : value, ... }
    for todo in todo_list:
        if todo.id == id:
            todo.item = new_item
            return { "message" : "update 성공!" }
        
    return {
        "message" : "일치하는 id 없음"
    }


# ==============================================
# 완성하셔야합니다
# ==============================================
@router.delete("/todo")
async def delete_todo() -> dict:      # { key : value, ... }
    return {
        "message" : "DELETE : hello world"
    }

@router.get("/todo/all")
async def read_todo() -> dict:      
    return {
        "message::All" : todo_list
    }

# id 값이 맞는 todo를 todo_list에서 조회
@router.get("/todo/{id}")
async def search_todo(id : int) -> dict:      
    for todo in todo_list:
        if todo.id == id:
            return {
                "result" : todo
            }