# In List largest three numbers
n = 3
array = [1, 2, 3, 4]
values = [0]*n
for num in array:
    k=n
    for i in range(n):
        if num <= values[i]:
            k = i
            break
    if k:
        k -= 1
        for j in range(k):
            values[j] = values[j+1]
        values[k] = num

print(values)
print('************2')

# kth largest number
def largest(array, n, k):
    return array[n-k]

def find_largest(arr, n, k):
    array = []
    for i in range(n):
        array.append(min(arr))
        arr.remove(min(arr))
    return largest(array, n, k)

arr = [3, 4, 2, 5, 7, 8]
n = len(arr)
k = 3

largest = find_largest(arr, n, k)
print(largest)



