import json
from typing import Optional
from fastapi import FastAPI
from Backend.DataList import DataModelList
from Backend.PredictionModel import Model
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(data: DataModelList):
    records = data.records
    df = pd.DataFrame.from_records([r.to_dict() for r in records])
    model = Model()
    result = model.make_predictions(df)
    result = result.tolist()
    result = [round(p, 2) for p in result]
    res = {"Predictions": result}
    return res

@app.post("/predictmany")
def predict_many(data: DataModelList):
    records = data.records
    df = pd.DataFrame.from_records([r.to_dict() for r in records])
    model = Model()
    r2, rmse = model.retrain(df)
    return {"R2": r2, "RMSE": rmse}