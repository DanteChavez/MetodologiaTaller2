from fastapi import Request
from fastapi import Depends
from adapters.repositories.marca_repository import MarcaRepository
from application.services.marca_service import MarcaService


#para que se conserve entre seciones se tiene que hacer magia negra
#es decir request.app.state y el request
def get_marca_service(request: Request) -> MarcaService:
    if not hasattr(request.app.state, "marca_service"):
        marca_repository = MarcaRepository(None)
        request.app.state.marca_service = MarcaService(marca_repository)
    return request.app.state.marca_service
