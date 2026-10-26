# lecture 2025-11-11

import graphviz

class Graph:
    "undirected graphs represented by an adjacency dict"

    def __init__(self):
        self._adjdict = {}

    # setters
    def add_edge(self, a, b):
        self._adjdict[a] = self._adjdict.get(a, set())
        self._adjdict[a].add(b)
        self._adjdict[b] = self._adjdict.get(b, set())
        self._adjdict[b].add(a)

    # getters
    def vertices(self):
        return set(self._adjdict.keys())

    def edges(self):
        return {(a, b) for (a, bs) in self._adjdict.items() for b in bs if a <= b}
    
    def edges_long_way(self):
        es = set()
        for (a, bs) in self._adjdict.items():
            for b in bs:
                if a <= b:
                    es.add((a, b))
        return es


def viz(graph):
    dot = graphviz.Graph()
    for a in graph.vertices():
        dot.node(str(a))
    for a, b in graph.edges():
        dot.edge(str(a), str(b))
    dot.render('_intrograph.gv', view=True)
    
    

G = Graph()

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)




print(G.vertices())
print(G.edges())
print(G._adjdict)

viz(G)



