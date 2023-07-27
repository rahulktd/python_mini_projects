# Two Pointers Technique

# Two pointers is really an easy and effective technique
# that is typically used for searching pairs in a sorted array.
#
# Given a sorted array A (sorted in ascending order), having N integers,
# find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

# A[] = {10, 20, 35, 50, 75, 80}
# X = =70
# i = 0
# j = 5
#
# A[i] + A[j] = 10 + 80 = 90
# Since A[i] + A[j] > X, j--
# i = 0
# j = 4
#
# A[i] + A[j] = 10 + 75 = 85
# Since A[i] + A[j] > X, j--
# i = 0
# j = 3
#
# A[i] + A[j] = 10 + 50 = 60
# Since A[i] + A[j] < X, i++
# i = 1
# j = 3
# m
# A[i] + A[j] = 20 + 50 = 70
# Thus this signifies that Pair is Found.


# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if arr[i] + arr[j] == x:
#             print(arr[i],'+',arr[j],'=',x)
#         if arr[i] + arr[j] > x:
#             break

arr = [10, 20, 35, 50, 75, 80]
x = 70
n = len(arr)
first_pointer = 0
second_pointer = n-1
found = False

while first_pointer < second_pointer:
    if arr[first_pointer] + arr[second_pointer] == x:
        print(arr[first_pointer],'+',arr[second_pointer],'=',x)
        found = True
        first_pointer += 1
        second_pointer -= 1

    elif arr[first_pointer] + arr[second_pointer] < x:
        first_pointer += 1

    else:
        second_pointer -= 1
if not found:
    print("No pair found with given total", x)

