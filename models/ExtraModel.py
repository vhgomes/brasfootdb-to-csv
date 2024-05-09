from pydantic import BaseModel


class ExtraTime(BaseModel):
    id: int
    o: int
