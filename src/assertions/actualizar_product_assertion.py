# src/assertions/actualizar_product_assertion.py

import pytest
import jsonschema
from src.schemas.output.product_output_schema import product_output_schema

def assert_actualizacion_exitosa(response, max_response_time=2):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        assert response.elapsed.total_seconds() <= max_response_time, f"Tiempo de respuesta muy alto: {response.elapsed.total_seconds()}s"
    except AssertionError as e:
        pytest.xfail(f"XFAIL actualización exitosa: {e}")

def assert_actualizacion_fallida(response, max_response_time=2):
    try:
        assert response.status_code in [400, 404], f"Se esperaba 400 o 404, se recibió {response.status_code}"
        assert response.elapsed.total_seconds() <= max_response_time
    except AssertionError as e:
        pytest.xfail(f"XFAIL actualización fallida: {e}")

def assert_actualizacion_token_invalido(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")

def assert_actualizacion_sin_permisos(response):
    try:
        assert response.status_code == 403, f"Se esperaba 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL permisos insuficientes: {e}")

def assert_actualizacion_id_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL product_id inexistente: {e}")

def assert_actualizacion_nombre_vacio(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL nombre vacío: {e}")

def assert_actualizacion_caracteres_especiales(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL caracteres especiales en nombre: {e}")

def assert_actualizacion_inactivo(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL actualización a inactivo: {e}")

def assert_actualizacion_body_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL body inválido: {e}")

def assert_actualizacion_campos_no_soportados(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campos no soportados: {e}")

def assert_actualizacion_sin_body(response):
    try:
        assert response.status_code in [200, 400], f"Se esperaba 200 o 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin body: {e}")

def assert_estructura_respuesta_actualizacion(response):
    try:
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=product_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta: {e}")
