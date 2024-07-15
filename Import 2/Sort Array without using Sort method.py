# Using Booble Sort Method (1)
array = [2, 5, 3, 4, 7, 6, 1, 8]

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

#print(array)
print('***********2')

# Using Sort with Lambda (2)
arr = [2, 5, 3, 4, 7, 6, 1, 8]

arr.sort(key=lambda arr: arr)
#print(arr)
print('************3')

# Use While with comparision (3)
list_a = [2, 5, 3, 4, 7, 6, 1, 8]
new_list = []
while list_a:
    minimum = list_a[0]
    for num in list_a:
        if num < minimum:
            minimum = num
    new_list.append(minimum)
    list_a.remove(minimum)
#print(new_list)
print('************4')

# Using While with min (4)
list_b = [2, 5, 3, 4, 7, 6, 1, 8]
new_list1 = []
while list_b:
    new_list1.append(min(list_b))
    list_b.remove(min(list_b))
#print(new_list1)
print('***********5')

# Using For with min
list_c = [2, 5, 3, 4, 7, 6, 1, 8]
new_arr = []
for i in range(len(list_c)):
    num = min(list_c)
    new_arr.append(num)
    list_c.remove(num)
print(new_arr)




# Sort list of list, Sort by second index (3)
from operator import itemgetter
test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]

result = sorted(test_list, key=itemgetter(1))
#print(result)
print('*********4')

# Sorting dictionary by key
myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

list_keys = list(myDict.keys())
list_keys.sort()
sorted_dict = {i: myDict[i] for i in list_keys}
#print(sorted_dict)