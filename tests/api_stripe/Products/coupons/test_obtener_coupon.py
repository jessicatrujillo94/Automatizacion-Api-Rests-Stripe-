import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.obtener_cupon_api import (
    obtener_cupon_valido,
    obtener_cupon_inexistente,
    obtener_cupon_sin_token,
    obtener_cupon_token_invalido,
    obtener_cupon_id_vacio,
    obtener_cupon_formato_invalido,
    obtener_cupon_validar_estructura,
    obtener_cupon_valido_true,
    obtener_cupon_valido_false,
    obtener_cupon_validar_duration,
    obtener_cupon_validar_descuento,
    obtener_cupon_sin_permisos,
)
from src.assertions.obtener_coupon_assertion import (
    assert_obtener_cupon_valido,
    assert_obtener_cupon_inexistente,
    assert_obtener_cupon_sin_token,
    assert_obtener_cupon_token_invalido,
    assert_obtener_cupon_id_vacio,
    assert_obtener_cupon_formato_invalido,
    assert_obtener_cupon_validar_estructura,
    assert_obtener_cupon_valido_true,
    assert_obtener_cupon_valido_false,
    assert_obtener_cupon_validar_duration,
    assert_obtener_cupon_validar_descuento,
    assert_obtener_cupon_sin_permisos,
)

@allure.epic("EPIC: Gestión de Coupons")
@allure.feature("Feature: Obtener Coupons")
@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.smoke
@pytest.mark.functional
def test_CPNGET001_obtener_cupon_valido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "coupon")
    logger.info("Iniciando test_CPNGET001_obtener_cupon_valido")
    response = obtener_cupon_valido(coupon_creado)
    assert_obtener_cupon_valido(response)
    assert_obtener_cupon_validar_estructura(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET002_obtener_cupon_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET002_obtener_cupon_inexistente")
    response = obtener_cupon_inexistente()
    assert_obtener_cupon_inexistente(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET003_obtener_cupon_sin_token(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET003_obtener_cupon_sin_token")
    response = obtener_cupon_sin_token(coupon_creado)
    assert_obtener_cupon_sin_token(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET004_obtener_cupon_token_invalido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET004_obtener_cupon_token_invalido")
    response = obtener_cupon_token_invalido(coupon_creado)
    assert_obtener_cupon_token_invalido(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET005_obtener_cupon_id_vacio():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET005_obtener_cupon_id_vacio")
    response = obtener_cupon_id_vacio()
    assert_obtener_cupon_id_vacio(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET006_obtener_cupon_formato_invalido():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET006_obtener_cupon_formato_invalido")
    response = obtener_cupon_formato_invalido()
    assert_obtener_cupon_formato_invalido(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.regression
@pytest.mark.negative
def test_CPNGET007_validar_estructura_respuesta(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET007_validar_estructura_respuesta")
    response = obtener_cupon_validar_estructura(coupon_creado)
    assert_obtener_cupon_validar_estructura(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
def test_CPNGET008_verificar_valid_true(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNGET008_verificar_valid_true")
    response = obtener_cupon_valido_true(coupon_creado)
    assert_obtener_cupon_valido_true(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
def test_CPNGET009_verificar_valid_false(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNGET009_verificar_valid_false")
    response = obtener_cupon_valido_false(coupon_creado)
    assert_obtener_cupon_valido_false(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.regression
def test_CPNGET010_validar_duration(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "coupon")
    logger.info("Iniciando test_CPNGET010_validar_duration")
    response = obtener_cupon_validar_duration(coupon_creado)
    assert_obtener_cupon_validar_duration(response, "once")

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.regression
def test_CPNGET011_validar_descuento(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "coupon")
    logger.info("Iniciando test_CPNGET011_validar_descuento")
    response = obtener_cupon_validar_descuento(coupon_creado)
    assert_obtener_cupon_validar_descuento(response)

@allure.story("HU: HU007-Obtener Coupon")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNGET012_obtener_cupon_sin_permisos(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNGET012_obtener_cupon_sin_permisos")
    response = obtener_cupon_sin_permisos(coupon_creado)
    assert_obtener_cupon_sin_permisos(response)
