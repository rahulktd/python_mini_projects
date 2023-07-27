# Leaders in an array

arr = [16,17,4,3,5,2]
n = len(arr)
leaders = []
for i in range(n):
    for j in range(i+1,n):
        if arr[i] <= arr[j]:
            break
    if j == n-1:
        leaders.append(arr[i])

print(leaders)