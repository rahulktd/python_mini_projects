alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = 5

for i in range(1, n + 1):
    pattern = "".join(alphabets[:i]).upper()
    print(pattern)

print("\n")

x = 5
start_char = 'A'
for i in range(1, x + 1):
    for j in range(i):
        print(chr(ord(start_char) + j), end="")
    print()

