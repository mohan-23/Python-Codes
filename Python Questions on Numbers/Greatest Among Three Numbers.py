# method 1
num1 = 12
num2 = 15
num3 = 20

if num1 >= num2 and num1 >= num3:
    print("Num1 is Greater")
if num2 >= num1 and num2 >=num3:
    print("Num2 is Greater")
if num3 >= num2 and num3 >= num1:
    print("Num3 is Greater")

# method 2 
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)