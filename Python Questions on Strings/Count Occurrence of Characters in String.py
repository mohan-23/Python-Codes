# method 1 (Using For Loop)
string = 'occurrence'
char = 'e'
count = 0
for i in range(len(string)):
    if string[i] == char:
        count += 1
print("Total Number of occurrence of", char, 'is:', count)
print('------------')

# method 2 (Using While Loop)
str = 'character'
char = 't'
index, count = 0, 0
while (index < len(str)):
    if str[index] == char:
        count += 1
    index += 1
print("Total Number of occurrence of", char, 'is:', count)