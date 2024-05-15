# method 1 (Using While Loop)
num = 153
sum = 0
temp = num

count = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //=10
if num == sum:
    print("Number is Amstrong Number")
else:
    print("Number is not a Amstrong Number")

# method 2 (Using List Comprehension)
num = 153
digits = [int(digit) for digit in str(num)]
print(digits)
count = len(digits)
print(count)
sum = 0
for number in digits:
    sum += number**count

if num == sum:
    print("Number is Amstrong Number")
else:
    print("Number is not a Amstrong Number")

# method 3 (Using For Loop)
n=str(153)
L=len(n)

sum=0
for i in (n):
    sum += (int(i) ** L)
if sum == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")