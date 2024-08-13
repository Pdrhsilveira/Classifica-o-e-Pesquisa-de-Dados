def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        menor_id = i
        for j in range(i + 1, n):
            if data[j] < data[menor_id]:
                menor_id = j

        data[i], data[menor_id] = data[menor_id], data[i]

dados = [3, 2, 1, 4, 5]
inverso = [5, 4, 3, 2, 1]
duplicados = [1, 1, 4, 5, 2, 4, 3]
ordenados = [1, 2, 3, 4, 5]

selection_sort(dados)
print("Elementos aleatórios sem repetição:", dados)

selection_sort(inverso)
print("Elementos ordenados na ordem inversa:", inverso)

selection_sort(duplicados)
print("Elementos duplicados:", duplicados)

selection_sort(ordenados)
print("Elementos já ordenados:", ordenados)

print("-------------------------------------------------------")

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

def lst_selection_sort(lst):
    if lst is None:
        return lst

    inicio = lst
    while inicio.prox is not None:
        menor = inicio
        atual = inicio.prox

        while atual is not None:
            if atual.info < menor.info:
                menor = atual
            atual = atual.prox

        inicio.info, menor.info = menor.info, inicio.info
        inicio = inicio.prox

    return lst

dados = lst_cria()
for valor in [3, 2, 1, 4, 5]:
    dados = lst_insere(dados, valor)

inverso = lst_cria()
for valor in [5, 4, 3, 2, 1]:
    inverso = lst_insere(inverso, valor)

duplicados = lst_cria()
for valor in [1, 1, 4, 5, 2, 4, 3]:
    duplicados = lst_insere(duplicados, valor)

ordenados = lst_cria()
for valor in [1, 2, 3, 4, 5]:
    ordenados = lst_insere(ordenados, valor)

dados = lst_selection_sort(dados)
inverso = lst_selection_sort(inverso)
duplicados = lst_selection_sort(duplicados)
ordenados = lst_selection_sort(ordenados)

print("Elementos aleatórios sem repetição:")
lst_imprime(dados)

print("Elementos ordenados na ordem inversa:")
lst_imprime(inverso)

print("Elementos duplicados:")
lst_imprime(duplicados)

print("Elementos já ordenados:")
lst_imprime(ordenados)

