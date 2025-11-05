import pytest
import os
import time
from dotenv import load_dotenv
from src.stripe_api.crear_products_api import crear_producto_campos_minimos, crear_producto_inactivo, eliminar_producto
from src.stripe_api.obtener_products_api import obtener_lista_completa_productos, obtener_productos_inactivos
from src.stripe_api.crear_prices_api import crear_price_campos_minimos
from src.stripe_api.crear_coupons_api import crear_cupon_valido, eliminar_cupon
from src.stripe_api.listar_promotion_codes_api import listar_promotion_codes
from src.stripe_api.crear_promotion_code_api import crear_codigo_promocional_valido, crear_codigo_promocional_inactivo
from src.stripe_api.listar_tax_codes_api import listar_tax_codes
from src.stripe_api.listar_tax_rates_api import listar_tax_rates
from src.stripe_api.crear_tax_rate_api import crear_tax_rate
from src.stripe_api.stripe_api import StripeAPI
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
TOKEN_CADUCADO = os.getenv("API_KEY_EXPIRED")
TOKEN_INVALIDO = os.getenv("API_KEY_INVALIDA")
TOKEN_SIN_PERMISO = os.getenv("TOKEN_SIN_PERMISO")

@pytest.fixture
def producto_creado():
    """
    Fixture que crea un producto antes del test y lo elimina al finalizar.
    """
    response = crear_producto_campos_minimos()
    yield response
    eliminar_producto(response)

@pytest.fixture
def one_product_id():
    response = obtener_lista_completa_productos()  
    products = response.json().get("data", []) 
    if len(products) > 0:
        product = products[0]
        yield product.get("id")
    else:
        # Create a new one only if none exist
        resp = crear_producto_campos_minimos()
        yield resp.json().get("id")
        eliminar_producto(resp)   

@pytest.fixture
def one_product_id_inactive():
    response = obtener_productos_inactivos()  
    products = response.json().get("data", []) 
    if len(products) > 0:
        product = products[0]
        yield product.get("id")
    else:
        resp = crear_producto_inactivo()
        yield resp.json().get("id") 
        eliminar_producto(resp)   

@pytest.fixture    
def one_price_id():
    response = obtener_lista_completa_productos()  
    products = response.json().get("data", []) 
    product_id = None
    resp_producto = None
    if len(products) > 0:
        product_id = products[0].get("id")
    else:
        # Create a new one only if none exist
        resp_producto = crear_producto_campos_minimos()
        product_id = resp_producto.json().get("id")
    
    resp_price = crear_price_campos_minimos(product_id)
    yield resp_price.json().get("id")
    if resp_producto:
        eliminar_producto(resp_producto)

    
@pytest.fixture(scope="session")
def coupon_creado():
    response = crear_cupon_valido()
    coupon_id = response.json().get("id")

    yield response

    if coupon_id:
        eliminar_cupon(response)

@pytest.fixture(scope="session")
def one_promotion_code(coupon_creado):        
    response = listar_promotion_codes(filter={"active": "true"})  
    promotions_code = response.json().get("data", []) 
    promotion_code = None
    if len(promotions_code) > 0:
        promotion_code = promotions_code[0]
    else:
        response_promotion = crear_codigo_promocional_valido(coupon_creado)
        promotion_code = response_promotion.json()

    yield promotion_code
    if coupon_creado:
        eliminar_cupon(coupon_creado)

@pytest.fixture(scope="session")
def one_promotion_code_inactivo(coupon_creado):
    response = listar_promotion_codes(filter={"active": "false"})
    promotions_code = response.json().get("data", [])
    promotion_code = None

    if len(promotions_code) > 0:
        promotion_code = promotions_code[0]
    else:
        response_promotion = crear_codigo_promocional_inactivo(coupon_creado)
        promotion_code = response_promotion.json()

    yield promotion_code

    # Cleanup
    if coupon_creado:
        eliminar_cupon(coupon_creado)
@pytest.fixture(scope="session")
def tax_code_valido():
    response = listar_tax_codes()
    taxs_codes = response.json().get("data", [])
    if len(taxs_codes) > 0:
        tax_code = taxs_codes[0]
    else:
        tax_code = {}
    yield tax_code

@pytest.fixture(scope="session")
def tax_rate_valido():
    response = listar_tax_rates()
    taxs_rates = response.json().get("data", [])
    tax_rate = {}
    if len(taxs_rates) > 0:
        tax_rate = taxs_rates[0]
    else:
        new_tax_rate = crear_tax_rate()
        tax_rate = new_tax_rate.json()
    yield tax_rate

@pytest.fixture(scope="session")
def pausa():
    time.sleep(60)
    yield


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def api_client(headers):
    return StripeAPI(base_url=BASE_URL, headers=headers)

@pytest.fixture(scope="session")
def headers_with_api_key():
    return {
        "Authorization": "Bearer "+API_KEY,
        "Content-Type": "application/json"
    }
@pytest.fixture(scope="session")
def headers_without_api_key():
    return {
        "Content-Type": "application/json"
    }
""" @pytest.fixture(scope="session")
def crear_lista_sin_token(request):
    params = request.param
    payload = params["payload"]
    name = payload.get("name")
    content = payload.get("content", None)
    folder_id = params.get("folder_id",ID_FOLDER)
    response = crear_lista_no_token(folder_id=folder_id, name=name, content=content)
    yield response, payload, folder_id
    if(response.status_code in [201, 200] and response.json().get("id")):
        eliminar_lista(response.json().get("id"))

@pytest.fixture(scope="session")
def crear_lista_con_token_invalido(request):
    params = request.param
    payload = params["payload"]
    name = payload.get("name")
    content = payload.get("content", None)
    folder_id = params.get("folder_id",ID_FOLDER)
    response = crear_lista_token_invalido(folder_id=folder_id, name=name, content=content)
    yield response, payload, folder_id
    if(response.status_code in [201, 200] and response.json().get("id")):
        resp_delete = eliminar_lista(response.json().get("id"))
        logger.warning(f"No se pudo eliminar la lista {response.json().get('id')}. Status: {resp_delete.status_code}, Response: {resp_delete.text}")
 """