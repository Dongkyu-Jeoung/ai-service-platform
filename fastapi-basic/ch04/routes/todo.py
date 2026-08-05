from fastapi import APIRouter, Path, HTTPException, status, Depends
from schemas.todo_schema import Todo, TodoItem, TodoItems

from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from database import get_db
from models.todo_model import TodoModel

router = APIRouter()

# todo_list
todo_list = []

# C
@router.post("/todo", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def add_todo(todo : TodoItem, db:Session = Depends(get_db)) -> dict:        
    todo_data = TodoModel(item = todo.item)             # id 값은 DB에 auto_increment 설정 돼 있음
    db.add(todo_data)
    db.commit()
    db.refresh(todo_data)

    return todo_data

# R
# 원하는 id의 Todo 객체 조회
@router.get("/todo/{id}", response_model=Todo)
async def read_todo(id : int, db: Session = Depends(get_db)) -> dict:
    todo = db.get(TodoModel, id)        # pk 값을 이용해 조회 (결과 : 단일 row)
    
    if todo is None:
    # 검색되는 id가 없을 경우 404 err 처리
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )
    # return { "message" : "일치하는id가 없습니다."}

    return todo
# 전체 todo_list 조회
@router.get("/todo", response_model=TodoItems)
async def getAll(db:Session = Depends(get_db)) -> dict:
    todos = db.execute(select(TodoModel).order_by(TodoModel.id)).scalars().all()
    return {"todos" : todos}

# U
@router.put("/todo/{id}")
async def update_todo(todo_data : TodoItem, id:int = Path(...)) -> dict:
    for todo in todo_list:
        if todo.id == id:
            todo.item = todo_data.item
            return {
                "message" : "업데이트 성공"
            }
    # 검색되는 id가 없을 경우 404 err 처리
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
    # return { "message" : "id를 확인해주세요" }

# D
# delete all
@router.delete("/todo")
async def deleteAll() -> dict:
    if len(todo_list) > 0 :
        todo_list.clear()
        return {
            "message" : "목록 초기화 완료"
        }
    return { "message" : "삭제할 항목이 없습니다." }


# id 입력 받아 해당 todo 삭제
@router.delete("/todo/{id}")
async def delete_todo(id : int = Path(...)) -> dict:
    for idx in range(len(todo_list)):
        todo = todo_list[idx]
        if todo.id == id:
            todo_list.pop(idx)
            return {
                "message" : "삭제가 완료됐습니다."   
            }

    # 검색되는 id가 없을 경우 404 err 처리
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )