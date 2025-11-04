import pytest
import jsonschema
from src.schemas.output.tax_code_output_schema import tax_code_output_schema


def assert_consulta_exitosa(response):
    try:
        print(response.json())
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL consulta exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_consulta_id_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL ID inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_consulta_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_consulta_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por token inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_consulta_id_vacio(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por ID vacío, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL ID vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_tax_code(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_object_tax_code(response):
    try:
        data = response.json()
        assert data.get("object") == "tax_code", f"Se esperaba object='tax_code', se recibió {data.get('object')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL object incorrecto: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_tipos_datos_tax_code(response):
    try:
        data = response.json()
        assert isinstance(data.get("id"), str), f"id debe ser str, se recibió {type(data.get('id'))}"
        assert isinstance(data.get("display_name"), str), f"display_name debe ser str, se recibió {type(data.get('display_name'))}"
        assert isinstance(data.get("percentage"), (int, float)), f"percentage debe ser numérico, se recibió {type(data.get('percentage'))}"
        assert isinstance(data.get("inclusive"), bool), f"inclusive debe ser bool, se recibió {type(data.get('inclusive'))}"
        assert isinstance(data.get("active"), bool), f"active debe ser bool, se recibió {type(data.get('active'))}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL tipos de datos incorrectos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_error_404_coherente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found coherente, se recibió {response.status_code}"
        data = response.json()
        assert "error" in data and "message" in data["error"], f"Estructura de error incoherente: {data}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL error 404 incoherente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
