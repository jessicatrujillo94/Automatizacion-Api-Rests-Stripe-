import logging

# Crear y configurar el logger
logger = logging.getLogger("clickup_tests")
logger.setLevel(logging.DEBUG)

# Formato de logs con fecha y hora
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Handler para archivo
file_handler = logging.FileHandler("test_logs.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
