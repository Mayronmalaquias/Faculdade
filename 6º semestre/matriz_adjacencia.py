class GrafoMatriz:
    def __init__(self, vertices):
        self.vertices = vertices
        self.mapa_indices = {vertice: i for i, vertice in enumerate(vertices)}
        self.num_vertices = len(vertices)
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]


    def adicionar_aresta(self, v1,v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            self.matriz[linha][coluna] = 1
            self.matriz[coluna][linha] = 1
        else:
            print("Não existe um dos vertices no grafo")
    
    def mostrar_matriz(self):
        print("   ", "  ".join(self.vertices))
        print("----" * self.num_vertices)
        for i, vertice in enumerate(self.vertices):
            print(f"{vertice} |", "  ".join(map(str, self.matriz[i])))
        


vertices = ['A','B','C','D','E','F']
meu_grafo = GrafoMatriz(vertices)
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
meu_grafo.adicionar_aresta('D', 'D')

meu_grafo.mostrar_matriz()