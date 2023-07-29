# Sort an array in wave form

def sortInWave(arr, n):
    for i in range(0, n - 1, 2):
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
print(arr)


def waveForm_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if j % 2 == 0:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [3, 1, 4, 2, 5]
waveForm_sort(arr)
print(arr)
