from pydantic import BaseModel


class Estadio(BaseModel):
    nome: str
    capacidade: int
