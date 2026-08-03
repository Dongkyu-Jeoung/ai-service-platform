from fastapi import APIRouter, Path, HTTPException, status
from ch03.schemas.todo_schema import Todo, TodoItem, TodoItems

router = APIRouter()

# todo_list
todo_list = []

# C
@router.post("/todo")
async def add_todo(todo : Todo) -> dict:
    todo_list.append(todo)
    return {
        "message" : "Todo 객체 추가 완료",
        "list" : todo_list
    }   

# R
# 원하는 id의 Todo 객체 조회
@router.get("/todo/{id}")
async def read_todo(id : int) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {
                "message" : "조회완료",
                "result" : todo
            }

    # 검색되는 id가 없을 경우 404 err 처리
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
    #return { "message" : "일치하는id가 없습니다."}

# 전체 todo_list 조회
@router.get("/todo", response_model=TodoItems)
async def getAll() -> dict:
    return {
        "todos" : todo_list
    }

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