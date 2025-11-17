import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PromotionCodeEndpoints
import time

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"
API_KEY_WITHOUT_PERMISSION = f"Bearer {os.getenv('API_KEY_WITHOUT_PERMISSION')}"

def crear_codigo_promocional_valido(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "active": True,
        "code": "PROMO2025",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_inactivo(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "active": False,
        "code": "PROMO2025",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_sin_coupon():
    headers = build_headers()
    payload = {
        "active": True,
        "code": "PROMO_SIN_COUPON",
        "promotion[type]": "coupon",
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_duplicado(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO2025",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_token_invalido(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers(API_KEY_INVALIDA)
    payload = {
        "code": "PROMO_TOKEN_INVALIDO",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_sin_token(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers_sin_authorization()
    payload = {
        "code": "PROMO_SIN_TOKEN",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_limite_uso(usage_limit=0,coupon=None):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_LIMITE_USO",
        "restrictions[usage_limit]": usage_limit,
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_active_invalido(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_ACTIVE_INVALIDO",
        "active": "yes",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id

    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_permisos_restringidos(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers(API_KEY_WITHOUT_PERMISSION)
    payload = {
        "coupon": "coupon_valido",
        "code": "PROMO_PERMISOS_RESTRINGIDOS",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_coupon_inexistente():
    headers = build_headers()
    payload = {
        "code": "PROMO_COUPON_INEXISTENTE",
        "promotion[type]": "coupon",
        "promotion[coupon]": "coupon_inexistente"
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response
def crear_codigo_promocional_coupon_existente(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_COUPON_EXISTENTE",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_estructura_respuesta(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_VALIDAR_ESTRUCTURA",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_validar_tipos(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_VALIDAR_TIPOS",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id,
        "active": True,
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_validar_json_header(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_JSON_HEADER",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id,
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response

def crear_codigo_promocional_medir_tiempo_respuesta(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PROMO_TIEMPO_RESPUESTA",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id,
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    start = time.time()
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    duration = time.time() - start
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return {"response": response, "duration": duration}

def crear_codigo_promocional_code_case_sensitive(coupon):
    coupon_id = coupon.json().get("id")
    headers = build_headers()
    payload = {
        "code": "PromoMayuscula",
        "promotion[type]": "coupon",
        "promotion[coupon]": coupon_id,
    }
    endpoint = PromotionCodeEndpoints.CREATE_PROMOTION_CODE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response
