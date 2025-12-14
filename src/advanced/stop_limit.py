def stop_limit_order(client, symbol, side, qty, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=qty,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )
        return order
    except Exception as e:
        logger.error(f"Stop-limit failed: {e}")
        return None