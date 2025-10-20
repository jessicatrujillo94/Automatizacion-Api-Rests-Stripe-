import pytest
from src.logs.conflogger import log_request_response
from src.assertions.crear_product_assertion import assert_creacion_exitosa
from src.assertions.obtener_products_asserions import assert_obtencion_exitosa
from src.assertions.actualizar_product_assertion import assert_actualizacion_exitosa
from src.assertions.eliminar_product_assertion import assert_eliminacion_exitosa
from src.stripe_api.crear_products_api import crear_producto_campos_minimos

from src.stripe_api.obtener_products_api import obtener_producto, obtener_lista_completa_productos
from src.stripe_api.actualizar_product_api import actualizar_nombre_producto
from src.stripe_api.eliminar_product_api import eliminar_producto_existente
from src.logs.logger import logger


@pytest.mark.functional
def test_e2e_crud_producto():
    logger.info("POST - Crear producto")
    resp_create = crear_producto_campos_minimos()
    assert_creacion_exitosa(resp_create)
    product_id = resp_create.json().get("id")

    logger.info("GET - Obtener lista de productos")
    resp_get = obtener_producto(resp_create.json().get("id"))
    assert_obtencion_exitosa(resp_get)

    logger.info("POST - Actualizar producto")
    resp_update = actualizar_nombre_producto(resp_create)
    assert_actualizacion_exitosa(resp_update)
    assert resp_update.json().get("name") == "Producto Actualizado"

    logger.info("DELETE - Eliminar producto")
    resp_delete = eliminar_producto_existente(resp_create)
    assert_eliminacion_exitosa(resp_delete)
    assert resp_delete.json().get("deleted") is True

    logger.info("GET - Verificar producto eliminado")
    resp_get_final = obtener_lista_completa_productos()
    assert_obtencion_exitosa(resp_get_final)
    assert all(p["id"] != product_id for p in resp_get_final.json().get("data", []))
