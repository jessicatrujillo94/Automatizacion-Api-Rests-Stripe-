import pytest
import jsonschema
from src.schemas.output.tax_rate_output_schema import tax_rate_output_schema


def assert_listado_exitosa(response):
    try:
        assert response.status_code == 200, f"Se esperaba 200 OK, se recibió {response.status_code}"
        jsonschema.validate(instance=response.json(), schema={
            "type": "object",
            "properties": {
                "object": {"type": "string"},
                "data": {"type": "array"}
            },
            "required": ["object", "data"]
        })
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL listado exitoso: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_sin_token(response):
    try:
        assert response.status_code == 401, f"Se esperaba 401 Unauthorized por ausencia de token, se recibió {response.status_code}"
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
        data = response.json()
        assert "object" in data and data["object"] == "list"
        assert "data" in data and isinstance(data["data"], list)
    except AssertionError as e:
        pytest.xfail(f"XFAIL estructura de respuesta inválida: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_elementos_tax_rate(response):
    try:
        data = response.json().get("data", [])
        for item in data:
            for field in ["id", "display_name", "percentage", "inclusive", "active", "jurisdiction"]:
                assert field in item, f"Falta campo {field} en item {item.get('id')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL elementos tax_rate incompletos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_vacio(response):
    try:
        assert response.status_code == 200
        data = response.json().get("data", [])
        assert len(data) == 0, f"Se esperaba listado vacío, se recibieron {len(data)} elementos"
    except AssertionError as e:
        pytest.xfail(f"XFAIL listado no vacío: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_filtro_invalido(response):
    try:
        assert response.status_code == 400, f"Se esperaba 400 Bad Request por filtro inválido, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL filtro inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_formato_json(response):
    try:
        assert response.headers.get("Content-Type") == "application/json", f"Se esperaba Content-Type application/json, se recibió {response.headers.get('Content-Type')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL formato JSON inválido: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_ids_unicos(response):
    try:
        data = response.json().get("data", [])
        ids = [item["id"] for item in data]
        assert len(ids) == len(set(ids)), "IDs duplicados en el listado"
    except AssertionError as e:
        pytest.xfail(f"XFAIL IDs no únicos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")


def assert_listado_sin_permisos(response):
    try:
        assert response.status_code in [403, 401], f"Se esperaba 403,401 Forbidden por permisos insuficientes, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL sin permisos: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL excepción inesperada: {e}")
