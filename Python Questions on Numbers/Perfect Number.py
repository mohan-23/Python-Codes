# A Perfect Number is a positive integer that is equal to the sum of its 
#positive divisors, 
# excluding the number itself. (1+2+3 = 6)
num = 6
sum = 0
for i in range(1, (num//2) + 1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i

if sum == num:
    print("Given Number is a Perfect Number")
else:
    print("Given Number is a not a Perfect Number")