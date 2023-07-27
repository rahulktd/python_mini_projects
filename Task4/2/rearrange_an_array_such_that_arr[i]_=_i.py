# Rearrange an array such that arr[i] = i

arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
# arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)
for i in range(n):
    for j in range(n):
        if i == arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
for i in range(n):
    if arr[i] != i:
        arr[i] = -1
print(arr)