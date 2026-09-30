from fastapi import FastAPI

app = FastAPI(title="Simple API")

# In-memory storage for example data
items = [
    {"id": 1, "name": "Sample Item", "completed": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
