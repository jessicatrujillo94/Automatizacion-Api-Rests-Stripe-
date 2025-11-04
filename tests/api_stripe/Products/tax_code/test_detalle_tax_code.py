import pytest
from src.logs.logger import logger
from src.stripe_api.consultar_tax_code_api import (
    consultar_tax_code,
    consultar_tax_code_inexistente,
    consultar_tax_code_sin_token,
    consultar_tax_code_token_invalido,
    consultar_tax_code_id_vacio,
    consultar_tax_code_malformado,
    consultar_tax_code_id_corto,
    consultar_tax_code_id_largo,
    consultar_tax_code_case_sensitive,
)
from src.assertions.consultar_tax_code_assertion import (
    assert_consulta_exitosa,
    assert_consulta_id_inexistente,
    assert_consulta_sin_token,
    assert_consulta_token_invalido,
    assert_consulta_id_vacio,
    assert_estructura_respuesta_tax_code,
    assert_object_tax_code,
    assert_tipos_datos_tax_code,
    assert_error_404_coherente,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_TAXGET001_obtener_tax_code_existente(tax_code_valido):
    logger.info("Iniciando test_TAXGET001_obtener_tax_code_existente")
    respuesta = consultar_tax_code(tax_code_valido)
    assert_consulta_exitosa(respuesta)
    assert_estructura_respuesta_tax_code(respuesta)
    assert_object_tax_code(respuesta)
    assert_tipos_datos_tax_code(respuesta)

@pytest.mark.functional
def test_TAXGET002_obtener_tax_code_inexistente():
    logger.info("Iniciando test_TAXGET002_obtener_tax_code_inexistente")
    respuesta = consultar_tax_code_inexistente()
    assert_consulta_id_inexistente(respuesta)
    assert_error_404_coherente(respuesta)

@pytest.mark.functional
def test_TAXGET003_obtener_tax_code_sin_token(tax_code_valido):
    logger.info("Iniciando test_TAXGET003_obtener_tax_code_sin_token")
    respuesta = consultar_tax_code_sin_token(tax_code_valido)
    assert_consulta_sin_token(respuesta)

@pytest.mark.functional
def test_TAXGET004_obtener_tax_code_token_invalido(tax_code_valido):
    logger.info("Iniciando test_TAXGET004_obtener_tax_code_token_invalido")
    respuesta = consultar_tax_code_token_invalido(tax_code_valido)
    assert_consulta_token_invalido(respuesta)

@pytest.mark.functional
def test_TAXGET005_obtener_tax_code_id_vacio():
    logger.info("Iniciando test_TAXGET005_obtener_tax_code_id_vacio")
    respuesta = consultar_tax_code_id_vacio()
    assert_consulta_id_vacio(respuesta)

@pytest.mark.regression
def test_TAXGET006_validar_estructura_respuesta(tax_code_valido):
    logger.info("Iniciando test_TAXGET006_validar_estructura_respuesta")
    respuesta = consultar_tax_code(tax_code_valido)
    assert_estructura_respuesta_tax_code(respuesta)
    assert_object_tax_code(respuesta)
    assert_tipos_datos_tax_code(respuesta)

@pytest.mark.regression
def test_TAXGET007_validar_campo_object(tax_code_valido):
    logger.info("Iniciando test_TAXGET007_validar_campo_object")
    respuesta = consultar_tax_code(tax_code_valido)
    assert_object_tax_code(respuesta)

@pytest.mark.regression
def test_TAXGET008_validar_tipos_datos(tax_code_valido):
    logger.info("Iniciando test_TAXGET008_validar_tipos_datos")
    respuesta = consultar_tax_code(tax_code_valido)
    assert_tipos_datos_tax_code(respuesta)

@pytest.mark.functional
def test_TAXGET010_id_malformado():
    logger.info("Iniciando test_TAXGET010_id_malformado")
    respuesta = consultar_tax_code_malformado()
    assert_consulta_id_inexistente(respuesta)

@pytest.mark.functional
def test_TAXGET011_id_corto():
    logger.info("Iniciando test_TAXGET011_id_corto")
    respuesta = consultar_tax_code_id_corto()
    assert_consulta_id_inexistente(respuesta)

@pytest.mark.functional
def test_TAXGET012_id_largo():
    logger.info("Iniciando test_TAXGET012_id_largo")
    respuesta = consultar_tax_code_id_largo()
    assert_consulta_id_inexistente(respuesta)

@pytest.mark.functional
def test_TAXGET013_validar_content_type(tax_code_valido):
    logger.info("Iniciando test_TAXGET013_validar_content_type")
    respuesta = consultar_tax_code(tax_code_valido)
    assert respuesta.headers["Content-Type"] == "application/json"

@pytest.mark.functional
def test_TAXGET014_mayusculas_minusculas_tax_code(tax_code_valido):
    logger.info("Iniciando test_TAXGET014_mayusculas_minusculas_tax_code")
    respuesta = consultar_tax_code_case_sensitive(tax_code_valido)
    assert_consulta_exitosa(respuesta)

@pytest.mark.functional
def test_TAXGET015_error_404_coherente():
    logger.info("Iniciando test_TAXGET015_error_404_coherente")
    respuesta = consultar_tax_code_inexistente()
    assert_error_404_coherente(respuesta)
