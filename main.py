from fastapi import FastAPI #import

app = FastAPI() #initializing fast api

items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items

