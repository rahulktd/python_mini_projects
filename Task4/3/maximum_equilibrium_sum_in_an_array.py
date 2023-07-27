# Maximum equilibrium sum in an array

# Given an array arr[].
# Find the maximum value of prefix sum which is also suffix sum for index i in arr[].

# Input : arr[] = {-1, 2, 3, 0, 3, 2, -1}
# Output : 4
# Prefix sum of arr[0..3] =
#             Suffix sum of arr[3..6]
#
# Input : arr[] = {-2, 5, 3, 1, 2, 6, -4, 2}
# Output : 7
# Prefix sum of arr[0..3] =
#               Suffix sum of arr[3..7]

arr = [-2, 5, 3, 1, 2, 6, -4, 2]
n = len(arr)

track_max = float('-inf')
for i in range(n):
    prefix_total = sum(arr[:i + 1])
    suffix_total = sum(arr[i:])

    if prefix_total == suffix_total:
        track_max = max(track_max,prefix_total)
print(track_max)

