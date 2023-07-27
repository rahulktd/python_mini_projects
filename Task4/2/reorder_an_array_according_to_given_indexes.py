# Reorder an array according to given indexes

# Input:  arr[]   = [10, 11, 12];
#             index[] = [1, 0, 2];
# Output: arr[]   = [11, 10, 12]
#            index[] = [0,  1,  2]

arr = [10,11,12]
index = [1,0,2]
n = len(arr)
temp = [0]*n
for i in range(n):
    temp[index[i]] = arr[i]

for i in range(n):
    arr[i] = temp[i]
    index[i] = i
print(arr)
print(index)