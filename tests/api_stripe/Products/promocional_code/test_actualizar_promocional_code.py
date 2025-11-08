import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.actualizar_promotion_code_api import (
    actualizar_promo_active_false,
    actualizar_promo_restriction_usage,
    actualizar_promo_id_invalido,
    actualizar_promo_sin_token,
    actualizar_promo_token_invalido,
    actualizar_promo_body_vacio,
    actualizar_promo_active_invalido,
    actualizar_promo_restriction_invalido,
    actualizar_promo_multiple_campos,
    consultar_promo_code_id,
    actualizar_promo_restriction_usage, 
    actualizar_promo_multiple_campos, 
    consultar_promo_code_id
)
from src.assertions.actualizar_promotion_code_assertion import (
    assert_actualizacion_exitosa,
    assert_actualizacion_fallida,
    assert_actualizacion_token_invalido,
    assert_actualizacion_sin_permisos,
    assert_actualizacion_id_inexistente,
    assert_actualizacion_body_invalido,
    assert_actualizacion_active_invalido,
    assert_actualizacion_restriction_invalido,
    assert_estructura_respuesta_actualizacion,
    assert_actualizacion_fallida,
    assert_actualizacion_restriction_invalido
)

@allure.epic("EPIC: Gestión de Promotion Codes")
@allure.feature("Feature: Actualizar Promotion Code")
@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.smoke
@pytest.mark.functional
def test_PMUP001_actualizar_active_false(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP001_actualizar_active_false")
    respuesta = actualizar_promo_active_false(one_promotion_code)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP002_actualizar_restriction_usage_valido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP002_actualizar_restriction_usage_valido")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=5)
    assert_actualizacion_exitosa(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP003_actualizar_promo_id_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP003_actualizar_promo_id_invalido")
    respuesta = actualizar_promo_id_invalido()
    assert_actualizacion_id_inexistente(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP004_actualizar_sin_token(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP004_actualizar_sin_token")
    respuesta = actualizar_promo_sin_token(one_promotion_code)
    assert_actualizacion_sin_permisos(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP005_actualizar_token_invalido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP005_actualizar_token_invalido")
    respuesta = actualizar_promo_token_invalido(one_promotion_code)
    assert_actualizacion_token_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP006_actualizar_body_vacio(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP006_actualizar_body_vacio")
    respuesta = actualizar_promo_body_vacio(one_promotion_code)
    assert_actualizacion_body_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP007_actualizar_active_invalido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP007_actualizar_active_invalido")
    respuesta = actualizar_promo_active_invalido(one_promotion_code)
    assert_actualizacion_active_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP008_actualizar_restriction_invalido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP008_actualizar_restriction_invalido")
    respuesta = actualizar_promo_restriction_invalido(one_promotion_code)
    assert_actualizacion_restriction_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP009_actualizar_multiple_campos(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP009_actualizar_multiple_campos")
    respuesta = actualizar_promo_multiple_campos(one_promotion_code)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.regression
@pytest.mark.negative
def test_PMUP010_validar_estructura_respuesta(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP010_validar_estructura_respuesta")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP011_actualizar_usage_limit_cero(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP011_actualizar_usage_limit_cero")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=0)
    assert_actualizacion_restriction_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP012_actualizar_usage_limit_uno(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP012_actualizar_usage_limit_uno")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=1)
    assert_actualizacion_exitosa(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP013_actualizar_usage_limit_max(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP013_actualizar_usage_limit_max")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=10000)
    assert_actualizacion_exitosa(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP014_actualizar_usage_limit_superior(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP014_actualizar_usage_limit_superior")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=10001)
    assert_actualizacion_restriction_invalido(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.negative
def test_PMUP015_actualizar_coupon_invalido(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "promotion_code")
    logger.info("Iniciando test_PMUP015_actualizar_coupon_invalido")
    respuesta = actualizar_promo_multiple_campos(one_promotion_code)
    assert_actualizacion_fallida(respuesta)

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.regression
def test_PMUP016_validar_formato_json(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "promotion_code")
    logger.info("Iniciando test_PMUP016_validar_formato_json")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_estructura_respuesta_actualizacion(respuesta)
    assert "application/json" in respuesta.headers.get("Content-Type", "")

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
@pytest.mark.performance
def test_PMUP017_tiempo_respuesta(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "performance", "api", "promotion_code")
    logger.info("Iniciando test_PMUP017_tiempo_respuesta")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert respuesta.elapsed.total_seconds() <= 2

@allure.story("HU: HU009-Actualizar Promotion Code")
@pytest.mark.functional
def test_PMUP018_actualizar_multiple_campos(one_promotion_code):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "promotion_code")
    logger.info("Iniciando test_PMUP018_actualizar_multiple_campos")
    respuesta = actualizar_promo_multiple_campos(one_promotion_code)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)
