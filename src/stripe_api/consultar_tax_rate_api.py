import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxRateEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def consultar_tax_rate(tax_rate_id):
    headers = build_headers()
    endpoint = TaxRateEndpoints.GET_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_inexistente():
    headers = build_headers()
    tax_rate_id = "txr_inexistente_123"
    endpoint = TaxRateEndpoints.GET_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_sin_token(tax_rate_id):
    headers = build_headers_sin_authorization()
    endpoint = TaxRateEndpoints.GET_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_token_invalido(tax_rate_id):
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = TaxRateEndpoints.GET_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_rate_id_malformado():
    headers = build_headers()
    tax_rate_id = "txr!@#malformado"
    endpoint = TaxRateEndpoints.GET_TAX_RATE.value.format(tax_rate_id=tax_rate_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
