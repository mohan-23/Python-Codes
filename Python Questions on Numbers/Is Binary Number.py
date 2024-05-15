num = 10001000100013
while num>0:
    j = num % 10
    if j != 0 and j != 1:
        print("Num is not Binary")
        break
    num = num // 10
    if num == 0:
        print("Num is Binary")