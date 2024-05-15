# method 1 (Using While Loop)
n = 12345
print(n)

reverse = 0 
while n != 0:
    reverse = reverse*10 + n%10
    n = n//10
    
print(reverse)

# method 2 (Using String Slicing)
n = 12345
result = int(str(n)[::-1])
print(result)

# method 3 (Using Recursion)
def reverse(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**(len(str(n))-1) + reverse(n // 10)
n = 12345
reversed_no = reverse(n)
print(reversed_no)

