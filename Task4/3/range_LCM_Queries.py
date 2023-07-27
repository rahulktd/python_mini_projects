# Range LCM Queries

# Given an array arr[] of integers of size N and an array of Q queries, query[],
# where each query is of type [L, R] denoting the range from index L to index R,
# the task is to find the LCM of all the numbers of the range for all the queries.

# Input: arr[] = {5, 7, 5, 2, 10, 12 ,11, 17, 14, 1, 44}
# query[] = {{2, 5}, {5, 10}, {0, 10}}
# Output: 60,15708, 78540
# Explanation: In the first query LCM(5, 2, 10, 12) = 60
# In the second query LCM(12, 11, 17, 14, 1, 44) = 15708
# In the last query LCM(5, 7, 5, 2, 10, 12, 11, 17, 14, 1, 44) = 78540
#
# Input: arr[] = {2, 4, 8, 16}, query[] = {{2, 3}, {0, 1}}
# Output: 16, 4

from  math import gcd

arr = [5, 7, 5, 2, 10, 12 ,11, 17, 14, 1, 44]
queries = [[2,5],[5,10],[0,10]]
results = []
for query in queries:
    l,r = query
    lcm_val = arr[l]
    for i in range(l+1,r+1):
        lcm_val = (lcm_val * arr[i]) // gcd(lcm_val, arr[i])
    results.append(lcm_val)
print(results)