def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
            print(i)
        else:

            n //= i
            print(n)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

num = 24
print("Prime factors of ", num, "are: ", prime_factors(num))
print('----')
print(24%2)