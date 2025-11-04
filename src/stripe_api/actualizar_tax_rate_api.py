import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxRateEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def actualizar_tax_rate(tax_rate_id, payload):
    headers = build_headers()
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_inexistente():
    headers = build_headers()
    tax_rate_id = "txrate_inexistente_123"
    payload = {"display_name": "Nombre prueba"}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_sin_token(tax_rate_id):
    headers = build_headers_sin_authorization()
    payload = {"display_name": "Sin token"}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_token_invalido(tax_rate_id):
    headers = {"Authorization": API_KEY_INVALIDA}
    payload = {"display_name": "Token inválido"}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_display_name_vacio(tax_rate_id):
    headers = build_headers()
    payload = {"display_name": ""}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_campo_extra(tax_rate_id):
    headers = build_headers()
    payload = {"display_name": "Prueba", "campo_extra": "No soportado"}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response


def actualizar_tax_rate_active_false(tax_rate_id):
    headers = build_headers()
    payload = {"active": False}
    endpoint = TaxRateEndpoints.UPDATE_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).post(endpoint=endpoint, headers=headers, payload=payload)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, payload=payload, response=response)
    return response
