from binance.client import Client
from logger import logger

def create_client(api_key, api_secret):
    try:
        client = Client(api_key, api_secret, testnet=True)
        client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Client initialized successfully.")
        return client
    except Exception as e:
        logger.error(f"Client initialization failed: {e}")
        raise