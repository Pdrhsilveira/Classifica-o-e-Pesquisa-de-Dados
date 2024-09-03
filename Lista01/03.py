def heapify(arr, n, i):
    maior = i  
    esq = 2 * i + 1  
    dir = 2 * i + 2 

    if esq < n and arr[i] < arr[esq]:
        maior = esq

    if dir < n and arr[maior] < arr[dir]:
        maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  # troca

        heapify(arr, n, maior)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("HEAP", arr)
