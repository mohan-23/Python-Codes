string = 'hello world ee'
freq_dict = {}
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
    
max_freq = max(freq_dict.values())

for char in freq_dict:
    if freq_dict[char] == max_freq:
        print(char, end=" ")
        