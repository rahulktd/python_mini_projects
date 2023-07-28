# Given an array (or string), the task is to reverse the array/string.

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
start = 0
end = n - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)