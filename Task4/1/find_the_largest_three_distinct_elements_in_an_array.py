# Find the largest three distinct elements in an array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr[-3:])

# another method
array1 = [1,2,3,4,5,6,7]
first = second = third = float('-inf')
for x in array1:
    if x > first:
        third = second
        second = first
        first = x
    elif x > second and x != first:
        third = second
        second = x
    elif x > third and x != second:
        third = x
print(first,second,third)
