class GrafoMatriz:
    def __init__(self, vertices):
        self.vertices = vertices
        self.mapa_indices = {vertice: i for i, vertice in enumerate(vertices)}
        self.num_vertices = len(vertices)
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def numero_de_vertices(self):
        print(f"Numero de vertices: {self.num_vertices}")

    
    def get_vertices(self):
        return self.vertices
    
    def get_aresta(self):
        return self.numero_de_aresta()
    
    def is_subgrafo(self, outro_grafo):
        contador = 0
        for i, val in enumerate(self.matriz):
            for j, valor in enumerate(val):
                if self.matriz[i][j] == 1:
                    if self.matriz[i][j] != outro_grafo.matriz[i][j]:
                        return False
        # print(f"Numero de aresta: {int(contador / 2)}")
        return True
    
    def is_subgrafo_gerador(self, outro_grafo):
        if self.get_vertices() == outro_grafo.get_vertices():
            return True
        else:
            return False
        # pass
    
    def is_subgrafo_induzido(self,outro_grafo):
        for i, val in enumerate(self.matriz):
            for j, valor in enumerate(val):
                if outro_grafo.matriz[i][j] == 1:
                    if self.matriz[i][j] != outro_grafo.matriz[i][j]:
                        return False
        return True


    def is_nulo(self):
        """Verifica se o grafo não possui arestas."""
        return self.numero_de_arestas() == 0

    def is_simples(self):
        for i in range(self.num_vertices):
            if self.matriz[i][i] == 1:
                return False  # Encontrou um laço
        return True

    def is_completo(self):
        if not self.is_simples():
            return False
        
        n = self.num_vertices
        max_arestas = n * (n - 1) // 2
        
        return self.numero_de_arestas() == max_arestas


    def numero_de_aresta(self):
        # print(self.matriz)
        contador = 0
        for i in self.matriz:
            for j in i:
                if j == 1:
                    contador += 1
        # print(f"Numero de aresta: {int(contador / 2)}")
        return int(contador / 2)


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

    def is_nulo(self):
        """Verifica se o grafo não possui arestas."""
        return self.numero_de_arestas() == 0

    def is_simples(self):
        """Verifica se o grafo não tem laços nem arestas múltiplas."""
        for no, vizinhos in self.lista_adjacencia.items():
            if no in vizinhos:
                return False  # Encontrou um laço
            if len(set(vizinhos)) != len(vizinhos):
                return False  # Encontrou arestas múltiplas (elementos duplicados na lista)
        return True

    def is_completo(self):
        """Verifica se o grafo é simples e cada vértice se conecta a todos os outros."""
        if not self.is_simples():
            return False
            
        n = self.numero_de_vertices()
        grau_esperado = n - 1
        
        # Em um grafo completo, todos os vértices devem ter grau n-1
        for no, vizinhos in self.lista_adjacencia.items():
            if len(vizinhos) != grau_esperado:
                return False
        return True

    def get_vertices(self):
        list_temp = []
        for i in self.lista_adjacencia:
            list_temp.append(i)
        return list_temp
    
    def get_aresta(self):
        list_temp = []
        for i, var in self.lista_adjacencia.items():
            list_temp.append(var)
        return list_temp
    
    def is_subgrafo(self, outro_grafo):
        for i in self.get_vertices():
            if i not in outro_grafo.get_vertices():
                return False

        for no, vizinho in self.lista_adjacencia.items():
            for i in vizinho:
                if i not in outro_grafo.lista_adjacencia[no]:
                    return False
        return True

        # print(f"Numero de aresta: {int(contador / 2)}")
        return True
    
    def is_subgrafo_gerador(self, outro_grafo):
        if(self.get_vertices() == outro_grafo.get_vertices()):
            return True
        return False
        # pass
    
    def is_subgrafo_induzido(self,outro_grafo):
        for no, vizinho in outro_grafo.lista_adjacencia.items():
            for i in vizinho:
                if i not in self.lista_adjacencia[no]:
                    return False
        return True


# vertices = ['A','B','C','D','E']
# meu_grafo = GrafoMatriz(vertices)
# meu_grafo.adicionar_aresta('A', 'B')
# meu_grafo.adicionar_aresta('A', 'C')
# meu_grafo.adicionar_aresta('C', 'D')
# meu_grafo.adicionar_aresta('C', 'E')
# meu_grafo.adicionar_aresta('B', 'D')
# print(" ")
# meu_grafo.mostrar_matriz()
# print(" ")
# meu_grafo.numero_de_vertices()
# meu_grafo.numero_de_aresta()
# meu_grafo.sequencia_de_graus()
# meu_grafo.remover_aresta('A', 'C')
# print(" ")
# meu_grafo.mostrar_matriz()
# vertices2 = ['A','B','C','D','E']
# novo_grafo = GrafoMatriz(vertices2)
# novo_grafo.adicionar_aresta('A', 'B')
# novo_grafo.adicionar_aresta('A', 'C')
# novo_grafo.adicionar_aresta('C', 'D')
# novo_grafo.adicionar_aresta('C', 'E')
# novo_grafo.adicionar_aresta('B', 'D')
# print(novo_grafo.is_subgrafo(meu_grafo))
# print(novo_grafo.is_subgrafo_gerador(meu_grafo))
# print(novo_grafo.is_subgrafo_induzido(meu_grafo))
# novo_grafo.mostrar_matriz()
# print(" ")



lista_adjacencia = GrafoEsparso()
lista_adjacencia.adicionar_no('A')
lista_adjacencia.adicionar_no('B')
lista_adjacencia.adicionar_no('C')
lista_adjacencia.adicionar_no('D')
lista_adjacencia.adicionar_no('E')

lista_adjacencia.adicionar_aresta('A', 'B')
lista_adjacencia.adicionar_aresta('A', 'C')
lista_adjacencia.adicionar_aresta('A', 'C')
# lista_adjacencia.adicionar_aresta('C', 'B')
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

lista_adjacencia1 = GrafoEsparso()
lista_adjacencia1.adicionar_no('A')
lista_adjacencia1.adicionar_no('B')
lista_adjacencia1.adicionar_no('C')
# lista_adjacencia1.adicionar_no('D')
# lista_adjacencia1.adicionar_no('E')
lista_adjacencia1.adicionar_aresta('A', 'B')
lista_adjacencia1.adicionar_aresta('A', 'C')
print(lista_adjacencia1.get_vertices())
print(lista_adjacencia1.get_aresta())
print(lista_adjacencia.get_vertices())
print(lista_adjacencia.get_aresta())
# print(lista_adjacencia1.get_vertices() in lista_adjacencia.get_vertices())
print(lista_adjacencia1.is_subgrafo(lista_adjacencia))
print(lista_adjacencia1.is_subgrafo_gerador(lista_adjacencia))
print(lista_adjacencia1.is_subgrafo_induzido(lista_adjacencia))
