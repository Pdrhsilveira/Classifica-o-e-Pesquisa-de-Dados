import math
import time

def busca_binaria_iterativa(lista, valor):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio  
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  

def busca_binaria_recursiva(lista, valor, esquerda=0, direita=None):
    if direita is None:
        direita = len(lista) - 1
    if esquerda > direita:
        return -1  
    meio = (esquerda + direita) // 2
    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return busca_binaria_recursiva(lista, valor, meio + 1, direita)
    else:
        return busca_binaria_recursiva(lista, valor, esquerda, meio - 1)

def pesquisa_por_salto(lista, valor):
    n = len(lista)
    salto = int(math.sqrt(n))
    prev = 0
    while lista[min(salto, n) - 1] < valor:
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(salto, n)):
        if lista[i] == valor:
            return i
    return -1

def pesquisa_fibonacci(lista, valor):
    n = len(lista)
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1 
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        if lista[i] < valor:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif lista[i] > valor:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    if fib_m1 and offset < n - 1 and lista[offset + 1] == valor:
        return offset + 1
    return -1

def teste_desempenho(algoritmo, lista, valor, repeticoes=1000):
    total_tempo = 0
    for _ in range(repeticoes):
        inicio = time.time()
        algoritmo(lista, valor)
        fim = time.time()
        total_tempo += (fim - inicio)
    return total_tempo / repeticoes

def main():
  
    lista = list(range(1000000))
    valor = 500000  

    print("Testando Busca Binária Iterativa")
    tempo = teste_desempenho(busca_binaria_iterativa, lista, valor)
    print(f"Tempo médio: {tempo:.10f} segundos")

    print("\nTestando Busca Binária Recursiva")
    tempo = teste_desempenho(busca_binaria_recursiva, lista, valor)
    print(f"Tempo médio: {tempo:.10f} segundos")

    print("\nTestando Pesquisa por Salto")
    tempo = teste_desempenho(pesquisa_por_salto, lista, valor)
    print(f"Tempo médio: {tempo:.10f} segundos")

    print("\nTestando Pesquisa Fibonacci")
    tempo = teste_desempenho(pesquisa_fibonacci, lista, valor)
    print(f"Tempo médio: {tempo:.10f} segundos")
   
main()
