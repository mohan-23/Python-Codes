# method 1
string = 'Vowels'
vowels = ('a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U')
result = ''
for char in string:
    if char in vowels:
        char = ''
    result += char
print(string, 'from', result)

# method 2
str = 'Vowels'
vowels = ('a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U')
for char in str:
    if char in vowels:
        str = str.replace(char, "")
print(str)