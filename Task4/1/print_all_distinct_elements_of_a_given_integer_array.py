# Print All Distinct Elements of a given integer array

arr = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)


# def Distinct(arr, n):
#     for i in range(0, n):
#         d = 0
#         for j in range(0, i):
#             if (arr[i] == arr[j]):
#                 d = 1
#                 break
#         if (d == 0):
#             print(arr[i])
#
# arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
# n = len(arr)
# Distinct(arr, n)
