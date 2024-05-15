# Left Rotation
# method 1 (Using pop() and append())
arr = [1, 2, 3, 4, 5]
arr.append(arr.pop(0))
arr.append(arr.pop(0))
print('After two left rotations:', arr)
print('---------')

# method 2 (Slicing)
arr = [1, 2, 3, 4, 5]
arr = arr[2:] + arr[:2]
print("After two left rotations:", arr)
print('----------')

# method 3 (Using For Loop)
arr = [1, 2, 3, 4, 5]
for i in range(2):
    temp = arr[0]
    for j in range(len(arr)-1):
        arr[j] = arr[j+1]
    arr[-1] = temp
print('After two left rotation:', arr)
print('--------')

# Right Rotation on Array elements by two positions
arr = [1, 2, 3, 4, 5, 6]
for i in range(2):
    temp = arr[len(arr)-1]
    for j in range(len(arr)-1, -1, -1):
        arr[j] = arr[j-1]
    arr[0] = temp
print('After performing right rotation:')
print(arr)