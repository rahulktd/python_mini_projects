# Sort a nearly sorted (or K sorted) array

# Given an array of N elements,
# where each element is at most K away from its target position,
# devise an algorithm that sorts in O(N log K) time.

# Examples:
#     Input: arr[] = {6, 5, 3, 2, 8, 10, 9}, K = 3
#     Output: arr[] = {2, 3, 5, 6, 8, 9, 10}

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
n = len(arr)
for i in range(1,n):
    key = arr[i]
    j = i - 1

    while j >= max(0, i-k) and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

for i in range(n):
    print(arr[i], end=' ')