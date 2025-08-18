class Grafo:
    def __init__(self):
        self.adjacencias = {}

    
    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []


    def adicionar_aresta(self, v1, v2):
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)
        if v2 not in self.adjacencias[v1]:
            self.adjacencias[v1].append(v2)
        if v1 not in self.adjacencias[v2]:
            self.adjacencias[v2].append(v1)


    def mostrar_grafo(self):
        for vertices, vizinhos in self.adjacencias.items():
            print(f"{vertices}: {', '.join(vizinhos)}")
        

meu_grafo = Grafo()
meu_grafo.adicionar_vertice('A')
meu_grafo.adicionar_vertice('B')
meu_grafo.adicionar_vertice('C')
meu_grafo.adicionar_vertice('D')
meu_grafo.adicionar_vertice('E')
meu_grafo.adicionar_vertice('F')

meu_grafo.adicionar_aresta('A', 'F')
meu_grafo.adicionar_aresta('A', 'B')
meu_grafo.adicionar_aresta('A', 'C')
meu_grafo.adicionar_aresta('B', 'F')
meu_grafo.adicionar_aresta('B', 'D')
meu_grafo.adicionar_aresta('B', 'C')
meu_grafo.adicionar_aresta('C', 'E')
meu_grafo.adicionar_aresta('D', 'E')
meu_grafo.adicionar_aresta('D', 'F')
meu_grafo.adicionar_aresta('E', 'F')

meu_grafo.mostrar_grafo()
