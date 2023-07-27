# Search an element in a sorted and rotated Array

# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
# Output : Found at index 8

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
target = 10
n = len(arr)
found = False
for i in range(n):
    if arr[i] == target:
        print('The key is at the index',i)
        found = True
        break
if not found:
    print('The key is not found in the array.')