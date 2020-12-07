from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get('/')
def hello_world():
    return "Welcome to the Helmet Predictor API"

@app.post('/api')
async def image(image: UploadFile = File(...)):
    return {"filename": image.filename}

if __name__ == "__main__" :
    uvicorn.run(app, port=8080, host='0.0.0.0')