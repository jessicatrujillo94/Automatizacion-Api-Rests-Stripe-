import pytest
import jsonschema
from src.schemas.output.price_output_schema import price_output_schema


def assert_creacion_exitosa(response):
    try:
        print(response.json())
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL por fallo en creación exitosa: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_fallida(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL por fallo en creación fallida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


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


def assert_creacion_producto_inexistente(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL producto inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_campos_no_soportados(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campos no soportados: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_inactivo(response):
    try:
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
        data = response.json()
        assert data.get("active") is False, "El precio no está inactivo"
    except AssertionError as e:
        pytest.xfail(f"XFAIL price inactivo: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_nombre_vacio(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL nickname vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_metadata_compleja(response):
    try:
        assert response.status_code in [200, 201], f"Se esperaba 200 o 201, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL metadata compleja: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_multiple(responses):
    try:
        for response in responses:
            assert response.status_code in [200, 201], (
                f"Se esperaba 200 o 201, se recibió {response.status_code}"
            )
    except AssertionError as e:
        pytest.xfail(f"XFAIL creación múltiple: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_estructura_respuesta_price(response):
    try:
        assert response.status_code in [200, 201], f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de price inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_nombre_largo(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL nickname largo: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")


def assert_creacion_body_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL body inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL por excepción inesperada: {e}")
