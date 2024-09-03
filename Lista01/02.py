import time

def merge(v, ini, meio, fim):
    p1 = ini
    p2 = meio + 1
    temp = []

    while p1 <= meio and p2 <= fim:
        if v[p1] <= v[p2]:
            temp.append(v[p1])
            p1 += 1
        else:
            temp.append(v[p2])
            p2 += 1

    while p1 <= meio:
        temp.append(v[p1])
        p1 += 1

    while p2 <= fim:
        temp.append(v[p2])
        p2 += 1

    for i in range(len(temp)):
        v[ini + i] = temp[i]

def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)      
        merge_sort(v, meio + 1, fim)   
        merge(v, ini, meio, fim)       

def medir_tempo(func, v, ini, fim):
    v_copia = v[  :]
    inicio = time.perf_counter()
    func(v_copia, ini, fim)
    fim = time.perf_counter()
    return fim - inicio, v_copia  

v = [38, 27, 43, 3, 9, 82, 10, 50, 16, 4, 24, 33, 67, 22, 55, 89, 14, 5, 30, 12, 72, 85, 99, 2, 17, 28, 13, 42, 37, 65]
tempo_execucao, lista_ordenada = medir_tempo(merge_sort, v, 0, len(v) - 1)

print("Lista ordenada:", lista_ordenada)
print("Tempo de execução:", tempo_execucao, "segundos")

import time

def bubble(data):
    n = len(data)
    for j in range(n):
        for i in range(j + 1, n):
            if data[i] < data[j]:
                aux = data[j]
                data[j] = data[i]
                data[i] = aux
    return

def medir_tempo(func, data):
    inicio = time.perf_counter()
    func(data)
    fim = time.perf_counter()
    return fim - inicio

dados = [3, 2, 1, 4, 5, 9, 8, 7, 6, 10, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]
inverso = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
duplicados = [1, 1, 4, 5, 2, 4, 3, 7, 7, 8, 2, 9, 9, 6, 5, 6, 3, 10, 10, 8]
ordenados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

tempo_dados = medir_tempo(bubble, dados)
print("Elementos aleatórios sem repetição:", dados, "| Tempo de execução:", tempo_dados, "segundos")

tempo_inverso = medir_tempo(bubble, inverso)
print("Elementos ordenados na ordem inversa:", inverso, "| Tempo de execução:", tempo_inverso, "segundos")

tempo_duplicados = medir_tempo(bubble, duplicados)
print("Elementos duplicados:", duplicados, "| Tempo de execução:", tempo_duplicados, "segundos")

tempo_ordenados = medir_tempo(bubble, ordenados)
print("Elementos já ordenados:", ordenados, "| Tempo de execução:", tempo_ordenados, "segundos")
