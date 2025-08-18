class GrafoMatriz:
    def __init__(self, vertices):
        self.vertices = vertices
        self.mapa_indices = {vertice: i for i, vertice in enumerate(vertices)}
        self.num_vertices = len(vertices)
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def numero_de_vertices(self):
        print(f"Numero de vertices: {self.num_vertices}")


    def numero_de_aresta(self):
        # print(self.matriz)
        contador = 0
        for i in self.matriz:
            for j in i:
                if j == 1:
                    contador += 1
        print(f"Numero de aresta: {int(contador / 2)}")


    def sequencia_de_graus(self):
        # print(self.matriz)
        contador = 0
        list_sequence = []
        for i, vert in enumerate(self.matriz):
            for j in vert:
                if j == 1:
                    contador += 1
            # print(f"{self.vertices[i]}: possui grau {contador}")
            list_sequence.append(contador)
            contador = 0
        print(f"Sequencia de graus: {list_sequence}")


    def remover_aresta(self, v1, v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            self.matriz[linha][coluna] = 0
            self.matriz[coluna][linha] = 0
            print(f"Aresta removida entre {v1} e {v2}")
        else:
            print("Não existe um dos vertices no grafo")

    def adicionar_aresta(self, v1,v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            self.matriz[linha][coluna] = 1
            self.matriz[coluna][linha] = 1
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print("Não existe um dos vertices no grafo")
    
    def mostrar_matriz(self):
        # print('\n')
        print("   ", "  ".join(self.vertices))
        print("----" * self.num_vertices)
        for i, vertice in enumerate(self.vertices):
            print(f"{vertice} |", "  ".join(map(str, self.matriz[i])))
        # print('\n')
        


vertices = ['A','B','C','D','E']
meu_grafo = GrafoMatriz(vertices)
meu_grafo.adicionar_aresta('A', 'B')
meu_grafo.adicionar_aresta('A', 'C')
meu_grafo.adicionar_aresta('C', 'D')
meu_grafo.adicionar_aresta('C', 'E')
meu_grafo.adicionar_aresta('B', 'D')
print(" ")
meu_grafo.mostrar_matriz()
print(" ")
meu_grafo.numero_de_vertices()
meu_grafo.numero_de_aresta()
meu_grafo.sequencia_de_graus()
meu_grafo.remover_aresta('A', 'C')
print(" ")
meu_grafo.mostrar_matriz()
print(" ")