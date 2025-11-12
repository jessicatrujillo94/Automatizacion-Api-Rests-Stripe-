import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PriceEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"

ENDPOINT = PriceEndpoints.CREATE_PRICE.value


def crear_price_campos_minimos(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers,  payload, response)
    return response


def crear_price_todos_campos(product_id):
    headers = build_headers()
    payload = {
        "unit_amount": 25,
        "currency": "usd",
        "product": product_id,
        "nickname": "Precio completo",
        "metadata[categoria]": "premium",
        "recurring[interval]": "month",
        "active": True
    }
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_sin_currency(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1000, "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_sin_unit_amount(product_id):
    headers = build_headers()
    payload = {"currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_sin_product():
    headers = build_headers()
    payload = {"unit_amount": 1000, "currency": "usd"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_unit_amount_invalido(product_id):
    headers = build_headers()
    payload = {"unit_amount": "mil", "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_currency_invalido(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1000, "currency": "XYZ", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_token_invalido(product_id):
    headers = build_headers(API_KEY_INVALIDA)
    payload = {"unit_amount": 1000, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_sin_token(product_id):
    headers = build_headers_sin_authorization()
    payload = {"unit_amount": 1000, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_producto_inexistente():
    headers = build_headers()
    payload = {"unit_amount": 1000, "currency": "usd", "product": "prod_inexistente123"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_campos_adicionales(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1000, "currency": "usd", "product": product_id, "campo_extra": "no_soportado"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_inactivo(product_id):
    headers = build_headers()
    payload = {"unit_amount": 5000, "currency": "usd", "product": product_id, "active": False}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_nickname_vacio(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1000, "currency": "usd", "product": product_id, "nickname": ""}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_metadata_compleja(product_id):
    headers = build_headers()
    payload = {
        "unit_amount": 2000,
        "currency": "usd",
        "product": product_id,
        "metadata": {"niveles": ["básico", "premium"], "detalles": {"plazo": "mensual", "iva": "incluido"}}
    }
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_multiples_prices(product_id):
    headers = build_headers()
    precios = [
        {"unit_amount": 100, "currency": "usd", "product": product_id},
        {"unit_amount": 200, "currency": "usd", "product": product_id},
        {"unit_amount": 300, "currency": "usd", "product": product_id},
    ]
    responses = []
    for price in precios:
        response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=price)
        log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload=price, response=response)
        responses.append(response)
    return responses


def crear_price_respuesta_estructura(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1500, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_nickname_largo(product_id):
    headers = build_headers()
    payload = {"unit_amount": 1200, "currency": "usd", "product": product_id, "nickname": "N" * 150}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_recurrente_mensual(product_id):
    headers = build_headers()
    payload = {"unit_amount": 2000, "currency": "usd", "product": product_id, "recurring[interval]": "month"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_recurrente_intervalo_invalido(product_id):
    headers = build_headers()
    payload = {"unit_amount": 2000, "currency": "usd", "product": product_id, "recurring[interval]": "biweekly"}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_unit_amount_cero(product_id):
    headers = build_headers()
    payload = {"unit_amount": 0, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_unit_amount_negativo(product_id):
    headers = build_headers()
    payload = {"unit_amount": -500, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_unit_amount_grande(product_id):
    headers = build_headers()
    payload = {"unit_amount": 999999999999, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_producto_inactivo(product_id):
    headers = build_headers()
    payload = {"unit_amount": 50, "currency": "usd", "product": product_id}
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def crear_price_body_vacio():
    headers = build_headers()
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload={})
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload={}, response=response)
    return response


def crear_price_body_invalido():
    headers = build_headers()
    payload = "unit_amount=1000&currency=usd"  # formato inválido
    response = StripeAPI(BASE_URL).post(endpoint=ENDPOINT, headers=headers, payload=payload)
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, payload, response)
    return response


def eliminar_price(response):
    try:
        if not response or not hasattr(response, "json"):
            return None
        data = response.json()
        price_id = data.get("id")

        if not price_id:
            return None

        headers = build_headers()
        payload = {"active": False}
        endpoint = PriceEndpoints.DELETE_PRICE.value.format(price_id=price_id)  # renombrar a UPDATE_PRICE si querés
        deactivate_response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
        log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=deactivate_response,payload=payload)
        return deactivate_response
    except Exception:
        return None

