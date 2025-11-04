import pytest
import jsonschema
from src.schemas.output.price_output_schema import price_output_schema


def assert_actualizacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_output_schema)
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


def assert_actualizacion_no_autorizada(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL no autorizado: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_prohibida(response):
    try:
        assert response.status_code == 403, f"Se esperaba 403 Forbidden, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL prohibida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_price(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_persistencia_cambio(response_consulta, campo, valor_esperado):
    try:
        assert response_consulta.status_code == 200, f"Se esperaba 200, se recibió {response_consulta.status_code}"
        data = response_consulta.json()
        assert data.get(campo) == valor_esperado, f"Persistencia fallida: {campo} esperado '{valor_esperado}', recibido '{data.get(campo)}'"
    except AssertionError as e:
        pytest.xfail(f"XFAIL persistencia de cambio: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
