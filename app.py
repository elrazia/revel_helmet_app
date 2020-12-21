from fastapi import FastAPI, UploadFile, File, Header, HTTPException
import uvicorn
from helper_functions import parse_rekognition_labels
import boto3
from typing import Optional

app = FastAPI()

client = boto3.client("rekognition")


@app.get("/")
def hello_world():
    return "Welcome to the Helmet Predictor API"

@app.post("/predict")
async def predict(image: UploadFile = File(...), content_length: Optional[str] = Header(None)):

    if int(content_length) > 4000000:
        raise HTTPException(status_code=413,detail="Please upload a photo smaller than 4MB.")

    # read image
    image_object = await image.read()

    # run predictions
    r = client.detect_labels(Image={"Bytes": image_object})
    return parse_rekognition_labels(r)

if __name__ == "__main__" :
    uvicorn.run(app, port=8080, host="0.0.0.0")
