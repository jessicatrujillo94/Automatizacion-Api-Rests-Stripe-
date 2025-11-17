import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.listar_tax_codes_api import (
    listar_tax_codes,
    listar_tax_codes_sin_token,
    listar_tax_codes_token_invalido,
    listar_tax_codes_filtrar_jurisdiccion,
    listar_tax_codes_limit,
    listar_tax_codes_starting_after,
    listar_tax_codes_vacio,
    listar_tax_codes_filtro_invalido,
    listar_tax_codes_sin_permisos,
)
from src.assertions.listar_tax_codes_assertion import (
    assert_listado_exitosa,
    assert_listado_sin_token,
    assert_listado_token_invalido,
    assert_estructura_respuesta_listado,
    assert_elementos_tax_code,
    assert_listado_vacio,
    assert_filtro_invalido,
    assert_formato_json,
    assert_jurisdiccion_coherente,
    assert_listado_sin_permisos,
)

@allure.epic("EPIC: Gestión de Tax Codes")
@allure.feature("Feature: Listar Tax Codes")
@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.smoke
@pytest.mark.functional
def test_TAXL001_listar_tax_codes_token_valido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "tax_code")
    logger.info("Iniciando test_TAXL001_listar_tax_codes_token_valido")
    respuesta = listar_tax_codes()
    assert_listado_exitosa(respuesta)
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_code(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXL002_listar_tax_codes_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_code")
    logger.info("Iniciando test_TAXL002_listar_tax_codes_sin_token")
    respuesta = listar_tax_codes_sin_token()
    assert_listado_sin_token(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXL003_listar_tax_codes_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_code")
    logger.info("Iniciando test_TAXL003_listar_tax_codes_token_invalido")
    respuesta = listar_tax_codes_token_invalido()
    assert_listado_token_invalido(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.regression
def test_TAXL004_validar_estructura_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_code")
    logger.info("Iniciando test_TAXL004_validar_estructura_respuesta")
    respuesta = listar_tax_codes()
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_code(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.regression
def test_TAXL005_validar_elementos_data():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_code")
    logger.info("Iniciando test_TAXL005_validar_elementos_data")
    respuesta = listar_tax_codes()
    assert_elementos_tax_code(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
def test_TAXL006_listar_filtrando_por_jurisdiccion():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_code")
    logger.info("Iniciando test_TAXL006_listar_filtrando_por_jurisdiccion")
    respuesta = listar_tax_codes_filtrar_jurisdiccion("US")
    assert_listado_exitosa(respuesta)
    assert_jurisdiccion_coherente(respuesta, "US")

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
def test_TAXL007_listar_tax_codes_limit_1():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_code")
    logger.info("Iniciando test_TAXL007_listar_tax_codes_limit_1")
    respuesta = listar_tax_codes_limit(1)
    assert_listado_exitosa(respuesta)
    assert len(respuesta.json().get("data", [])) <= 1

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
def test_TAXL009_listar_tax_codes_starting_after():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_code")
    logger.info("Iniciando test_TAXL009_listar_tax_codes_starting_after")
    respuesta = listar_tax_codes_starting_after("txcd_99999999")
    assert_listado_exitosa(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
def test_TAXL010_listar_tax_codes_vacio():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "tax_code")
    logger.info("Iniciando test_TAXL010_listar_tax_codes_vacio")
    respuesta = listar_tax_codes_vacio()
    assert_listado_vacio(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXL011_filtro_invalido_limit_negativo():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_code")
    logger.info("Iniciando test_TAXL011_filtro_invalido_limit_negativo")
    respuesta = listar_tax_codes_filtro_invalido(-5)
    assert_filtro_invalido(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_TAXL012_listar_tax_codes_sin_permisos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "tax_code")
    logger.info("Iniciando test_TAXL012_listar_tax_codes_sin_permisos")
    respuesta = listar_tax_codes_sin_permisos()
    assert_listado_sin_permisos(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.regression
def test_TAXL013_validar_formato_json():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_code")
    logger.info("Iniciando test_TAXL013_validar_formato_json")
    respuesta = listar_tax_codes()
    assert_formato_json(respuesta)

@allure.story("HU: HU040-Listar Tax Codes")
@pytest.mark.regression
def test_TAXL014_validar_nombre_descripcion_coherentes_con_jurisdiccion():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "tax_code")
    logger.info("Iniciando test_TAXL014_validar_nombre_descripcion_coherentes_con_jurisdiccion")
    respuesta = listar_tax_codes()
    assert_jurisdiccion_coherente(respuesta)
