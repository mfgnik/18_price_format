import sys


def format_price(price):
    try:
        int_price = int(float(price))
        frac_price = float(price) - int_price
    except ValueError:
        return None
    error = 10 ** -6
    if abs(frac_price) < error:
        return format_int_price(int_price)
    else:
        return format_frac_price(int_price, frac_price)


def format_int_price(price):
    return '{:,}'.format(price).replace(',', ' ')


def format_frac_price(int_price, frac_price):
    return '{}.{}'.format(int_price, round(frac_price * 100))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('No price')
    price = sys.argv[1]
    print(format_price(price))
