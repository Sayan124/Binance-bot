def place_oco(client, symbol, side, qty, take_profit, stop_loss):
    try:
        order = client.futures_oco_order(
            symbol=symbol,
            side=side,
            quantity=qty,
            price=take_profit,
            stopPrice=stop_loss
        )
        return order
    except Exception as e:
        logger.error(f"OCO failed: {e}")
        return None