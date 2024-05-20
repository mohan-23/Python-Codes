# Find the second largest number in list

def fin_largest(nums):
    largest = nums[0]
    second_large = nums[0]
    for num in nums:
        if num > largest:
            second_large = largest
            largest = num
        elif num > second_large and num != largest:
            second_large = num
    return second_large


nums = [3, 6, 5, 8, 9]
second_largest = fin_largest(nums)
print(second_largest)