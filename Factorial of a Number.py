# The factorial of a number is the multiplication of each and every 
# number till the given number except 0.
# method 1 (Using Iterative Method)
num = 5
factorial = 1
if num < 0:
    print("Factorial can't be calculated for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial *= i

print("Factorial of a", num, "is:", factorial)

# method 2 (Using Recursion)
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

num = 6
if num < 0:
    print("Factorial can't be calculated for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of a", num, "is:", fact(num))