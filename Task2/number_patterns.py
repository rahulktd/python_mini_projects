#python number pattern

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end="")
    print()

print("\n")

for i in range(1,n+1):
    for j in range(i):
        print(i, end="")
    print()

print("\n")

number = 1
for i in range(1, n+1):
    for j in range(i):
        print(number, end="")
        number = number + 1
    print()

print("\n")


for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(k,end=" ")
    print()

print('\n')

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(k,end=" ")
    print()

print('\n')

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j ,end=" ")
    print()

for i in range(n,0,-1):
    x = i * (n-i)
    y = i * ' '
    print (int(x+y))


