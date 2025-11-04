import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import TaxCodeEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"


def consultar_tax_code(tax_code_id):
    headers = build_headers()
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_inexistente():
    headers = build_headers()
    tax_code_id = "tx_inexistente_123"
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_sin_token(tax_code_id):
    headers = build_headers_sin_authorization()
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_token_invalido(tax_code_id):
    headers = {"Authorization": API_KEY_INVALIDA}
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_id_vacio():
    headers = build_headers()
    tax_code_id = ""
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_malformado():
    headers = build_headers()
    tax_code_id = "!@#malformado"
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_id_corto():
    headers = build_headers()
    tax_code_id = "tx_1"
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_id_largo():
    headers = build_headers()
    tax_code_id = "tx_" + "x" * 256
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response


def consultar_tax_code_case_sensitive(tax_code_id):
    headers = build_headers()
    tax_code_id_case = tax_code_id.upper()
    endpoint = TaxCodeEndpoints.GET_TAX_CODE_BY_ID.value.format(tax_code_id=tax_code_id_case)
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=f"{BASE_URL}{endpoint}", headers=headers, response=response)
    return response
