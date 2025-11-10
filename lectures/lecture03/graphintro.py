# live coding for lecture 3

import graphviz

class Graph:
    "undirected graph represented with adjacency dict"

    def __init__(self):
        self._adjdict = {}

    # setter methods
    def add_edge(self, a, b):
        self._adjdict[a] = self._adjdict.get(a, set())
        self._adjdict[a].add(b)
        self._adjdict[b] = self._adjdict.get(b, set())
        self._adjdict[b].add(a)

    def add_vertex(self, a):
        self._adjdict[a] = self._adjdict.get(a, set())

    # getter methods
    def vertices(self):
        return self._adjdict.keys()

    # the short way
    def edges(self):
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs if a <= b}

"""
    # the long way
    def edges(self):
        es = set()
        for a, bs in self._adjdict.items():
            for b in bs:
                if a <= b:
                    es.add((a, b))
        return es
"""

def viz(G):
    dot = graphviz.Graph()
    for a in G.vertices():
        dot.node(str(a))
    for a, b in G.edges():
        dot.edge(str(a), str(b))
    dot.render('_graphdemo.gv', view=True)
    

G = Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(4, 2)
G.add_vertex(6)


print(G._adjdict)
print(G.vertices())
print(G.edges())
viz(G)




