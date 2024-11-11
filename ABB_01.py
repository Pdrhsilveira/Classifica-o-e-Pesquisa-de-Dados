class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def pre_order(self):
        self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)

    def post_order(self):
        self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.value, end=" ")

    def in_order(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.value, end=" ")
            self._in_order_recursive(node.right)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

arvore = ABB()
arvore.insert(10)
arvore.insert(5)
arvore.insert(15)
arvore.insert(2)
arvore.insert(7)

print("Pré-ordem:")
arvore.pre_order()
print("\nPós-ordem:")
arvore.post_order()
print("\nOrdem Simétrica:")
arvore.in_order()

print("\nBuscando valor 7:")
resultado = arvore.search(7)
if resultado:
    print("Valor encontrado!")
else:
    print("Valor não encontrado")

print("\nDeletando o valor 7:")
arvore.delete(7)
print("Ordem Simétrica após deleção:")
arvore.in_order()
