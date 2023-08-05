from fastapi import APIRouter
from app.models import model1

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.post("/items")
def read_item(item: model1.Item):
    return item