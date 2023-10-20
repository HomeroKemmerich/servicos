from datetime import datetime
from pydantic import BaseModel

class Machine(BaseModel):
    id: int
    name: str
    lat: float
    lon: float
    status: str
    last_updated: datetime
    created: datetime