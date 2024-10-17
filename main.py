from typing import Union
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("regression.joblib")

class Item(BaseModel):
    size: int
    nb_rooms: int
    garden: int

@app.post("/predict")
def read_root(item: Item):
    price = model.predict([[item.size, item.nb_rooms, item.garden]])
    return {"price": price[0]}
