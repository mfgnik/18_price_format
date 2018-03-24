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
        return format_frac_price(price)


def format_int_price(price):
    list_with_digits = []
    string_with_price = str(int(price))
    for i in range(len(string_with_price)):
        list_with_digits.append(
            string_with_price[len(string_with_price) - 1 - i]
        )
        if i % 3 == 2:
            list_with_digits.append(' ')
    list_with_digits.reverse()
    return ''.join(list_with_digits).lstrip()


def format_frac_price(price):
    int_price = format_int_price(int(float(price)))
    letters_after_point = price[price.find('.') + 1:]
    first_letter = letters_after_point[0]
    if len(letters_after_point) > 2:
        second_letter, third_letter = map(int, letters_after_point[1:3])
        if third_letter >= 5:
            second_letter += 1
    elif len(letters_after_point) == 2:
        second_letter = letters_after_point[1]
    else:
        second_letter = 0
    return '{}.{}{}'.format(
        format_int_price(int_price),
        first_letter,
        second_letter
    )

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('No price')
    price = sys.argv[1]
    print(format_price(price))
