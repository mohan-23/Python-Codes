# Write a program to find largest number in a list

# Method 1
def find_largest(arr):
    largest = arr[0]
    smallest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest
    

arr = [12, 23, 16, 30]
largest_num = find_largest(arr)
print(f'Largest number {largest_num}')

# Method 2
array = [2, 5, 7, 9]
print(max(array))
