from enum import Enum

class ProductEndpoints(Enum):
    GET_PRODUCTS = "/products"
    GET_PRODUCT_BY_ID = "/products/{product_id}"
    CREATE_PRODUCT = "/products"
    UPDATE_PRODUCT = "/products/{product_id}"
    DELETE_PRODUCT = "/products/{product_id}"

class CustomerEndpoints(Enum):
    GET_CUSTOMERS = "/customers"
    GET_CUSTOMER_BY_ID = "/customers/{customer_id}"
    CREATE_CUSTOMER = "/customers"
    UPDATE_CUSTOMER = "/customers/{customer_id}"
    DELETE_CUSTOMER = "/customers/{customer_id}"