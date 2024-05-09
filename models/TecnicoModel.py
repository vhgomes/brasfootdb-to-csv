from pydantic import BaseModel


class Tecnico(BaseModel):
    nome: str
    pais: int
