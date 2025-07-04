import logging
from datetime import datetime
from typing import Dict, List
from fastapi import Request

from core.ports.repositories.marca_repository_base import MarcaRepositoryBase
from core.services.marca_service_base import MarcaServiceBase

logger = logging.getLogger(__name__)

class MarcaService(MarcaServiceBase):
    def __init__(self, marca_repository: MarcaRepositoryBase):
        # Inicializamos la clase padre correctamente
        super().__init__(marca_repository)
        logger.info("Servicio de Pagos (MarcaService) inicializado")

    def registrar_pago(self, nombre_cliente: str, monto: float) -> Dict:
        if monto <= 0:
            logger.error(f"Monto inválido: {monto}")
            raise ValueError("El monto debe ser mayor que cero")
            
        nuevo_pago = {
            "nombre_cliente": nombre_cliente,
            "monto": monto,
            "fecha": datetime.now().isoformat(),
            "estado": "COMPLETADO"
        }
        
        return self.marca_repository.guardar_pago(nuevo_pago)

    def listar_pagos(self) -> List[Dict]:
        return self.marca_repository.obtener_todos_pagos()

    def buscar_por_cliente(self, nombre_cliente: str) -> List[Dict]:
        return self.marca_repository.buscar_pagos_por_cliente(nombre_cliente)

    def eliminar_pago(self, pago_id: str) -> bool:
        return self.marca_repository.eliminar_pago(pago_id)