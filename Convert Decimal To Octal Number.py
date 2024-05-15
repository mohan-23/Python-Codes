def decimal_to_octal(decimal):
    if decimal == 0:
        return ''
    quotient = decimal // 8
    remainder = decimal % 8
    return decimal_to_octal(quotient) + str(remainder)

decimal = 157
octal = decimal_to_octal(decimal)
print("Octal number is", octal, "for", decimal)