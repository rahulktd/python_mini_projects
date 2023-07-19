# # 4 Program to Reverse a Number.
#
number = int(input("Enter a number with more than one digit: "))
num_digits = len(str(number))
reversed_str = str(number)[::-1]
#
print("Reversed number:", "{:0{num_digits}s}".format(reversed_str, num_digits=num_digits))
