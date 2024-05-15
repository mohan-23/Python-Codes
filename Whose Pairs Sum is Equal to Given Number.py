def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 12
result = find_pairs(arr, target_sum)
print('All pairs whose sum is equal to', target_sum, 'is: \n', result)