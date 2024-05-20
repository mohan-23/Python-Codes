# Write a program to sort a list of elements using the bubble sort algorithm.

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [3, 5, 1, 2, 4]
bubble_sort(nums)
print(nums)