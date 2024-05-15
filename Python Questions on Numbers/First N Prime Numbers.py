num = 10
for n in range(1, num):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# Prime Number given Range (Brute Force Method)
import math
m = 4
n = 45
for num in range(m, n+1):
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")