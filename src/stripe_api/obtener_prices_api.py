import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PriceEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"
API_KEY_WITHOUT_PERMISSION = f"Bearer {os.getenv('API_KEY_WITHOUT_PERMISSION')}"
ENDPOINT = PriceEndpoints.GET_PRICE_BY_ID.value


def obtener_price_valido(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_inexistente():
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id="price_inexistente123")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_sin_token(price_id):
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_token_invalido(price_id):
    headers = build_headers(API_KEY_INVALIDA)
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_vacio():
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id="")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_formato_incorrecto():
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id="abc123")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_metodo_incorrecto(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload={})
    log_request_response(f"{BASE_URL}{endpoint}", headers, {}, response)
    return response


def obtener_price_header_vacio(price_id):
    headers = {"Authorization": ""}
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_sin_permisos(price_id):
    headers = build_headers(token=API_KEY_WITHOUT_PERMISSION)
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_campos(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_tipos_datos(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_estructura_body(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_producto_existente(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_content_type(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_con_espacios(price_id):
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_caracteres_especiales():
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id="price_!@#")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response


def obtener_price_validar_estructura_error():
    headers = build_headers()
    endpoint = ENDPOINT.format(price_id="price_invalido")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(f"{BASE_URL}{endpoint}", headers, None, response)
    return response
