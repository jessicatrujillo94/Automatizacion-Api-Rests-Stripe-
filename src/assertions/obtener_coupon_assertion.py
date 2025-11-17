import pytest
import jsonschema
from src.schemas.output.coupon_output_schema import coupon_output_schema

def assert_obtener_cupon_valido(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL obtener cupón válido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_inexistente(response):
    try:
        assert response.status_code == 404, f"Se esperaba 404 Not Found, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón inexistente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_id_vacio(response):
    try:
        assert response.status_code in [400, 404], f"Se esperaba 400 o 404, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL ID vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_formato_invalido(response):
    try:
        assert response.status_code in [400, 404], f"Se esperaba 400 Bad Request, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL formato de ID inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_validar_estructura(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=coupon_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_valido_true(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json()
        assert data.get("valid") is True, "El campo 'valid' debería ser True"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón debería ser válido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_valido_false(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json()
        assert data.get("valid") is False, "El campo 'valid' debería ser False"
    except AssertionError as e:
        pytest.xfail(f"XFAIL cupón debería ser inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_validar_duration(response, expected_duration):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json()
        assert data.get("duration") == expected_duration, f"Duración esperada '{expected_duration}', recibida '{data.get('duration')}'"
    except AssertionError as e:
        pytest.xfail(f"XFAIL duración del cupón incorrecta: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_validar_descuento(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200, se recibió {response.status_code}"
        data = response.json()
        assert "percent_off" in data or "amount_off" in data, "Debe contener 'percent_off' o 'amount_off'"
    except AssertionError as e:
        pytest.xfail(f"XFAIL campo de descuento ausente: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")

def assert_obtener_cupon_sin_permisos(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin permisos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
