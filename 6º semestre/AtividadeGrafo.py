class GrafoMatriz:
    """
    Implementação de um Grafo utilizando Matriz de Adjacência.
    """
    def __init__(self, vertices):
        self.vertices = sorted(list(set(vertices)))
        self.mapa_indices = {vertice: i for i, vertice in enumerate(self.vertices)}
        self.num_vertices = len(self.vertices)
        self.num_arestas = 0
        # A matriz pode suportar valores > 1 para representar arestas múltiplas.
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    # --- Métodos de Informação ---
    def get_vertices(self):
        return self.vertices

    def get_numero_de_vertices(self):
        return self.num_vertices

    def get_numero_de_arestas(self):
        return self.num_arestas

    def get_arestas(self):
        arestas = set()
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                if self.matriz[i][j] > 0:
                    v1 = self.vertices[i]
                    v2 = self.vertices[j]
                    arestas.add(tuple(sorted((v1, v2))))
        return arestas

    # --- Métodos de Modificação ---
    def adicionar_aresta(self, v1, v2, permite_multiplas=False):
        """Adiciona uma aresta. Por padrão, não cria arestas múltiplas."""
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            
            if not permite_multiplas and self.matriz[linha][coluna] > 0:
                print(f"Aviso: Aresta entre {v1} e {v2} já existe. Não foi adicionada novamente.")
                return

            self.matriz[linha][coluna] += 1
            if linha != coluna: # Evita somar duas vezes em laços
                self.matriz[coluna][linha] += 1
            self.num_arestas += 1
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print(f"Erro: Um ou ambos os vértices '{v1}', '{v2}' não existem.")

    def remover_aresta(self, v1, v2):
        if v1 in self.mapa_indices and v2 in self.mapa_indices:
            linha = self.mapa_indices[v1]
            coluna = self.mapa_indices[v2]
            if self.matriz[linha][coluna] > 0:
                self.matriz[linha][coluna] -= 1
                if linha != coluna:
                    self.matriz[coluna][linha] -= 1
                self.num_arestas -= 1
                print(f"Aresta removida entre {v1} e {v2}")
            else:
                print(f"Erro: Não existe aresta entre {v1} e {v2}.")
        else:
            print(f"Erro: Um ou ambos os vértices '{v1}', '{v2}' não existem.")
    
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
        return list_sequence

    # --- Métodos de Verificação de Propriedades ---
    def is_nulo(self):
        """Verifica se o grafo é nulo (não possui arestas)."""
        return self.num_arestas == 0

    def is_simples(self):
        """Verifica se o grafo é simples (sem laços ou arestas múltiplas)."""
        for i in range(self.num_vertices):
            # Verifica se há laços (diagonal principal)
            if self.matriz[i][i] > 0:
                return False
            # Verifica se há arestas múltiplas (matriz triangular superior)
            for j in range(i + 1, self.num_vertices):
                if self.matriz[i][j] > 1:
                    return False
        return True
    

    def is_completo(self):
        """Verifica se o grafo é completo (simples e todos os vértices conectados)."""
        if not self.is_simples():
            return False
        
        # Num grafo completo, o número de arestas é n*(n-1)/2
        n = self.num_vertices
        if n < 2: return True # Grafo com 0 ou 1 vértice é completo.
        
        arestas_esperadas = n * (n - 1) / 2
        return self.num_arestas == arestas_esperadas

    # --- Métodos de Verificação de Subgrafos ---
    def is_subgrafo(self, super_grafo):
        if not set(self.vertices).issubset(set(super_grafo.vertices)):
            return False
        if not self.get_arestas().issubset(super_grafo.get_arestas()):
            return False
        return True
    

    def is_subgrafo_gerador(self, super_grafo):
        if set(self.vertices) != set(super_grafo.vertices):
            return False
        return self.is_subgrafo(super_grafo)

    def is_subgrafo_induzido(self, super_grafo):
        if not set(self.vertices).issubset(set(super_grafo.vertices)):
            return False
        for v1 in self.vertices:
            for v2 in self.vertices:
                idx1_self = self.mapa_indices[v1]
                idx2_self = self.mapa_indices[v2]
                idx1_super = super_grafo.mapa_indices[v1]
                idx2_super = super_grafo.mapa_indices[v2]
                aresta_em_self = self.matriz[idx1_self][idx2_self] > 0
                aresta_em_super = super_grafo.matriz[idx1_super][idx2_super] > 0
                if aresta_em_self != aresta_em_super:
                    return False
        return True


    def gerar_permutacoes(self, elementos):
        """
        Gera todas as permutações de uma lista de elementos sem usar bibliotecas.
        Utiliza um algoritmo recursivo de backtracking.
        """
        if len(elementos) <= 1:
            return [elementos]

        todas_as_permutacoes = []
        for i in range(len(elementos)):
            elemento_atual = elementos[i]
            elementos_restantes = elementos[:i] + elementos[i+1:]
            permutacoes_dos_restantes = self.gerar_permutacoes(elementos_restantes)
            for p in permutacoes_dos_restantes:
                todas_as_permutacoes.append([elemento_atual] + p)
        return todas_as_permutacoes


    def sao_isomorfos(self, g2):
        """
        Verifica se dois grafos, representados pelas classes GrafoMatriz ou GrafoEsparso,
        são isomorfos usando a abordagem de força bruta, SEM USO DE NENHUMA BIBLIOTECA.

        Args:
            g1: Uma instância de GrafoMatriz ou GrafoEsparso.
            g2: Uma instância de GrafoMatriz ou GrafoEsparso.

        Returns:
            bool: True se os grafos forem isomorfos, False caso contrário.
        """
        # 1. Verificação de Invariantes
        if self.get_numero_de_vertices() != g2.get_numero_de_vertices():
            print("Falha na verificação: Número de vértices diferente.")
            return False

        if self.get_numero_de_arestas() != g2.get_numero_de_arestas():
            print("Falha na verificação: Número de arestas diferente.")
            return False
        
        if sorted(self.sequencia_de_graus()) != sorted(g2.sequencia_de_graus()):
            print("Falha na verificação: Sequência de graus diferente.")
            return False

        # 2. Obter Matrizes de Adjacência
        if isinstance(self, GrafoMatriz):
            matriz1 = self.matriz
        else: # é GrafoEsparso
            vertices1 = sorted(self.get_vertices())
            mapa1 = {vertice: i for i, vertice in enumerate(vertices1)}
            n1 = len(vertices1)
            matriz1 = [[0] * n1 for _ in range(n1)]
            for v_origem, vizinhos in self.lista_adjacencia.items():
                for v_destino in vizinhos:
                    matriz1[mapa1[v_origem]][mapa1[v_destino]] = 1

        if isinstance(g2, GrafoMatriz):
            matriz2 = g2.matriz
        else: # é GrafoEsparso
            vertices2 = sorted(g2.get_vertices())
            mapa2 = {vertice: i for i, vertice in enumerate(vertices2)}
            n2 = len(vertices2)
            matriz2 = [[0] * n2 for _ in range(n2)]
            for v_origem, vizinhos in g2.lista_adjacencia.items():
                for v_destino in vizinhos:
                    matriz2[mapa2[v_origem]][mapa2[v_destino]] = 1
        
        n = self.get_numero_de_vertices()
        indices_vertices = list(range(n))
        
        # 3. Gera e testa todas as permutações USANDO A NOSSA FUNÇÃO
        permutacoes = self.gerar_permutacoes(indices_vertices)

        for p in permutacoes:
            mapeamento_valido = True
            for i in range(n):
                for j in range(n):
                    if matriz1[i][j] != matriz2[p[i]][p[j]]:
                        mapeamento_valido = False
                        break
                if not mapeamento_valido:
                    break
            
            if mapeamento_valido:
                vertices1_ord = sorted(self.get_vertices())
                vertices2_ord = sorted(g2.get_vertices())
                mapeamento_real = {vertices1_ord[i]: vertices2_ord[p[i]] for i in range(n)}
                print(f"Isomorfismo encontrado com o mapeamento: {mapeamento_real}")
                return True

        return False

        
    # --- Métodos de Exibição ---
    def mostrar_matriz(self):
        print("\n--- Matriz de Adjacência ---")
        header = "   " + "  ".join(map(str, self.vertices))
        print(header)
        print("─" * (len(header) + 2))
        for i, vertice in enumerate(self.vertices):
            row_str = f"{vertice} |" + "".join(f" {val: >2}" for val in self.matriz[i])
            print(row_str)
        print("-" * (len(header) + 2))



class GrafoEsparso:
    """
    Implementação de um Grafo utilizando Lista de Adjacência.
    """
    def __init__(self):
        # Usar um set para cada lista de adjacência garante que não haverá arestas múltiplas
        self.lista_adjacencia = {}
        self.num_arestas = 0

    # --- Métodos de Informação ---
    def get_vertices(self):
        return list(self.lista_adjacencia.keys())

    def get_numero_de_vertices(self):
        return len(self.lista_adjacencia)

    def get_numero_de_arestas(self):
        return self.num_arestas

    def get_arestas(self):
        arestas = set()
        for v1, vizinhos in self.lista_adjacencia.items():
            for v2 in vizinhos:
                arestas.add(tuple(sorted((v1, v2))))
        return arestas

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
    
    # --- Métodos de Modificação ---
    def adicionar_no(self, no):
        if no not in self.lista_adjacencia:
            self.lista_adjacencia[no] = set()

    def adicionar_aresta(self, v1, v2):
        # A estrutura de set previne arestas múltiplas naturalmente
        if v1 == v2: 
            print("Aviso: Tentativa de adicionar um laço, o que não é permitido em um grafo simples.")
            return
        self.adicionar_no(v1)
        self.adicionar_no(v2)
        if v2 not in self.lista_adjacencia[v1]:
            self.lista_adjacencia[v1].add(v2)
            self.lista_adjacencia[v2].add(v1)
            self.num_arestas += 1
            print(f"Aresta adicionada entre {v1} e {v2}")
        else:
            print(f"Aviso: Aresta entre {v1} e {v2} já existe.")

    def remover_aresta(self, v1, v2):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia.get(v1, set()):
            self.lista_adjacencia[v1].remove(v2)
            self.lista_adjacencia[v2].remove(v1)
            self.num_arestas -= 1
            print(f"Aresta removida entre {v1} e {v2}")
        else:
            print(f"Erro: Não existe aresta entre {v1} e {v2} para remover.")

    # --- Métodos de Verificação de Propriedades ---
    def is_nulo(self):
        """Verifica se o grafo é nulo (não possui arestas)."""
        return self.num_arestas == 0

    def is_simples(self):
        """Verifica se o grafo é simples (sem laços). A estrutura já previne arestas múltiplas."""
        # A estrutura de set na lista de adjacência já previne arestas múltiplas.
        # Só precisamos verificar se há laços, o que a nossa função `adicionar_aresta` já previne.
        # Esta função serve como uma checagem dupla.
        for v, vizinhos in self.lista_adjacencia.items():
            if v in vizinhos:
                return False # Laço encontrado
        return True

    def is_completo(self):
        """Verifica se o grafo é completo (simples e todos os vértices conectados)."""
        if not self.is_simples():
            return False
        
        n = self.get_numero_de_vertices()
        if n < 2: return True
        
        # Em um grafo completo, cada vértice deve ter grau n-1
        grau_esperado = n - 1
        for vizinhos in self.lista_adjacencia.values():
            if len(vizinhos) != grau_esperado:
                return False
        return True


    def gerar_permutacoes(self, elementos):
        """
        Gera todas as permutações de uma lista de elementos sem usar bibliotecas.
        Utiliza um algoritmo recursivo de backtracking.
        """
        if len(elementos) <= 1:
            return [elementos]

        todas_as_permutacoes = []
        for i in range(len(elementos)):
            elemento_atual = elementos[i]
            elementos_restantes = elementos[:i] + elementos[i+1:]
            permutacoes_dos_restantes = self.gerar_permutacoes(elementos_restantes)
            for p in permutacoes_dos_restantes:
                todas_as_permutacoes.append([elemento_atual] + p)
        return todas_as_permutacoes


    def sao_isomorfos(self, g2):
        """
        Verifica se dois grafos, representados pelas classes GrafoMatriz ou GrafoEsparso,
        são isomorfos usando a abordagem de força bruta, SEM USO DE NENHUMA BIBLIOTECA.

        Args:
            g1: Uma instância de GrafoMatriz ou GrafoEsparso.
            g2: Uma instância de GrafoMatriz ou GrafoEsparso.

        Returns:
            bool: True se os grafos forem isomorfos, False caso contrário.
        """
        # 1. Verificação de Invariantes
        if self.get_numero_de_vertices() != g2.get_numero_de_vertices():
            print("Falha na verificação: Número de vértices diferente.")
            return False

        if self.get_numero_de_arestas() != g2.get_numero_de_arestas():
            print("Falha na verificação: Número de arestas diferente.")
            return False
        
        if sorted(self.sequencia_de_graus()) != sorted(g2.sequencia_de_graus()):
            print("Falha na verificação: Sequência de graus diferente.")
            return False

        # 2. Obter Matrizes de Adjacência
        if isinstance(self, GrafoMatriz):
            matriz1 = self.matriz
        else: # é GrafoEsparso
            vertices1 = sorted(self.get_vertices())
            mapa1 = {vertice: i for i, vertice in enumerate(vertices1)}
            n1 = len(vertices1)
            matriz1 = [[0] * n1 for _ in range(n1)]
            for v_origem, vizinhos in self.lista_adjacencia.items():
                for v_destino in vizinhos:
                    matriz1[mapa1[v_origem]][mapa1[v_destino]] = 1

        if isinstance(g2, GrafoMatriz):
            matriz2 = g2.matriz
        else: # é GrafoEsparso
            vertices2 = sorted(g2.get_vertices())
            mapa2 = {vertice: i for i, vertice in enumerate(vertices2)}
            n2 = len(vertices2)
            matriz2 = [[0] * n2 for _ in range(n2)]
            for v_origem, vizinhos in g2.lista_adjacencia.items():
                for v_destino in vizinhos:
                    matriz2[mapa2[v_origem]][mapa2[v_destino]] = 1
        
        n = self.get_numero_de_vertices()
        indices_vertices = list(range(n))
        
        # 3. Gera e testa todas as permutações USANDO A NOSSA FUNÇÃO
        permutacoes = self.gerar_permutacoes(indices_vertices)

        for p in permutacoes:
            mapeamento_valido = True
            for i in range(n):
                for j in range(n):
                    if matriz1[i][j] != matriz2[p[i]][p[j]]:
                        mapeamento_valido = False
                        break
                if not mapeamento_valido:
                    break
            
            if mapeamento_valido:
                vertices1_ord = sorted(self.get_vertices())
                vertices2_ord = sorted(g2.get_vertices())
                mapeamento_real = {vertices1_ord[i]: vertices2_ord[p[i]] for i in range(n)}
                print(f"Isomorfismo encontrado com o mapeamento: {mapeamento_real}")
                return True

        return False

    # --- Métodos de Verificação de Subgrafos ---
    def is_subgrafo(self, super_grafo):
        if not self.lista_adjacencia.keys() <= super_grafo.lista_adjacencia.keys():
            return False
        for v, vizinhos in self.lista_adjacencia.items():
            if not vizinhos.issubset(super_grafo.lista_adjacencia.get(v, set())):
                return False
        return True

    def is_subgrafo_gerador(self, super_grafo):
        if self.lista_adjacencia.keys() != super_grafo.lista_adjacencia.keys():
            return False
        return self.is_subgrafo(super_grafo)

    def is_subgrafo_induzido(self, super_grafo):
        vertices_self = self.lista_adjacencia.keys()
        if not vertices_self <= super_grafo.lista_adjacencia.keys():
            return False
        for v1 in vertices_self:
            vizinhos_super = super_grafo.lista_adjacencia.get(v1, set())
            vizinhos_esperados_em_self = vizinhos_super.intersection(vertices_self)
            if self.lista_adjacencia[v1] != vizinhos_esperados_em_self:
                return False
        return True


    def colorir_grafo(self, ordem=None, verbose=True):
        if not self.lista_adjacencia:
            return 0, {}
        if ordem is None:
            ordem = sorted(self.get_vertices(), key=lambda v: (-len(self.lista_adjacencia[v]), v))
        cores = {}
        for v in ordem:
            usadas = {cores[u] for u in self.lista_adjacencia[v] if u in cores}
            cor = 1
            while cor in usadas:
                cor += 1
            cores[v] = cor
            if verbose:
                print(f"Tentando colorir a aula {v} com {cor} horários...")
        return max(cores.values()), cores



    # --- Métodos de Exibição ---
    def mostrar_lista_adjacencia(self):
        print("\n--- Lista de Adjacência ---")
        if not self.lista_adjacencia:
            print("O grafo está vazio.")
            return
        # Imprime em ordem para consistência
        for no in sorted(self.lista_adjacencia.keys()):
            vizinhos = self.lista_adjacencia[no]
            vizinhos_str = ", ".join(map(str, sorted(list(vizinhos))))
            print(f"{no} -> [ {vizinhos_str} ]")
        print("---------------------------")


if __name__ == "__main__":
    aulas = ['M', 'A', 'C', 'F', 'Q', 'P']
    g = GrafoEsparso()

    # Arestas de conflito
    g.adicionar_aresta('C', 'F')
    g.adicionar_aresta('C', 'A')
    g.adicionar_aresta('F', 'A')
    g.adicionar_aresta('M', 'P')
    g.adicionar_aresta('M', 'A')
    g.adicionar_aresta('P', 'A')
    g.adicionar_aresta('Q', 'F')

    print("-" * 30)
    # Lista conflitos (cada par só uma vez)
    vistos = set()
    for a in sorted(g.get_vertices()):
        for b in sorted(g.lista_adjacencia[a]):
            par = tuple(sorted((a, b)))
            if par not in vistos:
                print(f"- Aula {a} tem conflito com: {b}")
                vistos.add(par)
    print("-" * 30)

    ordem = sorted(g.get_vertices(), key=lambda v: (-len(g.lista_adjacencia[v]), v))
    numero_minimo, cores = g.colorir_grafo(ordem=ordem, verbose=True)

    print(f"Número mínimo de horários necessários: {numero_minimo}")
    print(cores)
