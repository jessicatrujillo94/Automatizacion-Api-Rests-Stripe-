import pytest
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


@pytest.mark.functional
def test_CPNDEL001_eliminar_cupon_existente(coupon_creado):
    logger.info("Iniciando test_CPNDEL001_eliminar_cupon_existente")
    respuesta = eliminar_cupon_existente(coupon_creado)
    assert_eliminacion_exitosa(respuesta)


@pytest.mark.functional
def test_CPNDEL002_eliminar_cupon_inexistente():
    logger.info("Iniciando test_CPNDEL002_eliminar_cupon_inexistente")
    respuesta = eliminar_cupon_inexistente()
    assert_eliminacion_inexistente(respuesta)


@pytest.mark.functional
def test_CPNDEL003_eliminar_cupon_sin_token(coupon_creado):
    logger.info("Iniciando test_CPNDEL003_eliminar_cupon_sin_token")
    respuesta = eliminar_cupon_sin_token(coupon_creado)
    assert_eliminacion_sin_token(respuesta)


@pytest.mark.functional
def test_CPNDEL004_eliminar_cupon_token_invalido(coupon_creado):
    logger.info("Iniciando test_CPNDEL004_eliminar_cupon_token_invalido")
    respuesta = eliminar_cupon_token_invalido(coupon_creado)
    assert_eliminacion_token_invalido(respuesta)


@pytest.mark.functional
def test_CPNDEL005_eliminar_cupon_ya_eliminado(coupon_creado):
    logger.info("Iniciando test_CPNDEL005_eliminar_cupon_ya_eliminado")
    respuesta = eliminar_cupon_ya_eliminado(coupon_creado)
    assert_eliminacion_ya_eliminado(respuesta)


@pytest.mark.functional
def test_CPNDEL006_verificar_eliminacion_reflejada_en_listado(coupon_creado):
    logger.info("Iniciando test_CPNDEL006_verificar_eliminacion_reflejada_en_listado")
    respuesta = verificar_cupon_eliminado_en_listado(coupon_creado)
    print(respuesta.json())
    assert_eliminacion_reflejada_en_listado(respuesta,coupon_creado.json().get("id"))
