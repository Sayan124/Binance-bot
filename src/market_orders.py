from logger import logger
from utils import validate_order

def place_market_order(client, symbol, side, qty):
    try:
        validate_order(symbol, qty)
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )
        logger.info(f"Market Order: {order}")
        return order
    except Exception as e:
        logger.error(f"Market order failed: {e}")
        return None