#Code Smells Example for long method
#Refactored code
def apply_discount(price):
    if price > 100:
        return price * 0.9
    else:
        return price * 0.95

def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            total += apply_discount(item.price)
    return total
