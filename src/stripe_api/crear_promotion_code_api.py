import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PromotionCodeEndpoints
import time

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"

def crear_codigo_promocional_valido():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "active": True,
        "code": "PROMO2025",
        "restrictions[usage_limit]": 10
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_sin_coupon():
    headers = build_headers()
    payload = {
        "active": True,
        "code": "PROMO_SIN_COUPON"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_duplicado():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_DUPLICADO"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_token_invalido():
    headers = build_headers(API_KEY_INVALIDA)
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_TOKEN_INVALIDO"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_sin_token():
    headers = build_headers_sin_authorization()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_SIN_TOKEN"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_limite_uso(usage_limit=0):
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_LIMITE_USO",
        "restrictions[usage_limit]": usage_limit
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_active_invalido():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_ACTIVE_INVALIDO",
        "active": "yes"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_permisos_restringidos():
    headers = {"Authorization": "Bearer sin_permisos"}
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_PERMISOS_RESTRINGIDOS"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_coupon_inexistente():
    headers = build_headers()
    payload = {
        "coupon": "coupon_inexistente",
        "code": "PROMO_COUPON_INEXISTENTE"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_estructura_respuesta():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_VALIDAR_ESTRUCTURA"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_validar_tipos():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_VALIDAR_TIPOS",
        "active": True,
        "restrictions[usage_limit]": 10
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_validar_json_header():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_JSON_HEADER"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_medir_tiempo_respuesta():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_TIEMPO_RESPUESTA"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    start = time.time()
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    duration = time.time() - start
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return {"response": response, "duration": duration}

def crear_codigo_promocional_code_case_sensitive():
    headers = build_headers()
    payload = {
        "coupon": "coupon_valido",
        "code": "PromoMayuscula"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMO_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response
