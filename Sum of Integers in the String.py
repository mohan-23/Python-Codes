string = 'Mohan123k111'
sum = 0
for char in string:
    if char.isdigit():
        sum += int(char)

print('Sum =', sum)