# Remove duplicates from the list

def remove_duplicates(nums):
    uniques = []
    for num in nums:
        if num not in uniques:
            uniques.append(num)
    return uniques

nums = [1, 4, 1, 3, 5, 6, 3]

unique_nums = remove_duplicates(nums)
print(unique_nums)

