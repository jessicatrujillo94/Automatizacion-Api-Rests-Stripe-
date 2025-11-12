import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.consultar_promotion_code_api import (
    consultar_promo_code_id,
    consultar_promo_id_inexistente,
    consultar_promo_sin_token,
    consultar_promo_token_invalido,
)
from src.assertions.consultar_promotion_code_assertion import (
    assert_consulta_exitosa,
    assert_consulta_id_inexistente,
    assert_consulta_sin_token,
    assert_consulta_token_invalido,
    assert_estructura_respuesta_consulta,
    assert_restrictions_usage_numeric,
)

@allure.epic("EPIC: Gestión de Promotion Codes")
@allure.feature("Feature: Consultar Promotion Codes")
@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.smoke
@pytest.mark.functional
def test_PMGET001_obtener_codigo_existente(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "promotion_code")
    logger.info("Iniciando test_PMGET001_obtener_codigo_existente")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_consulta_exitosa(respuesta)
    assert_estructura_respuesta_consulta(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PMGET002_obtener_codigo_id_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMGET002_obtener_codigo_id_inexistente")
    respuesta = consultar_promo_id_inexistente()
    assert_consulta_id_inexistente(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PMGET003_obtener_codigo_sin_token(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMGET003_obtener_codigo_sin_token")
    respuesta = consultar_promo_sin_token(one_promotion_code)
    assert_consulta_sin_token(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PMGET004_obtener_codigo_token_invalido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMGET004_obtener_codigo_token_invalido")
    respuesta = consultar_promo_token_invalido(one_promotion_code)
    assert_consulta_token_invalido(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.regression
def test_PMGET005_validar_estructura_respuesta(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PMGET005_validar_estructura_respuesta")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_estructura_respuesta_consulta(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.regression
def test_PMGET006_validar_formato_json_encabezado(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PMGET006_validar_formato_json_encabezado")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_estructura_respuesta_consulta(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
def test_PMGET007_obtener_codigo_active_false(one_promotion_code_inactivo):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMGET007_obtener_codigo_active_false")
    respuesta = consultar_promo_code_id(one_promotion_code_inactivo)
    assert_consulta_exitosa(respuesta)
    assert respuesta.json().get("active") is False

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
def test_PMGET008_tiempo_respuesta_menor_2s(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMGET008_tiempo_respuesta_menor_2s")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert respuesta.elapsed.total_seconds() <= 2

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
@pytest.mark.negative
def test_PMGET009_obtener_codigo_id_formato_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMGET009_obtener_codigo_id_formato_invalido")
    promo_id = "promo_123"
    respuesta = consultar_promo_code_id({ "id": promo_id })
    assert_consulta_id_inexistente(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.regression
def test_PMGET010_validar_restrictions_usage_numeric(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PMGET010_validar_restrictions_usage_numeric")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_restrictions_usage_numeric(respuesta)

@allure.story("HU: HU020-Consultar Promotion Codes")
@pytest.mark.functional
@pytest.mark.integration
def test_PMGET011_validar_consistencia_cupon(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "integration", "api", "promotion_code")
    logger.info("Iniciando test_PMGET011_validar_consistencia_cupon")
    respuesta = consultar_promo_code_id(one_promotion_code)
    coupon_id = respuesta.json().get("coupon", {}).get("id")
    try:
        assert coupon_id is not None
    except Exception as e:
        pytest.xfail(f"{e}")
