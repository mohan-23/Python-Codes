string = 'Ques123@2&A%$%'
alphabets = 0
digits = 0
special_chars = 0
for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1
print("Alphabets:", alphabets)
print('Digits:', digits)
print('Special Chars:', special_chars)