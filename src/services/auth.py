import os
from dotenv import load_dotenv
import logging
# Cargar variables desde el archivo .env
load_dotenv()

def get_token():
    token = os.getenv("API_KEY")
    if not token:
        raise EnvironmentError("La variable 'API_KEY' no existe en el archivo .env")
    return f"Bearer {token}"

def build_headers(token=None):

    """
    Construye los headers de autorización y Content-Type.
    Si token es None, lo toma de la variable de entorno,
    si es cadena vacía o cualquier otro valor, lo usa tal cual (incluso cadena vacía).
    """
    if token is None:
        token = get_token()

    token = token or get_token()

    if not token:
        raise ValueError("No se proporcionó un token de acceso y no se encontró en el entorno.")
    # Sólo falla si token es None, acepta "" (cadena vacía)
    if token is None:
        raise ValueError("No se proporcionó un token de acceso y no se encontró  en el entorno.")

    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return headers

def build_headers_sin_authorization():
    return {
        "Content-Type": "application/json"
    }

def build_headers_sin_content_type(token=None):
    """
    Construye los headers de autorización y Content-Type.
    Si token es None, lo toma de la variable de entorno,
    si es cadena vacía o cualquier otro valor, lo usa tal cual (incluso cadena vacía).
    """
    if token is None:
        token = get_token()

    # Sólo falla si token es None, acepta "" (cadena vacía)
    if token is None:
        raise ValueError("No se proporcionó un token de acceso y no se encontró  en el entorno.")

    headers = {
        "Authorization": f"{token}",
    }
    return headers



