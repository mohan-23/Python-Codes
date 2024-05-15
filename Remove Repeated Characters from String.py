# Using Set and String Concatenation
def remove_duplicates(string):
    unique_chars = set()
    output = ''
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            output += char
    return output

string = 'programming'
print(remove_duplicates(string))
print('-----------')

# Using List and Join
def remove_duplicate(str):
    unique_chars = []
    for char in str:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)

str = 'Hello'
print(remove_duplicate(str))
print('-----------')

## Find all nonrepeating Characters in the String
string = 'Hello Mohan'
freq_dict = {}
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
non_repeating_chars = ''
for char in string:
    if freq_dict[char] == 1:
        non_repeating_chars += char
print('Non-repeating Characters:', non_repeating_chars)

