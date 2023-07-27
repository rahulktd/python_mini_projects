# Merge two sorted arrays with O(1) extra space

# We are given two sorted arrays.
# We need to merge these two arrays
# such that the initial numbers (after complete sorting)
# are in the first array and the remaining numbers are in the second array
#
# Examples:
#     Input: ar1[] = {10}, ar2[] = {2, 3}
#     Output: ar1[] = {2}, ar2[] = {3, 10}
#
#     Input: ar1[] = {1, 5, 9, 10, 15, 20}, ar2[] = {2, 3, 8, 13}
#     Output: ar1[] = {1, 2, 3, 5, 8, 9}, ar2[] = {10, 13, 15, 20}

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
n1 = len(arr1)
n2 = len(arr2)
i,j = 0,0
k = n1-1
while i <= k and j <= n2:
    if arr1[i] < arr2[j]:
        i += 1
    else:
        temp = arr2[j]
        arr2[j] = arr1[k]
        arr1[k] = temp
        j += 1
        k -= 1
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)