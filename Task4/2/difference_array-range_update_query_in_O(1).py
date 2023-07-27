# Difference Array | Range update query in O(1)

# Input : A [] { 10, 5, 20, 40 }
#         update(0, 1, 10)
#         printArray()
#         update(1, 3, 20)
#         update(2, 2, 30)
#         printArray()
# Output : 20 15 20 40
#          20 35 70 60
# Explanation : The query update(0, 1, 10)
# adds 10 to A[0] and A[1]. After update,
# A[] becomes {20, 15, 20, 40}
# Query update(1, 3, 20) adds 20 to A[1],
# A[2] and A[3]. After update, A[] becomes
# {20, 35, 40, 60}.
# Query update(2, 2, 30) adds 30 to A[2].
# After update, A[] becomes {20, 35, 70, 60}.

