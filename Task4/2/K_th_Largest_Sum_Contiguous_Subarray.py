# K-th Largest Sum Contiguous Subarray
# Input: a[] = {20, -5, -1}, K = 3
# Output: 14
# Explanation: All sum of contiguous subarrays are (20, 15, 14, -5, -6, -1)
#              so the 3rd largest sum is 14.
arr = [20, -5, -1]
k = 3
n = len(arr)
result = []
for i in range(n):
    total = 0
    for j in range(i,n):
        total += arr[j]
        result.append(total)
result.sort(reverse=True)
print(result[k-1])

