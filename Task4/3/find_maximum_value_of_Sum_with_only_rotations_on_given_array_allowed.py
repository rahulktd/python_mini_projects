# Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

# Given an array arr[] of size N,
# the task is to find the maximum possible sum of i*arr[i]
# when the array can be rotated any number of times.

# Input: arr[] = {1, 20, 2, 10}
# Output: 72.We can get 72 by rotating array twice.
# {2, 10, 1, 20}
# 20*3 + 1*2 + 10*1 + 2*0 = 72
#
# Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Output: 330
# We can get 330 by rotating array 9 times.
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
# 0*1 + 1*2 + 2*3 … 9*10 = 330

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array_sum = 0

#stores sum of arr[i]*index
current_sum = 0

n = len(arr)

for i in range(0,n):
    array_sum += arr[i]
    current_sum += (i * arr[i])

maximum_value = current_sum

for j in range(1,n):
    current_sum += array_sum - n * arr[n-j]
    if current_sum > maximum_value:
        maximum_value = current_sum
print(maximum_value)
