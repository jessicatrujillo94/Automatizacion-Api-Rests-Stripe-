import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.buscar_prices_api import (
    buscar_precios_activos,
    buscar_precios_inactivos,
    buscar_precios_por_moneda,
    buscar_precios_por_producto,
    buscar_precios_combinando_filtros,
    buscar_precios_query_invalida,
    buscar_precios_query_vacia,
    buscar_precios_query_mal_estructurada,
    buscar_precios_token_invalido,
    buscar_precios_sin_token,
    buscar_precios_header_vacio,
    buscar_precios_metodo_incorrecto,
    buscar_precios_sin_permisos,
    buscar_precios_con_limit,
    buscar_precios_limit_excedido,
    buscar_precios_validar_estructura,
    buscar_precios_validar_object,
    buscar_precios_validar_data,
    buscar_precios_validar_campos_price,
    buscar_precios_caracteres_especiales,
    buscar_precios_query_larga,
    buscar_precios_moneda_inexistente,
    buscar_precios_sin_registros,
    buscar_precios_validar_url
)
from src.assertions.buscar_price_assertion import (
    assert_busqueda_exitosa,
    assert_busqueda_fallida,
    assert_busqueda_token_invalido,
    assert_busqueda_sin_token,
    assert_busqueda_header_vacio,
    assert_busqueda_metodo_incorrecto,
    assert_busqueda_sin_permisos,
    assert_busqueda_paginacion_valida,
    assert_busqueda_limit_excedido,
    assert_estructura_respuesta_busqueda,
    assert_object_search_result,
    assert_data_array_precios,
    assert_campos_objeto_price,
    assert_url_valida
)

@allure.epic("EPIC: Gestión de Prices")
@allure.feature("Feature: Buscar Prices")
@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB001_buscar_precios_activos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB001_buscar_precios_activos")
    respuesta = buscar_precios_activos()
    assert_busqueda_exitosa(respuesta)
    assert_estructura_respuesta_busqueda(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB002_buscar_precios_inactivos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB002_buscar_precios_inactivos")
    respuesta = buscar_precios_inactivos()
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB003_buscar_precios_por_moneda():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB003_buscar_precios_por_moneda")
    respuesta = buscar_precios_por_moneda("usd")
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB004_buscar_precios_por_producto(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    product_id = producto_creado.json()["id"]
    logger.info("Iniciando test_GETB004_buscar_precios_por_producto")
    respuesta = buscar_precios_por_producto(product_id)
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB005_buscar_precios_combinando_filtros(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    product_id = producto_creado.json()["id"]
    logger.info("Iniciando test_GETB005_buscar_precios_combinando_filtros")
    respuesta = buscar_precios_combinando_filtros(product_id=product_id)
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB006_buscar_precios_query_invalida():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB006_buscar_precios_query_invalida")
    respuesta = buscar_precios_query_invalida()
    assert_busqueda_fallida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB007_buscar_precios_query_vacia():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB007_buscar_precios_query_vacia")
    respuesta = buscar_precios_query_vacia()
    assert_busqueda_fallida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB008_buscar_precios_query_mal_estructurada():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB008_buscar_precios_query_mal_estructurada")
    respuesta = buscar_precios_query_mal_estructurada()
    assert_busqueda_fallida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB009_buscar_precios_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB009_buscar_precios_token_invalido")
    respuesta = buscar_precios_token_invalido()
    assert_busqueda_token_invalido(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB010_buscar_precios_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB010_buscar_precios_sin_token")
    respuesta = buscar_precios_sin_token()
    assert_busqueda_sin_token(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB011_buscar_precios_header_autorizacion_vacio():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB011_buscar_precios_header_autorizacion_vacio")
    respuesta = buscar_precios_header_vacio()
    assert_busqueda_header_vacio(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB012_buscar_precios_metodo_http_incorrecto():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB012_buscar_precios_metodo_http_incorrecto")
    respuesta = buscar_precios_metodo_incorrecto()
    assert_busqueda_metodo_incorrecto(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB013_buscar_precios_token_sin_permisos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB013_buscar_precios_token_sin_permisos")
    respuesta = buscar_precios_sin_permisos()
    assert_busqueda_sin_permisos(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB014_buscar_precios_limit_paginacion():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB014_buscar_precios_limit_paginacion")
    respuesta = buscar_precios_con_limit(5)
    assert_busqueda_exitosa(respuesta)
    assert_busqueda_paginacion_valida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB015_buscar_precios_limit_excedido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB015_buscar_precios_limit_excedido")
    respuesta = buscar_precios_limit_excedido()
    assert_busqueda_limit_excedido(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.regression
def test_GETB016_validar_estructura_respuesta_busqueda():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "price")
    logger.info("Iniciando test_GETB016_validar_estructura_respuesta_busqueda")
    respuesta = buscar_precios_validar_estructura()
    assert_estructura_respuesta_busqueda(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.regression
def test_GETB017_validar_object_en_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "price")
    logger.info("Iniciando test_GETB017_validar_object_en_respuesta")
    respuesta = buscar_precios_validar_object()
    assert_object_search_result(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.regression
def test_GETB018_validar_data_arreglo_objetos_price():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "price")
    logger.info("Iniciando test_GETB018_validar_data_arreglo_objetos_price")
    respuesta = buscar_precios_validar_data()
    assert_data_array_precios(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.regression
def test_GETB019_validar_campos_basicos_en_objeto_price():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "price")
    logger.info("Iniciando test_GETB019_validar_campos_basicos_en_objeto_price")
    respuesta = buscar_precios_validar_campos_price()
    assert_campos_objeto_price(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB020_buscar_precios_con_caracteres_especiales():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB020_buscar_precios_con_caracteres_especiales")
    respuesta = buscar_precios_caracteres_especiales()
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB021_buscar_precios_query_excede_longitud():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB021_buscar_precios_query_excede_longitud")
    respuesta = buscar_precios_query_larga()
    assert_busqueda_fallida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
@pytest.mark.negative
def test_GETB022_buscar_precios_moneda_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "price")
    logger.info("Iniciando test_GETB022_buscar_precios_moneda_inexistente")
    respuesta = buscar_precios_moneda_inexistente()
    assert_busqueda_fallida(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.functional
def test_GETB023_buscar_precios_sin_registros():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "price")
    logger.info("Iniciando test_GETB023_buscar_precios_sin_registros")
    respuesta = buscar_precios_sin_registros()
    assert_busqueda_exitosa(respuesta)

@allure.story("HU: HU007-Buscar Prices")
@pytest.mark.regression
def test_GETB024_validar_url_en_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "price")
    logger.info("Iniciando test_GETB024_validar_url_en_respuesta")
    respuesta = buscar_precios_validar_url()
    assert_url_valida(respuesta)
