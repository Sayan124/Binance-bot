import time

def twap_order(client, symbol, side, qty, parts, delay):
    chunk = qty / parts
    orders = []

    for _ in range(parts):
        o = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=round(chunk, 3)
        )
        orders.append(o)
        time.sleep(delay)

    return orders