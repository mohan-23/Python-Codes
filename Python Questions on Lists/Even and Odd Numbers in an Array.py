arr = [2, 3, 5, 4, 6, 7, 11]

even_nums = ''
odd_nums = ''
for num in arr:
    if num % 2 == 0:
        even_nums += str(num) + " "
    else:
        odd_nums += str(num) + " "
        
print('Even Numbers:', even_nums)
print('Odd Numbers:', odd_nums)