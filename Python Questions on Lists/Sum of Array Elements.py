# method 1 (Using Iteration)
arr = [1, 2, 3, 4]
sum = 0
for item in arr:
    sum += item
print(arr, 'sum =', sum)

# metho 2 (Using sum() Function)
arr = [1, 2, 3, 4]
sum_array = sum(arr)
print(sum(arr))
print(arr, 'sum =', sum_array)