# Write a Python program to count the number 4 in a given list.
# [1,2,3,4,5,6,4,7,3,4] = three times 4 is occuring

numbers = [1,2,3,4,5,6,4,7,3,4]
count = 0
for i in numbers:
    if i == 4:
        count = count +1
print("4 is occuring",count,"times")