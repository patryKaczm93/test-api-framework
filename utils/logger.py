from loguru import logger

logger.add("logs/api_tests.log", rotation="1 MB", level="INFO")

def log_request(response):
    logger.info(f"\n")
    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")