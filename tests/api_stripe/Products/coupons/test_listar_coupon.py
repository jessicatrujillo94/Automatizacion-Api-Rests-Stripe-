import pytest
from src.logs.logger import logger
from src.stripe_api.listar_coupon_api import (
    listar_cupones_valido,
    listar_cupones_sin_token,
    listar_cupones_token_invalido,
    listar_cupones_validar_estructura,
    listar_cupones_objetos_validos,
    listar_cupones_vacio,
    listar_cupones_has_more,
    listar_cupones_limit,
    listar_cupones_starting_after,
    listar_cupones_tiempo_respuesta,
    listar_cupones_tipo_object,
    listar_cupones_campos_numericos,
    listar_cupones_sin_permisos,
    listar_cupones_filtro_invalido,
    listar_cupones_expirados,
    listar_cupones_json_correcto,
)
from src.assertions.listar_coupon_assertion import (
    assert_listar_cupones_valido,
    assert_listar_cupones_sin_token,
    assert_listar_cupones_token_invalido,
    assert_listar_cupones_validar_estructura,
    assert_listar_cupones_objetos_validos,
    assert_listar_cupones_vacio,
    assert_listar_cupones_has_more,
    assert_listar_cupones_limit,
    assert_listar_cupones_starting_after,
    assert_listar_cupones_tiempo_respuesta,
    assert_listar_cupones_tipo_object,
    assert_listar_cupones_campos_numericos,
    assert_listar_cupones_sin_permisos,
    assert_listar_cupones_filtro_invalido,
    assert_listar_cupones_expirados,
    assert_listar_cupones_json_correcto,
)


@pytest.mark.smoke
@pytest.mark.functional
def test_CPNL001_listar_cupones_valido():
    logger.info("Iniciando test_CPNL001_listar_cupones_valido")
    response = listar_cupones_valido()
    assert_listar_cupones_valido(response)
    assert_listar_cupones_validar_estructura(response)


@pytest.mark.functional
def test_CPNL002_listar_cupones_sin_token():
    logger.info("Iniciando test_CPNL002_listar_cupones_sin_token")
    response = listar_cupones_sin_token()
    assert_listar_cupones_sin_token(response)


@pytest.mark.functional
def test_CPNL003_listar_cupones_token_invalido():
    logger.info("Iniciando test_CPNL003_listar_cupones_token_invalido")
    response = listar_cupones_token_invalido()
    assert_listar_cupones_token_invalido(response)


@pytest.mark.regression
def test_CPNL004_validar_estructura_array():
    logger.info("Iniciando test_CPNL004_validar_estructura_array")
    response = listar_cupones_validar_estructura()
    assert_listar_cupones_validar_estructura(response)


@pytest.mark.regression
def test_CPNL005_validar_objetos_en_data():
    logger.info("Iniciando test_CPNL005_validar_objetos_en_data")
    response = listar_cupones_objetos_validos()
    assert_listar_cupones_objetos_validos(response)


@pytest.mark.functional
def test_CPNL006_respuesta_vacia():
    logger.info("Iniciando test_CPNL006_respuesta_vacia")
    response = listar_cupones_vacio()
    assert_listar_cupones_vacio(response)


@pytest.mark.functional
def test_CPNL007_validar_has_more():
    logger.info("Iniciando test_CPNL007_validar_has_more")
    response = listar_cupones_has_more()
    assert_listar_cupones_has_more(response)


@pytest.mark.functional
def test_CPNL008_parametro_limit():
    logger.info("Iniciando test_CPNL008_parametro_limit")
    response = listar_cupones_limit(limit=1)
    assert_listar_cupones_limit(response)


@pytest.mark.functional
def test_CPNL009_parametro_starting_after(coupon_creado):
    logger.info("Iniciando test_CPNL009_parametro_starting_after")
    response = listar_cupones_starting_after(coupon_creado)
    assert_listar_cupones_starting_after(response)


@pytest.mark.performance
def test_CPNL010_tiempo_respuesta():
    logger.info("Iniciando test_CPNL010_tiempo_respuesta")
    response = listar_cupones_tiempo_respuesta()
    assert_listar_cupones_tiempo_respuesta(0,response.elapsed_time, max_seconds=2)


@pytest.mark.regression
def test_CPNL011_validar_tipo_object():
    logger.info("Iniciando test_CPNL011_validar_tipo_object")
    response = listar_cupones_tipo_object()
    assert_listar_cupones_tipo_object(response)


@pytest.mark.regression
def test_CPNL012_validar_campos_numericos():
    logger.info("Iniciando test_CPNL012_validar_campos_numericos")
    response = listar_cupones_campos_numericos()
    assert_listar_cupones_campos_numericos(response)


@pytest.mark.functional
def test_CPNL013_listar_cupones_sin_permisos():
    logger.info("Iniciando test_CPNL013_listar_cupones_sin_permisos")
    response = listar_cupones_sin_permisos()
    assert_listar_cupones_sin_permisos(response)


@pytest.mark.functional
def test_CPNL015_filtro_invalido():
    logger.info("Iniciando test_CPNL015_filtro_invalido")
    response = listar_cupones_filtro_invalido()
    assert_listar_cupones_filtro_invalido(response)


@pytest.mark.functional
def test_CPNL016_validar_cupones_expirados():
    logger.info("Iniciando test_CPNL016_validar_cupones_expirados")
    response = listar_cupones_expirados()
    assert_listar_cupones_expirados(response)


@pytest.mark.regression
def test_CPNL017_validar_json_correcto():
    logger.info("Iniciando test_CPNL017_validar_json_correcto")
    response = listar_cupones_json_correcto()
    assert_listar_cupones_json_correcto(response)
