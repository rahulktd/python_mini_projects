def findSubarrays(arr,start,end):
    if end == n:
        return
    elif start > end:
        return findSubarrays(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return findSubarrays(arr,start+1,end)



arr = [1, 2, 3]
n = len(arr)
start = 0
# end = n - 1
end = 0
findSubarrays(arr, start, end)