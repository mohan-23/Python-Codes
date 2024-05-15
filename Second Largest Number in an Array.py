# Second Largest Number in Array
arr = [2, 5, 6, 8, 4]
sorted_arr = sorted(arr)
for i in range(len(sorted_arr)-1, 0, -1):
    if sorted_arr[i] != sorted_arr[i-1]:
        print(sorted_arr[i-1])
        break
print('----------')

# Find Two Largest Numbers in Array
arr = [2, 5, 6, 8, 4]
sorted_arr = sorted(arr)
for i in range(len(sorted_arr)-1, 0, -1):
    if sorted_arr[i] != sorted_arr[i-1]:
        print(sorted_arr[i-1], 'and', sorted_arr[i])
        break