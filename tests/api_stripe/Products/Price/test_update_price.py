import pytest
from dotenv import load_dotenv
from src.logs.logger import logger
from src.stripe_api.actualizar_prices_api import (
    actualizar_price_nickname,
    actualizar_price_active_false,
    actualizar_price_metadata_simple,
    actualizar_price_multiples_campos,
    actualizar_price_id_invalido,
    actualizar_price_sin_token,
    actualizar_price_token_invalido,
    actualizar_price_header_vacio,
    actualizar_price_sin_permisos,
    actualizar_price_currency,
    actualizar_price_unit_amount,
    actualizar_price_body_vacio,
    actualizar_price_body_malformado,
    actualizar_price_nickname_caracteres_validos,
    actualizar_price_nickname_max_longitud,
    actualizar_price_nickname_vacio,
    actualizar_price_active_no_booleano,
    actualizar_price_metadata_compleja,
    actualizar_price_metadata_nula,
    actualizar_price_respuesta_estructura,
    consultar_price_id,
    actualizar_price_metadata_vacia,
    actualizar_price_nickname_unicode
)
from src.assertions.actualizar_price_assertion import (
    assert_actualizacion_exitosa,
    assert_actualizacion_fallida,
    assert_actualizacion_no_autorizada,
    assert_actualizacion_prohibida,
    assert_actualizacion_token_invalido,
    assert_estructura_respuesta_price,
    assert_persistencia_cambio
)

load_dotenv()


@pytest.mark.functional
def test_UPDP001_actualizar_price_nickname(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP001_actualizar_price_nickname")
    respuesta = actualizar_price_nickname(price_id)
    assert_actualizacion_exitosa(respuesta.get("response"))


@pytest.mark.functional
def test_UPDP002_actualizar_price_active_false(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP002_actualizar_price_active_false")
    respuesta = actualizar_price_active_false(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP003_actualizar_price_metadata_simple(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP003_actualizar_price_metadata_simple")
    respuesta = actualizar_price_metadata_simple(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP004_actualizar_price_multiples_campos(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP004_actualizar_price_multiples_campos")
    respuesta = actualizar_price_multiples_campos(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP005_actualizar_price_id_invalido():
    logger.info("Iniciando test_UPDP005_actualizar_price_id_invalido")
    respuesta = actualizar_price_id_invalido()
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP006_actualizar_price_sin_token(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP006_actualizar_price_sin_token")
    respuesta = actualizar_price_sin_token(price_id)
    assert_actualizacion_no_autorizada(respuesta)


@pytest.mark.functional
def test_UPDP007_actualizar_price_token_invalido(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP007_actualizar_price_token_invalido")
    respuesta = actualizar_price_token_invalido(price_id)
    assert_actualizacion_token_invalido(respuesta)


@pytest.mark.functional
def test_UPDP008_actualizar_price_header_vacio(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP008_actualizar_price_header_vacio")
    respuesta = actualizar_price_header_vacio(price_id)
    assert_actualizacion_prohibida(respuesta)


@pytest.mark.functional
def test_UPDP009_actualizar_price_sin_permisos(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP009_actualizar_price_sin_permisos")
    respuesta = actualizar_price_sin_permisos(price_id)
    assert_actualizacion_prohibida(respuesta)


@pytest.mark.functional
def test_UPDP010_actualizar_price_currency(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP010_actualizar_price_currency")
    respuesta = actualizar_price_currency(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP011_actualizar_price_unit_amount(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP011_actualizar_price_unit_amount")
    respuesta = actualizar_price_unit_amount(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP012_actualizar_price_body_vacio(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP012_actualizar_price_body_vacio")
    respuesta = actualizar_price_body_vacio(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP013_actualizar_price_body_malformado(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP013_actualizar_price_body_malformado")
    respuesta = actualizar_price_body_malformado(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP014_actualizar_price_nickname_caracteres_validos(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP014_actualizar_price_nickname_caracteres_validos")
    respuesta = actualizar_price_nickname_caracteres_validos(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP015_actualizar_price_nickname_max_longitud(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP015_actualizar_price_nickname_max_longitud")
    respuesta = actualizar_price_nickname_max_longitud(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP016_actualizar_price_nickname_vacio(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP016_actualizar_price_nickname_vacio")
    respuesta = actualizar_price_nickname_vacio(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP017_actualizar_price_active_no_booleano(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP017_actualizar_price_active_no_booleano")
    respuesta = actualizar_price_active_no_booleano(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.functional
def test_UPDP018_actualizar_price_metadata_compleja(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP018_actualizar_price_metadata_compleja")
    respuesta = actualizar_price_metadata_compleja(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP019_actualizar_price_metadata_nula(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP019_actualizar_price_metadata_nula")
    respuesta = actualizar_price_metadata_nula(price_id)
    assert_actualizacion_fallida(respuesta)


@pytest.mark.regression
def test_UPDP020_validar_estructura_respuesta_price(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP020_validar_estructura_respuesta_price")
    respuesta = actualizar_price_respuesta_estructura(price_id)
    assert_estructura_respuesta_price(respuesta)


@pytest.mark.regression
def test_UPDP021_validar_persistencia_cambio(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP021_validar_persistencia_cambio")
    data_update = actualizar_price_nickname(price_id)
    respuesta = consultar_price_id(price_id)
    assert_persistencia_cambio(response_consulta=respuesta, campo=data_update.get("field"), valor_esperado=data_update.get("field_value"))


@pytest.mark.functional
def test_UPDP022_actualizar_price_metadata_vacia(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP022_actualizar_price_metadata_vacia")
    respuesta = actualizar_price_metadata_vacia(price_id)
    assert_actualizacion_exitosa(respuesta)


@pytest.mark.functional
def test_UPDP023_actualizar_price_nickname_unicode(one_price_id):
    price_id = one_price_id
    logger.info("Iniciando test_UPDP023_actualizar_price_nickname_unicode")
    respuesta = actualizar_price_nickname_unicode(price_id)
    assert_actualizacion_exitosa(respuesta)
