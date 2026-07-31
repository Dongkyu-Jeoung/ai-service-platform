from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

# Person 클래스 정의
class Person(BaseModel):
    name: str
    age: int

person_list = []

# Path Variable (경로 매개변수)
@router.get("/hello/{name}")          # http://127.0.0.1:8000/hello/hong
async def say_hello(name : str) -> dict:      # { key : value, ... }
    return {
        "message" : "GET : hello world " + name
    }

# Query String (쿼리 매개변수)
@router.get("/hello2")          
async def say_hello(name : str = Query(None)) -> dict:      # http://127.0.0.1:8000/hello2?name=홍길동
    return {
        "message" : "GET : hello world " + name
    }

@router.post("/hello")
async def say_hello(person: Person) -> dict:      
    person_list.append(person)
    return {
        "message" : person_list
    }