# Find all triplets with zero sum
#
# Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
#
# Examples :
#     Input: arr[] = {0, -1, 2, -3, 1}
#     Output: (0 -1 1), (2 -3 1)
#     Explanation: The triplets with zero sum are 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0
#
#     Input: arr[] = {1, -2, 1, 0, 5}
#     Output: 1 -2  1
#     Explanation: The triplets with zero sum is 1 + -2 + 1 = 0

arr = [0, -1, 2, -3, 1]
n = len(arr)
triplet = False
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i] , arr[j] , arr[k])
                triplet =True
if not triplet:
    print("Not exist")