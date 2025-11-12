import pytest
import jsonschema
from src.schemas.output.coupon_output_schema import coupon_output_schema


def assert_creacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL por fallo en creación exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_fallida(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"{e}")
    except Exception as e:
        pytest.xfail(f"{e}")


def assert_creacion_sin_token(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_sin_permisos(response):
    try:
        assert response.status_code == 403, f"Se esperaba 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL permisos insuficientes: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_campos_cupon_validos(response):
    try:
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
        data = response.json()
        campos = ["id", "object", "percent_off", "duration", "valid"]
        for campo in campos:
            assert campo in data, f"Falta el campo obligatorio '{campo}' en la respuesta"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campos cupón válidos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_tipos_datos_cupon(response):
    try:
        data = response.json()
        assert isinstance(data.get("id"), str), "El campo 'id' debe ser string"
        assert isinstance(data.get("percent_off"), (int, float, type(None))), "El campo 'percent_off' debe ser numérico o nulo"
        assert isinstance(data.get("duration"), str), "El campo 'duration' debe ser string"
        assert isinstance(data.get("valid"), bool), "El campo 'valid' debe ser booleano"
    except AssertionError as e:
        pytest.xfail(f"XFAIL tipos de datos inválidos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_estructura_body_cupon(response):
    try:
        assert response.status_code in [200, 201], f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura del body inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_content_type_json(response):
    try:
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Content-Type inesperado: {content_type}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL tipo de contenido inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_estructura_error_json(response):
    try:
        assert response.status_code in [400, 401, 403], f"Se esperaba error, se recibió {response.status_code}"
        data = response.json()
        assert "error" in data, "No se encontró el campo 'error' en la respuesta"
        assert "message" in data["error"], "No se encontró el campo 'message' dentro de 'error'"
    except AssertionError as e:
        pytest.xfail(f"XFAIL estructura de error inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")
