# Find a triplet that sum to a given value

#Given an array and a value,
# find if there is a triplet in array whose sum is equal to the given value.

# array = [12,3,4,1,6,9]
# sum = 24
# output = 12,3,9

arr = [12,3,4,1,6,9]
target = 19
n = len(arr)
exist = False
for i in range(0, n-2):

    for j in range(i+1,n-1):

        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] == target:
                print(arr[i],'+',arr[j],'+',arr[k],'=',target)
                exist = True
if not exist:
    print('No triplets withe the given total')
