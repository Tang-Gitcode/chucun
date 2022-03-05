from fastapi import FastAPI
from enum import Enum

class MoudelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.post("")
async def


