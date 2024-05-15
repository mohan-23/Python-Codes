# method 1
string = 'que scol web site'
result = ''
char = 't'
for ch in string:
    if ch == " ":
        ch = char
    result += ch
print('String after removing space with t =', result)

# method 2
print(string.replace(" ", 't'))