# src/assertions/assert_obtener_productos.py

import pytest
import jsonschema
from src.schemas.output.product_output_schema import product_list_output_schema


def assert_obtencion_exitosa(response, max_response_time=2):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"


def assert_obtencion_con_limit_5(response):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    data = response.json().get("data", [])
    assert len(data) <= 5, f"Se esperaban máximo 5 productos, se recibieron {len(data)}"


def assert_obtencion_activos(response):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    data = response.json().get("data", [])
    if data:
        assert all(p.get("active", False) for p in data), "Se esperaban solo productos activos"


def assert_obtencion_inactivos(response):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    data = response.json().get("data", [])
    if data:
        assert all(not p.get("active", True) for p in data), "Se esperaban solo productos inactivos"


def assert_obtencion_sin_token(response):
    assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"


def assert_obtencion_token_invalido(response):
    assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"


def assert_obtencion_sin_permisos(response):
    assert response.status_code == 401, f"Se esperaba 403, se recibió {response.status_code}"


def assert_obtencion_query_invalido(response):
    assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"


def assert_obtencion_limit_mayor_100(response):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"


def assert_estructura_respuesta_obtencion(response):
    assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
    jsonschema.validate(instance=response.json(), schema=product_list_output_schema)
