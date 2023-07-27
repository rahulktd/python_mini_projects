# Minimum number of jumps to reach end

# Given an array arr[] where each element represents the max number of steps that can be made forward from that index.
# The task is to find the minimum number of jumps to reach the end of the array starting from index 0.
# If the end isn’t reachable, return -1.

# nput: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 9 -> 9)
# Explanation: Jump from 1st element to 2nd element as there is only 1 step.
#             Now there are three options 5, 8 or 9.
#             If 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.
#
# Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# Output: 10
# Explanation: In every step a jump is needed so the count of jumps is 10.

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

# to keep track of minimum number of jumps required to reach each index
jumps = [float('inf')] * n
jumps[0] = 0

for i in range(1,n):
    for j in range(i):
        if j + arr[j] >=i:
            jumps[i] = min(jumps[i], jumps[j]+1)
print(jumps[n-1])