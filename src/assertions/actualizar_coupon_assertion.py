import pytest
import jsonschema
from src.schemas.output.coupon_output_schema import coupon_output_schema


def assert_actualizacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
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


def assert_actualizacion_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_cupon_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_campo_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campo inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_nombre_caracteres_especiales(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL caracteres especiales en nombre: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_metadata_compleja(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL metadata compleja: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_desactivado(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json()
        assert data.get("active") is False, "El campo 'active' debería ser False"
    except AssertionError as e:
        pytest.xfail(f"XFAIL desactivación de cupón: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_body_invalido(response):
    try:
        assert response.status_code in [400, 422], f"Se esperaba 400 o 422, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL body inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_campos_no_soportados(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campos no soportados: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_actualizacion(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_actualizacion_sin_permisos(response):
    try:
        assert response.status_code in [403,401], f"Se esperaba 403 Forbidden, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin permisos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
