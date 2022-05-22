class Tree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:#Si el valor del nodo actual es mayor que el valor a insertar,verifique si el nodo actual tiene un hijo izquierdo
                if self.left is None:#Si el hijo de la izquierda no existe, asigne val al nodo actual
                    self.left = Tree(val)
                else:#Si el hijo de la izquierda existe, vuelva a llamar a la funcion insert () con el hijo de la izquierda como argumento autorreferencial (llamada recursiva)
                    self.left.insert(val)
            elif val > self.val:#Si el valor del nodo actual es menor que el valor que se va a insertar, verifique si el nodo actual tiene un hijo izquierdo
                    if self.right is None:#Si existe hijo derecho, vuelva a llamar a la función insert(), con el hijo derecho como argumento autorreferencial (llamada recursiva)
                        self.right = Tree(val)
                    else:#Si el hijo derecho no existe, asigne val al nodo actual
                        self.right.insert(val)
        else:
            self.val = val#Si el valor del nodo actual está vacío, la funcion asigna val al nodo actual
#Los árboles binarios siempre insertarán valores y NUNCA reemplazarán ni desplazarán ningún valor existente
    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.val)
        if self.right:
            self.right.printValues()

tree = Tree(20)
tree.left = Tree(18)
tree.right = Tree(22)
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)

tree.printValues()