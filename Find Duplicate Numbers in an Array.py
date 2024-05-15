# method 1
arr, occur = [], []
n = 5
for x in range(n):
    occur.append(0)

for x in range(n):
    element = int(input("Enter Input: "))
    arr.append(element)
    occur[arr[x]] = occur[arr[x]] + 1

for x in range(n):
    if occur[x] > 1:
        print(f"{x} is repeated {occur[x]} times")
print('-----------')

# method 2
array = [2, 2, 3, 1, 4]
occurr = [0, 0, 0, 0, 0]
L = len(array)

for x in range(L):
    occurr[array[x]] = occurr[array[x]] + 1

for x in range(L):
    if occurr[x] > 1:
        print(f"{x} is repeated {occurr[x]} times")
print('---------')

# method 3 
array = [1, 2, 1, 2, 4]
for x in array:
    if array.count(x) > 1:
        print(x)