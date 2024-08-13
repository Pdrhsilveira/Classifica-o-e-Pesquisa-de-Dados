def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp


dados = [3, 2, 1, 4, 5]
ordenados = [1, 2, 3, 4, 5]
inversos = [5, 4, 3, 2, 1]
duplicados = [1, 1, 4, 5, 2, 4, 3]

insertion_sort(dados)
print("Elementos aleatórios sem repetição:",dados)

insertion_sort(ordenados)
print("Elementos já ordenados:",ordenados)

insertion_sort(inversos)
print("Elementos ordenados na ordem inversa:",inversos)

insertion_sort(duplicados)
print("Elementos duplicados:",duplicados)

print("--------------------------------------------------------------------")


class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def lst_cria():
    return None

def lst_insere(lst, v):
    novo = Lista(v)
    novo.prox = lst
    return novo 

def lst_imprime(lst):
    atual = lst
    while not lst_vazia(atual):
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

def lst_vazia(lst):
    return lst is None


def lst_insertion_sort(lst):
    if lst is None or lst.prox is None:
        return lst
    
    sorted_lst = None
    
    
    while lst is not None:
        current = lst
        lst = lst.prox
        
        if sorted_lst is None or current.info < sorted_lst.info:
            current.prox = sorted_lst
            sorted_lst = current
        else:
            search = sorted_lst
            while search.prox is not None and search.prox.info < current.info:
                search = search.prox
            current.prox = search.prox
            search.prox = current
    
    return sorted_lst

dados = lst_cria()
for value in [3, 2, 1, 4, 5]:
    dados = lst_insere(dados, value)

ordenados = lst_cria()
for value in [1, 2, 3, 4, 5]:
    ordenados = lst_insere(ordenados, value)

inversos = lst_cria()
for value in [5, 4, 3, 2, 1]:
    inversos = lst_insere(inversos, value)

duplicados = lst_cria()
for value in [1, 1, 4, 5, 2, 4, 3]:
    duplicados = lst_insere(duplicados, value)

dados = lst_insertion_sort(dados)
ordenados = lst_insertion_sort(ordenados)
inversos = lst_insertion_sort(inversos)
duplicados = lst_insertion_sort(duplicados)

print("Elementos aleatórios sem repetição:")
lst_imprime(dados)

print("Elementos já ordenados:")
lst_imprime(ordenados)

print("Elementos ordenados na ordem inversa:")
lst_imprime(inversos)

print("Elementos duplicados:")
lst_imprime(duplicados)
