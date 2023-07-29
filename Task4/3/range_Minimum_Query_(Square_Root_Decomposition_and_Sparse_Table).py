# Range Minimum Query (Square Root Decomposition and Sparse Table)

# We have an array arr[0 . . . n-1].
# We should be able to efficiently find the minimum value
# from index L (query start) to R (query end) where 0 <= L <= R <= n-1.
# Consider a situation when there are many range queries.

# Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
#         query[] = [0, 4], [4, 7], [7, 8]
#
# Output: Minimum of [0, 4] is 0
#         Minimum of [4, 7] is 3
#         Minimum of [7, 8] is 12


arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
MAX = 500

lookup = []

#  list with MAX rows and MAX columns
for i in range(MAX):
    inner_list = []

    # add 0 'MAX times to each row
    for j in range(MAX):
        inner_list.append(0)

    lookup.append(inner_list)

# Fills lookup array --> lookup[n][n]

n = len(arr)

for i in range(n):
    lookup[i][i] = i

for i in range(n):
    for j in range(i + 1, n):

        # To find minimum of [0,4], we compare
        # minimum of arr[lookup[0][3]] with arr[4]

        if arr[lookup[i][j - 1]] < arr[j]:
            lookup[i][j] = lookup[i][j - 1]
        else:
            lookup[i][j] = j
q = [(0, 4), (4, 7), (7, 8)]
m = len(q)

for i in range(m):

    # Left and right
    # of current range

    L = q[i][0]
    R = q[i][1]
    print("Minimum of [" + str(L) + ", " +
          str(R) + "] is " +
          str(arr[lookup[L][R]]))