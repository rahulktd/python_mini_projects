# arr = [1, 2, 3, 4, 5, 6, 7]
# d = 2
#
# N = len(arr)
#
# for i in range(d):
#     temp = arr[0]
#     for j in range(1, N):
#         arr[j - 1] = arr[j]
#     arr[N - 1] = temp
#
# print(arr)

arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
k %= n
arr[0:n] = arr[::-1]
arr[0:k] = arr[0:k][::-1]
arr[k:n] = arr[k:n][::-1]

for i in range(0, len(arr)):
    print(arr[i], end=" ")
