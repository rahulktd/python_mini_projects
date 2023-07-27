# Smallest subarray with sum greater than a given value

# Given an array arr[] of integers and a number x,
# the task is to find the smallest subarray with a sum greater than the given value.

# arr[] = {1, 4, 45, 6, 0, 19}
#    x  =  51
# Output: 3
# Minimum length subarray is {4, 45, 6}

arr = [1, 4, 45, 6, 0, 19]
x = 51
n = len(arr)

min_len = n + 1

for i in range(0,n):
    curr_sum = arr[i]

    if curr_sum > x:
        print(1)

    for j in range(i+1,n):
        curr_sum += arr[j]

        if curr_sum > x and (j-i+1) < min_len:
            min_len = (j-i+1)
print(min_len)