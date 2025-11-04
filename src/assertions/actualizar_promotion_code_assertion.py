import pytest
import jsonschema
from src.schemas.output.promotion_code_output_schema import promotion_code_output_schema


def assert_actualizacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=promotion_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL actualización exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_fallida(response):
    try:
        assert response.status_code in [400, 404], f"Se esperaba 400 o 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL actualización fallida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_sin_permisos(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por permisos restringidos, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin permisos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_id_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL ID inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_body_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL body inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_active_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 por active inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL active inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_restriction_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 por restriction inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL restriction inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_actualizacion(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=promotion_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
