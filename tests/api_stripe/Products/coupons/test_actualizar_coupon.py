import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.actualizar_coupon_api import (
    actualizar_cupon_valido,
    actualizar_cupon_inexistente,
    actualizar_cupon_sin_token,
    actualizar_cupon_token_invalido,
    actualizar_cupon_campo_invalido,
    actualizar_cupon_nombre_caracteres_especiales,
    actualizar_cupon_metadata_compleja,
    actualizar_cupon_desactivar,
    actualizar_cupon_percent_off_alto,
    actualizar_cupon_body_vacio,
    actualizar_cupon_campos_no_soportados,
    actualizar_cupon_validar_estructura,
    actualizar_cupon_sin_permisos,
)
from src.assertions.actualizar_coupon_assertion import (
    assert_actualizacion_exitosa,
    assert_actualizacion_fallida,
    assert_actualizacion_sin_token,
    assert_actualizacion_token_invalido,
    assert_actualizacion_cupon_inexistente,
    assert_actualizacion_campo_invalido,
    assert_actualizacion_nombre_caracteres_especiales,
    assert_actualizacion_metadata_compleja,
    assert_actualizacion_desactivado,
    assert_actualizacion_body_invalido,
    assert_actualizacion_campos_no_soportados,
    assert_estructura_respuesta_actualizacion,
    assert_actualizacion_sin_permisos,
)

@allure.epic("EPIC: Gestión de Coupons")
@allure.feature("Feature: Actualizar Coupons")
@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.smoke
@pytest.mark.functional
def test_CPNUP001_actualizar_cupon_valido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "coupon")
    logger.info("Iniciando test_CPNUP001_actualizar_cupon_valido")
    respuesta = actualizar_cupon_valido(coupon_creado)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP002_actualizar_cupon_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP002_actualizar_cupon_inexistente")
    respuesta = actualizar_cupon_inexistente()
    assert_actualizacion_cupon_inexistente(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP003_actualizar_cupon_sin_token(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP003_actualizar_cupon_sin_token")
    respuesta = actualizar_cupon_sin_token(coupon_creado)
    assert_actualizacion_sin_token(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP004_actualizar_cupon_token_invalido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP004_actualizar_cupon_token_invalido")
    respuesta = actualizar_cupon_token_invalido(coupon_creado)
    assert_actualizacion_token_invalido(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP005_actualizar_cupon_campo_invalido(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP005_actualizar_cupon_campo_invalido")
    respuesta = actualizar_cupon_campo_invalido(coupon_creado)
    assert_actualizacion_campo_invalido(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
def test_CPNUP006_actualizar_nombre_caracteres_especiales(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNUP006_actualizar_nombre_caracteres_especiales")
    respuesta = actualizar_cupon_nombre_caracteres_especiales(coupon_creado)
    assert_actualizacion_nombre_caracteres_especiales(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
def test_CPNUP007_actualizar_metadata_compleja(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNUP007_actualizar_metadata_compleja")
    respuesta = actualizar_cupon_metadata_compleja(coupon_creado)
    assert_actualizacion_metadata_compleja(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
def test_CPNUP008_desactivar_cupon(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "coupon")
    logger.info("Iniciando test_CPNUP008_desactivar_cupon")
    respuesta = actualizar_cupon_desactivar(coupon_creado)
    assert_actualizacion_desactivado(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP009_percent_off_superior_a_100(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP009_percent_off_superior_a_100")
    respuesta = actualizar_cupon_percent_off_alto(coupon_creado)
    assert_actualizacion_fallida(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP010_actualizar_cupon_body_vacio(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP010_actualizar_cupon_body_vacio")
    respuesta = actualizar_cupon_body_vacio(coupon_creado)
    assert_actualizacion_body_invalido(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP011_actualizar_cupon_campos_no_soportados(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP011_actualizar_cupon_campos_no_soportados")
    respuesta = actualizar_cupon_campos_no_soportados(coupon_creado)
    assert_actualizacion_campos_no_soportados(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.regression
def test_CPNUP012_validar_estructura_respuesta_actualizacion(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "coupon")
    logger.info("Iniciando test_CPNUP012_validar_estructura_respuesta_actualizacion")
    respuesta = actualizar_cupon_validar_estructura(coupon_creado)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU004-Actualizar Coupons")
@pytest.mark.functional
@pytest.mark.negative
def test_CPNUP014_actualizar_cupon_sin_permisos(coupon_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "coupon")
    logger.info("Iniciando test_CPNUP014_actualizar_cupon_sin_permisos")
    respuesta = actualizar_cupon_sin_permisos(coupon_creado)
    assert_actualizacion_sin_permisos(respuesta)
