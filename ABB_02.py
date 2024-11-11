class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class Nodo:
    def __init__(self, produto):
        self.produto = produto  
        self.esquerda = None    
        self.direita = None     

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None  

    def inserir(self, produto):
        novo_nodo = Nodo(produto)
        if self.raiz is None:
            self.raiz = novo_nodo  
        else:
            self._inserir_recursivo(self.raiz, novo_nodo)

    def _inserir_recursivo(self, nodo_atual, novo_nodo):
        if novo_nodo.produto.id < nodo_atual.produto.id:
            if nodo_atual.esquerda is None:
                nodo_atual.esquerda = novo_nodo
            else:
                self._inserir_recursivo(nodo_atual.esquerda, novo_nodo)
        else:
            if nodo_atual.direita is None:
                nodo_atual.direita = novo_nodo
            else:
                self._inserir_recursivo(nodo_atual.direita, novo_nodo)

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, nodo_atual, id):
        if nodo_atual is None:
            return None  
        if nodo_atual.produto.id == id:
            return nodo_atual.produto
        elif id < nodo_atual.produto.id:
            return self._buscar_recursivo(nodo_atual.esquerda, id)
        else:
            return self._buscar_recursivo(nodo_atual.direita, id)

    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, nodo_atual, id):
        if nodo_atual is None:
            return None
        if id < nodo_atual.produto.id:
            nodo_atual.esquerda = self._remover_recursivo(nodo_atual.esquerda, id)
        elif id > nodo_atual.produto.id:
            nodo_atual.direita = self._remover_recursivo(nodo_atual.direita, id)
        else:
          
            if nodo_atual.esquerda is None:
                return nodo_atual.direita
            elif nodo_atual.direita is None:
                return nodo_atual.esquerda
            
            menor_nodo = self._encontrar_menor(nodo_atual.direita)
            nodo_atual.produto = menor_nodo.produto
            nodo_atual.direita = self._remover_recursivo(nodo_atual.direita, menor_nodo.produto.id)
        return nodo_atual

    def _encontrar_menor(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar_em_ordem(self):
        produtos = []
        self._em_ordem_recursivo(self.raiz, produtos)
        return produtos

    def _em_ordem_recursivo(self, nodo_atual, produtos):
        if nodo_atual is not None:
            self._em_ordem_recursivo(nodo_atual.esquerda, produtos)
            produtos.append(nodo_atual.produto)
            self._em_ordem_recursivo(nodo_atual.direita, produtos)

def main():
    arvore = ArvoreBinariaBusca()

    arvore.inserir(Produto(30, "Produto A", "Descrição A", 100.0))
    arvore.inserir(Produto(20, "Produto B", "Descrição B", 150.0))
    arvore.inserir(Produto(40, "Produto C", "Descrição C", 200.0))

    produto_buscado = arvore.buscar(20)
    if produto_buscado:
        print(f"Produto encontrado: {produto_buscado.nome} - Preço: {produto_buscado.preco}")
    else:
        print("Produto não encontrado.")

    arvore.remover(20)
    print("Produto com ID 20 removido.")

    produtos_ordenados = arvore.listar_em_ordem()
    for produto in produtos_ordenados:
        print(f"ID: {produto.id} - Nome: {produto.nome} - Preço: {produto.preco}")

main()
