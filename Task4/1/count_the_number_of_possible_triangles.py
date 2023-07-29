# Count the number of possible triangles

arr = [4, 6, 3, 7]
n = len(arr)
count = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (arr[i] + arr[j] > arr[k]
            and arr[i] + arr[k] > arr[j]
            and arr[k] + arr[j] > arr[i]):
                count += 1
print(count)
