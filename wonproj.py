from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Define a data model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Home route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint to read an item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# Endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}

# Endpoint to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with id {item_id} deleted"}
