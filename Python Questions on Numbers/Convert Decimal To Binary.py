# method 1 (Using Loop)
decimal = num = 13
binary = ''
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2
print("Binary number is", binary, "for", decimal)
print('=========')

# method 2 (Using bin() Function)
decimal = 34
binary = bin(decimal)
print("Binary number is", binary[2:], "for", decimal)