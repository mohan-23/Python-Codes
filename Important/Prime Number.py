# Write a program to check number is prime or not?

# Prime Number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

num = 6
if is_prime(num):
    print(f'{num} is a prime')
else:
    print(f'{num} is not a prime')

print('*********')

# Prime Numbers
number = 20

for num in range(number):
    if num > 1:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")