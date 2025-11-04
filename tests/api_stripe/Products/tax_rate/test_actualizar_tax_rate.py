import pytest
from src.logs.logger import logger
from src.stripe_api.actualizar_tax_rate_api import (
    actualizar_tax_rate,
    actualizar_tax_rate_inexistente,
    actualizar_tax_rate_sin_token,
    actualizar_tax_rate_token_invalido,
    actualizar_tax_rate_display_name_vacio,
    actualizar_tax_rate_campo_extra,
    actualizar_tax_rate_active_false,
)
from src.assertions.actualizar_tax_rate_assertion import (
    assert_actualizacion_exitosa,
    assert_actualizacion_id_inexistente,
    assert_actualizacion_sin_token,
    assert_actualizacion_token_invalido,
    assert_actualizacion_display_name_vacio,
    assert_actualizacion_campo_extra,
    assert_estructura_respuesta_actualizacion,
    assert_actualizacion_active,
)

@pytest.mark.functional
def test_TAXRUP001_actualizar_tax_rate_campos_validos(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP001_actualizar_tax_rate_campos_validos")
    respuesta = actualizar_tax_rate(tax_rate_creado)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@pytest.mark.functional
def test_TAXRUP002_actualizar_tax_rate_inexistente():
    logger.info("Iniciando test_TAXRUP002_actualizar_tax_rate_inexistente")
    respuesta = actualizar_tax_rate_inexistente()
    assert_actualizacion_id_inexistente(respuesta)

@pytest.mark.functional
def test_TAXRUP003_actualizar_tax_rate_sin_token(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP003_actualizar_tax_rate_sin_token")
    respuesta = actualizar_tax_rate_sin_token(tax_rate_creado)
    assert_actualizacion_sin_token(respuesta)

@pytest.mark.functional
def test_TAXRUP004_actualizar_tax_rate_token_invalido(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP004_actualizar_tax_rate_token_invalido")
    respuesta = actualizar_tax_rate_token_invalido(tax_rate_creado)
    assert_actualizacion_token_invalido(respuesta)

@pytest.mark.functional
def test_TAXRUP005_actualizar_tax_rate_display_name_vacio(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP005_actualizar_tax_rate_display_name_vacio")
    respuesta = actualizar_tax_rate_display_name_vacio(tax_rate_creado)
    assert_actualizacion_display_name_vacio(respuesta)

@pytest.mark.regression
def test_TAXRUP006_validar_estructura_respuesta(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP006_validar_estructura_respuesta")
    respuesta = actualizar_tax_rate(tax_rate_creado)
    assert_estructura_respuesta_actualizacion(respuesta)

@pytest.mark.functional
def test_TAXRUP007_forzar_error_campo_extra(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP007_forzar_error_campo_extra")
    respuesta = actualizar_tax_rate_campo_extra(tax_rate_creado)
    assert_actualizacion_campo_extra(respuesta)

@pytest.mark.performance
def test_TAXRUP008_tiempo_respuesta(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP008_tiempo_respuesta")
    respuesta = actualizar_tax_rate(tax_rate_creado)
    assert respuesta.elapsed.total_seconds() < 2, "Tiempo de respuesta mayor a 2s"

@pytest.mark.functional
def test_TAXRUP009_actualizar_active_false(tax_rate_creado):
    logger.info("Iniciando test_TAXRUP009_actualizar_active_false")
    respuesta = actualizar_tax_rate_active_false(tax_rate_creado)
    assert_actualizacion_active(respuesta, expected_active=False)
