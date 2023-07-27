# Sort an array which contain 1 to n values

array = [109,78.97,45,2,5,8]
n = len(array)
for i in range(n):
    for j in range(i+1,n):
        if array[i] > array[j]:
            array[i],array[j] = array[j],array[i]
print(array)