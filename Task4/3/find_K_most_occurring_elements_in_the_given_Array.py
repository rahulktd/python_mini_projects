# Find K most occurring elements in the given Array

# Given an array of N numbers and a positive integer K.
# The problem is to find K numbers with the most occurrences, i.e., the top K numbers having the maximum frequency.
# If two numbers have the same frequency then the number with a larger value should be given preference.
# The numbers should be displayed in decreasing order of their frequencies.
# It is assumed that the array consists of at least K numbers.

# Examples:
#     Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2
#     Output: 4 1
#     Explanation:
#     Frequency of 4 = 2, Frequency of 1 = 2
#     These two have the maximum frequency and 4 is larger than 1.

arr = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
n = len(arr)

# to store element:frequency pair
p = {}

for i in range(n):
    if arr[i] in p:
        p[arr[i]] += 1
    else:
        p[arr[i]] = 1

a = [0] * (len(p))
j = 0
for i in p:
    a[j] = [i, p[i]]
    j += 1
a = sorted(a, key=lambda x: x[0], reverse=True)
a = sorted(a, key=lambda x: x[1], reverse=True)

print(k, "numbers with most occurrences are:")
for i in range(k):
    print(a[i][0], end=" ")
