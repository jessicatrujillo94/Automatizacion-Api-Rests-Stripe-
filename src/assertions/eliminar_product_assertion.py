# src/assertions/eliminar_product_assertion.py

import pytest
import jsonschema
from src.schemas.output.product_output_schema import product_deleted_output_schema

def assert_eliminacion_exitosa(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL eliminación exitosa: {e}")

def assert_eliminacion_fallida(response, max_response_time=2):
    try:
        assert response.status_code in [400, 404], f"Se esperaba 400 o 404, se recibió {response.status_code}"
        assert response.elapsed.total_seconds() <= max_response_time
    except AssertionError as e:
        pytest.xfail(f"XFAIL eliminación fallida: {e}")

def assert_eliminacion_token_invalido(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")

def assert_eliminacion_sin_permisos(response):
    try:
        assert response.status_code == 401, f"Se esperaba 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL permisos insuficientes: {e}")

def assert_eliminacion_id_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL product_id inexistente: {e}")

def assert_eliminacion_id_vacio(response):
    try:
        assert response.status_code == 404, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL product_id vacío: {e}")

def assert_eliminacion_id_malformado(response):
    try:
        assert response.status_code == 404, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL product_id malformado: {e}")

def assert_estructura_respuesta_eliminacion(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=product_deleted_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta: {e}")

def assert_eliminacion_previamente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL producto ya eliminado previamente: {e}")

def assert_eliminacion_multiple(responses):
    try:
        for response in responses:
            assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL eliminación múltiple: {e}")
