# Find the Number Occurring Odd Number of Times

arr = [1, 2, 3, 2, 3, 1, 3]
n = len(arr)
found = False

for i in range(0,n):
    count = 0
    for j in range(0, n):
        if arr[i] == arr[j]:
            count += 1

    if (count % 2 != 0):
        print(arr[i])
        found = True

if not found:
    print("Not found")