import pytest
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

@pytest.mark.smoke
@pytest.mark.functional
def test_PMGET001_obtener_codigo_existente(promo_creado):
    logger.info("Iniciando test_PMGET001_obtener_codigo_existente")
    respuesta = consultar_promo_code_id(promo_creado)
    assert_consulta_exitosa(respuesta)
    assert_estructura_respuesta_consulta(respuesta)


@pytest.mark.functional
def test_PMGET002_obtener_codigo_id_inexistente():
    logger.info("Iniciando test_PMGET002_obtener_codigo_id_inexistente")
    respuesta = consultar_promo_id_inexistente()
    assert_consulta_id_inexistente(respuesta)


@pytest.mark.functional
def test_PMGET003_obtener_codigo_sin_token(promo_creado):
    logger.info("Iniciando test_PMGET003_obtener_codigo_sin_token")
    respuesta = consultar_promo_sin_token(promo_creado)
    assert_consulta_sin_token(respuesta)


@pytest.mark.functional
def test_PMGET004_obtener_codigo_token_invalido(promo_creado):
    logger.info("Iniciando test_PMGET004_obtener_codigo_token_invalido")
    respuesta = consultar_promo_token_invalido(promo_creado)
    assert_consulta_token_invalido(respuesta)


@pytest.mark.regression
def test_PMGET005_validar_estructura_respuesta(promo_creado):
    logger.info("Iniciando test_PMGET005_validar_estructura_respuesta")
    respuesta = consultar_promo_code_id(promo_creado)
    assert_estructura_respuesta_consulta(respuesta)


@pytest.mark.regression
def test_PMGET006_validar_formato_json_encabezado(promo_creado):
    logger.info("Iniciando test_PMGET006_validar_formato_json_encabezado")
    respuesta = consultar_promo_code_id(promo_creado)
    assert_estructura_respuesta_consulta(respuesta)


@pytest.mark.functional
def test_PMGET007_obtener_codigo_active_false(promo_creado_inactivo):
    logger.info("Iniciando test_PMGET007_obtener_codigo_active_false")
    respuesta = consultar_promo_code_id(promo_creado_inactivo)
    assert_consulta_exitosa(respuesta)
    assert respuesta.json().get("active") is False


@pytest.mark.performance
def test_PMGET008_tiempo_respuesta_menor_2s(promo_creado):
    logger.info("Iniciando test_PMGET008_tiempo_respuesta_menor_2s")
    respuesta = consultar_promo_code_id(promo_creado)
    assert respuesta.elapsed.total_seconds() <= 2


@pytest.mark.functional
def test_PMGET009_obtener_codigo_id_formato_invalido():
    logger.info("Iniciando test_PMGET009_obtener_codigo_id_formato_invalido")
    promo_id = "promo_123"
    respuesta = consultar_promo_code_id(promo_id)
    assert_consulta_id_inexistente(respuesta)


@pytest.mark.regression
def test_PMGET010_validar_restrictions_usage_numeric(promo_creado):
    logger.info("Iniciando test_PMGET010_validar_restrictions_usage_numeric")
    respuesta = consultar_promo_code_id(promo_creado)
    assert_restrictions_usage_numeric(respuesta)


@pytest.mark.integration
def test_PMGET011_validar_consistencia_cupon(promo_creado):
    logger.info("Iniciando test_PMGET011_validar_consistencia_cupon")
    respuesta = consultar_promo_code_id(promo_creado)
    coupon_id = respuesta.json().get("coupon", {}).get("id")
    assert coupon_id is not None
