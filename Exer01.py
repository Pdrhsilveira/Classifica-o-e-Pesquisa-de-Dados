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
