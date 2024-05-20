# Write a program to reverse a string

# Method 1
def reverse_text(string):
    return string[::-1]

string = 'Mohan'
reversed_text = reverse_text(string)
print(f'{string} is {reversed_text}')

print('***********')

# Method 2
string = 'Hello'

reverse_string = ''
for char in string:
    reverse_string = char + reverse_string

print(f'{string} is {reverse_string}')