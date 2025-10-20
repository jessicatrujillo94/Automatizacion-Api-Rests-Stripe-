import pytest
from dotenv import load_dotenv
from src.logs.logger import logger
from src.stripe_api.crear_products_api import (
    crear_producto_campos_minimos,
    crear_producto_todos_campos,
    crear_producto_sin_token,
    crear_producto_token_invalido,
    crear_producto_permisos_insuficientes,
    crear_producto_sin_nombre,
    crear_producto_nombre_vacio,
    crear_producto_nombre_caracteres_especiales,
    crear_producto_respuesta_estructura,
    crear_multiples_productos,
    crear_producto_nombre_largo,
    crear_producto_metadata_compleja,
    crear_producto_inactivo,
    crear_producto_body_invalido,
    crear_producto_campos_adicionales,
    eliminar_producto
)
from src.assertions.crear_product_assertion import (
    assert_creacion_exitosa,
    assert_creacion_fallida,
    assert_creacion_sin_token,
    assert_creacion_token_invalido,
    assert_creacion_permisos_insuficientes,
    assert_creacion_sin_campo_obligatorio,
    assert_creacion_nombre_vacio,
    assert_creacion_caracteres_especiales,
    assert_estructura_respuesta_producto,
    assert_creacion_multiple,
    assert_creacion_nombre_largo,
    assert_creacion_metadata_compleja,
    assert_creacion_inactivo,
    assert_creacion_body_invalido,
    assert_creacion_campos_no_soportados,
)

load_dotenv()

@pytest.mark.functional
def test_PRD001_crear_producto_campos_minimos_validos():
    logger.info("Iniciando test_PRD001_crear_producto_campos_minimos_validos")
    respuesta = crear_producto_campos_minimos()
    try:
        assert_creacion_exitosa(respuesta)
        assert_estructura_respuesta_producto(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD002_crear_producto_todos_campos_opcionales():
    logger.info("Iniciando test_PRD002_crear_producto_todos_campos_opcionales")
    respuesta = crear_producto_todos_campos()
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD003_crear_producto_sin_token():
    logger.info("Iniciando test_PRD003_crear_producto_sin_token")
    respuesta = crear_producto_sin_token()
    assert_creacion_sin_token(respuesta)


@pytest.mark.functional
def test_PRD004_crear_producto_token_invalido():
    logger.info("Iniciando test_PRD004_crear_producto_token_invalido")
    respuesta = crear_producto_token_invalido()
    assert_creacion_token_invalido(respuesta)


@pytest.mark.functional
def test_PRD005_crear_producto_permisos_insuficientes():
    logger.info("Iniciando test_PRD005_crear_producto_permisos_insuficientes")
    respuesta = crear_producto_permisos_insuficientes()
    assert_creacion_permisos_insuficientes(respuesta)


@pytest.mark.functional
def test_PRD006_crear_producto_sin_campo_obligatorio_name():
    logger.info("Iniciando test_PRD006_crear_producto_sin_campo_obligatorio_name")
    respuesta = crear_producto_sin_nombre()
    assert_creacion_sin_campo_obligatorio(respuesta)


@pytest.mark.functional
def test_PRD007_crear_producto_nombre_vacio():
    logger.info("Iniciando test_PRD007_crear_producto_nombre_vacio")
    respuesta = crear_producto_nombre_vacio()
    assert_creacion_nombre_vacio(respuesta)


@pytest.mark.functional
def test_PRD008_crear_producto_nombre_caracteres_especiales():
    logger.info("Iniciando test_PRD008_crear_producto_nombre_caracteres_especiales")
    respuesta = crear_producto_nombre_caracteres_especiales()
    try:
        assert_creacion_caracteres_especiales(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.regression
def test_PRD009_validar_estructura_respuesta_producto():
    logger.info("Iniciando test_PRD009_validar_estructura_respuesta_producto")
    respuesta = crear_producto_respuesta_estructura()
    try:
        assert_estructura_respuesta_producto(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD010_crear_multiples_productos_consecutivamente():
    logger.info("Iniciando test_PRD010_crear_multiples_productos_consecutivamente")
    respuestas = crear_multiples_productos()
    try:
        assert_creacion_multiple(respuestas)
    finally:
        for r in respuestas:
            eliminar_producto(r)


@pytest.mark.functional
def test_PRD011_crear_producto_nombre_largo():
    logger.info("Iniciando test_PRD011_crear_producto_nombre_largo")
    respuesta = crear_producto_nombre_largo()
    try:
        assert_creacion_nombre_largo(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD012_crear_producto_metadata_compleja():
    logger.info("Iniciando test_PRD012_crear_producto_metadata_compleja")
    respuesta = crear_producto_metadata_compleja()
    try:
        assert_creacion_metadata_compleja(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD013_crear_producto_inactivo():
    logger.info("Iniciando test_PRD013_crear_producto_inactivo")
    respuesta = crear_producto_inactivo()
    try:
        assert_creacion_inactivo(respuesta)
    finally:
        eliminar_producto(respuesta)


@pytest.mark.functional
def test_PRD014_crear_producto_body_invalido():
    logger.info("Iniciando test_PRD014_crear_producto_body_invalido")
    respuesta = crear_producto_body_invalido()
    assert_creacion_body_invalido(respuesta)


@pytest.mark.functional
def test_PRD015_crear_producto_campos_adicionales_no_soportados():
    logger.info("Iniciando test_PRD015_crear_producto_campos_adicionales_no_soportados")
    respuesta = crear_producto_campos_adicionales()
    try:
        assert_creacion_campos_no_soportados(respuesta)
    finally:
        eliminar_producto(respuesta)
