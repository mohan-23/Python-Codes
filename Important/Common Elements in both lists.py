# Write a program to find the common elements in both lists

def find_common(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

list_a = [1, 2, 3, 4]
list_b = [4, 5, 6, 7]
common = find_common(list_a, list_b)
print(common)