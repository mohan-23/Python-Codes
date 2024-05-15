# method 1 (Using While Loop)
arr = [1, 2, 3, 4]
L = len(arr)
end_index = L - 1
rev_arr = []

while end_index >= 0:
    rev_arr.append(arr[end_index])
    end_index -= 1

print(rev_arr)
print('----------')

# method 2 
for i in range(L-1, -1, -1):
    print(arr[i], end=" ")
print('\n')
print('----------')

# method 3
print(arr[::-1])