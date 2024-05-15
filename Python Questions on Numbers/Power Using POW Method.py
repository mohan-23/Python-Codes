# method 1 (Using POW Method)
base = 2
exponent = 3
print(base, "to power", exponent, "=", end=" ")
print(pow(base, exponent))

# method 2 (Using **)
result = base ** exponent
print(result)

# method 3 (Using For Loop)
power = 1
for i in range(exponent):
    power *= base
print(power)

# method 4 (Using While Loop)
results = 1
while exponent != 0:
    results = base * results
    exponent -= 1
print(results)