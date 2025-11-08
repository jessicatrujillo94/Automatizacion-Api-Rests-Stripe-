import pytest
import allure
from src.logs.logger import logger
from src.assertions.crear_product_assertion import assert_creacion_exitosa
from src.assertions.obtener_products_asserions import assert_obtencion_exitosa
from src.assertions.actualizar_product_assertion import assert_actualizacion_exitosa
from src.assertions.eliminar_product_assertion import assert_eliminacion_exitosa
from src.stripe_api.crear_products_api import crear_producto_campos_minimos
from src.stripe_api.obtener_products_api import obtener_producto, obtener_lista_completa_productos
from src.stripe_api.actualizar_product_api import actualizar_nombre_producto
from src.stripe_api.eliminar_product_api import eliminar_producto_existente

@allure.epic("EPIC: Gestión de Productos")
@allure.feature("Feature: CRUD Productos")
@allure.story("HU: HU080-E2E CRUD Producto")
@pytest.mark.functional
def test_e2e_crud_producto():
    product_id = None

    with allure.step("POST - Crear producto con campos mínimos"):
        logger.info("POST - Crear producto")
        resp_create = crear_producto_campos_minimos()
        assert_creacion_exitosa(resp_create)
        product_id = resp_create.json().get("id")
        allure.attach(str(resp_create.json()), name="Respuesta Creación", attachment_type=allure.attachment_type.JSON)

    with allure.step("GET - Obtener producto creado"):
        logger.info(f"GET - Obtener producto {product_id}")
        resp_get = obtener_producto(product_id)
        assert_obtencion_exitosa(resp_get)
        allure.attach(str(resp_get.json()), name="Respuesta GET", attachment_type=allure.attachment_type.JSON)

    with allure.step("POST - Actualizar nombre del producto"):
        logger.info(f"POST - Actualizar producto {product_id}")
        resp_update = actualizar_nombre_producto(resp_create)
        assert_actualizacion_exitosa(resp_update)
        assert resp_update.json().get("name") == "Producto Actualizado"
        allure.attach(str(resp_update.json()), name="Respuesta Actualización", attachment_type=allure.attachment_type.JSON)

    with allure.step("DELETE - Eliminar producto creado"):
        logger.info(f"DELETE - Eliminar producto {product_id}")
        resp_delete = eliminar_producto_existente(resp_create)
        assert_eliminacion_exitosa(resp_delete)
        assert resp_delete.json().get("deleted") is True
        allure.attach(str(resp_delete.json()), name="Respuesta Eliminación", attachment_type=allure.attachment_type.JSON)

    with allure.step("GET - Verificar producto eliminado en la lista"):
        logger.info("GET - Verificar producto eliminado")
        resp_get_final = obtener_lista_completa_productos()
        assert_obtencion_exitosa(resp_get_final)
        assert all(p["id"] != product_id for p in resp_get_final.json().get("data", []))
        allure.attach(str(resp_get_final.json()), name="Respuesta Lista Final", attachment_type=allure.attachment_type.JSON)
