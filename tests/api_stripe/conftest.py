import pytest
import os
import time
import requests
""" 
from src.stripe_api.crear_tarea_api import crear_tarea, eliminar_tarea, crear_lista_para_crear_tarea, \
    eliminar_lista_de_la_tarea_creada


from src.stripe_api.eliminar_tarea import crear_lista_para_tarea, crear_tarea_en_lista, eliminar_lista_tarea
from src.logs.conflogger import log_request_response

from src.stripe_api.obtener_folder import crear_folder, eliminar_folder
import uuid
from src.stripe_api.tags import crear_tag, eliminar_tag

from src.stripe_api.editar_folder import crear_folder, eliminar_folder
from src.stripe_api.grupo import (eliminar_grupo,crear_grupo)
 """
from src.logs.logger import logger
from dotenv import load_dotenv
from src.logs.conflogger  import log_request_response
from src.stripe_api.crear_products_api import crear_producto_campos_minimos, eliminar_producto

""" 
from src.stripe_api.crear_lista import (
    crear_lista as crear_lista_default,
    crear_lista_no_token,
    crear_lista_token_invalido,
    eliminar_lista
) """
from src.resources.enums.endpoints import (ProductEndpoints)
from src.stripe_api.stripe_api import StripeAPI
""" from src.payloads.payload_grupo import payload_grupo
from src.payloads.crear_payload_tag import payload_tag """
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
TOKEN_CADUCADO = os.getenv("TOKEN_CADUCADO")
TOKEN_SIN_PERMISO = os.getenv("TOKEN_SIN_PERMISO")

@pytest.fixture
def producto_creado():
    """
    Fixture que crea un producto antes del test y lo elimina al finalizar.
    """
    response = crear_producto_campos_minimos()
    yield response
    eliminar_producto(response)
@pytest.fixture(scope="session")
def pausa():
    time.sleep(60)
    yield


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def api_client(headers):
    return StripeAPI(base_url=BASE_URL, headers=headers)

@pytest.fixture(scope="session")
def headers_with_api_key():
    return {
        "Authorization": "Bearer "+API_KEY,
        "Content-Type": "application/json"
    }
@pytest.fixture(scope="session")
def headers_without_api_key():
    return {
        "Content-Type": "application/json"
    }
""" @pytest.fixture(scope="session")
def crear_lista_sin_token(request):
    params = request.param
    payload = params["payload"]
    name = payload.get("name")
    content = payload.get("content", None)
    folder_id = params.get("folder_id",ID_FOLDER)
    response = crear_lista_no_token(folder_id=folder_id, name=name, content=content)
    yield response, payload, folder_id
    if(response.status_code in [201, 200] and response.json().get("id")):
        eliminar_lista(response.json().get("id"))

@pytest.fixture(scope="session")
def crear_lista_con_token_invalido(request):
    params = request.param
    payload = params["payload"]
    name = payload.get("name")
    content = payload.get("content", None)
    folder_id = params.get("folder_id",ID_FOLDER)
    response = crear_lista_token_invalido(folder_id=folder_id, name=name, content=content)
    yield response, payload, folder_id
    if(response.status_code in [201, 200] and response.json().get("id")):
        resp_delete = eliminar_lista(response.json().get("id"))
        logger.warning(f"No se pudo eliminar la lista {response.json().get('id')}. Status: {resp_delete.status_code}, Response: {resp_delete.text}")
 """