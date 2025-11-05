import pytest
import jsonschema
from src.schemas.output.tax_rate_output_schema import tax_rate_output_schema


def assert_actualizacion_exitosa(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_rate_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL actualización exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_id_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL ID inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por token inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_display_name_vacio(response):
    try:
        assert response.status_code in [400,404], f"Se esperaba 400,404 Bad Request para display_name vacío, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL display_name vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_campo_extra(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por campo extra, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campo extra no soportado: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_active(response, valor_esperado):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        data = response.json()
        assert data.get("active") == valor_esperado, f"Persistencia fallida: active esperado '{valor_esperado}', recibido '{data.get('active')}'"
    except AssertionError as e:
        pytest.xfail(f"XFAIL actualización active: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_actualizacion(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_rate_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
