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

class PriceEndpoints(Enum):
    GET_PRICES = "/prices"
    GET_PRICE_BY_ID = "/prices/{price_id}"
    CREATE_PRICE = "/prices"
    UPDATE_PRICE = "/prices/{price_id}"
    DELETE_PRICE = "/prices/{price_id}"
    SEARCH_PRICE = "/prices/search"

class CouponEndpoints(Enum):
    GET_COUPONS = "/coupons"
    GET_COUPON_BY_ID = "/coupons/{coupon_id}"
    CREATE_COUPON = "/coupons"
    UPDATE_COUPON = "/coupons/{coupon_id}"
    DELETE_COUPON = "/coupons/{coupon_id}"

class PromotionCodeEndpoints(Enum):
    GET_PROMOTION_CODES = "/promotion_codes"
    GET_PROMOTION_CODE_BY_ID = "/promotion_codes/{promotion_code_id}"
    CREATE_PROMOTION_CODE = "/promotion_codes"
    UPDATE_PROMOTION_CODE = "/promotion_codes/{promotion_code_id}"
    DELETE_PROMOTION_CODE = "/promotion_codes/{promotion_code_id}"
    
class TaxCodeEndpoints(Enum):
    GET_TAX_CODES = "/tax_codes"
    GET_TAX_CODE_BY_ID = "/tax_codes/{tax_code_id}"

class TaxRateEndpoints(Enum):
    GET_TAX_RATES = "/tax_rates"
    GET_TAX_RATE_BY_ID = "/tax_rates/{tax_rate_id}"
    CREATE_TAX_RATE = "/tax_rates"
    UPDATE_TAX_RATE = "/tax_rates/{tax_rate_id}"
    DELETE_TAX_RATE = "/tax_rates/{tax_rate_id}"