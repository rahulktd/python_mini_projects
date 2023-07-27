# Minimum increment by k operations to make all elements equal

# You are given an array of n-elements,
# you have to find the number of operations needed to make all elements of array equal.
# Where a single operation can increment an element by k.
# If it is not possible to make all elements equal print -1.

# Input : arr[] = {4, 7, 19, 16},  k = 3
# Output : 10

arr = [4, 7, 19, 16]
k = 3
n = len(arr)

maximum = max(arr)
p = 0

for i in range(0,n):
    if (maximum - arr[i]) % k != 0:
        print(-1)
    else:
        p += (maximum - arr[i]) / k

print(int(p))

