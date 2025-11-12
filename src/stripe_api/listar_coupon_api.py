# src/stripe_api/listar_cupones_api.py

import os
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import CouponEndpoints
import time

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = CouponEndpoints.GET_COUPONS.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def listar_cupones_valido():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_sin_token():
    headers = build_headers_sin_authorization()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_token_invalido():
    headers = build_headers(token=API_KEY_INVALIDA)
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_validar_estructura():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_objetos_validos():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_vacio():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=f"{ENDPOINT}?limit=0", headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}?limit=0", headers=headers, response=response)
    return response


def listar_cupones_has_more():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=f"{ENDPOINT}?limit=1", headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}?limit=1", headers=headers, response=response)
    return response


def listar_cupones_limit(limit=1):
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=f"{ENDPOINT}?limit={limit}", headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}?limit={limit}", headers=headers, response=response)
    return response


def listar_cupones_starting_after(response):
    headers = build_headers()
    coupon_id = response.json()["id"]
    response = StripeAPI(BASE_URL).get(endpoint=f"{ENDPOINT}?starting_after={coupon_id}", headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}?starting_after={coupon_id}", headers=headers, response=response)
    return response


def listar_cupones_tiempo_respuesta():
    headers = build_headers()
    start_time = time.time()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    elapsed = time.time() - start_time
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    response.elapsed_time = elapsed
    return response


def listar_cupones_tipo_object():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_campos_numericos():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_sin_permisos():
    headers = build_headers_sin_authorization()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_filtro_invalido():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=f"{ENDPOINT}?limit=-5", headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}?limit=-5", headers=headers, response=response)
    return response


def listar_cupones_expirados():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response


def listar_cupones_json_correcto():
    headers = build_headers()
    response = StripeAPI(BASE_URL).get(endpoint=ENDPOINT, headers=headers)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response)
    return response
