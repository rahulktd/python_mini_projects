# # Find Subarray with given sum | Set 1 (Non-negative Numbers)
#
# arr = [1,4,20,3,10,5]
# sum = 33
# n = len(arr)
# for i in range(n):
#     current_sum = arr[i]
#     if current_sum == sum:
#         print(i)
#     else:
#         for j in range(i+1,n):
#             current_sum += arr[i]
#             if current_sum == sum:
#                 print(i,j)
#

arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
n = len(arr)

for i in range(n):
    current_sum = arr[i]

    if current_sum == target_sum:
        print(i)
    else:
        for j in range(i + 1, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                print(i, j)
                break
