from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return{"item_id": item_id}