def sort_array(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

my_array = [5, 2, 8, 1, 9]
sorted_array = sort_array(my_array)
# reverse = sorted_array[::-1]
# print(sorted_array)
# print(reverse)
#
# new = []
# l1 = len(sorted_array)
# l2 = len(reverse)
# max_length = l1 if l1 >= l2 else l2
#
# i = 0
# while i < max_length:
#     if i < l1:
#         new.append(sorted_array[i])
#     if i < l2:
#         new.append(reverse[i])
#     i += 1
#
# print(new)


n = len(sorted_array)
min_max_sorted = [0] * n
min_idx, max_idx = 0, n - 1

for i in range(0, n, 2):
    min_max_sorted[i] = sorted_array[min_idx]
    min_idx += 1

    if i + 1 < n:
        min_max_sorted[i + 1] = sorted_array[max_idx]
        max_idx -= 1

print(min_max_sorted)

# next method
n = len(my_array)
temp = n * [None]

small, large = 0, n - 1

flag = True

for i in range(n):
    if flag is True:
        temp[i] = my_array[large]
        large -= 1
    else:
        temp[i] = my_array[small]
        small += 1

    flag = bool(1 - flag)

for i in range(n):
    my_array[i] = temp[i]
print(my_array)

