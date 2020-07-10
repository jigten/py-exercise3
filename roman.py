numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def convert_to_roman(number):   
    result = []
    for numeral, value in zip(numerals, values):
        (q, r) = divmod(number, value)
        result.append(numeral * q)
        number -= (value * q)
        if number == 0:
            break

    return "".join(result)