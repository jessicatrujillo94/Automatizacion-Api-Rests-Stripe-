import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.eliminar_coupon_api import (
    eliminar_cupon_existente,
    eliminar_cupon_inexistente,
    eliminar_cupon_sin_token,
    eliminar_cupon_token_invalido,
    eliminar_cupon_ya_eliminado,
    verificar_cupon_eliminado_en_listado,
)
from src.assertions.eliminar_coupon_assertion import (
    assert_eliminacion_exitosa,
    assert_eliminacion_inexistente,
    assert_eliminacion_sin_token,
    assert_eliminacion_token_invalido,
    assert_eliminacion_ya_eliminado,
    assert_eliminacion_reflejada_en_listado,
)

@allure.epic("EPIC: Gestión de Coupons")
@allure.feature("Feature: Eliminar Coupons")
@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.smoke
@pytest.mark.functional
def test_CPNDEL001_eliminar_cupon_existente(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "coupon")
    logger.info("Iniciando test_CPNDEL001_eliminar_cupon_existente")
    respuesta = eliminar_cupon_existente(coupon_creado)
    assert_eliminacion_exitosa(respuesta)

@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNDEL002_eliminar_cupon_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNDEL002_eliminar_cupon_inexistente")
    respuesta = eliminar_cupon_inexistente()
    assert_eliminacion_inexistente(respuesta)

@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNDEL003_eliminar_cupon_sin_token(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNDEL003_eliminar_cupon_sin_token")
    respuesta = eliminar_cupon_sin_token(coupon_creado)
    assert_eliminacion_sin_token(respuesta)

@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNDEL004_eliminar_cupon_token_invalido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNDEL004_eliminar_cupon_token_invalido")
    respuesta = eliminar_cupon_token_invalido(coupon_creado)
    assert_eliminacion_token_invalido(respuesta)

@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.functional
def test_CPNDEL005_eliminar_cupon_ya_eliminado(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNDEL005_eliminar_cupon_ya_eliminado")
    respuesta = eliminar_cupon_ya_eliminado(coupon_creado)
    assert_eliminacion_ya_eliminado(respuesta)

@allure.story("HU: HU005-Eliminar Coupons")
@pytest.mark.functional
def test_CPNDEL006_verificar_eliminacion_reflejada_en_listado(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNDEL006_verificar_eliminacion_reflejada_en_listado")
    respuesta = verificar_cupon_eliminado_en_listado(coupon_creado)
    assert_eliminacion_reflejada_en_listado(respuesta, coupon_creado.json().get("id"))
