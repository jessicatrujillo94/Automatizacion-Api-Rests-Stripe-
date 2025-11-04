import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PromotionCodeEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def actualizar_promo_active_false(promotion_code_id):
    headers = build_headers()
    payload = {"active": False}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_restriction_usage(promotion_code_id, usage_limit=5):
    headers = build_headers()
    payload = {"restrictions[usage_limit]": usage_limit}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_id_invalido():
    headers = build_headers()
    promo_id = "promo_invalido_123"
    payload = {"active": True}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promo_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_sin_token(promotion_code_id):
    headers = build_headers_sin_authorization()
    payload = {"active": True}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_token_invalido(promotion_code_id):
    headers = build_headers(API_KEY_INVALIDA)
    payload = {"active": True}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_body_vacio(promotion_code_id):
    headers = build_headers()
    payload = {}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_active_invalido(promotion_code_id):
    headers = build_headers()
    payload = {"active": "yes"}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_restriction_invalido(promotion_code_id):
    headers = build_headers()
    payload = {"restrictions[usage_limit]": -5}
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_promo_multiple_campos(promotion_code_id):
    headers = build_headers()
    payload = {
        "active": True,
        "restrictions[usage_limit]": 10,
        "code": "PROMO_ACTUALIZADO"
    }
    endpoint = PromotionCodeEndpoints.UPDATE_PROMO_CODE.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def consultar_promo_code_id(promotion_code_id):
    headers = build_headers()
    endpoint = PromotionCodeEndpoints.GET_PROMO_CODE_BY_ID.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
