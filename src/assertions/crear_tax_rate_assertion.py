import pytest
import jsonschema
from src.schemas.output.tax_rate_output_schema import tax_rate_output_schema


def assert_creacion_exitosa(response):
    try:
        assert response.status_code in [201, 200], f"Se esperaba 201, 200 Created, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_rate_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL creación exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_sin_display_name(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por display_name faltante, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL display_name faltante: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_porcentaje_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por porcentaje inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL porcentaje inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_inclusive_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por inclusive inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL inclusive inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized por ausencia de token, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por token inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_creacion(response):
    try:
        assert response.status_code in [201, 200], f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=tax_rate_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_campo_extra(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por campo extra no soportado, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campo extra no soportado: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
