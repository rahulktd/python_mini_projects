# Merge an array of size n into another array of size m+n

# There are two sorted arrays. First one is of size m+n containing only m elements.
# Another one is of size n and contains n elements.
# Merge these two arrays into the first array of size m+n such that the output is sorted.


NA = -1
arr_m_n = [2, 8, NA, NA, NA, 13, NA, 15, 20]
arr_n = [5, 7, 9, 25]
n = len(arr_n)
m = len(arr_m_n) - n

j = m + n - 1
for i in range(m + n - 1, -1, -1):
    if arr_m_n[i] != NA:
        arr_m_n[j] = arr_m_n[i]
        j -= 1

i, j, k = n, 0, 0
while k < (m + n):
    if j == n or (i < (m + n) and arr_m_n[i] <= arr_n[j]):
        arr_m_n[k] = arr_m_n[i]
        k += 1
        i += 1
    else:
        arr_m_n[k] = arr_n[j]
        k += 1
        j += 1

for i in range(m + n):
    print(arr_m_n[i], " ", end="")
print()
