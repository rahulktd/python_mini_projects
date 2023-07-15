#Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.

print("Enter 3 numbers")
n1 = int(input('first number:'))
n2 = int(input('second number:'))
n3 = int(input('third number:'))

n = n1 + n2 + n3

if n1 != n2 != n3:
    print('the sum is',n)
elif n1 == n2 == n3:
    m = (n)*3
    print(m)
