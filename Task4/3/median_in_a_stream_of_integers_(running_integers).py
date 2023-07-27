# Median in a stream of integers (running integers)

# Given that integers are read from a data stream.
# Find the median of elements read so for in an efficient way.
# For simplicity assume, there are no duplicates.

# For example, let us consider the streams 5, 15, 1, 3
# After reading 1st element of stream - 5 -> median - 5
# After reading 2nd element of stream - 5, 15 -> median - 10
# After reading 3rd element of stream - 5, 15, 1 -> median - 5
# After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

# Making it clear, when the input size is odd, we take the middle element of sorted data.
# If the input size is even, we pick the average of the middle two elements in the sorted stream.

arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
n = len(arr)
p = [arr[0]]
print("Median after reading 1 element is", arr[0])
for i in range(1,n):
    num = arr[i]
    low, high = 0, i-1

    while low <= high:
        mid = (low+high)//2
        if num == p[mid]:
            posit = mid +1
            break
        elif num > p[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        posit = low

    p.insert(posit,num)
    count = i + 1
    if count % 2 != 0:
        median = p[count // 2] / 1
    else:
        median = (p[(count // 2) - 1] + p[count // 2]) / 2

    print(f"Median after reading {i + 1} elements is {median}")