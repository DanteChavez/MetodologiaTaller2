import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class MarcaRepository:
    def __init__(self, db):
        self.pagos = []
        self.contador_id = 1
        logger.info("Repositorio de Pagos (MarcaRepository) inicializado")

    def guardar_pago(self, pago_data: Dict) -> Dict:
        pago_data['id'] = str(self.contador_id)
        self.pagos.append(pago_data)
        self.contador_id += 1
        logger.info(f"Pago guardado: {pago_data}")
        return pago_data

    def obtener_todos_pagos(self) -> List[Dict]:
        logger.info("Obteniendo todos los pagos")
        return self.pagos.copy()  

    def buscar_pagos_por_cliente(self, nombre_cliente: str) -> List[Dict]:
        logger.info(f"Buscando pagos para cliente: {nombre_cliente}")
        return [
            p for p in self.pagos 
            if p['nombre_cliente'].lower() == nombre_cliente.lower()
        ]

    def eliminar_pago(self, pago_id: str) -> bool:
        logger.info(f"Intentando eliminar pago ID: {pago_id}")
        for i, pago in enumerate(self.pagos):
            if pago['id'] == pago_id:
                del self.pagos[i]
                logger.info(f"Pago {pago_id} eliminado")
                return True
        logger.warning(f"Pago {pago_id} no encontrado")
        return False