from logger import logger
from utils import validate_order

def place_limit_order(client, symbol, side, qty, price):
    try:
        validate_order(symbol, qty, price)
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=qty,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Limit Order: {order}")
        return order
    except Exception as e:
        logger.error(f"Limit order failed: {e}")
        return None