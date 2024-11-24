from pydantic import BaseModel
from typing import List

class Producto(BaseModel):
    nombre_producto: str
    demanda: str
    accion_sugerida: str
    motivo: str
    recomendaciones: List[str]

class Rubro(BaseModel):
    nombre_rubro: str
    productos: List[Producto]

class ResponseModel(BaseModel):
    rubros: List[Rubro]
    recomendaciones_generales: List[str]