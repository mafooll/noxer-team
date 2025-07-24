from src.app.services.fetch import fetch_products
from src.app.services.sync import sync_data


def periodic_sync():
    products = fetch_products()
    if products:
        sync_data(products)
