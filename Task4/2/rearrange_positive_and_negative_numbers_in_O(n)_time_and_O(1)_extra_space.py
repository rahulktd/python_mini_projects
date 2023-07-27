# Rearrange positive and negative numbers in O(n) time and O(1) extra space.

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
i = -1

for j in range(n):
    if arr[j]<0:
        i +=1
        arr[i],arr[j] = arr[j],arr[i]

pos, neg = i+1, 0
while (pos < n and neg < pos and arr[neg] < 0):
    arr[neg], arr[pos] = arr[pos],arr[neg]
    pos += 1
    neg += 2

print(arr)

# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# n = len(arr)
# x = 0
# for i in range(n):
#     if arr[i] < 0:
#         arr[i],arr[x] = arr[x],arr[i]
#         x +=1
# positive = x
# if x > 0:
#         negative = 1
# else:
#     negative = 0
# while positive < n and negative < positive and arr[negative] < 0:
#     arr[negative],arr[positive] = arr[positive], arr[negative]
#     positive +=1
#     negative +=2
# print(arr)