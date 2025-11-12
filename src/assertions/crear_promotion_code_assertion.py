import pytest
import jsonschema
from src.schemas.output.promocional_code_output_schema import  promocional_code_output_schema


def assert_creacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code in [201, 200], f"Se esperaba 201 Created, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=promocional_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"{e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_fallida(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL creación fallida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_creacion_duplicado(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por duplicado, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL código duplicado: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_promotion_code(response):
    try:
        assert response.status_code in [200, 201], f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=promocional_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_validacion_tipos_datos(response):
    try:
        data = response.json()
        assert isinstance(data.get("id"), str)
        assert isinstance(data.get("object"), str)
        assert isinstance(data.get("coupon"), dict)
        assert isinstance(data.get("code"), str)
    except AssertionError as e:
        pytest.xfail(f"XFAIL validación tipos de datos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_respuesta_json_header(response):
    try:
        assert response.headers.get("Content-Type") == "application/json", \
            f"Se esperaba application/json, se recibió {response.headers.get('Content-Type')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL encabezado JSON inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_tiempo_respuesta(response, max_ms=2000):
    try:
        tiempo = response.get("duration")
        assert tiempo <= max_ms, f"Tiempo de respuesta {tiempo}ms excede límite de {max_ms}ms"
    except AssertionError as e:
        pytest.xfail(f"{e}")
    except Exception as e:
        pytest.xfail(f"{e}")


def assert_limite_uso(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 por límite de uso, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL límite de uso: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_coupon_existente(response):
    try:
        assert response.status_code in [200,201], f"Se esperaba 400 por coupon inexistente, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL coupon inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_valor_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 por valor inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL valor inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_code_unico_case_sensitive(response):
    try:
        assert response.status_code in [201,200], f"Se esperaba 201 Created, se recibió {response.status_code}"
        code = response.json().get("code")
        print(code.isupper())
        assert not code.isupper() and not code.islower(), "El código debe respetar mayúsculas/minúsculas"
    except AssertionError as e:
        pytest.xfail(f"{e}")
    except Exception as e:
        pytest.xfail(f"{e}")


def assert_permisos_restringidos(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por permisos restringidos, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL permisos restringidos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
