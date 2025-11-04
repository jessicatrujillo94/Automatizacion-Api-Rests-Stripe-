import pytest
from src.logs.logger import logger
from src.stripe_api.obtener_prices_api import (
    obtener_price_valido,
    obtener_price_inexistente,
    obtener_price_sin_token,
    obtener_price_token_invalido,
    obtener_price_vacio,
    obtener_price_formato_incorrecto,
    obtener_price_metodo_incorrecto,
    obtener_price_header_vacio,
    obtener_price_sin_permisos,
    obtener_price_validar_campos,
    obtener_price_validar_tipos_datos,
    obtener_price_validar_estructura_body,
    obtener_price_validar_producto_existente,
    obtener_price_validar_content_type,
    obtener_price_con_espacios,
    obtener_price_caracteres_especiales,
    obtener_price_validar_estructura_error
)
from src.assertions.obtener_price_assertion import (
    assert_consulta_exitosa,
    assert_consulta_fallida,
    assert_consulta_sin_token,
    assert_consulta_token_invalido,
    assert_consulta_header_vacio,
    assert_consulta_metodo_incorrecto,
    assert_consulta_sin_permisos,
    assert_campos_price_validos,
    assert_tipos_datos_price,
    assert_estructura_body_price,
    assert_producto_existente,
    assert_content_type_json,
    assert_estructura_error_json
)


@pytest.mark.functional
@pytest.mark.smoke
def test_GETP001_obtener_price_valido(one_price_id):
    logger.info("Iniciando test_GETP001_obtener_price_valido")
    price_id = one_price_id
    respuesta = obtener_price_valido(price_id)
    assert_consulta_exitosa(respuesta)
    assert_campos_price_validos(respuesta)


@pytest.mark.functional
def test_GETP002_obtener_price_inexistente():
    logger.info("Iniciando test_GETP002_obtener_price_inexistente")
    respuesta = obtener_price_inexistente()
    assert_consulta_fallida(respuesta)


@pytest.mark.functional
def test_GETP003_obtener_price_sin_token():
    logger.info("Iniciando test_GETP003_obtener_price_sin_token")
    respuesta = obtener_price_sin_token("price_valid_id")
    assert_consulta_sin_token(respuesta)


@pytest.mark.functional
def test_GETP004_obtener_price_token_invalido():
    logger.info("Iniciando test_GETP004_obtener_price_token_invalido")
    respuesta = obtener_price_token_invalido("price_valid_id")
    assert_consulta_token_invalido(respuesta)


@pytest.mark.functional
def test_GETP005_obtener_price_vacio():
    logger.info("Iniciando test_GETP005_obtener_price_vacio")
    respuesta = obtener_price_vacio()
    assert_consulta_fallida(respuesta)


@pytest.mark.functional
def test_GETP006_obtener_price_formato_incorrecto():
    logger.info("Iniciando test_GETP006_obtener_price_formato_incorrecto")
    respuesta = obtener_price_formato_incorrecto()
    assert_consulta_fallida(respuesta)


@pytest.mark.functional
def test_GETP007_obtener_price_metodo_incorrecto(one_price_id):
    logger.info("Iniciando test_GETP007_obtener_price_metodo_incorrecto")
    respuesta = obtener_price_metodo_incorrecto(one_price_id)
    assert_consulta_metodo_incorrecto(respuesta)


@pytest.mark.functional
def test_GETP008_obtener_price_header_autorizacion_vacio(one_price_id):
    logger.info("Iniciando test_GETP008_obtener_price_header_autorizacion_vacio")
    respuesta = obtener_price_header_vacio(one_price_id)
    assert_consulta_header_vacio(respuesta)


@pytest.mark.functional
def test_GETP009_obtener_price_sin_permisos(one_price_id):
    logger.info("Iniciando test_GETP009_obtener_price_sin_permisos")
    respuesta = obtener_price_sin_permisos(one_price_id)
    assert_consulta_sin_permisos(respuesta)


@pytest.mark.regression
def test_GETP010_validar_campos_en_respuesta(one_price_id):
    logger.info("Iniciando test_GETP010_validar_campos_en_respuesta")
    respuesta = obtener_price_validar_campos(one_price_id)
    assert_campos_price_validos(respuesta)


@pytest.mark.regression
def test_GETP011_validar_tipos_de_datos(one_price_id):
    logger.info("Iniciando test_GETP011_validar_tipos_de_datos")
    respuesta = obtener_price_validar_tipos_datos(one_price_id)
    assert_tipos_datos_price(respuesta)


@pytest.mark.regression
def test_GETP012_validar_estructura_body(one_price_id):
    logger.info("Iniciando test_GETP012_validar_estructura_body")
    respuesta = obtener_price_validar_estructura_body(one_price_id)
    assert_estructura_body_price(respuesta)


@pytest.mark.functional
def test_GETP013_validar_producto_existente(one_price_id):
    logger.info("Iniciando test_GETP013_validar_producto_existente")
    respuesta = obtener_price_validar_producto_existente(one_price_id)
    assert_producto_existente(respuesta)


@pytest.mark.regression
def test_GETP014_validar_content_type_json(one_price_id):
    logger.info("Iniciando test_GETP014_validar_content_type_json")
    respuesta = obtener_price_validar_content_type(one_price_id)
    assert_content_type_json(respuesta)


@pytest.mark.functional
def test_GETP015_obtener_price_con_espacios(one_price_id):
    logger.info("Iniciando test_GETP015_obtener_price_con_espacios")
    respuesta = obtener_price_con_espacios(f"   {one_price_id}")
    assert_consulta_fallida(respuesta)


@pytest.mark.functional
def test_GETP016_obtener_price_caracteres_especiales():
    logger.info("Iniciando test_GETP016_obtener_price_caracteres_especiales")
    respuesta = obtener_price_caracteres_especiales()
    assert_consulta_fallida(respuesta)


@pytest.mark.regression
def test_GETP017_validar_estructura_error_json():
    logger.info("Iniciando test_GETP017_validar_estructura_error_json")
    respuesta = obtener_price_validar_estructura_error()
    assert_estructura_error_json(respuesta)
