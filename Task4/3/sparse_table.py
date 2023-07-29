# Sparse Table

# Example Problem 1 : Range Minimum Query
# We have an array arr[0 . . . n-1].
# We need to efficiently find the minimum value from index L (query start) to R (query end) where 0 <= L <= R <= n-1.
# Consider a situation when there are many range queries.
#
# Example:
#
# Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
#         query[] = [0, 4], [4, 7], [7, 8]
#
# Output: Minimum of [0, 4] is 0
#         Minimum of [4, 7] is 3
#         Minimum of [7, 8] is 12

import math

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(arr)

MAX = 500

lookup = []
# to fill lookup with 0
# creates a list of double the size of MAX with zeros
# it can be used to store minimum values for different range
for j in range(MAX):
    inner_list = []
    for i in range(MAX):
        inner_list.append(0)
    lookup.append(inner_list)

for i in range(n):
    lookup[i][0] = arr[i]

j = 1

while (1 << j) <= n:
    i = 0
    while i <= n - (1 << j):
        # if lookup[i][j - 1] < lookup[i + (1 << (j - 1))][j - 1]:
        #     lookup[i][j] = lookup[i][j - 1]
        # else:
        #     lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
        lookup[i][j] = math.gcd(lookup[i][j - 1], lookup[i + (1 << (j - 1))][j - 1])
        i += 1
    j += 1
# print(lookup[0][3])
# print(lookup[4][7])

L, R = 0, 5
j = int(math.log2(R - L + 1))
result = math.gcd(lookup[L][j], lookup[R - (1 << j) + 1][j])
print(result)
