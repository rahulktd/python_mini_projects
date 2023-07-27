# Sort an array of 0s, 1s and 2s | Dutch National Flag problem

# Given an array A[] consisting of only 0s, 1s, and 2s.
# The task is to write a function that sorts the given array.
# The functions should put all 0s first, then all 1s and all 2s in last.

# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
#
# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)

count_0 = 0
count_1 = 0
count_2 = 0

for i in range(n):
    if arr[i] == 0:
        count_0 += 1

    elif arr[i] == 1:
        count_1 += 1

    elif arr[i] == 2:
        count_2 += 1
i = 0

while count_0 > 0:
    arr[i] = 0
    i += 1
    count_0 -= 1

while count_1 > 0:
    arr[i] = 1
    i += 1
    count_1 -= 1

while count_2 > 0:
    arr[i] = 2
    i += 1
    count_2 -= 1
print(arr)