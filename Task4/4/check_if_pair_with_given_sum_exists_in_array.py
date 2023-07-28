# Given an array A[] of n numbers and another number x,
# the task is to check whether or not there exist two elements in A[] whose sum is exactly x.

# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2

arr = [0, -1, 2, -3, 1]
x = -5

n = len(arr)
found = False

for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] == x:
            found = True
            print('Yes')
if not found:
    print('No')