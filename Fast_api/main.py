from enum import Enum
from fastapi import FastAPI
from typing import Optional
# import uvicorn


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "这是一个说明"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "这是一个说明"}

    return {"model_name": model_name, "message": "这是一个说明"}


@app.get("users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owenr_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "这是一个惊人的项目,有很长的描述"}
        )
    return item


@app.get("/files{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# if __name__ == '__main__':
#     uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, debug=True)
