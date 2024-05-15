def main(a):
    a = a + '2'
    a = a * 2
    return a

#print(main('Python'))  /  Python2Python2

#==============

res = (lambda x, y: x * y)(2, 2)
#print(res)   / 4

#==============

list_1 = [1, 2, 4, 6]
list_2 = list_1

list_2[0] = 'A'

#print(list_1)  /  ['A', 2, 4, 6]
#print(list_2)  /  ['A', 2, 4, 6]

#===============

list = [1, 2, 3, 4, 5]

#print(min(list))  / 1
#print(max(list))  / 5

min = list[0]
max = list[0]

for i in range(len(list)):
    if list[i] < min:
        min = list[i]

    if list[i] > max:
        max = list[i]

#print(min)  / 1
#print(max)  / 5

#============

lists = [10, 20, 30, 40]
#print(sum(lists))  / 100

result = 0

for item in lists:
    result += item

#print(result)  / 100

#==============

# Count the Number
list = [ 1, 1, 2, 3, 4, 4, 5, 4, 6]
#print(list.count(4))  / 3

num = 4
count = 0

for item in list:
    if item == num:
        count += 1

#print(count)  / 3

#================

def test(x):
    if x == 0:
        return 0
    else:
        return test(x-1)
    
res = test(3)
#print(res)  / 0

#===============

# Item in list or Not
list = [1, 2, 3, 4, 5]
item = 4
#print(item in list)  / True

matchFound = False
for num in list:
    if num == item:
        matchFound = True
        break

#print('Match Found', matchFound)  / Match Found True

#=============

# Find Duplicate items
list = [1, 2, 1, 3, 4, 1, 3, 1, 4]

unqList = []
dupList = []

for num in list:
    if num not in unqList:
        unqList.append(num)
    else:
        if num not in dupList:
            dupList.append(num)

#print(unqList)  / [1, 2, 3, 4]
#print(dupList)  / [1, 3, 4]

#===============

num1 = 1_00  # 100
num2 = 2_0   # 20
#print(num1 * num2)  / 2000

#==============

# Replace Method
x = 'abc'

x.replace('a', '1')
x + 'def'
#print(x)  / abc

x = x.replace('a', '1')
x = x + 'def'
#print(x)  / 1bcdef

#================

# Range Function
x = 1
y = 10

#lst = list(range(x, y))
#print(lst)  / [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Unique Numbers in List
numbers = [ 1, 2, 3, 1, 2, 1, 4]
#print(set(numbers))  / {1, 2, 3, 4}

unqNums = []

for num in numbers:
    if num not in unqNums:
        unqNums.append(num)

#print(unqNums)  / [1, 2, 3, 4]

#===============

x = [x+1 for x in range(3)]
x.reverse() # 3 2 1
x.extend(x)
#print(x)  / [3, 2, 1, 3, 2, 1]

#================

# Multiply list items
list = [1, 2, 3, 4, 5]

result = 1
for item in list:
    result = result * item

#print(result)  / 120

#=================

# List - Swap First & Last
list = [1, 2, 3, 4]

list[0], list[-1] = list[-1], list[0]
#print(list)  / [4, 2, 3, 1]

#==============

list = [1, 2, 3]
list.insert(4,3)
#print(list)  / [1, 2, 3, 3]

#===============

# List to Dictionary
data = ['java', 'Python', 'reactjs']
#print(data)  / ['java', 'Python', 'reactjs']
 
data = {item : len(item) for item in data}
#print(data)  / {'java': 4, 'Python': 6, 'reactjs': 7}  

#================

# Dictionary Remove Items
productData = {
    'title': 'Mac',
    'price': 25000,
    'reviews': 200,
    'rating': 4.5
}

productData.pop('rating')
#print(productData)  / {'title': 'Mac', 'price': 25000, 'reviews': 200}
del productData['price']
#print(productData)  / {'title': 'Mac', 'reviews': 200}
productData.clear()
#print(productData)  / {}

#===================

data = [2, 1, 3]
data.pop(2)
#print(data)  / [2, 1]

#===============

list = [1, 2, 3, 2, 1]
list.remove(2)
#print(list)  / [1, 3, 2, 1]

num = 1
for item in list:
    if item == num:
        list.remove(num)

#print(list)  / [3, 2]

#=================

# Loop List with Index, value
data = ['Python', 'Java', 'HTML']
#print(tuple(enumerate(data)))  / ((0, 'Python'), (1, 'Java'), (2, 'HTML'))

for i, item in enumerate(data):
    pass
    #print(i, item)  /  #0 Python
                        #1 Java
                        #2 HTML
#================

# Move to Last
nums = [1, 1, 2, 3, 4, 1, 2]
#print(nums)  / [1, 1, 2, 3, 4, 1, 2]

for num in nums:
    if num == 1:
        nums.remove(num) 
        nums.append(num)
#print(nums)  / [2, 3, 4, 2, 1, 1, 1]

#================

# Target sum Elements
list = [3, 4, 6, 5, 2, 1]
sum = 9

for n1 in list:
    for n2 in list:
        if n1 + n2 == sum:
            pass
            #print(n1, n2)

sums = []
for a in list:
    for b in list:
        if a + b == sum:
            sums.append((a, b))

#print(sums)  / [(3, 6), (4, 5), (6, 3), (5, 4)]

#===============

# Prime Number
num = 7 # Prime Number

for i in range(2, num):
    if num % i == 0:
        #print(num, 'Not a Prime Number')
        break
else:
    #print(num, 'Prime Number')
    pass

#===================

# Prime Numbers from Range 1 to 100
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
    
primeNumbers = filter(is_prime, range(1, 100))
#print(*primeNumbers)  /  1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

# Find unmatch character position
from itertools import zip_longest

str1 = 'Python'
str2 = 'Pytha'

i = 1
for x, y in zip_longest(str1, str2):
    if x != y:
        #print(x, y, '-', i)  / (o a - 5, n None - 6)
        pass
    i += 1


#================

# Find max length word in list
datas = ['Javascript', 'Java', 'React', "Springboot"]
maxLength = [len(item) for item in datas]
#maxi = max(maxLength)
#print(maxi)

maxChar = []

for item in datas:
    if len(item) == maxLength:
        maxChar.append(item)

print(maxChar)


arr = [1, 2, 3, 4]
print(sum(arr))