def occurences(array):
    values = {}
    for num in array:
        if num in values:
            values[num] += 1
        else:
            values[num] = 1
    return values


array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = occurences(array)
print(counts)