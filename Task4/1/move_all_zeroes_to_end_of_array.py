# Move all zeroes to end of array

arr = [5, 6, 0, 4, 6, 0, 9, 80, 0, 0, 8, 0, 0, 6, 8, 0]
l = len(arr)
x = 0
for i in range(l):
    if arr[i] != 0:
        arr[x], arr[i] = arr[i], arr[x]
        x += 1
print(arr)
