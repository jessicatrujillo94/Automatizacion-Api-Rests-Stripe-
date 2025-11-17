# src/stripe_api/obtener_cupon_api.py

import os
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import CouponEndpoints

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = CouponEndpoints.GET_COUPON_BY_ID.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def obtener_cupon_valido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_inexistente():
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id="cupon_inexistente123")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_sin_token(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_token_invalido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers(token=API_KEY_INVALIDA)
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_id_vacio():
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id="")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_formato_invalido():
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id="@@##$$")
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_validar_estructura(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_valido_true(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_valido_false(response_creacion):
    coupon_id = response_creacion.json().get("id_expired")  # assuming expired coupon fixture
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_validar_duration(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_validar_descuento(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def obtener_cupon_sin_permisos(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
