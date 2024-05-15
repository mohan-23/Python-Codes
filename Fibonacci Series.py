
# Fibonacci Series (Using Iterative Methods)
# A Fibonacci series is a series in which next number is a sum of previous two numbers.
n = 5
first, second = 0, 1

for i in range(n):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)

print("============")

# mothod 2 (Using Recursive Method)
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
n = 5
for i in range(0, n):
    print(fibonacci(i))