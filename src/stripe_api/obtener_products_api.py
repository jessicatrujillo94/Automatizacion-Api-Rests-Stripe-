# src/stripe_api/obtener_products_api.py

from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import ProductEndpoints
import os

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = ProductEndpoints.GET_PRODUCTS.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def obtener_lista_completa_productos():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def obtener_productos_con_limit_5():
    headers = build_headers()
    endpoint = f"{ENDPOINT}?limit=5"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_productos_activos():
    headers = build_headers()
    endpoint = f"{ENDPOINT}?active=true"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_productos_inactivos():
    headers = build_headers()
    endpoint = f"{ENDPOINT}?active=false"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_productos_sin_token():
    headers = build_headers_sin_authorization()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def obtener_productos_token_invalido():
    headers = build_headers(token=API_KEY_INVALIDA)
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def obtener_productos_sin_permisos():
    headers = build_headers_sin_authorization()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def obtener_productos_query_invalido():
    headers = build_headers()
    endpoint = f"{ENDPOINT}?limit=abc"  # parámetro inválido
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_productos_limit_mayor_100():
    headers = build_headers()
    endpoint = f"{ENDPOINT}?limit=200"  # límite máximo excedido
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_productos_validar_estructura():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response

def obtener_producto(product_id):
    headers = build_headers()
    endpoint = ProductEndpoints.GET_PRODUCT_BY_ID.format(product_id=product_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
