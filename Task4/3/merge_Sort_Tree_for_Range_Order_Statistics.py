# Merge Sort Tree for Range Order Statistics

# kthSmallest(start, end, k) : Find the Kth smallest
#                              number in the range from array
#                              index 'start' to 'end'.

# Examples:
# Input : arr[] = {3, 2, 5, 1, 8, 9|
#      Query 1: start = 2, end = 5, k = 2
#      Query 2: start = 1, end = 6, k = 4
# Output : 2
#          5
# Explanation:
# [2, 5, 1, 8] represents the range from 2 to
# 5 and 2 is the 2nd smallest number

# in the range[3, 2, 5, 1, 8, 9] represents
# the range from 1 to 6 and 5 is the 4th
# smallest number in the range

arr = [3, 2, 5, 1, 8, 9]
# query_1 = [2,5,2]
query_1 = [1,6,4]
if query_1[1] > len(arr) or (query_1[1] - query_1[0] + 1) < query_1[2]:
    print('Kth element is not present')
else:
    temp = arr[query_1[0] - 1:query_1[1]]
    temp.sort()
    print(temp[query_1[2] - 1])

