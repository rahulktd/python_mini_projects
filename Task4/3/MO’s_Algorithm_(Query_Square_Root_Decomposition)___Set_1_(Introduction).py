# MO’s Algorithm (Query Square Root Decomposition) | Set 1 (Introduction)

# We are given an array and a set of query ranges,
# we are required to find the sum of every query range.

# Example:
# Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
#         query[] = [0, 4], [1, 3] [2, 4]
# Output: Sum of arr[] elements in range [0, 4] is 8
#         Sum of arr[] elements in range [1, 3] is 4
#         Sum of arr[] elements in range [2, 4] is 6

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
query = [[0,4],[1,3],[2,4]]

# start = query[0][0]
# end = query[0][1]
# a = arr[start:(end+1)]
# print(sum(a))

for q in query:
    L,R = q
    s = 0
    for i in range(L,R+1):
        s += arr[i]
    print(q,'=',s)

