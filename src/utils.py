def validate_order(symbol, qty, price=None):
    if qty <= 0:
        raise ValueError("Quantity must be positive.")
    if price is not None and price <= 0:
        raise ValueError("Price must be positive.")
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures allowed.")
    return True