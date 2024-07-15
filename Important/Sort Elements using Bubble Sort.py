# Write a program to sort a list of elements using the bubble sort algorithm.

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


nums = [3, 5, 1, 2, 4]
bubble_sort(nums)
print(nums)