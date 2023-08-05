from pydantic import BaseModel
import datetime

class deployment(BaseModel):
    deployment_id: int
    customer_id: int
    version_id: int
    revision_id: int
    deployment_date: datetime.date
    deployment_purpose: str = None
