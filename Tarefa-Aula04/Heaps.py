def heapify_max(lista, n, i):
    maior = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2  

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        heapify_max(lista, n, maior)

def heap_sort_max(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify_max(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  
        heapify_max(lista, i, 0)


lista = [12, 11, 13, 5, 6, 7]
heap_sort_max(lista)
print("HeapSort com Heap Máximo:", lista)

#================================================================================

def heapify_min(lista, n, i):
    menor = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2  

    if esquerda < n and lista[esquerda] < lista[menor]:
        menor = esquerda

    if direita < n and lista[direita] < lista[menor]:
        menor = direita

    if menor != i:
        lista[i], lista[menor] = lista[menor], lista[i]

        heapify_min(lista, n, menor)

def heap_sort_min(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify_min(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i] 
        heapify_min(lista, i, 0)

lista = [12, 11, 13, 5, 6, 7]
heap_sort_min(lista)
print("HeapSort com Heap Mínimo:", lista)
