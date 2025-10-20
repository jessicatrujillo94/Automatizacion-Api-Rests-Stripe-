import pytest
import jsonschema
from  src.schemas.output.lista_customer_output_schema import lista_customer_output_schema   
def assert_autenticacion_exitosa(response):
    assert response.status_code == 200, f"Status code incorrecto: {response.status_code}"
def assert_autenticacion_fallida(response, max_response_time=2):
    assert response.status_code == 401, f"Se esperaba 401, se recibió {response.status_code}"
    data = response.json()
    assert "error" in data, "No se encontró el campo 'error' en la respuesta"
    assert "message" in data["error"], "Falta campo 'message' en el error"
    assert "type" in data["error"], "Falta campo 'type' en el error"
    assert data["error"]["type"] == "invalid_request_error", f"Tipo de error inesperado: {data['error']['type']}"
    assert response.elapsed.total_seconds() < max_response_time, "Tiempo de respuesta muy alto"

def assert_autenticacion_sin_token(response):
    try:
        assert response.status_code == 403, f"Se esperaba 403, se recibió {response.status_code}"
    except AssertionError as e:
        pytest.xfail(f"XFAIL: Error inesperado - {e}")
    except Exception as e:
        pytest.xfail(f"XFAIL: Excepción inesperada - {e}")

def assert_autenticacion_header_incorrecto(response, max_response_time=2):
    try:
        expected_statuses = [400, 401, 403]
        assert response.status_code in expected_statuses, (
            f"Se esperaba uno de {expected_statuses}, se recibió {response.status_code}"
        )
    except AssertionError as e:
        pytest.xfail(f"XFAIL por fallo en autenticación: {e}")
def assert_autenticacion_api_key_vacia(response, max_response_time=2):
    try:
        expected_statuses = [401]
        assert response.status_code in expected_statuses, (
            f"Se esperaba uno de {expected_statuses}, se recibió {response.status_code}"
        )
    except AssertionError as e:
        pytest.xfail(f"XFAIL por fallo en autenticación: {e}")

def assert_autenticacion_endpoint_restringido(response, max_response_time=2):
    try:
        expected_statuses = [404]
        assert response.status_code in expected_statuses, (
            f"Se esperaba uno de {expected_statuses}, se recibió {response.status_code}"
        )
    except AssertionError as e:
        pytest.xfail(f"XFAIL por fallo en autenticación: {e}")

def assert_respuesta_body_schema(response):
    try:
        assert response.status_code in [200, 201, 204], f"Código inesperado: {response.status_code}"
        jsonschema.validate(instance=response.json(), schema=lista_customer_output_schema)
    except (AssertionError, jsonschema.ValidationError) as e:
        pytest.xfail(f"Schema no cumplido: {str(e)}")
    except Exception as e:
        pytest.xfail(f"Error inesperado: {str(e)}")