# Find the Missing Number
#
# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.
#
# Note: There are no duplicates in the list.
#
# Examples:
#     Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
#     Output: 5
#     Explanation: The missing number between 1 to 8 is 5

arr = [1, 2, 3, 5]
n =len(arr)
temp = [0]*(n+1)
for i in range(0,n):
    temp[arr[i] - 1] = 1
for i in range(0,n+1):
    if temp[i] == 0:
        ans = i + 1
print(ans)