# method 1 (To Compare String ==)
string = 'MADAM'
if (string == string[::-1]):
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")
print("------------")

# method 2 (Using For Loop and Method)
def is_palindrome(string):
    for i in range(0, len(string)//2):
        print(i)
        if string[i] != string[len(string)-i-1]:
            return False
        return True
    

string = 'MADAM'
if is_palindrome(string):
    print("String is a palindrome")
else:
    print("String is not a palindrome")