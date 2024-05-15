# method (Using For Loop)
# A Prime Number is a natural number greater than 1 that can be divided by only 1 and number itself.
n = 7
count = 0
for i in range(2, n//2):
    print(i)
    if n%i == 0:
        count = 1
        break
if count == 1:
    print("Number is not Prime")
else:
    print("Number is Prime")