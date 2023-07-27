# Print left rotation of array in O(n) time and O(1) space
def leftRotate(arr, n, k):
	mod = k % n
	rotated_arr = []
	for i in range(n):
		rotated_arr.append(arr[(mod + i) % n])
	return rotated_arr

arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 4
rotated = leftRotate(arr, n, k)
print(rotated)

