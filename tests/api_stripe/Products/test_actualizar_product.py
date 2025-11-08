import pytest
import allure
from src.logs.logger import logger
from src.stripe_api.actualizar_product_api import (
    actualizar_nombre_producto,
    actualizar_varios_campos_producto,
    actualizar_metadata_producto,
    actualizar_producto_token_invalido,
    actualizar_producto_sin_permisos,
    actualizar_producto_id_inexistente,
    actualizar_producto_nombre_vacio,
    actualizar_producto_nombre_caracteres_especiales,
    actualizar_producto_inactivo,
    actualizar_producto_body_invalido,
    actualizar_producto_campos_no_soportados,
    actualizar_producto_sin_body,
    actualizar_producto_validar_estructura,
)
from src.assertions.actualizar_product_assertion import (
    assert_actualizacion_exitosa,
    assert_actualizacion_fallida,
    assert_actualizacion_token_invalido,
    assert_actualizacion_sin_permisos,
    assert_actualizacion_id_inexistente,
    assert_actualizacion_nombre_vacio,
    assert_actualizacion_caracteres_especiales,
    assert_actualizacion_inactivo,
    assert_actualizacion_body_invalido,
    assert_actualizacion_campos_no_soportados,
    assert_actualizacion_sin_body,
    assert_estructura_respuesta_actualizacion,
)

@allure.epic("EPIC: Gestión de Productos")
@allure.feature("Feature: Actualizar Productos")
@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.smoke
@pytest.mark.functional
def test_PRAC001_actualizar_nombre_producto_existente(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("smoke", "functional", "api", "product")
    logger.info("Iniciando test_PRAC001_actualizar_nombre_producto_existente")
    respuesta = actualizar_nombre_producto(producto_creado)
    assert_actualizacion_exitosa(respuesta)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
def test_PRAC002_actualizar_varios_campos_producto(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    logger.info("Iniciando test_PRAC002_actualizar_varios_campos_producto")
    respuesta = actualizar_varios_campos_producto(producto_creado)
    assert_actualizacion_exitosa(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
def test_PRAC003_actualizar_metadata_producto(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    logger.info("Iniciando test_PRAC003_actualizar_metadata_producto")
    respuesta = actualizar_metadata_producto(producto_creado)
    assert_actualizacion_exitosa(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC004_actualizar_producto_token_invalido(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC004_actualizar_producto_token_invalido")
    respuesta = actualizar_producto_token_invalido(producto_creado)
    assert_actualizacion_token_invalido(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC005_actualizar_producto_sin_permisos(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC005_actualizar_producto_sin_permisos")
    respuesta = actualizar_producto_sin_permisos(producto_creado)
    assert_actualizacion_sin_permisos(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC006_actualizar_producto_id_inexistente():
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC006_actualizar_producto_id_inexistente")
    respuesta = actualizar_producto_id_inexistente()
    assert_actualizacion_id_inexistente(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC007_actualizar_producto_nombre_vacio(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC007_actualizar_producto_nombre_vacio")
    respuesta = actualizar_producto_nombre_vacio(producto_creado)
    assert_actualizacion_nombre_vacio(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
def test_PRAC008_actualizar_producto_nombre_caracteres_especiales(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    logger.info("Iniciando test_PRAC008_actualizar_producto_nombre_caracteres_especiales")
    respuesta = actualizar_producto_nombre_caracteres_especiales(producto_creado)
    assert_actualizacion_caracteres_especiales(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
def test_PRAC009_actualizar_producto_inactivo(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    logger.info("Iniciando test_PRAC009_actualizar_producto_inactivo")
    respuesta = actualizar_producto_inactivo(producto_creado)
    assert_actualizacion_inactivo(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC010_actualizar_producto_body_invalido(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC010_actualizar_producto_body_invalido")
    respuesta = actualizar_producto_body_invalido(producto_creado)
    assert_actualizacion_body_invalido(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
@pytest.mark.negative
def test_PRAC011_actualizar_producto_campos_no_soportados(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "negative", "api", "product")
    logger.info("Iniciando test_PRAC011_actualizar_producto_campos_no_soportados")
    respuesta = actualizar_producto_campos_no_soportados(producto_creado)
    assert_actualizacion_campos_no_soportados(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.regression
def test_PRAC012_validar_estructura_respuesta_actualizacion(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("regression", "api", "product")
    logger.info("Iniciando test_PRAC012_validar_estructura_respuesta_actualizacion")
    respuesta = actualizar_producto_validar_estructura(producto_creado)
    assert_estructura_respuesta_actualizacion(respuesta)

@allure.story("HU: HU003-Actualizar Productos")
@pytest.mark.functional
def test_PRAC013_actualizar_producto_sin_enviar_body(producto_creado):
    allure.dynamic.label("owner", "Jessica Trujillo")
    allure.dynamic.tag("functional", "api", "product")
    logger.info("Iniciando test_PRAC013_actualizar_producto_sin_enviar_body")
    respuesta = actualizar_producto_sin_body(producto_creado)
    assert_actualizacion_sin_body(respuesta)
