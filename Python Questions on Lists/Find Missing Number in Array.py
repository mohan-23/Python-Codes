# method 1
array = []
n = 3
for x in range(n-1):
    x = int(input('Enter Input:'))
    array.append(x)
sum = (n*(n+1))/2
sum_arr = 0
for i in range(n-1):
    sum_arr = sum_arr + array[i]
print(int(sum-sum_arr))
print('---------')

# method 2
lists = [1, 2, 3, 5]

L = len(lists)
sum = (L*(L+1))/2
sum_arr = 0
for x in range(L-1):
    sum_arr += lists[x]
print(int(sum-sum_arr))
    