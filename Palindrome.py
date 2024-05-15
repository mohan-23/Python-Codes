# A Plindrome number is a number which reverse is equal to the original number means number itself.
# method 1 (Using Iterative Method)
num = 121
reverse, temp = 0, num
while temp != 0:
    reverse = reverse*10 + temp%10
    temp = temp // 10

if reverse == num:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

# method 2 (Using Recursive Method)
def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num%10) + str(reverse(num//10)))
    
def is_palindrome(num):
    if num == reverse(num):
        return 1
    return 0

num = 121
if is_palindrome(num) == 1:
    print("Number is a Palindrome")
else:
    print("Number is not a Palindrome")