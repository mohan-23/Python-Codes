def anagram_check(str1, str2):
    print(sorted(str1))
    print(sorted(str2))
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1 = 'python'
str2 = 'onpyht'
if anagram_check(str1, str2):
    print("Anagram")
else:
    print("Not a Anagram")