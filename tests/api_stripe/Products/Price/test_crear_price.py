import pytest
from dotenv import load_dotenv
from src.logs.logger import logger
from src.stripe_api.crear_prices_api import (
    crear_price_campos_minimos,
    crear_price_todos_campos,
    crear_price_sin_currency,
    crear_price_sin_unit_amount,
    crear_price_sin_product,
    crear_price_unit_amount_invalido,
    crear_price_currency_invalido,
    crear_price_token_invalido,
    crear_price_sin_token,
    crear_price_producto_inexistente,
    crear_price_campos_adicionales,
    crear_price_inactivo,
    crear_price_nickname_vacio,
    crear_price_metadata_compleja,
    crear_multiples_prices,
    crear_price_respuesta_estructura,
    crear_price_nickname_largo,
    crear_price_recurrente_mensual,
    crear_price_recurrente_intervalo_invalido,
    crear_price_unit_amount_cero,
    crear_price_unit_amount_negativo,
    crear_price_unit_amount_grande,
    crear_price_producto_inactivo,
    crear_price_body_vacio,
    crear_price_body_invalido,
    eliminar_price
)
from src.assertions.crear_price_assertion import (
    assert_creacion_exitosa,
    assert_creacion_fallida,
    assert_creacion_sin_token,
    assert_creacion_token_invalido,
    assert_creacion_producto_inexistente,
    assert_creacion_campos_no_soportados,
    assert_creacion_inactivo,
    assert_creacion_nombre_vacio,
    assert_creacion_metadata_compleja,
    assert_creacion_multiple,
    assert_estructura_respuesta_price,
    assert_creacion_nombre_largo,
    assert_creacion_body_invalido,
)

load_dotenv()

@pytest.mark.functional
def test_POSTP001_crear_price_campos_minimos_validos(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP001_crear_price_campos_minimos_validos")
    respuesta = crear_price_campos_minimos(product_id)
    try:
        assert_creacion_exitosa(respuesta)
        assert_estructura_respuesta_price(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.functional
def test_POSTP002_crear_price_todos_campos_opcionales(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP002_crear_price_todos_campos_opcionales")
    respuesta = crear_price_todos_campos(product_id)
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.functional
def test_POSTP003_crear_price_sin_currency(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP003_crear_price_sin_currency")
    respuesta = crear_price_sin_currency(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP004_crear_price_sin_unit_amount(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP004_crear_price_sin_unit_amount")
    respuesta = crear_price_sin_unit_amount(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP005_crear_price_sin_product(producto_creado):
    logger.info("Iniciando test_POSTP005_crear_price_sin_product")
    respuesta = crear_price_sin_product()
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP006_crear_price_unit_amount_invalido(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP006_crear_price_unit_amount_invalido")
    respuesta = crear_price_unit_amount_invalido(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP007_crear_price_currency_invalido(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP007_crear_price_currency_invalido")
    respuesta = crear_price_currency_invalido(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.security
def test_POSTP008_crear_price_token_invalido(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP008_crear_price_token_invalido")
    respuesta = crear_price_token_invalido(product_id)
    assert_creacion_token_invalido(respuesta)


@pytest.mark.security
def test_POSTP009_crear_price_sin_token(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP009_crear_price_sin_token")
    respuesta = crear_price_sin_token(product_id)
    assert_creacion_sin_token(respuesta)


@pytest.mark.functional
def test_POSTP010_crear_price_producto_inexistente(producto_creado):
    logger.info("Iniciando test_POSTP010_crear_price_producto_inexistente")
    respuesta = crear_price_producto_inexistente()
    assert_creacion_producto_inexistente(respuesta)


@pytest.mark.functional
def test_POSTP011_crear_price_campos_adicionales_no_soportados(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP011_crear_price_campos_adicionales_no_soportados")
    respuesta = crear_price_campos_adicionales(product_id)
    assert_creacion_campos_no_soportados(respuesta)


@pytest.mark.functional
def test_POSTP012_crear_price_inactivo(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP012_crear_price_inactivo")
    respuesta = crear_price_inactivo(product_id)
    try:
        assert_creacion_inactivo(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.functional
def test_POSTP013_crear_price_nickname_vacio(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP013_crear_price_nickname_vacio")
    respuesta = crear_price_nickname_vacio(product_id)
    assert_creacion_nombre_vacio(respuesta)


@pytest.mark.functional
def test_POSTP014_crear_price_metadata_compleja(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP014_crear_price_metadata_compleja")
    respuesta = crear_price_metadata_compleja(product_id)
    try:
        assert_creacion_metadata_compleja(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.regression
def test_POSTP015_crear_multiples_prices_consecutivamente(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP015_crear_multiples_prices_consecutivamente")
    respuestas = crear_multiples_prices(product_id)
    try:
        assert_creacion_multiple(respuestas)
    finally:
        for r in respuestas:
            eliminar_price(r)


@pytest.mark.regression
def test_POSTP016_validar_estructura_respuesta_price(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP016_validar_estructura_respuesta_price")
    respuesta = crear_price_respuesta_estructura(product_id)
    try:
        assert_estructura_respuesta_price(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.functional
def test_POSTP017_crear_price_nickname_largo(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP017_crear_price_nickname_largo")
    respuesta = crear_price_nickname_largo(product_id)
    assert_creacion_nombre_largo(respuesta)


@pytest.mark.functional
def test_POSTP018_crear_price_recurrente_mensual(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP018_crear_price_recurrente_mensual")
    respuesta = crear_price_recurrente_mensual(product_id)
    try:
        assert_creacion_exitosa(respuesta)
    finally:
        eliminar_price(respuesta)


@pytest.mark.functional
def test_POSTP019_crear_price_recurrente_intervalo_invalido(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP019_crear_price_recurrente_intervalo_invalido")
    respuesta = crear_price_recurrente_intervalo_invalido(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP020_crear_price_unit_amount_cero(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP020_crear_price_unit_amount_cero")
    respuesta = crear_price_unit_amount_cero(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP021_crear_price_unit_amount_negativo(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP021_crear_price_unit_amount_negativo")
    respuesta = crear_price_unit_amount_negativo(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP022_crear_price_unit_amount_grande(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP022_crear_price_unit_amount_grande")
    respuesta = crear_price_unit_amount_grande(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP023_crear_price_producto_inactivo(producto_creado):
    logger.info("Iniciando test_POSTP023_crear_price_producto_inactivo")
    respuesta = crear_price_producto_inactivo()
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP024_crear_price_body_vacio(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP024_crear_price_body_vacio")
    respuesta = crear_price_body_vacio(product_id)
    assert_creacion_fallida(respuesta)


@pytest.mark.functional
def test_POSTP025_crear_price_body_invalido(producto_creado):
    product_id = producto_creado.json().get("id")
    logger.info("Iniciando test_POSTP025_crear_price_body_invalido")
    respuesta = crear_price_body_invalido(product_id)
    assert_creacion_body_invalido(respuesta)