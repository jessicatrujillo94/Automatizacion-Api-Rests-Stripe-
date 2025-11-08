import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.crear_tax_rate_api import (
    crear_tax_rate,
    crear_tax_rate_con_todos_campos,
    crear_tax_rate_sin_display_name,
    crear_tax_rate_porcentaje_invalido,
    crear_tax_rate_inclusive_invalido,
    crear_tax_rate_sin_token,
    crear_tax_rate_token_invalido,
    crear_tax_rate_campo_extra,
)
from src.assertions.crear_tax_rate_assertion import (
    assert_creacion_exitosa,
    assert_creacion_sin_display_name,
    assert_creacion_porcentaje_invalido,
    assert_creacion_inclusive_invalido,
    assert_creacion_sin_token,
    assert_creacion_token_invalido,
    assert_estructura_respuesta_creacion,
    assert_creacion_campo_extra,
)

@allure.epic("EPIC: Gestión de Tax Rates")
@allure.feature("Feature: Crear Tax Rate")
@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.smoke
@pytest.mark.functional
def test_TAXRPOST001_crear_tax_rate_campos_obligatorios():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST001_crear_tax_rate_campos_obligatorios")
    respuesta = crear_tax_rate()
    assert_creacion_exitosa(respuesta)
    assert_estructura_respuesta_creacion(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
def test_TAXRPOST002_crear_tax_rate_todos_campos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST002_crear_tax_rate_todos_campos")
    respuesta = crear_tax_rate_con_todos_campos()
    assert_creacion_exitosa(respuesta)
    assert_estructura_respuesta_creacion(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST003_crear_tax_rate_sin_display_name():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST003_crear_tax_rate_sin_display_name")
    respuesta = crear_tax_rate_sin_display_name()
    assert_creacion_sin_display_name(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST004_crear_tax_rate_porcentaje_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST004_crear_tax_rate_porcentaje_invalido")
    respuesta = crear_tax_rate_porcentaje_invalido()
    assert_creacion_porcentaje_invalido(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST005_crear_tax_rate_inclusive_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST005_crear_tax_rate_inclusive_invalido")
    respuesta = crear_tax_rate_inclusive_invalido()
    assert_creacion_inclusive_invalido(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST006_crear_tax_rate_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST006_crear_tax_rate_sin_token")
    respuesta = crear_tax_rate_sin_token()
    assert_creacion_sin_token(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST007_crear_tax_rate_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST007_crear_tax_rate_token_invalido")
    respuesta = crear_tax_rate_token_invalido()
    assert_creacion_token_invalido(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.regression
def test_TAXRPOST008_validar_estructura_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST008_validar_estructura_respuesta")
    respuesta = crear_tax_rate()
    assert_estructura_respuesta_creacion(respuesta)

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
def test_TAXRPOST009_tiempo_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST009_tiempo_respuesta")
    respuesta = crear_tax_rate()
    assert respuesta.elapsed.total_seconds() < 2, "Tiempo de respuesta mayor a 2s"

@allure.story("HU: HU050-Crear Tax Rate")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXRPOST010_forzar_error_campo_extra():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_rate")
    logger.info("Iniciando test_TAXRPOST010_forzar_error_campo_extra")
    respuesta = crear_tax_rate_campo_extra()
    assert_creacion_campo_extra(respuesta)
