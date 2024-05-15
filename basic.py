m = 2
n = 8

if m > n:
    max = m
else:
    max = n

while True:
    if (max % m == 0) and (max % n == 0):
        lcm = max
        break
    max += 1
print(max)
print('-----------')

a = 2
b = 8

if a > b:
    maximum = a
else:
    maximum = b

lcm_found = False
for i in range(maximum, (a*b+1)):
    if not lcm_found:
        if (i % a == 0) and (i % b == 0):
            lcm_found = True
            lcm = i
print(lcm)
print('------------')


i = 8
j = 2

if i > j:
    small = j
else:
    small = i

for k in range(1, small+1):
    if ((i % k == 0) and (j % k == 0)):
        gcd = k
print(gcd)
print('-----------------')

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 8
b = 6

result = gcd(a, b)
print(result)