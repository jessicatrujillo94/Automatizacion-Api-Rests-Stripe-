import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import CouponEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"
API_KEY_EXPIRED = f"Bearer {os.getenv('API_KEY_EXPIRED')}"
API_KEY_WITHOUT_PERMISSION = f"Bearer {os.getenv('API_KEY_WITHOUT_PERMISSION')}"
ENDPOINT = CouponEndpoints.CREATE_COUPON.value


def crear_cupon_valido():
    headers = build_headers()
    payload = {"percent_off": 25, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_sin_duration():
    headers = build_headers()
    payload = {"percent_off": 20}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_percent_off_negativo():
    headers = build_headers()
    payload = {"percent_off": -10, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_token_invalido():
    headers = build_headers(API_KEY_INVALIDA)
    payload = {"percent_off": 15, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_sin_token():
    headers = build_headers_sin_authorization()
    payload = {"percent_off": 10, "duration": "repeating", "duration_in_months": 3}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_campos_validos():
    headers = build_headers()
    payload = {"id": "cupon_basic", "percent_off": 30, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_validar_estructura_respuesta():
    headers = build_headers()
    payload = {"percent_off": 10, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_con_amount_off():
    headers = build_headers()
    payload = {"amount_off": 500, "currency": "usd", "duration": "repeating", "duration_in_months": 2}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_duration_repeating():
    headers = build_headers()
    payload = {"percent_off": 10, "duration": "repeating", "duration_in_months": 6}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_duration_once():
    headers = build_headers()
    payload = {"percent_off": 100, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_percent_off_cero():
    headers = build_headers()
    payload = {"percent_off": 0, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_caracteres_especiales_id():
    headers = build_headers()
    payload = {"id": "cupón_#@!", "percent_off": 10, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_redeem_by_pasado():
    headers = build_headers()
    payload = {"percent_off": 20, "duration": "once", "redeem_by": 1609459200}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_campo_no_soportado():
    headers = build_headers()
    payload = {"percent_off": 15, "duration": "once", "campo_extra": "valor inesperado"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_multiples_consecutivos():
    headers = build_headers()
    cupones = [
        {"percent_off": 5, "duration": "once"},
        {"percent_off": 10, "duration": "repeating", "duration_in_months": 3},
        {"percent_off": 10, "currency": "usd", "duration": "forever"},
    ]
    responses = []
    for cupon in cupones:
        response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=cupon)
        log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=cupon, response=response)
        responses.append(response)
    return responses


def crear_cupon_con_metadata():
    headers = build_headers()
    payload = {
        "percent_off": 15,
        "duration": "once",
        "metadata[tipo]": "promocional",
        "metadata[campaña]": "verano2025",
    }
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_body_vacio():
    headers = build_headers()
    payload = {}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_con_currency_y_amount_off():
    headers = build_headers()
    payload = {"amount_off": 1000, "currency": "usd", "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_token_expirado():
    headers = build_headers(API_KEY_EXPIRED)
    payload = {"percent_off": 10, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response)
    return response


def crear_cupon_sin_permisos():
    headers = build_headers(API_KEY_WITHOUT_PERMISSION)
    payload = {"percent_off": 10, "duration": "once"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(url=ENDPOINT, headers=headers, response=response, payload=payload)
    return response


def eliminar_cupon(response):
    try:
        if not response or not hasattr(response, "json"):
            return None
        data = response.json()
        cupon_id = data.get("id")
        if not cupon_id:
            return None
        headers = build_headers()
        endpoint = CouponEndpoints.DELETE_COUPON.value.format(coupon_id=cupon_id)
        delete_response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
        print(delete_response.json())
        return delete_response
    except Exception:
        return None
