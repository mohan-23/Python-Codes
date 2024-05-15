# method 1 Ascending
string = 'mohan'
str_list = list(string)
sorted_string = ''.join(sorted(str_list))
print(sorted_string)
print('---------')

# Descending
print(''.join(sorted(str_list, reverse=True)))



