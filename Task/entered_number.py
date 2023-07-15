#Write a python program to check entered number is between 100-700 or 700-900
n = int(input("Enter a number:"))
if n >= 100 and n<= 700:
    print("Number is between 100-700")

elif n >= 700 and n<= 900:
    print("Number is between 700-900")
else:
    print("Number is not in the range")