def add_numbers(x, y):
    while y != 0:
        carry = x & y
        print(carry)
        x = x ^ y
        print(x)
        y = carry << 1
        print(y)
    return x

num1 = 10
num2 = 15

sum_result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")