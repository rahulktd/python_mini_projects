# Segregate even and odd numbers using Lomuto’s Partition Scheme

# Input: arr[] = {7, 2, 9, 4, 6, 1, 3, 8, 5}
# Output: 2 4 6 8 7 9 1 3 5

# odd numbers at the end of the array

# arr = [7, 2, 9, 57, 76, 87, 4, 6, 1, 3, 8, 5]
arr = [1, 3, 2, 4, 7, 6, 9, 10]

n = len(arr)

pivot = arr[- 1]

i = 0

for j in range(n):
    if arr[j] % 2 == 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
print(arr)

