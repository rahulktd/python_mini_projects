# Space optimization using bit manipulations

# Given two numbers say a and b,
# mark the multiples of 2 and 5 between a and b using less than O(|b – a|) space and output each of the multiples.

# Examples :
#
# Input : 2 10
# Output : 2 4 5 6 8 10
#
# Input: 60 95
# Output: 60 62 64 65 66 68 70 72 74 75 76 78
#         80 82 84 85 86 88 90 92 94 95

import math

# a = 2
# b = 10
# n = abs(b - a) + 1
# array = [0] * n
#
# for i in range(a,b+1):
#     if i % 2 == 0 or i % 5 == 0:
#         array[i - a] = 1
# for i in range(a,b+1):
#     if array[i - a] == 1:
#         print(i, end=' ')

a = 2
b = 10

for i in range(a, b + 1):
    if i % 2 == 0 or i % 5 == 0:
        print(i, end=" ")
