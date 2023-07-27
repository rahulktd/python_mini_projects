# Find the largest three distinct elements in an array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr[-2])

# another method
array1 = [1, 2, 3, 4, 5, 6, 7]
first = second = float('-inf')
for x in array1:
    if x > first:
        second = first
        first = x
    elif x > second and x != first:
        third = second
        second = x
print(second)


# arr2 = [5,8,9,9.5]
# n = len(arr2)
# f = 0
# s = 0
# for i in range(1, n):
#     if arr2[i] > f:
#         f = i
# for i in range(1, n):
#     if arr2[i] != f and arr2[i] > s:
#         s = i
# print(arr2[s])