# Square Root (Sqrt) Decomposition Algorithm

# The key concept of this technique is
# to decompose a given array into small chunks specifically of size sqrt(N)

# For example, one common range query is to find the sum of all numbers within a given range
# (start index to end index). Another query could be finding the maximum or minimum value within the range.
#
# The Square Root Decomposition Algorithm helps us speed up these range queries.
# Instead of processing each query individually
# from scratch (which could be slow for large arrays), we divide the array into smaller blocks.
# Each block contains a fixed number of elements, usually roughly the square root of the array size.

#array of 10000 elements initialised with 0
arr = [0] * 10000

input_array = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]

# copy input_array to arr
arr[:len(input_array)] = input_array

# query(3,8)
l,r = 3,8
_sum = 0
for i in range(l, r+1):
    _sum += arr[i]
print("Sum of elements is",_sum)

# query(1,6)
l,r = 1,6
_sum = 0
for i in range(l, r+1):
    _sum += arr[i]
print("Sum of elements is",_sum)


# query(8,8)
l,r = 8,8
_sum = 0
for i in range(l, r+1):
    _sum += arr[i]
print("Sum of elements is",_sum)

arr[8] = 0
# query(8,8)
l,r = 8,8
_sum = 0
for i in range(l, r+1):
    _sum += arr[i]
print("Sum of elements is",_sum)