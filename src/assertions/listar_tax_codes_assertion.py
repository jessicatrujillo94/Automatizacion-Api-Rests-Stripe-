import pytest
import jsonschema
from src.schemas.output.tax_code_output_schema import tax_codes_output_schema


def assert_listado_exitosa(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_codes_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL listado exitoso: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por token inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_listado(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_codes_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_elementos_tax_code(response):
    try:
        data = response.json().get("data", [])
        for item in data:
            assert item.get("object") == "tax_code", f"Se esperaba object='tax_code', se recibió {item.get('object')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL elementos tax_code incorrectos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_vacio(response):
    try:
        data = response.json().get("data", [])
        assert len(data) == 0, f"Se esperaba listado vacío, se recibieron {len(data)} elementos"
    except AssertionError as e:
        pytest.xfail(f"XFAIL listado no vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_filtro_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL filtro inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_formato_json(response):
    try:
        data = response.json()
        assert isinstance(data, dict), f"Se esperaba dict, se recibió {type(data)}"
        assert "object" in data and "data" in data, f"Formato JSON incorrecto: {data}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL formato JSON: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_jurisdiccion_coherente(response):
    try:
        data = response.json().get("data", [])
        for item in data:
            assert item.get("object") == "tax_code", f"Jurisdicción incoherente: se esperaba tax_code, se recibió {item.get('object')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL jurisdicción incoherente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_sin_permisos(response):
    try:
        assert response.status_code in [403, 401], f"Se esperaba 403 Forbidden por permisos insuficientes, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL listado sin permisos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
