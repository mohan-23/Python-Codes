arr = [2, 1, 2, 3, 4]
count = [0, 0, 0, 0, 0]

new_arr = []
for x in range(len(arr)):
    count[arr[x]] = count[arr[x]] + 1
    if count[arr[x]] > 1:
        new_arr.append(arr[x])
print(new_arr)
print('-----------')

# method 2
array = [1, 2, 3, 1, 2, 5]
duplicate = set()
array.sort()
for x in array:
    if array.count(x) > 1:
        duplicate.add(array[x])
print(*duplicate)
    