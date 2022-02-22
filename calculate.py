taxes_by_country = {'FR': 0.2, 'DE': 0.2, 'UK': 0.21, 'IT': 0.25, 'ES': 0.19, 'PL': 0.21, 'RO': 0.2, 'NL': 0.2,
                    'BE': 0.24, 'EL': 0.2, 'CZ': 0.19, 'PT': 0.23, 'HU': 0.27, 'SE': 0.23, 'AT': 0.22, 'BG': 0.21,
                    'DK': 0.21, 'FI': 0.17, 'SK': 0.18, 'IE': 0.21, 'HR': 0.23, 'LT': 0.23, 'SI': 0.24, 'LV': 0.2,
                    'EE': 0.22, 'CY': 0.21, 'LU': 0.25, 'MT': 0.2}

discount_thresholds = {50000: 0.15, 10000: 0.10, 7000: 0.07, 5000: 0.05, 1000: 0.03}


def total_price_for_quantities(prices, quantities):
    total = 0
    for price, quantity in zip(prices, quantities):
        total += price * quantity
    return total


def apply_taxes(price, country):
    price = price + (price * taxes_by_country[country])
    return price


def apply_discount(price, request):
    if request["reduction"] == 'STANDARD':
        for threshold in sorted(discount_thresholds.keys(), reverse=True):
            if price >= threshold:
                return price - (price * discount_thresholds[threshold])
        return price
    elif request["reduction"] == 'HALF PRICE':
        return price / 2
    elif request["reduction"] == 'PAY THE PRICE':
        return price
    return -1


def compute_invoice(request):
    price = total_price_for_quantities(request["prices"], request["quantities"])
    price = apply_taxes(price, request["country"])
    price = apply_discount(price, request)
    return price