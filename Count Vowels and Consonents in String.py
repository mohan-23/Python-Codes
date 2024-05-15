string = "Question1234"
vowels = 0
consonents = 0
for char in string:
    if char in ('a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels += 1
    elif char.isalpha():
        consonents += 1
print('Vowels:', vowels)
print('consonents:', consonents)