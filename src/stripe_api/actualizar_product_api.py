# src/stripe_api/actualizar_product_api.py

from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import ProductEndpoints
import os

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = ProductEndpoints.UPDATE_PRODUCT.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"

def actualizar_nombre_producto(response_creacion):
    producto_id = response_creacion.json().get("id")
    print(producto_id)
    headers = build_headers()
    payload = {"name": "Producto Actualizado"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_varios_campos_producto(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {
        "name": "Producto Actualizado Varios",
        "description": "Actualizando varios campos",
        "active": True
    }
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_metadata_producto(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"metadata[tipo]": "premium"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_token_invalido(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers(token=API_KEY_INVALIDA)
    payload = {"name": "Intento con token inválido"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_sin_permisos(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    payload = {"name": "Intento sin permisos"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_id_inexistente():
    headers = build_headers()
    payload = {"name": "Producto inexistente"}
    endpoint = f"{ENDPOINT}/prod_inexistente123"
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_nombre_vacio(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"name": ""}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_nombre_caracteres_especiales(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"name": "@@##$$Producto!!??"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_inactivo(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"active": False}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_body_invalido(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = "esto_no_es_json_valido"
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_campos_no_soportados(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"campo_no_existente": "valor"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_sin_body(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_producto_validar_estructura(response_creacion):
    producto_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"description": "Probando estructura de respuesta"}
    endpoint = ENDPOINT.format(product_id=producto_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
