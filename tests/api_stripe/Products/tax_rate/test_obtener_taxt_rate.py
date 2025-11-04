import pytest
from src.logs.logger import logger
from src.stripe_api.consultar_tax_rate_api import (
    consultar_tax_rate,
    consultar_tax_rate_inexistente,
    consultar_tax_rate_sin_token,
    consultar_tax_rate_token_invalido,
    consultar_tax_rate_id_malformado,
)
from src.assertions.consultar_tax_rate_assertion import (
    assert_consulta_exitosa,
    assert_consulta_id_inexistente,
    assert_consulta_sin_token,
    assert_consulta_token_invalido,
    assert_estructura_respuesta_consulta,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_TAXRGET001_consultar_tax_rate_valido(tax_rate_creado):
    logger.info("Iniciando test_TAXRGET001_consultar_tax_rate_valido")
    respuesta = consultar_tax_rate(tax_rate_creado)
    assert_consulta_exitosa(respuesta)
    assert_estructura_respuesta_consulta(respuesta)

@pytest.mark.functional
def test_TAXRGET002_consultar_tax_rate_inexistente():
    logger.info("Iniciando test_TAXRGET002_consultar_tax_rate_inexistente")
    respuesta = consultar_tax_rate_inexistente()
    assert_consulta_id_inexistente(respuesta)

@pytest.mark.functional
def test_TAXRGET003_consultar_tax_rate_sin_token(tax_rate_creado):
    logger.info("Iniciando test_TAXRGET003_consultar_tax_rate_sin_token")
    respuesta = consultar_tax_rate_sin_token(tax_rate_creado)
    assert_consulta_sin_token(respuesta)

@pytest.mark.functional
def test_TAXRGET004_consultar_tax_rate_token_invalido(tax_rate_creado):
    logger.info("Iniciando test_TAXRGET004_consultar_tax_rate_token_invalido")
    respuesta = consultar_tax_rate_token_invalido(tax_rate_creado)
    assert_consulta_token_invalido(respuesta)

@pytest.mark.regression
def test_TAXRGET005_validar_estructura_respuesta(tax_rate_creado):
    logger.info("Iniciando test_TAXRGET005_validar_estructura_respuesta")
    respuesta = consultar_tax_rate(tax_rate_creado)
    assert_estructura_respuesta_consulta(respuesta)

@pytest.mark.performance
def test_TAXRGET006_tiempo_respuesta(tax_rate_creado):
    logger.info("Iniciando test_TAXRGET006_tiempo_respuesta")
    respuesta = consultar_tax_rate(tax_rate_creado)
    assert respuesta.elapsed.total_seconds() < 2, "Tiempo de respuesta mayor a 2s"

@pytest.mark.functional
def test_TAXRGET007_id_malformado():
    logger.info("Iniciando test_TAXRGET007_id_malformado")
    respuesta = consultar_tax_rate_id_malformado("txr_!@#")
    assert_consulta_id_inexistente(respuesta)
