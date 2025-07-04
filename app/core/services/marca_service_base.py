from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Dict, List

class EstadoPago(Enum):
    COMPLETADO = "COMPLETADO"
    PENDIENTE = "PENDIENTE"
    CANCELADO = "CANCELADO"

class MarcaServiceBase(ABC):
    def __init__(self, marca_repository):
        self.marca_repository = marca_repository

    @abstractmethod
    def registrar_pago(self, nombre_cliente: str, monto: float) -> Dict:
        pass
    
    @abstractmethod
    def listar_pagos(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def buscar_por_cliente(self, nombre_cliente: str) -> List[Dict]:
        pass
    
    @abstractmethod
    def eliminar_pago(self, pago_id: str) -> bool:
        pass