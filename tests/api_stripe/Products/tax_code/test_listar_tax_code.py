import pytest
from src.logs.logger import logger
from src.stripe_api.listar_tax_codes_api import (
    listar_tax_codes,
    listar_tax_codes_sin_token,
    listar_tax_codes_token_invalido,
    listar_tax_codes_filtrar_jurisdiccion,
    listar_tax_codes_limit,
    listar_tax_codes_starting_after,
    listar_tax_codes_vacio,
    listar_tax_codes_filtro_invalido,
    listar_tax_codes_sin_permisos,
)
from src.assertions.listar_tax_codes_assertion import (
    assert_listado_exitosa,
    assert_listado_sin_token,
    assert_listado_token_invalido,
    assert_estructura_respuesta_listado,
    assert_elementos_tax_code,
    assert_listado_vacio,
    assert_filtro_invalido,
    assert_formato_json,
    assert_jurisdiccion_coherente,
    assert_listado_sin_permisos,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_TAXL001_listar_tax_codes_token_valido():
    logger.info("Iniciando test_TAXL001_listar_tax_codes_token_valido")
    respuesta = listar_tax_codes()
    assert_listado_exitosa(respuesta)
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_code(respuesta)

@pytest.mark.functional
def test_TAXL002_listar_tax_codes_sin_token():
    logger.info("Iniciando test_TAXL002_listar_tax_codes_sin_token")
    respuesta = listar_tax_codes_sin_token()
    assert_listado_sin_token(respuesta)

@pytest.mark.functional
def test_TAXL003_listar_tax_codes_token_invalido():
    logger.info("Iniciando test_TAXL003_listar_tax_codes_token_invalido")
    respuesta = listar_tax_codes_token_invalido()
    assert_listado_token_invalido(respuesta)

@pytest.mark.regression
def test_TAXL004_validar_estructura_respuesta():
    logger.info("Iniciando test_TAXL004_validar_estructura_respuesta")
    respuesta = listar_tax_codes()
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_tax_code(respuesta)

@pytest.mark.regression
def test_TAXL005_validar_elementos_data():
    logger.info("Iniciando test_TAXL005_validar_elementos_data")
    respuesta = listar_tax_codes()
    assert_elementos_tax_code(respuesta)

@pytest.mark.functional
def test_TAXL006_listar_filtrando_por_jurisdiccion():
    logger.info("Iniciando test_TAXL006_listar_filtrando_por_jurisdiccion")
    respuesta = listar_tax_codes_filtrar_jurisdiccion("US")
    assert_listado_exitosa(respuesta)
    assert_jurisdiccion_coherente(respuesta, "US")

@pytest.mark.functional
def test_TAXL007_listar_tax_codes_limit_1():
    logger.info("Iniciando test_TAXL007_listar_tax_codes_limit_1")
    respuesta = listar_tax_codes_limit(1)
    assert_listado_exitosa(respuesta)
    assert len(respuesta.json().get("data", [])) <= 1

@pytest.mark.functional
def test_TAXL009_listar_tax_codes_starting_after():
    logger.info("Iniciando test_TAXL009_listar_tax_codes_starting_after")
    respuesta = listar_tax_codes_starting_after("txcd_99999999")
    assert_listado_exitosa(respuesta)

@pytest.mark.functional
def test_TAXL010_listar_tax_codes_vacio():
    logger.info("Iniciando test_TAXL010_listar_tax_codes_vacio")
    respuesta = listar_tax_codes_vacio()
    assert_listado_vacio(respuesta)

@pytest.mark.functional
def test_TAXL011_filtro_invalido_limit_negativo():
    logger.info("Iniciando test_TAXL011_filtro_invalido_limit_negativo")
    respuesta = listar_tax_codes_filtro_invalido(-5)
    assert_filtro_invalido(respuesta)

@pytest.mark.functional
def test_TAXL012_listar_tax_codes_sin_permisos():
    logger.info("Iniciando test_TAXL012_listar_tax_codes_sin_permisos")
    respuesta = listar_tax_codes_sin_permisos()
    assert_listado_sin_permisos(respuesta)

@pytest.mark.regression
def test_TAXL013_validar_formato_json():
    logger.info("Iniciando test_TAXL013_validar_formato_json")
    respuesta = listar_tax_codes()
    assert_formato_json(respuesta)

@pytest.mark.regression
def test_TAXL014_validar_nombre_descripcion_coherentes_con_jurisdiccion():
    logger.info("Iniciando test_TAXL014_validar_nombre_descripcion_coherentes_con_jurisdiccion")
    respuesta = listar_tax_codes()
    assert_jurisdiccion_coherente(respuesta)
