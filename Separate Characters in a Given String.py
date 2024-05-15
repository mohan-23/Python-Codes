# Using For Loop
string = "Hello Python"
for char in string:
    print(char)

print('----------')

# Using join() Method
string = "Mohan"
new_str = '\n'.join(list(string))
print(new_str)
print('----------')

# Using Lambda Function
str = "Hello Mohan"
list(map(lambda x: print(x),str))
print('----------')

# Concatenate Two Strings using join() Method
str1 = 'kandukoori'
str2 = 'Mohan'
print("".join([str1, str2]))
print('--------')

# Concatenate Two Strings Without using join() Method
str1 = 'Hello'
str2 = 'Mohan'
string = str1 + str2
print(string)