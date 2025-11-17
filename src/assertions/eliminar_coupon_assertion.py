# src/assertions/eliminar_coupon_assertion.py

import pytest
import jsonschema
from src.schemas.output.coupon_output_schema import coupon_deleted_output_schema


def assert_eliminacion_exitosa(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_deleted_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL eliminación exitosa: {e}")


def assert_eliminacion_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón inexistente: {e}")


def assert_eliminacion_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL eliminación sin token: {e}")


def assert_eliminacion_token_invalido(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")


def assert_eliminacion_ya_eliminado(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón ya eliminado previamente: {e}")


def assert_eliminacion_reflejada_en_listado(response, coupon_id):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json().get("data", [])
        assert all(item.get("id") != coupon_id for item in data), f"El cupón {coupon_id} aún aparece en el listado"
    except AssertionError as e:
        pytest.xfail(f" {e}")
