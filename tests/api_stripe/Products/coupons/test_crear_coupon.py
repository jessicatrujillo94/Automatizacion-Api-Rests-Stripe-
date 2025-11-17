import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.crear_coupons_api import (
    crear_cupon_valido,
    crear_cupon_sin_duration,
    crear_cupon_percent_off_negativo,
    crear_cupon_token_invalido,
    crear_cupon_sin_token,
    crear_cupon_campos_validos,
    crear_cupon_validar_estructura_respuesta,
    crear_cupon_con_amount_off,
    crear_cupon_duration_repeating,
    crear_cupon_duration_once,
    crear_cupon_percent_off_cero,
    crear_cupon_caracteres_especiales_id,
    crear_cupon_redeem_by_pasado,
    crear_cupon_campo_no_soportado,
    crear_cupon_multiples_consecutivos,
    crear_cupon_con_metadata,
    crear_cupon_body_vacio,
    crear_cupon_con_currency_y_amount_off,
    crear_cupon_token_expirado,
    crear_cupon_sin_permisos,
    eliminar_cupon
)
from src.assertions.crear_coupon_assertion import (
    assert_creacion_exitosa,
    assert_creacion_fallida,
    assert_creacion_sin_token,
    assert_creacion_token_invalido,
    assert_creacion_sin_permisos,
    assert_campos_cupon_validos,
    assert_tipos_datos_cupon,
    assert_estructura_body_cupon,
    assert_content_type_json,
    assert_estructura_error_json,
)

@allure.epic("EPIC: Gestión de Coupons")
@allure.feature("Feature: Crear Coupons")
@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN001_crear_cupon_datos_validos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN001_crear_cupon_datos_validos")
    respuesta = crear_cupon_valido()
    try:
        assert_creacion_exitosa(respuesta)
        assert_campos_cupon_validos(respuesta)
        assert_tipos_datos_cupon(respuesta)
        assert_content_type_json(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN002_crear_cupon_sin_duration():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN002_crear_cupon_sin_duration")
    respuesta = crear_cupon_sin_duration()
    try:
        assert_creacion_fallida(respuesta)
        assert_estructura_error_json(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN003_crear_cupon_percent_off_negativo():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN003_crear_cupon_percent_off_negativo")
    respuesta = crear_cupon_percent_off_negativo()
    try:
        assert_creacion_fallida(respuesta)
        assert_estructura_error_json(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN004_crear_cupon_token_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN004_crear_cupon_token_invalido")
    respuesta = crear_cupon_token_invalido()
    assert_creacion_token_invalido(respuesta)
    assert_estructura_error_json(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN005_crear_cupon_sin_token():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN005_crear_cupon_sin_token")
    respuesta = crear_cupon_sin_token()
    assert_creacion_sin_token(respuesta)
    assert_estructura_error_json(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN006_crear_cupon_campos_validos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN006_crear_cupon_campos_validos")
    respuesta = crear_cupon_campos_validos()
    try:
        assert_creacion_exitosa(respuesta)
        assert_campos_cupon_validos(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.regression
def test_POSTCPN007_validar_estructura_respuesta_cupon():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "coupon")
    logger.info("Iniciando test_POSTCPN007_validar_estructura_respuesta_cupon")
    respuesta = crear_cupon_validar_estructura_respuesta()
    try:
        assert_estructura_body_cupon(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN008_crear_cupon_con_amount_off():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN008_crear_cupon_con_amount_off")
    respuesta = crear_cupon_con_amount_off()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN009_crear_cupon_duration_repeating():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN009_crear_cupon_duration_repeating")
    respuesta = crear_cupon_duration_repeating()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN010_crear_cupon_duration_once_valor_limite():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN010_crear_cupon_duration_once_valor_limite")
    respuesta = crear_cupon_duration_once()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN011_crear_cupon_percent_off_cero():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN011_crear_cupon_percent_off_cero")
    respuesta = crear_cupon_percent_off_cero()
    try:
        assert_creacion_fallida(respuesta)
        assert_estructura_error_json(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN012_crear_cupon_caracteres_especiales_id():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN012_crear_cupon_caracteres_especiales_id")
    respuesta = crear_cupon_caracteres_especiales_id()
    try:
        assert_creacion_fallida(respuesta)
        assert_estructura_error_json(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN013_crear_cupon_redeem_by_pasado():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN013_crear_cupon_redeem_by_pasado")
    respuesta = crear_cupon_redeem_by_pasado()
    try:
        assert_creacion_fallida(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN014_crear_cupon_campo_no_soportado():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN014_crear_cupon_campo_no_soportado")
    respuesta = crear_cupon_campo_no_soportado()
    try:
        assert_creacion_fallida(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN015_crear_multiples_cupones_consecutivos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN015_crear_multiples_cupones_consecutivos")
    respuestas = crear_cupon_multiples_consecutivos()
    try:
        for r in respuestas:
            assert_creacion_exitosa(r)
    finally:
        for r in respuestas:
            eliminar_cupon(r)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN016_crear_cupon_con_metadata_compleja():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN016_crear_cupon_con_metadata_compleja")
    respuesta = crear_cupon_con_metadata()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN017_crear_cupon_body_vacio():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN017_crear_cupon_body_vacio")
    respuesta = crear_cupon_body_vacio()
    assert_creacion_fallida(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
def test_POSTCPN018_crear_cupon_con_currency_y_amount_off():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_POSTCPN018_crear_cupon_con_currency_y_amount_off")
    respuesta = crear_cupon_con_currency_y_amount_off()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_cupon(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN019_crear_cupon_token_expirado():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN019_crear_cupon_token_expirado")
    respuesta = crear_cupon_token_expirado()
    assert_creacion_token_invalido(respuesta)

@allure.story("HU: HU003-Crear Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_POSTCPN020_crear_cupon_sin_permisos():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_POSTCPN020_crear_cupon_sin_permisos")
    respuesta = crear_cupon_sin_permisos()
    assert_creacion_sin_permisos(respuesta)
