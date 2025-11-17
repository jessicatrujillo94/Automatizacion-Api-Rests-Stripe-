import pytest
import allure
from src.stripe_api.obtener_products_api import (
    obtener_lista_completa_productos,
    obtener_productos_con_limit_5,
    obtener_productos_activos,
    obtener_productos_inactivos,
    obtener_productos_sin_token,
    obtener_productos_token_invalido,
    obtener_productos_sin_permisos,
    obtener_productos_query_invalido,
    obtener_productos_limit_mayor_100,
    obtener_productos_validar_estructura,
)
from src.assertions.obtener_products_asserions import (
    assert_obtencion_exitosa,
    assert_obtencion_con_limit_5,
    assert_obtencion_activos,
    assert_obtencion_inactivos,
    assert_obtencion_sin_token,
    assert_obtencion_token_invalido,
    assert_obtencion_sin_permisos,
    assert_obtencion_query_invalido,
    assert_obtencion_limit_mayor_100,
    assert_estructura_respuesta_obtencion,
)

@allure.epic("EPIC: Gestión de Productos")
@allure.feature("Feature: Obtener Productos")
@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.smoke
@pytest.mark.functional
def test_obtener_lista_completa_productos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "product")
    response = obtener_lista_completa_productos()
    assert_obtencion_exitosa(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
def test_obtener_productos_con_limit_5():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    response = obtener_productos_con_limit_5()
    assert_obtencion_con_limit_5(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
def test_obtener_productos_activos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    response = obtener_productos_activos()
    assert_obtencion_activos(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
def test_obtener_productos_inactivos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    response = obtener_productos_inactivos()
    assert_obtencion_inactivos(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_obtener_productos_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    response = obtener_productos_sin_token()
    assert_obtencion_sin_token(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_obtener_productos_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    response = obtener_productos_token_invalido()
    assert_obtencion_token_invalido(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_obtener_productos_sin_permisos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    response = obtener_productos_sin_permisos()
    assert_obtencion_sin_permisos(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_obtener_productos_query_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    response = obtener_productos_query_invalido()
    assert_obtencion_query_invalido(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_obtener_productos_limit_mayor_100():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    response = obtener_productos_limit_mayor_100()
    assert_obtencion_limit_mayor_100(response)

@allure.story("HU: HU003-Obtener Productos")
@pytest.mark.functional
def test_obtener_productos_validar_estructura():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    response = obtener_productos_validar_estructura()
    assert_estructura_respuesta_obtencion(response)
