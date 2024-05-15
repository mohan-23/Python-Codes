# method 1
arr = [1, 2, 3, 4]
arr.append(5)
print(arr)

# method 2
new_arr = arr + [6]
print(new_arr)

# Insert an Element at a given Location of an Array.
array = [1, 2, 3, 4, 5]
num = 0
index = 2
if index >= len(array):
    print('Enter index smaller than', len(array))
else:
    array.insert(index, num)
print("After inserting", num, 'at index', index, '=\n', array)