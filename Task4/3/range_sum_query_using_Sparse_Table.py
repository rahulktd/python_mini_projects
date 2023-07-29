# Range sum query using Sparse Table

# We have an array arr[].
# We need to find the sum of all the elements in the range L and R where 0 <= L <= R <= n-1.
# Consider a situation when there are many range queries.

# Input : 3 7 2 5 8 9
#         query(0, 5)
#         query(3, 5)
#         query(2, 4)
# Output : 34
#          22
#          15

arr = [3, 7, 2, 5, 8, 9]
k = 16
n = len(arr)

table = []
for i in range(n):
    inner_list = []
    for j in range(k + 1):
        inner_list.append(0)
    table.append(inner_list)

for i in range(n):
    table[i][0] = arr[i]

for j in range(1, k + 1):
    for i in range(0, n - (1 << j) + 1):
        table[i][j] = table[i][j - 1] + table[i + (1 << (j - 1))][j - 1]

L, R = 0, 5
answer = 0
for j in range(k, -1, -1):
    if L + (1 << j) - 1 <= R:
        answer = answer + table[L][j]
        L += 1 << j

print(answer)

L, R = 3, 5
answer = 0
for j in range(k, -1, -1):
    if L + (1 << j) - 1 <= R:
        answer = answer + table[L][j]
        L += 1 << j

print(answer)