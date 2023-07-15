# Write a Python program that accepts a filename from the user and prints the extension of the file.

file = input("Enter the file name:")

ext = file.split('.')

print("file is",ext[1])