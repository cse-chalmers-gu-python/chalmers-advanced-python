# live coding for lecture 4

import graphviz

class Graph:
    "undirected graph represented with adjacency dict"

    def __init__(self, adjdict=None):
        if adjdict:
            self._adjdict = adjdict
        else:
            self._adjdict = {}

    # setter methods
    def add_edge(self, a, b):
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set()).add(a)

    def add_vertex(self, a):
        self._adjdict[a] = self._adjdict.get(a, set())

    def remove_vertex(self, a):
        pass
        
    # getter methods
    def vertices(self):
        return self._adjdict.keys()

    def edges(self):
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs if a <= b}

    def viz(self):
        dot = graphviz.Graph()
        for a in self.vertices():
            dot.node(str(a))
        for a, b in self.edges():
            dot.edge(str(a), str(b))
        dot.render('_graphdemo.gv', view=True)    

    # hidden methods

    def __repr__(self):
        return 'Graph(' + str(self._adjdict) + ')'

    def __eq__(self, other):
        return self._adjdict == other._adjdict
    
        
H = Graph({1: {2, 3, 4}, 2: {1, 5}, 3: {1}, 4: {1}, 5: {2}, 6: set()})

G = Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(5, 2)
G.add_vertex(6)

print(G == H)

"""
print(G)
print(G.vertices())
print(G.edges())
G.viz()
"""



