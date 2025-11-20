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
        return set(self._adjdict.keys())

    def edges(self):
        "edges in one direction"
        return {(a, b) for a, bs in self._adjdict.items()
                       for b in bs if a <= b}

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



if __name__ == '__main__':
  G = Graph()
  print(G)
  G.add_edge(1, 2)
  G.add_edge(1, 3)
  G.add_edge(1, 4)
  G.add_edge(5, 2)
  G.add_vertex(6)

  print(G)
  print(G.edges())





