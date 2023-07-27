# Find the Rotation Count in Rotated Sorted array

# Input: arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation: Initial array must be {2, 3, 6, 12, 15, 18}.
# We get the given array after rotating the initial array twice.

arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
minimum_value = arr[0]
minimum_index = 0
for i in range(n):
    if minimum_value > arr[i]:
        minimum_value = arr[i]
        minimum_index = i
print(minimum_index)