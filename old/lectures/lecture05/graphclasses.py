# lecture 5, 2025-11-17

import graphviz

class Graph:
    """
    undirected graph represented by adjacency dict
    showing the neighbours of each vertex
    """

    def __init__(self, edges=None):
        self._adjdict = {}
        if edges:
            for (a, b) in edges:
                self.add_edge(a, b)

    # setter methods
    "add a to the neighbours of b and vice-versa"
    def add_edge(self, a, b):
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set()).add(a)

    def add_vertex(self, a):
        self._adjdict[a] = self._adjdict.get(a, set())

    def remove_vertex(self, a):
        self._adjdict[a] = set()
        for b in self._adjdict:
            self._adjdict[b].discard(a)
        
    # getter methods
    def vertices(self):
        return self._adjdict.keys()

    def edges(self):
        "edges in one direction"
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs if a <= b}

    def vizclass(self):
        return graphviz.Graph() 

    def viz(self):
        dot = self.vizclass()
        for a in self.vertices():
            dot.node(str(a))
        for a, b in self.edges():
            dot.edge(str(a), str(b))
        dot.render('_graphdemo.gv', view=True)    

    # hidden methods

    def __len__(self):
        return len(self.vertices())

    def __str__(self):
        return str(self._adjdict)

    def __eq__(self, other):
        return self._adjdict == other._adjdict

    def __getitem__(self, a):
        "return the set of neighbours of a vertex"
        return self._adjdict[a]
    
    def __setitem__(self, a, bs):
        "change the set of neighbours of a vertex"
        ## self._adjdict[a] = bs  # not safe!
        self.remove_vertex(a)
        for b in bs:
            self.add_edge(a, b)


class DiGraph(Graph):
    "directed graphs"

    "add b to the neighbours of a, and b to vertices if not yet there"
    def add_edge(self, a, b):
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set())

    def edges(self):
        "edges in one direction"
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs}
    
    def vizclass(self):
        return graphviz.Digraph() 

class WeightedGraph(Graph):
    "graphs where edges have weights, stored in a dict"

    def __init__(self, edges=None):
        super().__init__(edges)
        self._weightdict = {}

    def set_weight(self, a, b, w):
        if (a, b) in self.edges():
            self._weightdict[(a, b)] = w
        
    def get_weight(self, a, b):
        return self._weightdict.get((a, b), None)

    def viz(self):
        dot = self.vizclass()
        for a in self.vertices():
            dot.node(str(a))
        for a, b in self.edges():
            dot.edge(str(a), str(b), label=str(self.get_weight(a, b)))
        dot.render('_graphdemo.gv', view=True)    

        
# added an example on multiple inheritance after the lecture

class WeightedDiGraph(WeightedGraph, DiGraph):
    # you don't need to overwrite anything, but syntax requires a statement
    pass
    

if __name__ == '__main__':
  G = WeightedDiGraph()
  G.add_edge(1, 2)
  G.add_edge(1, 3)
  G.add_edge(1, 4)
  G.add_edge(5, 2)
  G.add_vertex(6)

  G.set_weight(1, 2, 120)
  G.set_weight(1, 4, 140)


  H = Graph({(1, 2), (2, 4), (4, 3), (4, 2)})

  print(G)
  print(G.edges())
  G.viz()





