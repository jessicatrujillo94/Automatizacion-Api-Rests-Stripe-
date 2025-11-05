import pytest
from src.logs.logger import logger
from src.stripe_api.listar_tax_rates_api import (
    listar_tax_rates,
    listar_tax_rates_sin_token,
    listar_tax_rates_token_invalido,
    listar_tax_rates_vacio,
    listar_tax_rates_limit,
    listar_tax_rates_starting_after,
    listar_tax_rates_filtro_invalido,
    listar_tax_rates_sin_permisos,
)
from src.assertions.listar_tax_rates_assertion import (
    assert_listado_exitosa,
    assert_listado_sin_token,
    assert_listado_token_invalido,
    assert_estructura_respuesta_listado,
    assert_elementos_tax_rate,
    assert_listado_vacio,
    assert_filtro_invalido,
    assert_formato_json,
    assert_ids_unicos,
    assert_listado_sin_permisos,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_TAXRL001_listar_tax_rates_token_valido():
    logger.info("Iniciando test_TAXRL001_listar_tax_rates_token_valido")
    respuesta = listar_tax_rates()
    assert_listado_exitosa(respuesta)
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_rate(respuesta)

@pytest.mark.functional
def test_TAXRL002_listar_tax_rates_sin_token():
    logger.info("Iniciando test_TAXRL002_listar_tax_rates_sin_token")
    respuesta = listar_tax_rates_sin_token()
    assert_listado_sin_token(respuesta)

@pytest.mark.functional
def test_TAXRL003_listar_tax_rates_token_invalido():
    logger.info("Iniciando test_TAXRL003_listar_tax_rates_token_invalido")
    respuesta = listar_tax_rates_token_invalido()
    assert_listado_token_invalido(respuesta)

@pytest.mark.regression
def test_TAXRL004_validar_estructura_respuesta():
    logger.info("Iniciando test_TAXRL004_validar_estructura_respuesta")
    respuesta = listar_tax_rates()
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_rate(respuesta)

@pytest.mark.regression
def test_TAXRL005_validar_elementos_data():
    logger.info("Iniciando test_TAXRL005_validar_elementos_data")
    respuesta = listar_tax_rates()
    assert_elementos_tax_rate(respuesta)

@pytest.mark.functional
def test_TAXRL006_listar_tax_rates_vacio():
    logger.info("Iniciando test_TAXRL006_listar_tax_rates_vacio")
    respuesta = listar_tax_rates_vacio()
    assert_listado_vacio(respuesta)

@pytest.mark.functional
def test_TAXRL007_listar_tax_rates_limit_1():
    logger.info("Iniciando test_TAXRL007_listar_tax_rates_limit_1")
    respuesta = listar_tax_rates_limit(1)
    assert_listado_exitosa(respuesta)
    assert len(respuesta.json().get("data", [])) <= 1

@pytest.mark.functional
def test_TAXRL008_listar_tax_rates_starting_after():
    logger.info("Iniciando test_TAXRL008_listar_tax_rates_starting_after")
    respuesta = listar_tax_rates_starting_after("txr_1SQCA3A8CmS6V2ZIDw9cy8q1")
    assert_listado_exitosa(respuesta)

@pytest.mark.functional
def test_TAXRL009_tiempo_respuesta():
    logger.info("Iniciando test_TAXRL009_tiempo_respuesta")
    respuesta = listar_tax_rates()
    assert respuesta.elapsed.total_seconds() < 2, "Tiempo de respuesta mayor a 2s"

@pytest.mark.functional
def test_TAXRL010_filtro_invalido_limit_negativo():
    logger.info("Iniciando test_TAXRL010_filtro_invalido_limit_negativo")
    respuesta = listar_tax_rates_filtro_invalido(-5)
    assert_filtro_invalido(respuesta)

@pytest.mark.functional
def test_TAXRL011_validar_ids_unicos():
    logger.info("Iniciando test_TAXRL011_validar_ids_unicos")
    respuesta = listar_tax_rates()
    assert_ids_unicos(respuesta)

@pytest.mark.regression
def test_TAXRL012_validar_tipo_objeto_tax_rate():
    logger.info("Iniciando test_TAXRL012_validar_tipo_objeto_tax_rate")
    respuesta = listar_tax_rates()
    for item in respuesta.json().get("data", []):
        assert item.get("object") == "tax_rate", f"Objeto inesperado: {item.get('object')}"

@pytest.mark.functional
def test_TAXRL013_listar_tax_rates_sin_permisos():
    logger.info("Iniciando test_TAXRL013_listar_tax_rates_sin_permisos")
    respuesta = listar_tax_rates_sin_permisos()
    assert_listado_sin_permisos(respuesta)
