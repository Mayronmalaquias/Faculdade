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
        
class GrafoEsparso:
    def __init__(self):
        self.lista_adjacencia = {}
        self.numero_de_no = 0

    
    def adicionar_no(self, no):
        if no not in self.lista_adjacencia:
            self.lista_adjacencia[no] = []
            self.numero_de_no += 1
    

    def numero_de_vertices(self):
        return self.numero_de_no


    def numero_de_aresta(self):
        # print(self.matriz)
        contador = 0
        for i in self.lista_adjacencia:
            for j in self.lista_adjacencia[i]:
                contador += 1
                
        return int(contador / 2)


    def sequencia_de_graus(self):
        # print(self.matriz)
        list_sequence = []
        contador = 0
        for i in self.lista_adjacencia:
            for j in self.lista_adjacencia[i]:
                contador += 1
            list_sequence.append(contador)
            contador = 0
        return list_sequence


    def remover_aresta(self, v1, v2):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia:
            self.lista_adjacencia[v1].remove(v2)
            #self.lista_adjacencia[v2].remove(v1)
            print(f"Aresta removida entre {v1} e {v2}")
        else:
            print("Não existe um dos vertices no grafo")

    def adicionar_aresta(self, v1,v2):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia:
            self.lista_adjacencia[v1].append(v2)
            self.lista_adjacencia[v2].append(v1)
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print("Não existe um dos vertices no grafo")
    
    def mostrar_matriz(self):
        print("Lista de Adjacencia")
        for no, vizinho in self.lista_adjacencia.items():
            print(f"{no} -> [ {vizinho}]")


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



lista_adjacencia = GrafoEsparso()
lista_adjacencia.adicionar_no('A')
lista_adjacencia.adicionar_no('B')
lista_adjacencia.adicionar_no('C')
lista_adjacencia.adicionar_no('D')
lista_adjacencia.adicionar_no('E')

lista_adjacencia.adicionar_aresta('A', 'B')
lista_adjacencia.adicionar_aresta('A', 'C')
lista_adjacencia.adicionar_aresta('A', 'C')
lista_adjacencia.adicionar_aresta('C', 'D')
lista_adjacencia.adicionar_aresta('C', 'E')
lista_adjacencia.adicionar_aresta('B', 'D')
print(" ")
lista_adjacencia.mostrar_matriz()
print(" ")
print(f"Numero de vertices: {lista_adjacencia.numero_de_vertices()}")
print(f"Numero de aresta: {lista_adjacencia.numero_de_aresta()}")
print(f"Sequencia de graus: {lista_adjacencia.sequencia_de_graus()}")
print(" ")

lista_adjacencia.remover_aresta('A', 'C')
lista_adjacencia.remover_aresta('C', 'A')
print(" ")
lista_adjacencia.mostrar_matriz()