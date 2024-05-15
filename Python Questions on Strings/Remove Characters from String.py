# method 1 (Using Replace Method)
str = 'I am Mohan'
char = 'a'
print(str.replace(char, " "))
print('----------')

# method 2 (Using Translate Method)
def remove_char(s1, s2):
    dict = {ord(s2): None}
    print(s1.translate(dict))

s1 = 'question'
s2 = 'e'
remove_char(s1, s2)
print("-------------")

# method 3
string = "Mohan"
char = 'o'
new_string = ""
for chr in string:
    if chr == char:
        chr = ""
    else:
        new_string += chr
print(new_string)

