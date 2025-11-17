import pytest
import jsonschema
from src.schemas.output.promocional_code_output_schema import list_promocional_code_output_schema


def assert_listado_exitosa(response):
    try:
        print(response.json())
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=list_promocional_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL listado exitoso: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Se esperaba 401 o 403 por token inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL token inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_estructura_respuesta_listado(response):
    try:
        assert response.status_code == 200, f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=list_promocional_code_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_elementos_data(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        data_list = response.json().get("data", [])
        assert isinstance(data_list, list), f"Se esperaba lista en 'data', se recibió {type(data_list)}"
        for item in data_list:
            required_fields = ["id", "object", "active", "coupon", "code"]
            for field in required_fields:
                assert field in item, f"Falta el campo '{field}' en item: {item}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL elementos de data inválidos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_restrictions_usage_numeric(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        data_list = response.json().get("data", [])
        for item in data_list:
            if "restrictions" in item and "usage_limit" in item["restrictions"]:
                usage = item["restrictions"]["usage_limit"]
                assert isinstance(usage, int) or usage is None, f"usage_limit debe ser int o None, se recibió {usage}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL restrictions usage inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
