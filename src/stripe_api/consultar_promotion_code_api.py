import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PromotionCodeEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def consultar_promo_code_id(promotion_code):
    promotion_code_id = promotion_code.get("id")
    headers = build_headers()
    endpoint = PromotionCodeEndpoints.GET_PROMOTION_CODE_BY_ID.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_promo_id_inexistente():
    headers = build_headers()
    promotion_code_id = "promo_inexistente_123"
    endpoint = PromotionCodeEndpoints.GET_PROMOTION_CODE_BY_ID.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_promo_sin_token(promotion_code_id):
    headers = build_headers_sin_authorization()
    endpoint = PromotionCodeEndpoints.GET_PROMOTION_CODE_BY_ID.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_promo_token_invalido(promotion_code_id):
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = PromotionCodeEndpoints.GET_PROMOTION_CODE_BY_ID.value.format(promotion_code_id=promotion_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
