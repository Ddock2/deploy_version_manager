from pydantic import BaseModel

class customer(BaseModel):
    customer_id: int
    customer_name: str
