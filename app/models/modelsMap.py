from pydantic import BaseModel

class deployment_os_map(BaseModel):
    deployment_os_map_id: int
    os_id: int
    deployment_id: int

class deployment_module_map(BaseModel):
    deployment_module_map_id: int
    module_id: int
    deployment_id: int
