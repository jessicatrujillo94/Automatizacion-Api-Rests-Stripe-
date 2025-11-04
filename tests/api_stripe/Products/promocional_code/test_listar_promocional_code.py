import pytest
from src.logs.logger import logger
from src.stripe_api.listar_promotion_codes_api import (
    listar_promotion_codes,
    listar_sin_token,
    listar_token_invalido,
    listar_active_true,
    listar_active_false,
    listar_permisos_restringidos,
)
from src.assertions.listar_promotion_codes_assertion import (
    assert_listado_exitosa,
    assert_listado_sin_token,
    assert_listado_token_invalido,
    assert_estructura_respuesta_listado,
    assert_elementos_data,
    assert_restrictions_usage_numeric,
)

@pytest.mark.smoke
@pytest.mark.functional
def test_PML001_listar_todos_codigos_token_valido():
    logger.info("Iniciando test_PML001_listar_todos_codigos_token_valido")
    respuesta = listar_promotion_codes()
    assert_listado_exitosa(respuesta)
    assert_estructura_respuesta_listado(respuesta)
    assert_elementos_data(respuesta)

@pytest.mark.functional
def test_PML002_listar_codigos_sin_token():
    logger.info("Iniciando test_PML002_listar_codigos_sin_token")
    respuesta = listar_sin_token()
    assert_listado_sin_token(respuesta)

@pytest.mark.functional
def test_PML003_listar_codigos_token_invalido():
    logger.info("Iniciando test_PML003_listar_codigos_token_invalido")
    respuesta = listar_token_invalido()
    assert_listado_token_invalido(respuesta)

@pytest.mark.regression
def test_PML004_validar_estructura_respuesta():
    logger.info("Iniciando test_PML004_validar_estructura_respuesta")
    respuesta = listar_promotion_codes()
    assert_estructura_respuesta_listado(respuesta)

@pytest.mark.regression
def test_PML005_validar_campos_elementos_data():
    logger.info("Iniciando test_PML005_validar_campos_elementos_data")
    respuesta = listar_promotion_codes()
    assert_elementos_data(respuesta)

@pytest.mark.functional
def test_PML006_listar_codigos_activos():
    logger.info("Iniciando test_PML006_listar_codigos_activos")
    respuesta = listar_active_true()
    assert_listado_exitosa(respuesta)
    for item in respuesta.json().get("data", []):
        assert item.get("active") is True

@pytest.mark.functional
def test_PML007_listar_codigos_inactivos():
    logger.info("Iniciando test_PML007_listar_codigos_inactivos")
    respuesta = listar_active_false()
    assert_listado_exitosa(respuesta)
    for item in respuesta.json().get("data", []):
        assert item.get("active") is False

@pytest.mark.functional
def test_PML008_validar_has_more_mas_de_10():
    logger.info("Iniciando test_PML008_validar_has_more_mas_de_10")
    respuesta = listar_promotion_codes()
    data_length = len(respuesta.json().get("data", []))
    has_more = respuesta.json().get("has_more")
    assert (data_length > 10 and has_more) or (data_length <= 10 and not has_more)

@pytest.mark.functional
def test_PML009_respuesta_vacia_cuando_no_existen_codigos():
    logger.info("Iniciando test_PML009_respuesta_vacia_cuando_no_existen_codigos")
    # Asumimos que limpiar_promos() elimina todos los promotion_codes de prueba
    from src.stripe_api.limpiar_promos_api import limpiar_promos
    limpiar_promos()
    respuesta = listar_promotion_codes()
    assert respuesta.json().get("data") == []

@pytest.mark.regression
def test_PML010_validar_restrictions_usage_limit_tipo():
    logger.info("Iniciando test_PML010_validar_restrictions_usage_limit_tipo")
    respuesta = listar_promotion_codes()
    assert_restrictions_usage_numeric(respuesta)

@pytest.mark.regression
def test_PML011_validar_tipo_objeto_en_data():
    logger.info("Iniciando test_PML011_validar_tipo_objeto_en_data")
    respuesta = listar_promotion_codes()
    for item in respuesta.json().get("data", []):
        assert item.get("object") == "promotion_code"

@pytest.mark.functional
def test_PML012_listar_codigos_permisos_restringidos():
    logger.info("Iniciando test_PML012_listar_codigos_permisos_restringidos")
    respuesta = listar_permisos_restringidos()
    assert_listado_sin_token(respuesta)
