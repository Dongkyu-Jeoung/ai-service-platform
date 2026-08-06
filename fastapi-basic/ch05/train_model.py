# LinearRegression

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame(
    {
        "study_hour" : [1, 2, 3, 4, 5, 6, 7, 8],
        "score" : [42, 50 , 58, 59, 67, 74, 86, 93]
    }
)

x = df[["study_hour"]]
y = df[["score"]]

model = LinearRegression()

model.fit(x, y)

joblib.dump(model, "models/model.pkl")

print("모델 저장 완료")