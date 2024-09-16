def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

inversa = [5, 4, 3, 2, 1]
print("Inversa:", bubble_sort(inversa))

ordenada = [1, 2, 3, 4, 5]
print("Ordenados:", bubble_sort(ordenada))

repetidos = [3, 3, 1, 2, 3]
print("Repetidos:", bubble_sort(repetidos))

aleatoria = [4, 2, 5, 1, 3]
print("Aleatórios:", bubble_sort(aleatoria))
