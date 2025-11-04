import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxCodeEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def listar_tax_codes():
    headers = build_headers()
    endpoint = TaxCodeEndpoints.LIST_TAX_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_sin_token():
    headers = build_headers_sin_authorization()
    endpoint = TaxCodeEndpoints.LIST_TAX_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_token_invalido():
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = TaxCodeEndpoints.LIST_TAX_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_filtrar_jurisdiccion(jurisdiccion):
    headers = build_headers()
    endpoint = f"{TaxCodeEndpoints.LIST_TAX_CODES.value}?jurisdiction={jurisdiccion}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_limit(limit):
    headers = build_headers()
    endpoint = f"{TaxCodeEndpoints.LIST_TAX_CODES.value}?limit={limit}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_starting_after(starting_after):
    headers = build_headers()
    endpoint = f"{TaxCodeEndpoints.LIST_TAX_CODES.value}?starting_after={starting_after}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_vacio():
    headers = build_headers()
    endpoint = f"{TaxCodeEndpoints.LIST_TAX_CODES.value}?limit=0"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_filtro_invalido(limit):
    headers = build_headers()
    endpoint = f"{TaxCodeEndpoints.LIST_TAX_CODES.value}?limit={limit}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def listar_tax_codes_sin_permisos():
    headers = {"Authorization": "Bearer sin_permisos"}
    endpoint = TaxCodeEndpoints.LIST_TAX_CODES.value
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
