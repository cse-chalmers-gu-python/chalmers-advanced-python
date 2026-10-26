# live coding for lecture 5 Tuesday, based on lecture 4

import graphviz

class Graph:
    "undirected graph represented by adjacency dict"

    def __init__(self, es=None):
        self._adjdict = {}
        if es:
            for (a, b) in es:
                self.add_edge(a, b)

    # setter methods
    def add_edge(self, a, b):
        "add edge in both directions"
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set()).add(a)

    def add_vertex(self, a):
        self._adjdict[a] = self._adjdict.get(a, set())

    def remove_vertex(self, a):
        del self._adjdict[a]
        for b in self._adjdict:
            self._adjdict[b].discard(a)
        
    # getter methods
    def vertices(self):
        return self._adjdict.keys()

    def edges(self):
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs if a <= b}

    def vizmethod(self):
        return graphviz.Graph()
    
    def viz(self):
        dot = self.vizmethod()
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
    
        
class DiGraph(Graph):

    # overwrite: store edge in only one direction
    def add_edge(self, a, b):
        "add edge only in one direction but the targets vertex if needed"
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set())

    def edges(self):
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs}

    def vizmethod(self):
        return graphviz.Digraph()


class WeightedGraph(Graph):

    def __init__(self, es=None):
        super().__init__(es)
        self._weightdict = {}

    def set_weight(self, a, b, w):
        self.add_edge(a, b)
        self._weightdict[(a, b)] = w
        
    def get_weight(self, a, b):
        return self._weightdict.get((a, b), None)

    def viz(self):
        dot = self.vizmethod()
        for a in self.vertices():
            dot.node(str(a))
        for a, b in self.edges():
            dot.edge(str(a), str(b), label=str(self.get_weight(a, b)))
        dot.render('_graphdemo.gv', view=True)    

    def __str__(self):
        return (str(self._adjdict) + str(self._weightdict))

class WeightedDiGraph(WeightedGraph, DiGraph):
    pass

    
if __name__ == '__main__':
    G = WeightedDiGraph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(4, 1)
    G.add_edge(5, 2)
    G.add_edge(2, 5)
    G.add_vertex(6)

    G.set_weight(1, 2, 120)
    G.set_weight(1, 3, 260)
    G.set_weight(5, 2, 20)
    G.set_weight(2, 5, 1260)

#    G.remove_vertex(3)

    # before: inconsistent
    # G = Graph({1: {2, 3, 4}, 2: {1, 5}, 4: {1}, 5: {2}, 6: set()})
    
    # G = Graph({(1, 2), (2, 5), (1, 4)})

    print(G)
    print(G.vertices())
    print(G.edges())
    G.viz()




