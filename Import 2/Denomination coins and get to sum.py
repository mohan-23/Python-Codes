import sys

def coinChange(rupees, sum):
    if sum == 0:
        return 0
    if sum < 0:
        return sys.maxsize
    coins = sys.maxsize
    for coin in rupees:
        result = coinChange(rupees, sum-coin)
        if result != sys.maxsize:
            coins = min(coins, result + 1)
    return coins


rupees = [1,2,3,4,5]
sum = 16

coins_sum = coinChange(rupees, sum)
print(coins_sum)