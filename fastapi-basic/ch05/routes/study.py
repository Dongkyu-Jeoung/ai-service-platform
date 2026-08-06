import joblib
import pandas as pd
import numpy as np
from fastapi import APIRouter
from schemas.study import Study

router = APIRouter()

# 1. 모델 호출
model = joblib.load("models/model.pkl")

@router.post("/predict")                        # 공부시간 입력 ==> 점수 예측
async def study_pred(features: Study) -> dict:
    # 2. Pydantic -> dict 타입 변경
    data = features.model_dump()                # { "study_hour" : 3 } 형태로 변경

    # 3. dict -> DataFrame 형태로 변경
    df = pd.DataFrame([data])

    # 4. predict 실행
    pred = model.predict(df).item()                        # return이 무조건 배열로 오니까 0번지(예측값)만 받음

    return {
        "predict_score" : round(pred, 2)
    }