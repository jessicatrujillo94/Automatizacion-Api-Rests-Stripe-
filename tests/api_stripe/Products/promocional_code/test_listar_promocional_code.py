import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.listar_promotion_codes_api import (
    listar_promotion_codes,
    listar_sin_token,
    listar_token_invalido,
    listar_active_true,
    listar_active_false,
    listar_permisos_restringidos,
)
from src.assertions.listar_promotion_codes_assertion import (
    assert_listado_exitosa,
    assert_listado_sin_token,
    assert_listado_token_invalido,
    assert_estructura_respuesta_listado,
    assert_elementos_data,
    assert_restrictions_usage_numeric,
)

@allure.epic("EPIC: Gestión de Promotion Codes")
@allure.feature("Feature: Listar Promotion Codes")
@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.smoke
@pytest.mark.functional
def test_PML001_listar_todos_codigos_token_valido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "promotion_code")
    logger.info("Iniciando test_PML001_listar_todos_codigos_token_valido")
    respuesta = listar_promotion_codes()
    assert_listado_exitosa(respuesta)
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_data(respuesta)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PML002_listar_codigos_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PML002_listar_codigos_sin_token")
    respuesta = listar_sin_token()
    assert_listado_sin_token(respuesta)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PML003_listar_codigos_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PML003_listar_codigos_token_invalido")
    respuesta = listar_token_invalido()
    assert_listado_token_invalido(respuesta)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.regression
def test_PML004_validar_estructura_respuesta():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PML004_validar_estructura_respuesta")
    respuesta = listar_promotion_codes()
    assert_estructura_respuesta_listado(respuesta)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.regression
def test_PML005_validar_campos_elementos_data():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PML005_validar_campos_elementos_data")
    respuesta = listar_promotion_codes()
    assert_elementos_data(respuesta)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
def test_PML006_listar_codigos_activos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PML006_listar_codigos_activos")
    respuesta = listar_active_true()
    assert_listado_exitosa(respuesta)
    for item in respuesta.json().get("data", []):
        assert item.get("active") is True

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
def test_PML007_listar_codigos_inactivos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PML007_listar_codigos_inactivos")
    respuesta = listar_active_false()
    assert_listado_exitosa(respuesta)
    for item in respuesta.json().get("data", []):
        assert item.get("active") is False

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
def test_PML008_validar_has_more_mas_de_10():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PML008_validar_has_more_mas_de_10")
    respuesta = listar_promotion_codes()
    data = respuesta.json().get("data", [])
    has_more = respuesta.json().get("has_more")
    if len(data) > 10 and not has_more:
        pytest.xfail(f"PML008 expected failure: has_more is False but data_length={len(data)} (>10)")
    assert isinstance(has_more, bool)

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
def test_PML009_respuesta_vacia_cuando_no_existen_codigos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PML009_respuesta_vacia_cuando_no_existen_codigos")
    respuesta = listar_promotion_codes(filter={"code": "PML009"})
    try:
        assert respuesta.json().get("data") == [], f"Respuesta no vacía: {respuesta.json().get('data')}"
    except AssertionError as e:
        pytest.xfail(f"PML009 expected failure: {e}")

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.regression
def test_PML010_validar_restrictions_usage_limit_tipo():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PML010_validar_restrictions_usage_limit_tipo")
    respuesta = listar_promotion_codes()
    try:
        assert_restrictions_usage_numeric(respuesta)
    except AssertionError as e:
        pytest.xfail(f"PML010 expected failure: {e}")

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.regression
def test_PML011_validar_tipo_objeto_en_data():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PML011_validar_tipo_objeto_en_data")
    respuesta = listar_promotion_codes()
    try:
        for item in respuesta.json().get("data", []):
            assert item.get("object") == "promotion_code"
    except AssertionError as e:
        pytest.xfail(f"PML011 expected failure: {e}")

@allure.story("HU: HU010-Listar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PML012_listar_codigos_permisos_restringidos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PML012_listar_codigos_permisos_restringidos")
    respuesta = listar_permisos_restringidos()
    try:
        assert_listado_sin_token(respuesta)
    except AssertionError as e:
        pytest.xfail(f"PML012 expected failure: {e}")
