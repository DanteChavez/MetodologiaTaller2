from abc import ABC, abstractmethod
from typing import Dict, List

class MarcaRepositoryBase(ABC):
    @abstractmethod
    def guardar_pago(self, pago_data: Dict) -> Dict:
        pass
    
    @abstractmethod
    def obtener_todos_pagos(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def buscar_pagos_por_cliente(self, nombre_cliente: str) -> List[Dict]:
        pass
    
    @abstractmethod
    def eliminar_pago(self, pago_id: str) -> bool:
        pass