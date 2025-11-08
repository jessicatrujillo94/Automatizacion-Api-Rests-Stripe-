import pytest
from dotenv import load_dotenv
from src.logs.logger import logger

from src.stripe_api.auth_stripe_api import (
    autenticacion_api_key_valida,
    autenticacion_api_key_invalida,
    autenticacion_sin_token,
    autenticacion_header_incorrecto,
    autenticacion_api_key_vacia,
    autenticacion_endpoint_restringido,
)

from src.assertions.auth_assertions import (
    assert_autenticacion_exitosa,
    assert_autenticacion_fallida,
    assert_autenticacion_sin_token,
    assert_autenticacion_header_incorrecto,
    assert_autenticacion_api_key_vacia,
    assert_autenticacion_endpoint_restringido,
    assert_respuesta_body_schema,
)

# Carga de variables de entorno (donde se guarda la API Key)
load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
def test_LOGIN001_autenticacion_exitosa_api_key_valida():
    """ Test LOGIN001: Autenticación exitosa con API Key válida """
    logger.info("Iniciando test_LOGIN001_autenticacion_exitosa_api_key_valida")
    respuesta = autenticacion_api_key_valida()
    assert_autenticacion_exitosa(respuesta)
    assert_respuesta_body_schema(respuesta)


@pytest.mark.functional
@pytest.mark.negative
def test_LOGIN002_autenticacion_fallida_api_key_invalida():
    """ Test LOGIN002: Autenticación fallida con API Key inválida """
    logger.info("Iniciando test_LOGIN002_autenticacion_fallida_api_key_invalida")

    respuesta = autenticacion_api_key_invalida()
    assert_autenticacion_fallida(respuesta)


@pytest.mark.functional
def test_LOGIN003_autenticacion_ausente_sin_token():
    """ Test LOGIN003: Autenticación ausente (sin header Authorization) """
    logger.info("Iniciando test_LOGIN003_autenticacion_ausente_sin_token")

    respuesta = autenticacion_sin_token()
    assert_autenticacion_sin_token(respuesta)


@pytest.mark.functional
def test_LOGIN004_header_formato_incorrecto():
    """ Test LOGIN004: Header con formato incorrecto (sin 'Bearer') """
    logger.info("Iniciando test_LOGIN004_header_formato_incorrecto")

    respuesta = autenticacion_header_incorrecto()
    assert_autenticacion_header_incorrecto(respuesta)


@pytest.mark.functional
@pytest.mark.negative
def test_LOGIN005_api_key_vacia_en_header():
    """ Test LOGIN005: Clave vacía en header Authorization """
    logger.info("Iniciando test_LOGIN005_api_key_vacia_en_header")

    respuesta = autenticacion_api_key_vacia()
    assert_autenticacion_api_key_vacia(respuesta)


@pytest.mark.functional
@pytest.mark.negative
def test_LOGIN006_autenticacion_endpoint_restringido():
    """ Test LOGIN006: Autenticación con endpoint restringido o sin permisos """
    logger.info("Iniciando test_LOGIN006_autenticacion_endpoint_restringido")
    respuesta = autenticacion_endpoint_restringido()
    assert_autenticacion_endpoint_restringido(respuesta)


@pytest.mark.regression
def test_LOGIN007_validar_estructura_body_respuesta():
    """ Test LOGIN007: Validar estructura del body de respuesta exitosa """
    logger.info("Iniciando test_LOGIN007_validar_estructura_body_respuesta")

    respuesta = autenticacion_api_key_valida()
    assert_respuesta_body_schema(respuesta)
