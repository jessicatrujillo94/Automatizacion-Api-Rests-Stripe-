import pytest
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
)

@pytest.mark.smoke
@pytest.mark.functional
def test_PMUP001_actualizar_active_false(one_promotion_code):
    logger.info("Iniciando test_PMUP001_actualizar_active_false")
    respuesta = actualizar_promo_active_false(one_promotion_code)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)


@pytest.mark.functional
def test_PMUP002_actualizar_restriction_usage_valido(one_promotion_code):
    logger.info("Iniciando test_PMUP002_actualizar_restriction_usage_valido")
    respuesta = actualizar_promo_restriction_usage(one_promotion_code, usage_limit=5)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_PMUP003_actualizar_promo_id_invalido():
    logger.info("Iniciando test_PMUP003_actualizar_promo_id_invalido")
    respuesta = actualizar_promo_id_invalido()
    assert_actualizacion_id_inexistente(respuesta)


@pytest.mark.functional
def test_PMUP004_actualizar_sin_token(one_promotion_code):
    logger.info("Iniciando test_PMUP004_actualizar_sin_token")
    respuesta = actualizar_promo_sin_token(one_promotion_code)
    assert_actualizacion_sin_permisos(respuesta)


@pytest.mark.functional
def test_PMUP005_actualizar_token_invalido(one_promotion_code):
    logger.info("Iniciando test_PMUP005_actualizar_token_invalido")
    respuesta = actualizar_promo_token_invalido(one_promotion_code)
    assert_actualizacion_token_invalido(respuesta)


@pytest.mark.functional
def test_PMUP006_actualizar_body_vacio(one_promotion_code):
    logger.info("Iniciando test_PMUP006_actualizar_body_vacio")
    respuesta = actualizar_promo_body_vacio(one_promotion_code)
    assert_actualizacion_body_invalido(respuesta)


@pytest.mark.functional
def test_PMUP007_actualizar_active_invalido(one_promotion_code):
    logger.info("Iniciando test_PMUP007_actualizar_active_invalido")
    respuesta = actualizar_promo_active_invalido(one_promotion_code)
    assert_actualizacion_active_invalido(respuesta)


@pytest.mark.functional
def test_PMUP008_actualizar_restriction_invalido(one_promotion_code):
    logger.info("Iniciando test_PMUP008_actualizar_restriction_invalido")
    respuesta = actualizar_promo_restriction_invalido(one_promotion_code)
    assert_actualizacion_restriction_invalido(respuesta)


@pytest.mark.functional
def test_PMUP009_actualizar_multiple_campos(one_promotion_code):
    logger.info("Iniciando test_PMUP009_actualizar_multiple_campos")
    respuesta = actualizar_promo_multiple_campos(one_promotion_code)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)


@pytest.mark.regression
def test_PMUP010_validar_estructura_respuesta(one_promotion_code):
    logger.info("Iniciando test_PMUP010_validar_estructura_respuesta")
    respuesta = consultar_promo_code_id(one_promotion_code)
    assert_estructura_respuesta_actualizacion(respuesta)
