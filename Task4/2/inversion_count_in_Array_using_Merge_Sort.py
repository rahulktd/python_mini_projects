# Inversion count in Array using Merge Sort

# Inversion Count for an array indicates – how far (or close) the array is from being sorted.
# If the array is already sorted, then the inversion count is 0,
# but if the array is sorted in reverse order, the inversion count is the maximum.
#
# Given an array arr[]. The task is to find the inversion count of arr[].
# Where two elements arr[i] and arr[j] form an inversion if a[i] > a[j] and i < j.

# Examples:
#     Input: arr[] = {8, 4, 2, 1}
#     Output: 6
#     Explanation: Given array has six inversions: (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

arr = [8,4,2,1]
n =len(arr)
inversion_count = 0
for i in range(n):
    for j in range(i+1,n):
        if (arr[i] > arr[j]):
            inversion_count += 1
print(inversion_count)