# src/stripe_api/eliminar_product_api.py

from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import ProductEndpoints
import os

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = ProductEndpoints.DELETE_PRODUCT.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"

def eliminar_producto_existente(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_inexistente():
    headers = build_headers()
    endpoint = f"{ENDPOINT}/prod_inexistente123"
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_sin_token(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_token_invalido(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers(token=API_KEY_INVALIDA)
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_sin_permisos(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_id_vacio():
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id="")
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_id_malformado():
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id="@@##$$")
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_validar_estructura(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_producto_ya_eliminado(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id=producto_id)
    # Intento de eliminación doble
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response

def eliminar_multiples_productos(responses_creacion):
    headers = build_headers()
    respuestas = []
    for resp in responses_creacion:
        producto_id = resp.json().get("id")
        endpoint = ENDPOINT.format(product_id=producto_id)
        response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
        log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response, payload={})
        respuestas.append(response)
    return respuestas
