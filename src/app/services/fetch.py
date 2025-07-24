import requests
from loguru import logger
from src.app.config import Config


def fetch_products():
    logger.info("Fetching products from API")

    try:
        response_true = requests.get(Config.API_MAIN_TRUE)
        response_false = requests.get(Config.API_MAIN_FALSE)

        products_true = response_true.json().get("products", [])
        products_false = response_false.json().get("products", [])

        logger.debug(f"Fetched true products: {len(products_true)}")
        logger.debug(f"Fetched false products: {len(products_false)}")

        return products_true + products_false

    except requests.RequestException as e:
        logger.error(f"Error fetching data: {e}")
        return []

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return []
