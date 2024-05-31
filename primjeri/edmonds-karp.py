import collections
	
class Graph:

    """"
    Ova klasa predstavlja reprezentaciju usmjerenog grafa
    preko matrice susjedstva.
    """

    def __init__(self, graph):
        self.graph = graph #rezidualni graf
        self.row = len(graph)
	
    def bfs(self, s, t, parent):

        """
        Vraca true ako postoji put od izvora 's' do utoka 't' u rezidualnom grafu.
        Takodjer popunjava parent[] kako bi sacuvao putanju.
        """
        
        # Oznacava sve cvorove koji nisu posjeceni
        visited = [False] * self.row
        
        # Kreira red za BFS
        queue = collections.deque()
        
        # Oznacava cvor izvor kao posjecen i izbacuje ga iz reda
        queue.append(s)
        visited[s] = True
        
        # Standardna BFS petlja
        while queue:
            u = queue.popleft()
        
            # Uzima sve susjede cvora kojeg smo izbacili iz reda (cvor u)
            # Ako susjed nije posjecen onda ga oznacavamo kao posjecenog i
            # izbacujemo iz reda
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                
        # Ako smo dosli to utoka u BFS-u pocevsi of izvora, onda vracamo
        # true, inace false
        return visited[t]
        
    def edmonds_karp(self, source, sink):
        # Ovaj niz popunjava BFS, cuvaju se putanje
        parent = [-1] * self.row
        
        max_flow = 0  # Nema protoka u pocetku
        
        # Sve dok postoji put od izvora do utoka povecavaj protok
        while self.bfs(source, sink, parent):
            # Nadji minimalni preostali kapacitet grana na putanji koju
            # je popunio BFS. Odnosno, nadji maksimalni protok kroz tu putanju.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            
            # Dodaj trenutni protok na ukupni protok
            max_flow += path_flow
            
            # Azuriraj preostale kapacitet grana i obrnutih grana na putanji
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        
        return max_flow
    
# PRIMJER 1
    
matrica1 = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

graf1 = Graph(matrica1)

izvor = 0
utok = 5

maks_protok1 = graf1.edmonds_karp(izvor, utok)
print("Maksimalni protok 1:", maks_protok1)
print()

# PRIMJER 2

matrica2 = [[0, 10, 0, 8, 0, 0],
            [0, 0, 5, 2, 0, 0],
            [0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 10, 0],
            [0, 0, 8, 0, 0, 10],
            [0, 0, 0, 0, 0, 0]]

graf2 = Graph(matrica2)

izvor = 0
utok = 5

maks_protok2 = graf2.edmonds_karp(izvor, utok)
print("Maksimalni protok 2:", maks_protok2)
print()
