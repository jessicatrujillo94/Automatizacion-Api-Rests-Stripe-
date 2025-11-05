# API Stripe Tests

Automated tests for the Stripe API, organized by product type and functionality.

## Folder Structure

tests/
└── api_stripe/
├── Authentication/
│ └── auth.py
├── conftest.py
└── Products/
├── coupons/
│ ├── test_actualizar_coupon.py
│ ├── test_crear_coupon.py
│ ├── test_eliminar_coupon.py
│ ├── test_listar_coupon.py
│ └── test_obtener_coupon.py
├── Price/
│ ├── test_buscar_precios.py
│ ├── test_crear_price.py
│ ├── test_obtener_price.py
│ └── test_update_price.py
├── promocional_code/
│ ├── test_actualizar_promocional_code.py
│ ├── test_crear_promocional_code.py
│ ├── test_listar_promocional_code.py
│ └── test_obtener_promocional_code.py
├── tax_code/
│ ├── test_detalle_tax_code.py
│ └── test_listar_tax_code.py
├── tax_rate/
│ ├── test_actualizar_tax_rate.py
│ ├── test_crear_tax_rate.py
│ ├── test_listar_tax_rate.py
│ └── test_obtener_tax_rate.py
├── test_actualizar_product.py
├── test_crear_product.py
├── test_e2e_product.py
├── test_eliminar_product.py
└── test_obtener_product.py


## Test Categories

### Authentication
- `auth.py`: Tests for authentication mechanisms, token validation, and error handling.

### Coupons
- CRUD operations: create, list, update, delete, and retrieve coupons.

### Price
- Operations on product prices: creation, updating, retrieving, and searching.

### Promotional Code
- CRUD operations and listing of promotion codes.

### Tax Code
- Listing and retrieving tax codes.

### Tax Rate
- Creation, updating, listing, and retrieving tax rates.

### Products
- CRUD operations for products, including end-to-end (`e2e`) tests.

---

## Running Tests

Use `pytest` to run the tests. Examples:

```bash
# Run all tests
pytest tests/api_stripe/

# Run tests for a specific folder
pytest tests/api_stripe/Products/tax_rate/

# Run a specific test function
pytest tests/api_stripe/Products/tax_rate/test_crear_tax_rate.py::test_TAXRPOST001_crear_tax_rate_campos_obligatorios
