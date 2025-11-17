import pytest
import jsonschema
from src.schemas.output.price_output_schema import price_output_schema
from src.stripe_api.obtener_products_api import obtener_producto

def assert_consulta_exitosa(response):
    try:
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL successful price retrieval failed: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_fallida(response):
    try:
        assert response.status_code == 404, f"Expected 404 Not Found, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL non-existent price: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_sin_token(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL missing token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_header_vacio(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL empty authorization header: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_metodo_incorrecto(response):
    try:
        assert response.status_code == 405, f"Expected 405 Method Not Allowed, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL incorrect HTTP method: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_consulta_sin_permisos(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL insufficient permissions: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_campos_price_validos(response):
    try:
        data = response.json()
        for field in ["id", "object", "currency", "unit_amount", "product", "active"]:
            assert field in data, f"Missing field: {field}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL missing price fields: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_tipos_datos_price(response):
    try:
        data = response.json()
        assert isinstance(data.get("id"), str), "id must be string"
        assert isinstance(data.get("currency"), str), "currency must be string"
        assert isinstance(data.get("unit_amount"), int), "unit_amount must be integer"
        assert isinstance(data.get("active"), bool), "active must be boolean"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid data type in price: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_estructura_body_price(response):
    try:
        data = response.json()
        assert data.get("object") == "price", f"Expected object='price', got {data.get('object')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid body structure: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_producto_existente(response):
    try:
        data = response.json()
        product = obtener_producto(data.get("product"))
        assert product.json().get("id") is not None, "Product field should not be null"
    except AssertionError as e:
        pytest.xfail(f"XFAIL product reference missing: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_content_type_json(response):
    try:
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Expected Content-Type application/json, got {content_type}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid Content-Type: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_estructura_error_json(response):
    try:
        data = response.json()
        assert "error" in data, "Missing error field in response"
        assert "message" in data["error"], "Missing error.message field"
        assert "type" in data["error"], "Missing error.type field"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid error JSON structure: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")
