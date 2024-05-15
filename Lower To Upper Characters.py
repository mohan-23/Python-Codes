# method 1 (Upper)
string = "Mohan"
result = ''
for char in string:
    if char.lower():
        char = char.upper()
    result += char
print(string, 'To', result)
print('----------')

# method 2
print(string.upper())
print('-----------')

# method 3 (Lower)
string = "MOHAN"
result = ''
for char in string:
    if char.upper():
        char = char.lower()
    result += char
print(string, 'To', result)
print('----------')

# method 4
print(string.lower())
print('----------')

# Convert Lowercase Vowels to Uppercase using Replace Method
str = 'hello world'
vowels = 'aeiou'
for char in str:
    if char in vowels:
        upper_char = char.upper()
        str = str.replace(char, upper_char)
print(str)