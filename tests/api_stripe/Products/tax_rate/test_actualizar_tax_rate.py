import pytest
import allure
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

@allure.epic("EPIC: Gestión de Tax Rates")
@allure.feature("Feature: Actualizar Tax Rate")
@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
def test_TAXRUP001_actualizar_tax_rate_campos_validos(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP001_actualizar_tax_rate_campos_validos")
    respuesta = actualizar_tax_rate(tax_rate_valido)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRUP002_actualizar_tax_rate_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP002_actualizar_tax_rate_inexistente")
    respuesta = actualizar_tax_rate_inexistente()
    assert_actualizacion_id_inexistente(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRUP003_actualizar_tax_rate_sin_token(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP003_actualizar_tax_rate_sin_token")
    respuesta = actualizar_tax_rate_sin_token(tax_rate_valido)
    assert_actualizacion_sin_token(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRUP004_actualizar_tax_rate_token_invalido(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP004_actualizar_tax_rate_token_invalido")
    respuesta = actualizar_tax_rate_token_invalido(tax_rate_valido)
    assert_actualizacion_token_invalido(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRUP005_actualizar_tax_rate_display_name_vacio(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP005_actualizar_tax_rate_display_name_vacio")
    respuesta = actualizar_tax_rate_display_name_vacio(tax_rate_valido)
    assert_actualizacion_display_name_vacio(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.regression
def test_TAXRUP006_validar_estructura_respuesta(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP006_validar_estructura_respuesta")
    respuesta = actualizar_tax_rate(tax_rate_valido)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRUP007_forzar_error_campo_extra(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP007_forzar_error_campo_extra")
    respuesta = actualizar_tax_rate_campo_extra(tax_rate_valido)
    assert_actualizacion_campo_extra(respuesta)

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
@pytest.mark.performance
def test_TAXRUP008_tiempo_respuesta(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "performance", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP008_tiempo_respuesta")
    respuesta = actualizar_tax_rate(tax_rate_valido)
    assert respuesta.elapsed.total_seconds() < 2, "Tiempo de respuesta mayor a 2s"

@allure.story("HU: HU051-Actualizar Tax Rate")
@pytest.mark.functional
def test_TAXRUP009_actualizar_active_false(tax_rate_valido):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_rate")
    logger.info("Iniciando test_TAXRUP009_actualizar_active_false")
    respuesta = actualizar_tax_rate_active_false(tax_rate_valido)
    assert_actualizacion_active(respuesta, valor_esperado=False)
