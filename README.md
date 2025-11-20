# DIPLOMADO INGENIERÍA DE CALIDAD DE SOFTWARE COMERCIAL (3ra Edición)
## CARRERA DE INGENIERÍA SISTEMAS
API Stripe Test
---
Proyecto de automatización de pruebas sobre la API de Stripe, desarrollado en Python + pytest, con soporte para Allure Reports y ejecución en pipelines CI/CD.
### Requisitos
Se necesita una versión de Python >= 3.10
pip instalado
### Instalación
1. Clona el repositorio:  
```bash
git clone https://github.com/jessicatrujillo94/Automatizacion-Api-Rests-Stripe-.git
```
2. Crea y activa un entorno virtual:  
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Instala dependencias:  
```bash
pip install -r requirements.txt
```
---
### Ejecucion de Test
El proyecto está configurado con **Python y Pytest Projects** para API Rest:
> Comandos principales
Comando	Descripción

| Comando | Descripción |
|---------|-------------|
| `pytest -v` | Ejecuta **todos los tests** |
| `pytest -m smoke` | Ejecuta tests marcados con @pytest.mark.smoke **API**(`tests/**/*.py`) |
| `pytest -m regression` | Ejecuta tests marcados con @pytest.mark.regression **API**(`tests/**/*.py`) |
| `pytest -m functional ` |Ejecuta tests marcados con @pytest.mark.functional **API**(`tests/**/*.py`) |

---
### Reportes Allure

1. Allure:  
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
2. Reporte General
```bash
pytest -m smoke --alluredir=allure-results
 allure serve allure-results
```
3. Reporte Smoke
```bash
pytest -m smoke --alluredir=allure-results
 allure serve allure-results
```
4. Reporte Regression
```bash
pytest -m regression --alluredir=allure-results
 allure serve allure-results
```
5. Reporte Functional
```bash
pytest -m functional --alluredir=allure-results
 allure serve allure-results
```

### Estructura relevante
```
Stripe/
│
├── src/                     # "Código fuente del framework QA"
│   ├── assertions/          # "Funciones y validaciones personalizadas"
│   ├── payloads/            # "Cuerpos JSON usados en los tests"
│   ├── resources/           # "Datos externos, utilidades y archivos base"
│   ├── schemas/             # "Esquemas para validación de respuestas"
│   ├── services/            # "Lógica de servicios (peticiones HTTP)"
│   └── stripe_api/          # "Integraciones específicas con la API de Stripe"
│
├── tests/                   # "Casos de prueba organizados por módulos"
 └── conftest/               # "Manejar autenticación y limpiar datos antes "
├── venv/                    # "Entorno virtual local"
├── .env                     # "Variables de entorno (API keys, tokens)"
├── README.md                # "Documentación principal del proyecto"
├── requirements.txt         # "Dependencias necesarias para ejecutar el proyecto"
```
### Configuracion .env
```ini
# Environment variables for STRIPE API access
BASE_URL=https://api.stripe.com/v1/
API_KEY=sk_test_xxx_NO_SUBIR
API_KEY_INVALIDA=asdasdasd
API_KEY_EXPIRED=ASDASDASDASD
API_KEY_WITHOUT_PERMISSION=ASDASDASDASD
```
