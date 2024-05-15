# method 1 (Using + Operator)
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
merged_arr = arr1 + arr2
print(merged_arr)
print('---------')

# method 2 (Using append() Method)
for num in arr2:
    arr1.append(num)
print('After merge:', arr1)
print('--------')

# method 3 (Using extend() Method)
arr1 = [1, 2, 3]
arr1.extend(arr2)
print('Merge:', arr1)
