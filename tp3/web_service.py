from fastapi import FastAPI
import mlflow
import pandas as pd
import mlflow.sklearn
import random

mlflow.set_tracking_uri(uri="http://host.docker.internal:8080")

app = FastAPI()

current_model_uri = "runs:/eb1428946cf14a54b4d21a65df3a305d/iris_model"
current_model = mlflow.sklearn.load_model(current_model_uri)

next_model = current_model

p = 0.7

@app.post("/predict")
async def predict(data: list[float]):
    data = pd.DataFrame([data])

    model_choice = current_model if random.random() < p else next_model
    prediction = model_choice.predict(data)
    return {"prediction": int(prediction[0])}

@app.post("/update-model")
async def update_model(new_model_uri: str):
    global current_model_uri, current_model
    current_model_uri = new_model_uri
    current_model = mlflow.sklearn.load_model(current_model_uri)
    return {"status": "model updated"}

@app.post("/accept-next-model")
async def accept_next_model(new_model_uri: str):
    global current_model_uri, next_model
    current_model_uri = new_model_uri
    next_model = mlflow.sklearn.load_model(new_model_uri)
    return {"status": "next model accepted as current"}