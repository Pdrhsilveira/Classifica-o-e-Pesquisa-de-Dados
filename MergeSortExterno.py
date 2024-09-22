import os #PODER MEXER NO SISTEMA
import heapq #ORDENAR POR HEAP


def dividir_arquivo(arquivo_entrada, tamanho_bloco, diretorio_saida="blocos"):
    with open(arquivo_entrada, 'r') as f:
        os.makedirs(diretorio_saida, exist_ok=True)
        bloco = []
        contador = 0
        
        for linha in f:
            bloco.append(int(linha.strip()))
            
            if len(bloco) >= tamanho_bloco:
                bloco.sort()  
                salvar_bloco(bloco, f"{diretorio_saida}/bloco_{contador}.txt")
                bloco = []
                contador += 1
        
        if bloco:
            bloco.sort()
            salvar_bloco(bloco, f"{diretorio_saida}/bloco_{contador}.txt")

def salvar_bloco(bloco, arquivo_saida):
    with open(arquivo_saida, 'w') as f:
        for item in bloco:
            f.write(f"{item}\n")

def merge_externo(lista_arquivos, arquivo_saida):
    files = []
    
    for arquivo in lista_arquivos:
        files.append(open(arquivo, 'r'))
        
    heap = []

    for i, f in enumerate(files):
        linha = f.readline()
        
        if linha:
            heapq.heappush(heap, (int(linha.strip()), i))

    with open(arquivo_saida, 'w') as output:
        while heap:
            valor, idx = heapq.heappop(heap)
            output.write(f"{valor}\n")
            linha = files[idx].readline()
            
            if linha:
                heapq.heappush(heap, (int(linha.strip()), idx))

    for f in files:
        f.close()

def main():
    tamanho_bloco = 1000  
    arquivo_entrada = "dados_grandes.txt"  
    diretorio_saida = "blocos_ordenados" 


    dividir_arquivo(arquivo_entrada, tamanho_bloco, diretorio_saida)

    arquivos_blocos = []
    
    for i in range(len(os.listdir(diretorio_saida))):
        arquivos_blocos.append(f"{diretorio_saida}/bloco_{i}.txt")

    merge_externo(arquivos_blocos, "arquivo_ordenado.txt")

