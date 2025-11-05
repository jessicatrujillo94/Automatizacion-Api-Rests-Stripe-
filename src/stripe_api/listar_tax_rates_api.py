import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxRateEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"
API_KEY_WITHOUT_PERMISSION = f"Bearer {os.getenv('API_KEY_WITHOUT_PERMISSION')}"

def listar_tax_rates():
    headers = build_headers()
    endpoint = TaxRateEndpoints.GET_TAX_RATES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_sin_token():
    headers = build_headers_sin_authorization()
    endpoint = TaxRateEndpoints.GET_TAX_RATES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_token_invalido():
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = TaxRateEndpoints.GET_TAX_RATES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_vacio(filters = {}):
    headers = build_headers()
    endpoint = f"{TaxRateEndpoints.GET_TAX_RATES.value}?limit=0"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers, params=filters)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response, payload=filters)
    return response


def listar_tax_rates_limit(limit):
    headers = build_headers()
    endpoint = f"{TaxRateEndpoints.GET_TAX_RATES.value}?limit={limit}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_starting_after(starting_after):
    headers = build_headers()
    endpoint = f"{TaxRateEndpoints.GET_TAX_RATES.value}?starting_after={starting_after}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_filtro_invalido(limit):
    headers = build_headers()
    endpoint = f"{TaxRateEndpoints.GET_TAX_RATES.value}?limit={limit}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_rates_sin_permisos():
    headers = {"Authorization": API_KEY_WITHOUT_PERMISSION}
    endpoint = TaxRateEndpoints.GET_TAX_RATES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
