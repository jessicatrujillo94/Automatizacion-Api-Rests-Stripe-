import os
import requests
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.logger import logger
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import CustomerEndpoints
import jsonschema
BASE_URL = os.getenv('BASE_URL')
API_KEY_INVALIDA = os.getenv('API_KEY_INVALIDA')
API_KEY = os.getenv('API_KEY')
def autenticacion_api_key_valida():
    headers = build_headers()
    endpoint = CustomerEndpoints.GET_CUSTOMERS.value
    url = f"{BASE_URL}{endpoint}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)
    return response


def autenticacion_api_key_invalida():
    """
    Prueba de autenticación fallida con API Key inválida.
    """
    headers = build_headers(API_KEY_INVALIDA)
    endpoint = CustomerEndpoints.GET_CUSTOMERS.value
    url = f"{BASE_URL}{endpoint}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)
    return response


def autenticacion_sin_token():
    """
    Prueba de autenticación sin enviar token (header Authorization ausente).
    """
    headers = build_headers_sin_authorization()
    endpoint = CustomerEndpoints.GET_CUSTOMERS.value
    url = f"{BASE_URL}{endpoint}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)

    return response
def autenticacion_header_incorrecto():
    """
    Prueba de autenticación con formato incorrecto del header (sin 'Bearer').
    """
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    endpoint = CustomerEndpoints.GET_CUSTOMERS.value
    url = f"{BASE_URL}{endpoint}"

    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)

    return response


def autenticacion_api_key_vacia():
    """
    Prueba de autenticación con API Key vacía en el header.
    """
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
    endpoint = CustomerEndpoints.GET_CUSTOMERS.value
    url = f"{BASE_URL}{endpoint}"

    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)

    return response


def autenticacion_endpoint_restringido():
    """
    Prueba de autenticación hacia un endpoint restringido.
    """
    headers = build_headers(os.getenv("STRIPE_API_KEY_VALIDA"))
    endpoint = "/v1/restricted_resource"
    url = f"{BASE_URL}{endpoint}"
    response = StripeAPI(BASE_URL).get(endpoint=endpoint, headers=headers)
    log_request_response(url=url, headers=headers, response=response)
    return response
