from typing import List

from pydantic import BaseModel

from models.TeamModel import Time
from models.ExtraPlayerModel import Extra


class Jogador(BaseModel):
    nome: str
    estrela: bool
    pais: int
    time: str = None
    idade: int
    posicao: int
    titular: bool
    top_mundial: bool
    lado: str
    caracteristicas: List[int]
    extra: Extra
