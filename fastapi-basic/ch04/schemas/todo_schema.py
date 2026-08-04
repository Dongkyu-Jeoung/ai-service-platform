from typing import List
from pydantic import BaseModel, ConfigDict, Field

# TodoItems Model -> 전체 리스트 호출 시 사용
class TodoItems(BaseModel):
    todos : List[TodoItem] = Field(default_factory=list)


# TodoItem Model : 업데이트 요청 시 호출되는 모델 객체
class TodoItem(BaseModel):
    item : str

    model_config = ConfigDict(
        json_schema_extra={
            "example" : {
                "item" : "HTML"     # 수정할 내용 (예시)
            }
            
        }
    )

# Todo Model
class Todo(BaseModel):
    id : int
    item : str

    model_config = ConfigDict(  # swagger 테스트 -> 샘플 실행
        json_schema_extra ={
            "example" : {
                "id": 1,
                "item": "FastAPI 공부"
            }
            
        }
    )