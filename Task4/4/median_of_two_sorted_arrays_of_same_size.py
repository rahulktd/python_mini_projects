# Median of two sorted arrays of same size
#
# There are 2 sorted arrays A and B of size n each.
# Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n).

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]

merged_arr = sorted(arr1+arr2)
n = len(merged_arr)

# if n is even
if n % 2 == 0:
    print('Median =',(merged_arr[n//2 - 1] + merged_arr[n//2])/2)

else:
    print('Median =',merged_arr[n//2])