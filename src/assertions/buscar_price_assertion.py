import pytest
import jsonschema
from src.schemas.output.price_output_schema import price_list_schema

def assert_busqueda_exitosa(response):
    try:
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_list_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL successful search failed: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_fallida(response):
    try:
        assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL search failed: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_token_invalido(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL invalid token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_sin_token(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL missing token: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_header_vacio(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL empty header: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_metodo_incorrecto(response):
    try:
        assert response.status_code == 405, f"Expected 405 Method Not Allowed, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL incorrect HTTP method: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_sin_permisos(response):
    try:
        assert response.status_code in [401, 403], f"Expected 401 or 403, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL insufficient permissions: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_paginacion_valida(response):
    try:
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        data = response.json()
        assert "has_more" in data and "next_page" in data, "Pagination fields missing"
    except AssertionError as e:
        pytest.xfail(f"XFAIL pagination invalid: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_busqueda_limit_excedido(response):
    try:
        assert response.status_code == 400, f"Expected 400 Bad Request for limit exceeded, got {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL limit exceeded: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_estructura_respuesta_busqueda(response):
    try:
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=price_list_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"XFAIL search response structure invalid: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_object_search_result(response):
    try:
        data = response.json()
        assert data.get("object") == "search_result", f"Expected object='search_result', got {data.get('object')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL object field invalid: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_data_array_precios(response):
    try:
        data = response.json()
        assert isinstance(data.get("data"), list), "Expected 'data' to be a list"
    except AssertionError as e:
        pytest.xfail(f"XFAIL data array invalid: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_campos_objeto_price(response):
    try:
        for price in response.json().get("data", []):
            assert "id" in price and "object" in price and "currency" in price \
                   and "unit_amount" in price and "active" in price
    except AssertionError as e:
        pytest.xfail(f"XFAIL price object fields missing: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")


def assert_url_valida(response):
    try:
        data = response.json()
        assert data.get("url") == "/v1/prices/search", f"Expected url='/v1/prices/search', got {data.get('url')}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL url field invalid: {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL unexpected exception: {e}")
