array = [1, 2, 3, 4]
num = 4
array.remove(num)
print(array)
print('-----------')

# Delete last Element of an Array
arr = [1, 2, 3, 5, 8]
removed_item = arr.pop()
print(removed_item)
print(arr)
print('-----------')

# Delete Element at given index in Array (using pop() method)
arrr = [1, 4, 6, 9, 3]
index = 2
arrr.pop(index)
print(arrr)
print('----------')

# (Using del Keyword)
array = [2, 6, 4, 9, 1]
index = 1
del array[index]
print(array)
print('---------')

# (Using Slicing Keyword)
arr = [1, 2, 3, 4, 5, 6]
arr = arr[:2] + arr[3:]
print(arr)
