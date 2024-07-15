def findIndex(arr, number):
    index = 0
    for num in arr:
        if num == number:
            index = arr.index(num)
    return index
 
arr = [4, 2, 5, 7, 6, 9, 8]
number = 6

index = findIndex(arr, number)
print(index)

