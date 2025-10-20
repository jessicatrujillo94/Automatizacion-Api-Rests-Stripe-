from src.logs.logger import logger
def log_request_response(url, headers=None, payload=None, response=None):
    """
    - URL y status code se loguean como INFO.
    - HTTP method también como INFO.
    - Headers, payload y response body se loguean como DEBUG.
    """
    logger.info(f"URL solicitada: {url}")

    if response is not None:
        logger.info(f"HTTP method: {response.request.method}")
        logger.info(f"Status code: {response.status_code}")

    if headers:
        logger.debug(f"Headers: {headers}")
    if payload:
        logger.debug(f"Payload: {payload}")
    if response is not None:
        try:
            logger.debug(f"Response JSON: {response.json()}")
        except ValueError:
            logger.debug(f"Response Text: {response.text}")