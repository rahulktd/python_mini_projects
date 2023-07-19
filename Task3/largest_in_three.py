# 3 Find the Largest Among Three Numbers.

list1 = []
for i in range(0,3):
    element = int(input("Enter the numbers:"))
    list1.append(element)
print('Current list is',list1)

list1.sort()
print(list1[-1])