from fastapi import APIRouter
from app.models import modelVersion
from app.db.connect import db_conn
import json

router = APIRouter()

@router.get("/versions")
def get_version():
    conn = db_conn()
    conn.connect()
    result = conn.execute("select * from version;")
    conn.close()

    print(result)

    json_list = []

    for row in result:
        version = modelVersion.version(row[0], row[1], row[2], row[3], row[4])
        json_list.append(json.loads(version.print_json()))

    return json_list

    # row = result[0]
    # version = modelVersion.version(row[0], row[1], row[2], row[3], row[4])
    # return json.loads(version.print_json())