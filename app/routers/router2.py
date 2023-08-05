from fastapi import APIRouter
from app.db.connect import db_conn

router = APIRouter()

@router.get("/test/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"test": item_id, "q": q}

@router.get("/{table}")
def read_table(table: str):
    conn = db_conn()
    conn.connect()
    result = conn.execute("select * from " + table + ";")
    conn.close()

    return result