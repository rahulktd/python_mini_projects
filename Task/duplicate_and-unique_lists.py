#Input a list from user and extract Unique and duplicate values into a new list

n = int(input("Enter the number of elements to be added to list:"))
list1 = []
for i in range(0,n):
    element = int(input("Enter the numbers:"))
    list1.append(element)
print('Current list is',list1)

# x = set(list1)
# unique = list(x)
# print('The unique list is',unique)
#
# duplicate = []
# for j in list1:
#     if j not in unique:
#         duplicate.append(j)
# print('Duplicate value list is',duplicate)
unique = []
duplicate = []

for i in list1:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print('The unique list is',unique)
print('Duplicate value list is',duplicate)


