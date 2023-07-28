# Largest Sum Contiguous Subarray (Kadane’s Algorithm)

# Given an array arr[] of size N.
# The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.

arr= [-2, -3, 4, -1, -2, 1, 5, -3]
maximum_till_now = float('-inf')
maximum_ending_here = 0

for i in arr:
    maximum_ending_here = maximum_ending_here + i
    maximum_till_now = max(maximum_till_now, maximum_ending_here)

    if maximum_ending_here < 0:
        maximum_ending_here = 0
        
print(maximum_till_now)