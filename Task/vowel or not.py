#Write a Python program to test whether a passed letter is a vowel or not.

letter = str(input("Enter a letter:"))

vowels = ['a','e','i','o','u']

if letter.lower() in vowels:
    print("The entered letter is vowel")
else:
    print("Entered letter is consonant")

