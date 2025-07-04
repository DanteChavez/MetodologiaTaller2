import sys
import os
import logging

from fastapi import FastAPI
from adapters.handlers import handler_marca, handler_health_check

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

session_creation_count = 0

prefix_string = "/ms-personas-marcas"

app = FastAPI()
app.include_router(handler_marca.router_marca, prefix=prefix_string)
app.include_router(handler_health_check.router_health)