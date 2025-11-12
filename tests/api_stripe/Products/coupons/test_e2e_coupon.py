import pytest
import allure
from src.logs.logger import logger
from src.assertions.crear_coupon_assertion import assert_creacion_exitosa
from src.assertions.obtener_coupon_assertion import assert_obtener_cupon_valido
from src.assertions.actualizar_coupon_assertion import assert_actualizacion_exitosa
from src.assertions.eliminar_coupon_assertion import assert_eliminacion_exitosa
from src.assertions.listar_coupon_assertion import assert_listar_cupones_valido
from src.stripe_api.crear_coupons_api import eliminar_cupon, crear_cupon_campos_validos
from src.stripe_api.obtener_cupon_api import obtener_cupon_valido
from src.stripe_api.actualizar_coupon_api import actualizar_cupon_valido
from src.stripe_api.listar_coupon_api import listar_cupones_valido

@allure.epic("EPIC: Gestión de Cupones")
@allure.feature("Feature: CRUD Cupones")
@allure.story("HU: HU081-E2E CRUD Cupones")
@pytest.mark.functional
def test_e2e_crud_cupones():
    coupon_id = None

    with allure.step("POST - Crear un nuevo cupón con datos válidos"):
        logger.info("POST - Crear cupón")
        resp_create = crear_cupon_campos_validos()
        assert_creacion_exitosa(resp_create)
        coupon_id = resp_create.json().get("id")
        allure.attach(str(resp_create.json()), name="Respuesta Creación", attachment_type=allure.attachment_type.JSON)

    with allure.step("GET - Consultar el cupón recién creado"):
        logger.info(f"GET - Obtener cupón {coupon_id}")
        resp_get = obtener_cupon_valido(resp_create)
        assert_obtener_cupon_valido(resp_get)
        allure.attach(str(resp_get.json()), name="Respuesta GET", attachment_type=allure.attachment_type.JSON)

    with allure.step("POST - Actualizar los datos del cupón existente"):
        logger.info(f"POST - Actualizar cupón {coupon_id}")
        resp_update = actualizar_cupon_valido(resp_create)
        assert_actualizacion_exitosa(resp_update)
        allure.attach(str(resp_update.json()), name="Respuesta Actualización", attachment_type=allure.attachment_type.JSON)

    with allure.step("DELETE - Eliminar el cupón creado"):
        logger.info(f"DELETE - Eliminar cupón {coupon_id}")
        resp_delete = eliminar_cupon(resp_create)
        assert_eliminacion_exitosa(resp_delete)
        assert resp_delete.json().get("deleted") is True
        allure.attach(str(resp_delete.json()), name="Respuesta Eliminación", attachment_type=allure.attachment_type.JSON)

    with allure.step("GET - Intentar obtener el cupón eliminado"):
        logger.info(f"GET - Consultar cupón eliminado {coupon_id}")
        resp_get_deleted = obtener_cupon_valido(resp_create)
        assert resp_get_deleted.status_code not in [200]
        allure.attach(str(resp_get_deleted.json()), name="Respuesta GET Eliminado", attachment_type=allure.attachment_type.JSON)
