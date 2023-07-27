# Find the smallest missing number

# Input: {0, 1, 2, 6, 9}, n = 5, m = 10
# Output: 3
#
# Input: {4, 5, 10, 11}, n = 4, m = 12
# Output: 0
#
# Input: {0, 1, 2, 3}, n = 4, m = 5
# Output: 4
#
# Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
# Output: 8

arr = [0, 1, 2, 3]
m = 5
n = len(arr)
vec = [0]*m

for i in range(n):
    vec[arr[i]] = 1
for i in range(m):
    if vec[i]==0:
        print('Missing number is',i)

