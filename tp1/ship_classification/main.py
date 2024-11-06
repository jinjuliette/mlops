from typing import Union
import joblib
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
import numpy as np

app = FastAPI()

model = joblib.load("navires_classification.joblib")

class Item(BaseModel):
    image: UploadFile

classes = {
    0: "coastguard_scaled",
    1: "containership_scaled",
    2: "corvette_scaled",
    3: "cruiser_scaled",
    4: "cv_scaled",
    5: "destroyer_scaled",
    6: "methanier_scaled",
    7: "smallfish_scaled",
    8: "submarine_scaled",
    9: "tug_scaled",
}

def read_imagefile(file: UploadFile) -> Image.Image:
    """Read and open image from UploadFile."""
    image = Image.open(BytesIO(file.file.read()))
    return image

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    img = read_imagefile(image)
    
    img = img.resize((224, 224))
    img_array = np.array(img)

    img_array = img_array / 255.0
    img_array = img_array[np.newaxis, ...]

    prediction = model.predict(img_array)
    predicted_class = prediction.argmax(axis=1)[0]

    return {"ship": classes[predicted_class]}

# from PIL import Image
# from numpy import asarray
 
# img = Image.open('/kaggle/working/test_images/cv_scaled/1089.jpg')
# numpydata = asarray(img)
# list = np.array([numpydata])
# test = list.astype('float32') / 255
# res_test = model.predict(test).argmax(axis=1)
# df = pd.DataFrame({"Category":res_test})