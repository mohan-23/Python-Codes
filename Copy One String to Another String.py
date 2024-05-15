# Using For Loop
input = 'Hello World'
new_string = ''
for char in input:
    new_string += char
print("New String:", new_string)
print('----------')

# Copy String using Slice Operator
string = 'Mohan'
new_string = string[:]
print('New String =', new_string)
print("-----------")

# By Assigning through Variable
string = 'Programming'
new_string = str(string)
print('New String ::', new_string)
