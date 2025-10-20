import pytest
from src.logs.logger import logger
from src.stripe_api.eliminar_product_api import (
    eliminar_producto_existente,
    eliminar_producto_inexistente,
    eliminar_producto_sin_token,
    eliminar_producto_token_invalido,
    eliminar_producto_sin_permisos,
    eliminar_producto_id_vacio,
    eliminar_producto_id_malformado,
    eliminar_producto_validar_estructura,
    eliminar_producto_ya_eliminado,
    eliminar_multiples_productos,
)
from src.stripe_api.crear_products_api import crear_multiples_productos
from src.assertions.eliminar_product_assertion import (
    assert_eliminacion_exitosa,
    assert_eliminacion_fallida,
    assert_eliminacion_token_invalido,
    assert_eliminacion_sin_permisos,
    assert_eliminacion_id_inexistente,
    assert_eliminacion_id_vacio,
    assert_eliminacion_id_malformado,
    assert_estructura_respuesta_eliminacion,
    assert_eliminacion_previamente,
    assert_eliminacion_multiple,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_ELIM001_eliminar_producto_existente(producto_creado):
    logger.info("Iniciando test_ELIM001_eliminar_producto_existente")
    respuesta = eliminar_producto_existente(producto_creado)
    assert_eliminacion_exitosa(respuesta)


@pytest.mark.functional
def test_ELIM002_eliminar_producto_inexistente():
    logger.info("Iniciando test_ELIM002_eliminar_producto_inexistente")
    respuesta = eliminar_producto_inexistente()
    assert_eliminacion_id_inexistente(respuesta)


@pytest.mark.functional
def test_ELIM003_eliminar_producto_sin_token(producto_creado):
    logger.info("Iniciando test_ELIM003_eliminar_producto_sin_token")
    respuesta = eliminar_producto_sin_token(producto_creado)
    assert_eliminacion_sin_permisos(respuesta)


@pytest.mark.functional
def test_ELIM004_eliminar_producto_token_invalido(producto_creado):
    logger.info("Iniciando test_ELIM004_eliminar_producto_token_invalido")
    respuesta = eliminar_producto_token_invalido(producto_creado)
    assert_eliminacion_token_invalido(respuesta)


@pytest.mark.functional
def test_ELIM005_eliminar_producto_sin_permisos(producto_creado):
    logger.info("Iniciando test_ELIM005_eliminar_producto_sin_permisos")
    respuesta = eliminar_producto_sin_permisos(producto_creado)
    assert_eliminacion_sin_permisos(respuesta)


@pytest.mark.functional
def test_ELIM006_eliminar_producto_id_vacio():
    logger.info("Iniciando test_ELIM006_eliminar_producto_id_vacio")
    respuesta = eliminar_producto_id_vacio()
    assert_eliminacion_id_vacio(respuesta)


@pytest.mark.functional
def test_ELIM007_eliminar_producto_id_malformado():
    logger.info("Iniciando test_ELIM007_eliminar_producto_id_malformado")
    respuesta = eliminar_producto_id_malformado()
    assert_eliminacion_id_malformado(respuesta)


@pytest.mark.regression
def test_ELIM008_validar_estructura_respuesta_eliminacion(producto_creado):
    logger.info("Iniciando test_ELIM008_validar_estructura_respuesta_eliminacion")
    respuesta = eliminar_producto_validar_estructura(producto_creado)
    assert_estructura_respuesta_eliminacion(respuesta)


@pytest.mark.functional
def test_ELIM009_eliminar_producto_ya_eliminado(producto_creado):
    logger.info("Iniciando test_ELIM009_eliminar_producto_ya_eliminado")
    respuesta = eliminar_producto_ya_eliminado(producto_creado)
    assert_eliminacion_previamente(respuesta)


@pytest.mark.functional
def test_ELIM010_eliminar_multiples_productos_consecutivamente():
    logger.info("Iniciando test_ELIM010_eliminar_multiples_productos_consecutivamente")
    products = crear_multiples_productos()
    respuestas = eliminar_multiples_productos(products)
    assert_eliminacion_multiple(respuestas)
