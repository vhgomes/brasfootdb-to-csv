from pydantic import BaseModel


class Extra(BaseModel):
    aid: int
    hash: int
    sid: int
    tid: int
