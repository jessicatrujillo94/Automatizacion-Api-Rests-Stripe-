# tests/test_obtener_productos_api.py

import pytest
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


@pytest.mark.smoke
@pytest.mark.functional
def test_obtener_lista_completa_productos():
    response = obtener_lista_completa_productos()
    assert_obtencion_exitosa(response)


@pytest.mark.functional
def test_obtener_productos_con_limit_5():
    response = obtener_productos_con_limit_5()
    assert_obtencion_con_limit_5(response)


@pytest.mark.functional
def test_obtener_productos_activos():
    response = obtener_productos_activos()
    assert_obtencion_activos(response)


@pytest.mark.functional
def test_obtener_productos_inactivos():
    response = obtener_productos_inactivos()
    assert_obtencion_inactivos(response)


@pytest.mark.functional
def test_obtener_productos_sin_token():
    response = obtener_productos_sin_token()
    assert_obtencion_sin_token(response)


@pytest.mark.functional
def test_obtener_productos_token_invalido():
    response = obtener_productos_token_invalido()
    assert_obtencion_token_invalido(response)


@pytest.mark.functional
def test_obtener_productos_sin_permisos():
    response = obtener_productos_sin_permisos()
    assert_obtencion_sin_permisos(response)


@pytest.mark.functional
def test_obtener_productos_query_invalido():
    response = obtener_productos_query_invalido()
    assert_obtencion_query_invalido(response)


@pytest.mark.functional
def test_obtener_productos_limit_mayor_100():
    response = obtener_productos_limit_mayor_100()
    assert_obtencion_limit_mayor_100(response)


@pytest.mark.functional
def test_obtener_productos_validar_estructura():
    response = obtener_productos_validar_estructura()
    assert_estructura_respuesta_obtencion(response)
