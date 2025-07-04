from datetime import date
from typing import Optional

from pydantic import BaseModel


class MarcaInputObtener(BaseModel):
    id: Optional[int] = None
    origen: Optional[str] = None
    ramo: Optional[int] = None
    producto: Optional[int] = None
    modulo: Optional[int] = None
    ip_origen: Optional[str] = None
    fecha: Optional[date] = None
    rut_cliente: Optional[str] = None
    marca: Optional[bool] = None

class MarcaInputGuardar(BaseModel):
    origen: str
    ramo: int
    producto: int
    modulo: int
    ip_origen: str
    rut_cliente: str
    marca: bool