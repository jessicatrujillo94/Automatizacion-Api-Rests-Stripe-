import pytest
from src.logs.logger import logger
from src.stripe_api.crear_promotion_code_api import (
    crear_codigo_promocional_valido,
    crear_codigo_promocional_sin_coupon,
    crear_codigo_promocional_duplicado,
    crear_codigo_promocional_token_invalido,
    crear_codigo_promocional_sin_token,
    crear_codigo_promocional_limite_uso,
    crear_codigo_promocional_active_invalido,
    crear_codigo_promocional_permisos_restringidos,
    crear_codigo_promocional_coupon_inexistente,
    crear_codigo_promocional_coupon_existente,
    crear_codigo_promocional_estructura_respuesta,
    crear_codigo_promocional_validar_tipos,
    crear_codigo_promocional_validar_json_header,
    crear_codigo_promocional_medir_tiempo_respuesta,
    crear_codigo_promocional_code_case_sensitive,
)
from src.assertions.crear_promotion_code_assertion import (
    assert_creacion_exitosa,
    assert_creacion_fallida,
    assert_creacion_token_invalido,
    assert_creacion_sin_token,
    assert_creacion_duplicado,
    assert_estructura_respuesta_promotion_code,
    assert_validacion_tipos_datos,
    assert_respuesta_json_header,
    assert_tiempo_respuesta,
    assert_limite_uso,
    assert_coupon_existente,
    assert_valor_invalido,
    assert_code_unico_case_sensitive,
    assert_permisos_restringidos,
)


@pytest.mark.functional
def test_POSTPMCD001_crear_codigo_promocional_valido(coupon_creado):
    logger.info("Iniciando test_POSTPMCD001_crear_codigo_promocional_valido")
    respuesta = crear_codigo_promocional_valido(coupon_creado)
    assert_creacion_exitosa(respuesta)
    assert_estructura_respuesta_promotion_code(respuesta)


@pytest.mark.functional
def test_POSTPMCD002_crear_codigo_promocional_sin_coupon():
    logger.info("Iniciando test_POSTPMCD002_crear_codigo_promocional_sin_coupon")
    respuesta = crear_codigo_promocional_sin_coupon()
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTPMCD003_crear_codigo_promocional_duplicado(coupon_creado):
    logger.info("Iniciando test_POSTPMCD003_crear_codigo_promocional_duplicado")
    respuesta = crear_codigo_promocional_duplicado(coupon_creado)
    assert_creacion_duplicado(respuesta)


@pytest.mark.functional
def test_POSTPMCD004_crear_codigo_promocional_token_invalido(coupon_creado):
    logger.info("Iniciando test_POSTPMCD004_crear_codigo_promocional_token_invalido")
    respuesta = crear_codigo_promocional_token_invalido(coupon_creado)
    assert_creacion_token_invalido(respuesta)


@pytest.mark.functional
def test_POSTPMCD005_crear_codigo_promocional_sin_token(coupon_creado):
    logger.info("Iniciando test_POSTPMCD005_crear_codigo_promocional_sin_token")
    respuesta = crear_codigo_promocional_sin_token(coupon_creado)
    assert_creacion_sin_token(respuesta)


@pytest.mark.regression
def test_POSTPMCD006_validar_estructura_respuesta(coupon_creado):
    logger.info("Iniciando test_POSTPMCD006_validar_estructura_respuesta")
    respuesta = crear_codigo_promocional_estructura_respuesta(coupon_creado)
    assert_estructura_respuesta_promotion_code(respuesta)
    


@pytest.mark.regression
def test_POSTPMCD007_validar_tipos_datos(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD007_validar_tipos_datos")
    respuesta = crear_codigo_promocional_validar_tipos(coupon_id)
    assert_validacion_tipos_datos(respuesta)


@pytest.mark.regression
def test_POSTPMCD008_validar_respuesta_json_header(coupon_creado):
    logger.info("Iniciando test_POSTPMCD008_validar_respuesta_json_header")
    respuesta = crear_codigo_promocional_validar_json_header(coupon_creado)
    assert_respuesta_json_header(respuesta)


@pytest.mark.functional
def test_POSTPMCD009_medir_tiempo_respuesta(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD009_medir_tiempo_respuesta")
    respuesta = crear_codigo_promocional_medir_tiempo_respuesta(coupon_id)
    assert_tiempo_respuesta(respuesta, max_ms=2000)


@pytest.mark.functional
def test_POSTPMCD010_crear_codigo_promocional_con_limite_uso(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD010_crear_codigo_promocional_con_limite_uso")
    respuesta = crear_codigo_promocional_limite_uso(1,coupon_id)
    assert_limite_uso(respuesta)


@pytest.mark.functional
def test_POSTPMCD011_validar_coupon_existente(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD011_validar_coupon_existente")
    respuesta = crear_codigo_promocional_coupon_existente(coupon_id)
    assert_coupon_existente(respuesta)


@pytest.mark.functional
def test_POSTPMCD012_crear_codigo_promocional_active_invalido(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD012_crear_codigo_promocional_active_invalido")
    respuesta = crear_codigo_promocional_active_invalido(coupon_id)
    assert_valor_invalido(respuesta)


@pytest.mark.functional
def test_POSTPMCD013_crear_codigo_promocional_code_case_sensitive(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD013_crear_codigo_promocional_code_case_sensitive")
    respuesta = crear_codigo_promocional_code_case_sensitive(coupon_id)
    assert_code_unico_case_sensitive(respuesta)


@pytest.mark.functional
def test_POSTPMCD014_crear_codigo_promocional_permisos_restringidos(coupon_creado):
    coupon_id = coupon_creado
    logger.info("Iniciando test_POSTPMCD014_crear_codigo_promocional_permisos_restringidos")
    respuesta = crear_codigo_promocional_permisos_restringidos(coupon_id)
    assert_permisos_restringidos(respuesta)
