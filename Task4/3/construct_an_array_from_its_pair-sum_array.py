# Construct an array from its pair-sum array

# Given a pair-sum array and size of the original array (n), construct the original array.
# A pair-sum array for an array is the array that contains sum of all pairs in ordered form.
#
# For example pair-sum array for arr[] = {6, 8, 3, 4}
#                             is    {14, 9, 10, 11, 12, 7}.
#
# In general, pair-sum array for arr[0..n-1] is {arr[0]+arr[1], arr[0]+arr[2], …….,
# arr[1]+arr[2], arr[1]+arr[3], ……., arr[2]+arr[3], arr[2]+arr[4], …., arr[n-2]+arr[n-1}.

pair_sum_array = [15, 13, 11, 10, 12, 10, 9, 8, 7, 5]
n = 5
arr = [0] * n

arr[0] = (pair_sum_array[0] + pair_sum_array[1] - pair_sum_array[n-1]) // 2
for i in range(1,n):
    arr[i] = pair_sum_array[i - 1] - arr[0]
print(arr)
