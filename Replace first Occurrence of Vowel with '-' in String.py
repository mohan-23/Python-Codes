def replace_vowel(string):
    vowels = 'aeiouAEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + "-" + string[i+1:]
            break
    return string

string = 'question'
print(string, 'To', replace_vowel(string))
