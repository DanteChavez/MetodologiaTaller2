import logging
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from fastapi import Request

from adapters.dependency.dependencies import get_marca_service
from application.services.marca_service import MarcaService

logger = logging.getLogger(__name__)
router_marca = APIRouter()


@router_marca.post("/pagos", status_code=status.HTTP_201_CREATED)
async def registrar_pago(
    nombre_cliente: str,
    monto: float,
    request: Request,
    marca_service: MarcaService = Depends(get_marca_service)
):
    try:
        return marca_service.registrar_pago(nombre_cliente, monto)
    except ValueError as e:
        logger.error(f"Error al registrar pago: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router_marca.get("/pagos", response_model=List[dict])
async def listar_pagos(
    request: Request,
    marca_service: MarcaService = Depends(get_marca_service)
):
    return marca_service.listar_pagos()

@router_marca.get("/pagos/cliente/{nombre_cliente}", response_model=List[dict])
async def buscar_pagos_cliente(
    nombre_cliente: str,
    request: Request,
    marca_service: MarcaService = Depends(get_marca_service)
):
    return marca_service.buscar_por_cliente(nombre_cliente)

@router_marca.delete("/pagos/{pago_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_pago(
    pago_id: str,
    request: Request,
    marca_service: MarcaService = Depends(get_marca_service)
):
    if not marca_service.eliminar_pago(pago_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo eliminar el pago (no existe o estado incorrecto)"
        )