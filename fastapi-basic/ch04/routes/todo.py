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
@router.put("/todo/{id}", response_model = Todo)
async def update_todo(todo_data : TodoItem, id:int = Path(...), db: Session = Depends(get_db)) -> dict:
    todo = db.get(TodoModel, id)        

    # 검색되는 id가 없을 경우 404 err 처리
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )

    # 내용(item) 교체
    todo.item = todo_data.item
    db.commit()
    db.refresh(todo)

    return todo

# D
# delete all
@router.delete("/todo")
async def deleteAll(db : Session = Depends(get_db)) -> dict:
    result = db.execute(
        delete(TodoModel)
    )
    db.commit()

    if result.rowcount == 0:
        return {
            "message" : "todos 테이블의 데이터가 존재하지 않음"
        }
    return {
        "message" : "전체 데이터 삭제 완료!"
    }


# id 입력 받아 해당 todo 삭제
@router.delete("/todo/{id}")
async def delete_todo(id : int = Path(...), db : Session = Depends(get_db)) -> dict:
    todo = db.get(TodoModel, id)
    if todo is None :
        # 검색되는 id가 없을 경우 404 err 처리
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )

    db.delete(todo)
    db.commit()

    return {
        "message" : "todo 삭제 완료!"
    }