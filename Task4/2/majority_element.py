# Majority Element

# Find the majority element in the array.
# A majority element in an array A[] of size n
# is an element that appears more than n/2 times
# (and hence there is at most one such element).

# Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size.

# Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is greater than the half of the size of the array size.

arr = [3, 3, 0, 2, 4, 4, 2, 4]
n = len(arr)
max_count = 0
index = -1
for i in range(n):
    count = 1
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            count += 1
    if count > max_count:
        max_count = count
        index = i
if max_count >= n//2:
    print(arr[index])
else:
    print('No majority elements')