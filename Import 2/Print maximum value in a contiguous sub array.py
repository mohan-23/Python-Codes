numbers = [-2,-3,4,-1,-2,1,5,-3]

maxSum = 0
maxTemp = 0
for i in range(len(numbers)):
    maxTemp += numbers[i]
    if maxTemp < 0:
        maxTemp = 0
    elif maxSum < maxTemp:
        maxSum = maxTemp

print(maxSum)