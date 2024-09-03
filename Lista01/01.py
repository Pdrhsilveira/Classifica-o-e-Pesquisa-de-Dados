#Implementar os algoritmos Quick Sort e o ShellSort

#quick sort
def particiona(V, inicio, final):
    esq = inicio
    dir = final
    pivo = V[inicio]

    while esq < dir:
        while esq < final and V[esq] <= pivo:
            esq += 1
        while dir > inicio and V[dir] > pivo:
            dir -= 1
        
        if esq < dir:
            V[esq], V[dir] = V[dir], V[esq]
    
    V[inicio], V[dir] = V[dir], pivo
    
    return dir

def quicksort(V, inicio, final):
    if inicio < final:
        pivo_index = particiona(V, inicio, final)
        quicksort(V, inicio, pivo_index - 1)
        quicksort(V, pivo_index + 1, final)


V = [3, 6, 8, 10, 1, 2, 1]
quicksort(V, 0, len(V) - 1)
print(V)

print(50 *"=")

#shell sort


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        
        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        
        alist[position] = currentvalue


alist = [19, 2, 31, 45, 6, 11, 121, 27]
shellSort(alist)
print("LISTA ORDENADA:", alist)
