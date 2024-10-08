def shopping(items, discount) -> float:
    """Adds the prices of every item together. If discount is true, it lowers the total price by 0.1 (ten percent)"""
    total = 0
    for item_price in items:
        total += item_price
    if discount == True:
        total = total - (total * 0.1)
    return total

cart = [19.99, 5.49, 12.89, 3.49, 99.99]
discount = True

print(shopping(cart, discount))