arr = [-1,4,-2,1,-3,-4,2,4]
arr = list(set(arr))

maxSum = 0
maxTemp = 0
for i in range(len(arr)):
    maxTemp += arr[i]
    if maxTemp < 0:
        maxTemp = 0
    if maxSum < maxTemp:
        maxSum = maxTemp
print(maxSum)