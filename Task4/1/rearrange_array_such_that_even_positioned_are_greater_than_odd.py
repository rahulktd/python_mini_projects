def sort_array(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

my_array = [5, 2, 8, 1, 9]
sorted_array = sort_array(my_array)
# print(sorted_list)

n = len(sorted_array)
ans = [0] * n
p = 0
q = n - 1
for i in range(n):
    if (i + 1) % 2 == 0:
        ans[i] = sorted_array[q]
        q = q - 1
    else:
        ans[i] = sorted_array[p]
        p = p + 1
for i in range(n):
        print(ans[i], end = " ")

print('\n')

#another method

a = len(my_array)
for i in range(1, n, 2):
    maximum = i
    for j in range(i + 2, n, 2):
        if my_array[j] > maximum:
            maximum = j
    my_array[i], my_array[maximum] = my_array[maximum], my_array[i]
print(my_array)



