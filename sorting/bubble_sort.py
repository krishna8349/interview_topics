def bubble_sprt(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [45, 55, 8,30]

bubble_sprt(arr)

for i in range(len(arr)):
    print(arr[i], end= " ")