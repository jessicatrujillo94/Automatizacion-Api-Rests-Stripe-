import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxRateEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def crear_tax_rate(payload=None):
    headers = build_headers()
    payload = payload or {
        "display_name": "Tasa Básica",
        "percentage": 15.0,
        "inclusive": True
    }
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_con_todos_campos():
    headers = build_headers()
    payload = {
        "display_name": "Tasa Completa",
        "percentage": 12.5,
        "inclusive": False,
        "description": "Descripción completa",
        "jurisdiction": "US",
        "country": "US",
        "state": "CA"
    }
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_sin_display_name():
    headers = build_headers()
    payload = {"percentage": 10.0, "inclusive": True}
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_porcentaje_invalido():
    headers = build_headers()
    payload = {"display_name": "Tasa inválida", "percentage": 150.0, "inclusive": True}
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_inclusive_invalido():
    headers = build_headers()
    payload = {"display_name": "Inclusive inválido", "percentage": 10.0, "inclusive": "yes"}
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_sin_token():
    headers = build_headers_sin_authorization()
    payload = {"display_name": "Sin token", "percentage": 5.0, "inclusive": True}
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_token_invalido():
    headers = {"Authorization": API_KEY_INVALIDA}
    payload = {"display_name": "Token inválido", "percentage": 5.0, "inclusive": True}
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def crear_tax_rate_campo_extra():
    headers = build_headers()
    payload = {
        "display_name": "Tasa Extra",
        "percentage": 10.0,
        "inclusive": True,
        "campo_extra": "No soportado"
    }
    endpoint = TaxRateEndpoints.CREATE_TAX_RATE.value
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response
