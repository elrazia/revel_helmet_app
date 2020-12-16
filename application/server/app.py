from fastapi import FastAPI, UploadFile, File
import uvicorn

######### Modularize #########
from PIL import Image
from io import BytesIO
import boto3
######### End Modularize #########

app = FastAPI()

######### Modularize #########
def read_imagefile(file) -> Image.Image:
    return Image.open(BytesIO(file))

client = boto3.client('rekognition')
######### End Modularize #########

@app.get('/')
def hello_world():
    return "Welcome to the Helmet Predictor API"

@app.post('/api')
async def predict(image: UploadFile = File(...)):
    # read image
    pic = await image.read()
    # run predictions
    response = client.detect_labels(Image={"Bytes": pic})
    return {"code": 'response'}

if __name__ == "__main__" :
    uvicorn.run(app, port=8080, host='0.0.0.0')