# Find a peak element which is not smaller than its neighbours

# Given an array arr[] of integers.
# Find a peak element i.e. an element that is not smaller than its neighbors.
#
# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)
start = 0
end = n-1
while start < end:
    mid = start + (end-start)//2

    if arr[mid] > arr[mid+1]:
        end = mid
    else:
        start = mid + 1

print(arr[end])