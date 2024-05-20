# Write a python programm to check if a string is a pallindrome?

# Method 1
def pallindrome(string):
    rev_string = string[::-1]
    if string == rev_string:
        return True
    else:
        return False


string = 'madam'

if (pallindrome(string)):
    print(f'{string} is a Pallindrome')
else:
    print(f'{string} is not a Pallindrome')

print('**************')


# Method 2

string = 'madam'

reverse_string = ''

for char in string:
    reverse_string = char + reverse_string

if (string == reverse_string):
    print(f'{string} is a pallindrome')
else:
    print(f'{string} is not a pallindrome')

print('***********')

# Method 1

def reverse(number):
    if number < 10:
        return number
    return int(str(number % 10) + str(reverse(number // 10)))

def is_pallindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

num = 121

if is_pallindrome(num):
    print(f'{num} is pallindrome')
else:
    print(f'{num} is not a pallindrome')

print('*************')

# Method 2

num = 121

reverse, temp = 0, num
while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if reverse == num:
    print(f'{num} is pallindrome')
else:
    print(f'{num} is not a pallindrome')