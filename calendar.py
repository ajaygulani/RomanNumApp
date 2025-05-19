def number_to_roman(number):
    number = int(number)
    roman = ""

    while number >= 1000:
        roman += "M"
        number -= 1000

    if number >= 500:
        roman += "D"
        number -= 500

    while number >= 100:
        roman += "C"
        number -= 100

    if number >= 50:
        roman += "L"

    while number >= 10:
        roman += "X"
        number -= 10

    if number >= 5:
        roman += "V"
        number -= 5

    while number >= 1:
        roman += "I"
        number -= 1

    return roman