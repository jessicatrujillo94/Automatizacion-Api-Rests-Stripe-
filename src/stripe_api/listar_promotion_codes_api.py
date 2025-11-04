import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PromotionCodeEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def listar_promotion_codes():
    headers = build_headers()
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_sin_token():
    headers = build_headers_sin_authorization()
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_token_invalido():
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_active_true():
    headers = build_headers()
    params = {"active": True}
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers, params=params)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_active_false():
    headers = build_headers()
    params = {"active": False}
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers, params=params)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_permisos_restringidos():
    headers = {"Authorization": "Bearer sin_permisos"}
    endpoint = PromotionCodeEndpoints.LIST_PROMO_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
