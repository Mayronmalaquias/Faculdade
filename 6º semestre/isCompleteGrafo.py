import itertools

class GrafoMatriz:
    """Implementação de Grafo utilizando Matriz de Adjacência (Grafo Denso)."""
    def __init__(self, vertices):
        self.vertices = vertices
        self.mapa_indices = {vertice: i for i, vertice in enumerate(vertices)}
        self.num_vertices = len(vertices)
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def numero_de_vertices(self):
        return self.num_vertices

    def numero_de_arestas(self):
        contador = 0
        # Percorremos apenas o triângulo superior da matriz para não contar arestas duas vezes
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                if self.matriz[i][j] == 1:
                    # Laços são contados como uma aresta
                    if i == j:
                        contador += 1
                    else:
                        contador += 1
        return contador

    def sequencia_de_graus(self):
        list_sequence = []
        for i in range(self.num_vertices):
            # O grau de um vértice é a soma dos elementos em sua linha (ou coluna)
            grau = sum(self.matriz[i])
            list_sequence.append(grau)
        return list_sequence

    def adicionar_aresta(self, v1, v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            self.matriz[linha][coluna] = 1
            # Para grafos não-direcionados, a matriz é simétrica
            if linha != coluna:
                self.matriz[coluna][linha] = 1
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print("Um ou ambos os vértices não existem no grafo")

    def remover_aresta(self, v1, v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            self.matriz[linha][coluna] = 0
            self.matriz[coluna][linha] = 0
            print(f"Aresta removida entre {v1} e {v2}")
        else:
            print("Um ou ambos os vértices não existem no grafo")

    def mostrar_matriz(self):
        print("   ", "  ".join(self.vertices))
        print("----" * (self.num_vertices + 1))
        for i, vertice in enumerate(self.vertices):
            print(f"{vertice} |", "  ".join(map(str, self.matriz[i])))

    # --- NOVOS MÉTODOS ---
    def is_nulo(self):
        """Verifica se o grafo não possui arestas."""
        return self.numero_de_arestas() == 0

    def is_simples(self):
        """Verifica se o grafo não tem laços."""
        # A representação por matriz de adjacência com 0s e 1s já impede arestas múltiplas.
        # Precisamos apenas verificar a diagonal principal para laços.
        for i in range(self.num_vertices):
            if self.matriz[i][i] == 1:
                return False  # Encontrou um laço
        return True

    def is_completo(self):
        """Verifica se o grafo é simples e cada par de vértices distintos está conectado."""
        if not self.is_simples():
            return False
        
        # Um grafo completo com N vértices tem N*(N-1)/2 arestas.
        n = self.num_vertices
        max_arestas = n * (n - 1) // 2
        
        return self.numero_de_arestas() == max_arestas

class GrafoEsparso:
    """Implementação de Grafo utilizando Lista de Adjacência (Grafo Esparso)."""
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_no(self, no):
        if no not in self.lista_adjacencia:
            self.lista_adjacencia[no] = []

    def numero_de_vertices(self):
        return len(self.lista_adjacencia)

    def numero_de_arestas(self):
        contador = 0
        visitados = set()
        for no, vizinhos in self.lista_adjacencia.items():
            for vizinho in vizinhos:
                # Evita contar a aresta (A,B) e (B,A) duas vezes
                if (vizinho, no) not in visitados:
                    contador += 1
                    visitados.add((no, vizinho))
        return contador

    def sequencia_de_graus(self):
        return [len(vizinhos) for vizinhos in self.lista_adjacencia.values()]

    def adicionar_aresta(self, v1, v2):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia:
            self.lista_adjacencia[v1].append(v2)
            if v1 != v2: # Evita adicionar v1 duas vezes na lista de v1 se for um laço
                 self.lista_adjacencia[v2].append(v1)
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print("Um ou ambos os vertices não existem no grafo")

    def remover_aresta(self, v1, v2):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia:
            # Remove a aresta nos dois sentidos
            if v2 in self.lista_adjacencia[v1]:
                self.lista_adjacencia[v1].remove(v2)
            if v1 in self.lista_adjacencia[v2] and v1 != v2:
                self.lista_adjacencia[v2].remove(v1)
            print(f"Aresta removida entre {v1} e {v2}")
        else:
            print("Um ou ambos os vertices não existem no grafo")

    def mostrar_lista(self):
        print("Lista de Adjacencia")
        for no, vizinhos in self.lista_adjacencia.items():
            print(f"{no} -> {vizinhos}")

    # --- NOVOS MÉTODOS ---
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

# --- Testes ---

print("="*20)
print("TESTANDO GRAFO COMPLETO (K4)")
print("="*20)
vertices_k4 = ['A', 'B', 'C', 'D']
grafo_completo = GrafoMatriz(vertices_k4)

# Adiciona todas as arestas possíveis
grafo_completo.adicionar_aresta('A', 'B')
grafo_completo.adicionar_aresta('A', 'C')
grafo_completo.adicionar_aresta('A', 'D')
grafo_completo.adicionar_aresta('B', 'C')
grafo_completo.adicionar_aresta('B', 'D')
grafo_completo.adicionar_aresta('C', 'D')

grafo_completo.mostrar_matriz()
print(f"eh nulo? {grafo_completo.is_nulo()}")       # Esperado: False
print(f"eh simples? {grafo_completo.is_simples()}")   # Esperado: True
print(f"eh completo? {grafo_completo.is_completo()}") # Esperado: True
print("\n")


print("="*20)
print("TESTANDO GRAFO NULO")
print("="*20)
grafo_nulo = GrafoMatriz(['X', 'Y', 'Z'])
grafo_nulo.mostrar_matriz()
print(f"eh nulo? {grafo_nulo.is_nulo()}")       # Esperado: True
print(f"eh simples? {grafo_nulo.is_simples()}")   # Esperado: True
print(f"eh completo? {grafo_nulo.is_completo()}") # Esperado: False
print("\n")


print("="*20)
print("TESTANDO GRAFO NAO-SIMPLES (COM LACO E ARESTA MULTIPLA)")
print("="*20)
grafo_nao_simples = GrafoEsparso()
for no in ['A', 'B', 'C']:
    grafo_nao_simples.adicionar_no(no)

grafo_nao_simples.adicionar_aresta('A', 'B')
grafo_nao_simples.adicionar_aresta('A', 'B') # Aresta múltipla
grafo_nao_simples.adicionar_aresta('C', 'C') # Laço

grafo_nao_simples.mostrar_lista()
print(f"Numero de Arestas: {grafo_nao_simples.numero_de_arestas()}")
print(f"eh nulo? {grafo_nao_simples.is_nulo()}")       # Esperado: False
print(f"eh simples? {grafo_nao_simples.is_simples()}")   # Esperado: False
print(f"eh completo? {grafo_nao_simples.is_completo()}") # Esperado: False
print("\n")