# Find the element that appears once in an array where every other element_appears_twice

arr = [2, 3, 5, 4, 5, 3, 4]
n = len(arr)
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        print("Element that appears once is", arr[i])