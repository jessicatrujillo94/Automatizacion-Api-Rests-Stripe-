# src/stripe_api/eliminar_coupon_api.py

import os
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.services.auth import build_headers, build_headers_sin_authorization
from src.resources.enums.endpoints import CouponEndpoints

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = CouponEndpoints.DELETE_COUPON.value
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def eliminar_cupon_existente(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def eliminar_cupon_inexistente():
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id="cupon_inexistente_123")
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def eliminar_cupon_sin_token(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers_sin_authorization()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def eliminar_cupon_token_invalido(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers(token=API_KEY_INVALIDA)
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def eliminar_cupon_ya_eliminado(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)

    # Primer intento (elimina correctamente)
    StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
    # Segundo intento (debería devolver 404)
    response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)

    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def verificar_cupon_eliminado_en_listado(response_creacion):
    coupon_id = response_creacion.json().get("id")
    headers = build_headers()
    endpoint = ENDPOINT.format(coupon_id=coupon_id)
    StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
   
    endpoint = CouponEndpoints.GET_COUPONS.value
    params = {"limit": 100}
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers, params=params)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
