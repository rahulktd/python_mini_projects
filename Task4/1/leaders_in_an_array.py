# Leaders in an array

# An element is a leader if it is greater than all the elements to its right side.
# And the rightmost element is always a leader.

# Input: arr[] = {16, 17, 4, 3, 5, 2},
# Output: 17, 5, 2

arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
leaders = []
for i in range(n):
    for j in range(i+1, n):
        if arr[i] <= arr[j]:
            break
    if j == n-1:
        leaders.append(arr[i])

print(leaders)