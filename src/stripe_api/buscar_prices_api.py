import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import PriceEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"
ENDPOINT = PriceEndpoints.SEARCH_PRICE.value


def _prepare_params(query):
    if query:
        return {"query": query}
    else:
        return {}


def buscar_precios_activos():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_inactivos():
    headers = build_headers()
    params = _prepare_params(f"active:'false'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_por_moneda(currency="usd", ):
    headers = build_headers()
    params = _prepare_params(f"currency:'{currency}'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_por_producto(product_id):
    headers = build_headers()
    params = _prepare_params({f"product:'{product_id}'"})
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_combinando_filtros(
    product_id, currency="usd", active=True, 
):
    headers = build_headers()
    params = _prepare_params(
        f"product:'{product_id}' AND currency:'{currency}' AND active:'{active}'"
    )
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_query_invalida():
    headers = build_headers()
    params = _prepare_params(f"invalid_param:'xyz'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_query_vacia():
    headers = build_headers()
    params = _prepare_params({})
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_query_mal_estructurada():
    headers = build_headers()
    params = _prepare_params({"active":"true"})
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_token_invalido():
    headers = build_headers(API_KEY_INVALIDA)
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_sin_token():
    headers = build_headers_sin_authorization()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_header_vacio():
    headers = {}
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_metodo_incorrecto():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_sin_permisos():
    headers = build_headers("Bearer token_sin_permisos")
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_con_limit(limit=5 ):
    headers = build_headers()
    params = {**_prepare_params(f"active:'true'"), "limit": limit}
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_limit_excedido():
    headers = build_headers()
    params = {**_prepare_params(f"active:'true'"), "limit": 200}
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_validar_estructura():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_validar_object():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_validar_data():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_validar_campos_price():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_caracteres_especiales():
    headers = build_headers()
    params = _prepare_params("💲✨🔥")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_query_larga():
    headers = build_headers()
    params = _prepare_params(f"{'a' * 5000}")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_moneda_inexistente():
    headers = build_headers()
    params = _prepare_params(f"currency:'xyz'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_sin_registros():
    headers = build_headers()
    params = _prepare_params(f"")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response


def buscar_precios_validar_url():
    headers = build_headers()
    params = _prepare_params(f"active:'true'")
    response = StripeAPI(BASE_URL).get(
        endpoint=ENDPOINT, headers=headers, params=params
    )
    log_request_response(f"{BASE_URL}{ENDPOINT}", headers, params, response)
    return response
