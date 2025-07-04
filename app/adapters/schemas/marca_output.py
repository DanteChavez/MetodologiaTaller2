from pydantic import BaseModel
from datetime import datetime

class MarcaOutput(BaseModel):
    id: int
    origen: str
    ramo: int
    producto: int
    modulo: int
    ip_origen: str
    fecha: datetime
    rut_cliente: str
    marca: bool



