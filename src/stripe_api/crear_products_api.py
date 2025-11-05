import os
from src.services.auth import build_headers, build_headers_sin_authorization
from src.logs.conflogger import log_request_response
from src.stripe_api.stripe_api import StripeAPI
from src.resources.enums.endpoints import ProductEndpoints

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_KEY_INVALIDA = f"Bearer {os.getenv('API_KEY_INVALIDA')}"

ENDPOINT = ProductEndpoints.CREATE_PRODUCT.value


def crear_producto_campos_minimos():
    headers = build_headers()
    payload = {"name": "Producto básico"}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, payload=payload, response=response
    )
    return response


def crear_producto_todos_campos():
    headers = build_headers()
    payload = {
        "name": "Producto completo",
        "description": "Producto con todos los campos opcionales",
        "active": True,
        "metadata[categoria]": "general",
        "attributes[]": ["color", "tamaño"],
    }
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_sin_token():
    headers = build_headers_sin_authorization()
    payload = {"name": "Producto sin token"}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_token_invalido():
    headers = build_headers(API_KEY_INVALIDA)
    print(headers)
    payload = {"name": "Producto token inválido"}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_permisos_insuficientes():
    headers = build_headers()
    payload = {"name": "Producto restringido"}
    url = f"{BASE_URL}/v1/restricted_resource"
    response = StripeAPI(BASE_URL).post(
        endpoint="/v1/restricted_resource", headers=headers, payload=payload
    )
    log_request_response(url=url, headers=headers, response=response)
    return response


def crear_producto_sin_nombre():
    headers = build_headers()
    payload = {}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_nombre_vacio():
    headers = build_headers()
    payload = {"name": ""}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_nombre_caracteres_especiales():
    headers = build_headers()
    payload = {"name": "Producto_#@!_$$"}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_respuesta_estructura():
    headers = build_headers()
    payload = {"name": "Producto estructura válida"}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_multiples_productos():
    headers = build_headers()
    productos = [
        {"name": "Producto 1"},
        {"name": "Producto 2"},
        {"name": "Producto 3"},
    ]
    responses = []
    for producto in productos:
        response = StripeAPI(BASE_URL).post(
            endpoint=ENDPOINT, headers=headers, payload=producto
        )
        log_request_response(
            url=f"{BASE_URL}{ENDPOINT}",
            headers=headers,
            response=response,
            payload=producto,
        )
        responses.append(response)
    return responses


def crear_producto_nombre_largo():
    headers = build_headers()
    payload = {"name": "P" * 260}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_metadata_compleja():
    headers = build_headers()
    payload = {
        "name": "Producto con metadata compleja",
        "metadata": {
            "categorias": ["hogar", "decoración"],
            "detalles": {"peso": "1kg", "color": "rojo"},
        },
    }
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_inactivo():
    headers = build_headers()
    payload = {"name": "Producto inactivo", "active": False}
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_body_invalido():
    headers = build_headers()
    payload = "name=ProductoInvalido"  # formato incorrecto (no JSON / dict)
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def crear_producto_campos_adicionales():
    headers = build_headers()
    payload = {
        "name": "Producto con campos extra",
        "campo_invalido": "valor inesperado",
    }
    response = StripeAPI(BASE_URL).post(
        endpoint=ENDPOINT, headers=headers, payload=payload
    )
    log_request_response(
        url=f"{BASE_URL}{ENDPOINT}", headers=headers, response=response, payload=payload
    )
    return response


def eliminar_producto(response):
    try:
        if not response or not hasattr(response, "json"):
            return None
        data = response.json()
        producto_id = data.get("id")

        if not producto_id:
            return None

        headers = build_headers()
        endpoint = ProductEndpoints.DELETE_PRODUCT.value.format(product_id=producto_id)
        delete_response = StripeAPI(BASE_URL).delete(endpoint=endpoint, headers=headers)
        print(delete_response.json())
        return delete_response
    except Exception as e:
        return None
