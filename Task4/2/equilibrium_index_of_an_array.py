# Equilibrium index of an array

# Given a sequence arr[] of size n,
# Write a function int equilibrium(int[] arr, int n)
# that returns an equilibrium index (if any) or -1 if no equilibrium index exists.

# The equilibrium index of an array is an index such that
# the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# Examples:
#     Input: A[] = {-7, 1, 5, 2, -4, 3, 0}
#     Output: 3
#     3 is an equilibrium index, because:
#     A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

arr = [1,2,3]
n = len(arr)
left_sum = 0
right_sum = 0
found = False

for i in range(n):
    left_sum = 0
    right_sum = 0

    for j in range(i):
        left_sum += arr[j]

    for j in range(i+1,n):
        right_sum += arr[j]

    if left_sum == right_sum:
        found = True
        print(i)
        break

if not found:
    print(-1)