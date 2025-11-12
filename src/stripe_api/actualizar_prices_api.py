import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PriceEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def actualizar_price_nickname(price_id):
    headers = build_headers()
    payload = {"nickname": "Nuevo nombre de precio"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    
    return {
        "field": "nickname",
        "field_value": payload.get("nickname"),
        "response": response
    }


def actualizar_price_active_false(price_id):
    headers = build_headers()
    payload = {"active": False}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_metadata_simple(price_id):
    headers = build_headers()
    payload = {"metadata[categoria]": "nueva_categoria"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_multiples_campos(price_id):
    headers = build_headers()
    payload = {
        "nickname": "Precio actualizado",
        "metadata[categoria]": "premium",
        "active": True,
    }
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_id_invalido():
    headers = build_headers()
    price_id = "price_invalido_123"
    payload = {"nickname": "No existente"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_sin_token(price_id):
    headers = build_headers_sin_authorization()
    payload = {"nickname": "Sin token"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_token_invalido(price_id):
    headers = build_headers(API_KEY_INVALIDA)
    payload = {"nickname": "Token inválido"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_header_vacio(price_id):
    headers = {}
    payload = {"nickname": "Header vacío"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_sin_permisos(price_id):
    headers = {"Authorization": "Bearer sin_permisos"}
    payload = {"nickname": "Sin permisos suficientes"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_currency(price_id):
    headers = build_headers()
    payload = {"currency": "eur"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_unit_amount(price_id):
    headers = build_headers()
    payload = {"unit_amount": 2000}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_body_vacio(price_id):
    headers = build_headers()
    payload = {}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_body_malformado(price_id):
    headers = build_headers()
    payload = "nickname=NuevoPrecio"  # formato incorrecto
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_nickname_caracteres_validos(price_id):
    headers = build_headers()
    payload = {"nickname": "Plan Básico 💎"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_nickname_max_longitud(price_id):
    headers = build_headers()
    payload = {"nickname": "N" * 100}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_nickname_vacio(price_id):
    headers = build_headers()
    payload = {"nickname": ""}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_active_no_booleano(price_id):
    headers = build_headers()
    payload = {"active": "yes"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_metadata_compleja(price_id):
    headers = build_headers()
    payload = {
        "metadata[nivel1]": "básico",
        "metadata[nivel2]": "premium",
        "metadata[detalles]": "mensual",
    }
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_metadata_nula(price_id):
    headers = build_headers()
    payload = {"metadata[clave_nula]": ""}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_metadata_vacia(price_id):
    headers = build_headers()
    payload = {"metadata": {}}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_nickname_unicode(price_id):
    headers = build_headers()
    payload = {"nickname": "Plan Básico 💎"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_price_respuesta_estructura(price_id):
    headers = build_headers()
    payload = {"nickname": "Estructura de respuesta"}
    endpoint = PriceEndpoints.UPDATE_PRICE.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def consultar_price_id(price_id):
    headers = build_headers()
    endpoint = PriceEndpoints.GET_PRICE_BY_ID.value.format(price_id=price_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
