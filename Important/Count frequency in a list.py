def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency



array = [1, 3, 2, 4, 1, 5, 4, 3, 1]
frequency_count = count_frequency(array)
print(frequency_count)