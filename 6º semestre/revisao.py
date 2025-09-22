class GrafoEsparso:
    def __init__(self):
        self.lista_adjacencia = {}
        self.numero_aresta = 0

    
    def get_numero_aresta(self):
        return self.numero_aresta
 

    def get_numero_vertices(self):
        contador = 0
        for a in self.lista_adjacencia:
            contador += 1
        return contador
    

    def get_vertice(self):
        lista = []
        for a in self.lista_adjacencia:
            lista.append(a)
        return lista
    
    
    def get_arestas(self):
        lista = []
        for a in self.lista_adjacencia:
            lista.append(self.lista_adjacencia[a])
        return lista

    
    def adicionar_no(self, vertice):
        if vertice in self.lista_adjacencia:
            return "vertice já existe"
        self.lista_adjacencia[vertice] = []
        return f"adicionado vertice {vertice} na lista"
    

    def adicionar_aresta(self, v1, v2):
        if v1 not in self.get_vertice():
            self.adicionar_no(v1)
        elif v2 not in self.get_vertice():
            self.adicionar_no(v1)
        self.lista_adjacencia[v1].append(v2)
        self.lista_adjacencia[v2].append(v1)
        self.numero_aresta += 1
        return f"aresta entre {v1} e {v2} adicionada"


    def get_sequencia_de_graus(self):
        lista = []
        if self.get_numero_vertices == 0:
            return 
        lista_aresta = self.get_arestas()
        for a in lista_aresta:
            lista.append(len(a))
        lista = sorted(lista)
        return lista


    def remover_aresta(self, v1, v2):
        if v1 not in self.get_vertice() and v2 not in self.get_vertice():
            return
        self.lista_adjacencia[v1].remove(v2)
        self.lista_adjacencia[v2].remove(v1)
        self.numero_aresta -= 1
        return f"aresta de {v1} e {v2} removidas"


    def is_nulo(self):
        if self.get_numero_vertices() > 0:
            if self.get_numero_aresta() == 0:
                return True
            else:
                return False
        else:
            return False
    

    def is_simples(self):
        if self.is_nulo():
            return False
        for a in self.lista_adjacencia:
            if a in self.lista_adjacencia[a]:
                return False
            for b in self.lista_adjacencia[a]:
                # print(self.lista_adjacencia[a].count(b))
                if self.lista_adjacencia[a].count(b) > 1:
                    return False
        return True    
    

    def is_complete(self):
        if not self.is_simples:
            return False
        for a in self.lista_adjacencia:
            if len(self.lista_adjacencia[a]) == self.get_numero_vertices() - 1:
                return True
        return False
    

    def is_isomorfo(self, g1, g2):
        if g1.get_numero_vertices() != g2.get_numero_vertices():
            return False
        elif g1.get_numero_aresta() != g2.get_numero_aresta():
            return False
        elif g1.sequencia_de_grau() != g2.sequencia_de_grau():
            return False
        return True


    def is_subgrafo(self, g1, g2):
        for i in g1.get_vertices():
            if i not in g2.get_vertices():
                return False
        for i in g1.lista_adjacencia:
            for j in g1.lista_adjacencia[i]:
                if j not in g2.lista_adjacencia[i]:
                    return False
        return True


    def is_subgrafo_gerador(self, g2):
        if self.get_numero_vertives() != g2.get_numero_vertices():
            return False
        for i in self.lista_adjacencia:
            for j in self.lista_adjacencia[i]:
                if j in g2.lista_adjacencia[i]:
                    return True
        return False


    def is_subgrafo_induzido(self, g2):
        for i in self.get_vertice():
            if i not in g2.get_vertice():
                return False
        
        vh = self.get_vertice()
        for i in self.lista_adjacencia:
            for j in g2.lista_adjacencia[i]:
                if j not in self.lista_adjacencia[i] and j in vh:
                    return False
            for k in self.lista_adjacencia[i]:
                if k not in g2.lista_adjacencia[i] and k not in vh:
                    return False
        return True 
    
    def colorir_grafo(self, n_color):
        if self.get_numero_vertices() < n_color:
            return True
                
        list_color = []
        for i in range(n_color):
            list_color.append(i + 1)
        lista = {}
        for i in self.get_vertice():
            lista[i] = 0

        for i in self.get_vertice():
            flag_color = False
            lista_color_neigh = []
            for j in self.lista_adjacencia[i]:
                if lista[j] != 0:
                    lista_color_neigh.append(lista[j])
            for k in list_color:
                if k not in lista_color_neigh:
                    lista[i] = k
                    flag_color = True
                    break
            if not flag_color:
                return False
        return True
            




    def mostrar_lista(self):
        lista = []
        # print(self.lista_adjacencia)
        for a in self.lista_adjacencia:
            print(f"{a} -> {self.lista_adjacencia[a]}")


g = GrafoEsparso()
print(g.adicionar_no("A"))
print(g.adicionar_no("B"))
print(g.adicionar_no("C"))
print(g.get_numero_vertices())
print(g.get_vertice())
print(g.adicionar_aresta("A", "B"))
print(g.adicionar_aresta("B", "C"))
print(g.get_numero_aresta())
print(g.get_arestas())
print(g.get_sequencia_de_graus())
print(g.remover_aresta("B", "C"))
print(g.get_arestas())
# print(g.adicionar_aresta("A", "C"))
print(g.adicionar_aresta("B", "C"))
print(g.adicionar_aresta("A", "C"))
print(g.is_nulo())
print(g.is_simples())
print(g.is_complete())
g2 = GrafoEsparso()
print(g2.adicionar_no("A"))
print(g2.adicionar_no("B"))
print(g2.adicionar_no("C"))
print(g2.adicionar_no("D"))
print(g2.adicionar_no("E"))
print(g2.adicionar_aresta("A", "B"))
print(g2.adicionar_aresta("B", "C"))
# print(g2.adicionar_aresta("A", "C"))
# print(g2.adicionar_aresta("A", "D"))
# print(g2.adicionar_aresta("C", "D"))
# print(g2.adicionar_aresta("B", "D"))
print(g.is_subgrafo_induzido(g2))
print(g.colorir_grafo(2))
g.mostrar_lista()