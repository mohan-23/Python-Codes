# method 1 (LCM of Two Numbers)
num1 = 9
num2 = 18

if num1 > num2:
    greater = num1
else:
    greater = num2
while (True):
    if ((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1
print("LCM of", num1, "and", num2, "=", greater)
print('-----------')

# method 2
m=12
n=8

if m>n:
    big_num = m
else:
    big_num = n

lcm_found=False

for i in range(big_num, (m * n + 1)):
    if not lcm_found:
        if (i % m == 0) and (i % n == 0):
            lcm_found=True
            lcm=i
print(lcm)
print('------------')

# method 1 (GCD or HCF of Two Numbers) (Using Iteration Method)
num1 = 8
num2 = 2
if num1 > num2:
    minimum = num2
else:
    minimum = num1
for i in range(1, minimum+1):
    if ((num1 % i == 0) and (num2 % i == 0)):
        hcf = i
print("hcf/gcd of", num1, "and", num2, "=", hcf)
print("------------")

# method 2 (Using Recursion Method)
def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

num1 = 8
num2 = 6
print("hcf/gcd of", num1, "and", num2, "=", gcd(num1, num2))