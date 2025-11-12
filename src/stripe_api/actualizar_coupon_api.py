# src/stripe_api/actualizar_cupon_api.py

import os
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import CouponEndpoints

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = CouponEndpoints.UPDATE_COUPON.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def actualizar_cupon_valido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"name": "Cupón Actualizado", "metadata[categoria]": "promocion"}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_inexistente():
    headers = build_headers()
    payload = {"name": "Cupón inexistente"}
    endpoint = ENDPOINT.format(coupon_id="cupon_inexistente123")
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_sin_token(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    payload = {"name": "Intento sin token"}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_token_invalido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers(token=API_KEY_INVALIDA)
    payload = {"name": "Intento con token inválido"}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_campo_invalido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"durations": "invalido" }
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_nombre_caracteres_especiales(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"name": "Cupón_@@##$$🎉"}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_metadata_compleja(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {
        "metadata[categorias]": ["descuento", "temporada"], 
        "metadata[detalles]": {"porcentaje": 25, "limitado": True},
    }
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_desactivar(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"active": False}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_percent_off_alto(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"percent_off": 150}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_body_vacio(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_campos_no_soportados(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    payload = {"invalid_field": "valor"}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_validar_estructura(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def actualizar_cupon_sin_permisos(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    payload = {}
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
