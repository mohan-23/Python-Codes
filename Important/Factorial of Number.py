# Write a program ot find the factorial of a number

# Method 1
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = 3

result = factorial(num)
print(f'factorial of {num} is {result}')

print('***********')

# Mothod 2
num = 4
factorial = 1

if num < 0:
    print('Factorial can\'t be calculated for negative numbers')
elif num == 0:
    print('Factorial of 0 is 1')
else:
    for n in range(num, 0, -1):
        factorial *= n

print(f'factorial of {num} is {factorial}')