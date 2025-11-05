import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxRateEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def consultar_tax_rate(tax_rate):
    tax_rate_id = tax_rate.get("id")
    headers = build_headers()
    endpoint = TaxRateEndpoints.GET_TAX_RATE_BY_ID.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_inexistente(tax_rate=None):
    tax_rate_id = tax_rate.get("id") if tax_rate else "txr_inexistente_123"
    headers = build_headers()
    endpoint = TaxRateEndpoints.GET_TAX_RATE_BY_ID.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_sin_token(tax_rate):
    tax_rate_id = tax_rate.get("id")
    headers = build_headers_sin_authorization()
    endpoint = TaxRateEndpoints.GET_TAX_RATE_BY_ID.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_token_invalido(tax_rate):
    tax_rate_id = tax_rate.get("id")
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = TaxRateEndpoints.GET_TAX_RATE_BY_ID.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_id_malformado(tax_rate=None):
    tax_rate_id = tax_rate.get("id") if tax_rate else "txr!@#malformado"
    headers = build_headers()
    endpoint = TaxRateEndpoints.GET_TAX_RATE_BY_ID.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
