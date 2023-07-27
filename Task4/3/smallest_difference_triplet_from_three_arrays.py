# Smallest Difference Triplet from Three arrays

# Three arrays of same size are given.
# Find a triplet such that maximum – minimum in that triplet is minimum of all the triplets.
# A triplet should be selected in a way such that it should have one number from each of the three given arrays.
#
# If there are 2 or more smallest difference triplets,
# then the one with the smallest sum of its elements should be displayed.
#
#### goal is to find a triplet from three arrays, which have a minimum of max-min
# Examples:
#
# Input: arr1[] = {5, 2, 8}
# arr2[] = {10, 7, 12}
# arr3[] = {9, 14, 6}
# Output: 7, 6, 5
#### difference between max and min is 2, it is the minimum difference triplet
#
# Input: arr1[] = {15, 12, 18, 9}
# arr2[] = {10, 17, 13, 8}
# arr3[] = {14, 16, 11, 5}
# Output: 11, 10, 9

arr1 = [5, 2, 8]
arr2 = [10, 7, 12]
arr3 = [9, 14, 6]
n = len(arr1)

arr1.sort()
arr2.sort()
arr3.sort()

minimum = 0
middle = 0
maximum = 0

i, j, k = 0, 0, 0

difference = float('inf')

while i < n and j < n and k < n:
    total = arr1[i] + arr2[j] + arr3[k]
    current_maximum = max(arr1[i], arr2[j], arr3[k])
    current_minimum = min(arr1[i], arr2[j], arr3[k])

    if difference > current_maximum - current_minimum:
        difference = current_maximum - current_minimum
        maximum = current_maximum
        minimum = current_minimum
        middle = total - (current_maximum + current_minimum)

    if current_minimum == arr1[i]:
        i += 1
    elif current_minimum == arr2[j]:
        j += 1
    else:
        k += 1
print(maximum, ',', middle, ',', minimum)
