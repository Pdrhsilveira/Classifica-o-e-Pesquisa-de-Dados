#Pseudo CountingtSort

def counting_sort(lista):
    max_valor = max(lista)
    
    contador = []
    for _ in range(max_valor + 1):
        contador.append(0)  
    for num in lista:
        contador[num] += 1
    
    ordenada_array = []
    for i in range(len(contador)):
        for _ in range(contador[i]):  
            ordenada_array.append(i)
    
    return ordenada_array

lista = [4, 2, 2, 8, 3, 3, 1, 500, 1000]
ordenada_array = counting_sort(lista)
print("Lista ordenada0:", ordenada_array)
