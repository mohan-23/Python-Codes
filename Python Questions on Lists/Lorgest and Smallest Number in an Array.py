# method 1
arr = [ 1, 2, 5, 8, 10]
largest = arr[0]
smallest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]
        
print('Smallest:', smallest)
print("Largest:", largest)
print('---------')

# method 2
print('Smallest:', min(arr))
print('Largest:', max(arr))