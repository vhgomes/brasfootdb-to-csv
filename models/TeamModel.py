from typing import List

from pydantic import BaseModel

from models.EstadioModel import Estadio
from models.ExtraModel import ExtraTime
from models.TecnicoModel import Tecnico


class Time(BaseModel):
    pais: int
    estado: int
    forca_inicial: int
    cor1: str
    cor2: str
    id: str
    nome: str
    estadio: Estadio
    tecnico: Tecnico
    poder_investimento: int
    extra: ExtraTime
