import sys


def format_price(price):
    try:
        price_value = float(price)
    except (ValueError, TypeError):
        return None
    error = 10 ** -6
    if abs(price_value - int(price_value)) < error:
        return '{:,}'.format(int(price_value)).replace(',', ' ')
    else:
        return '{}'.format(round(price_value * 100 + error) / 100)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('No price')
    price = sys.argv[1]
    print(format_price(price))
