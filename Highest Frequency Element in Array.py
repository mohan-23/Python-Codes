# Using Dictionary
arr = [1, 2, 3, 4, 5, 7, 5, 8, 5, 9, 5]
freq_dict = {}
for item in arr:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1
highest_frequency_element = max(freq_dict, key=freq_dict.get)
print('Heghest Frequency Element:', highest_frequency_element)