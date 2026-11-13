class Graph:
    def __init__(self):
        self._adjdict = {} # {A: {B,C}}

    def add_vertex(self, a):
        self._adjdict.setdefault(a, set())

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self._adjdict[a].add(b)
        self._adjdict[b].add(a)

    def vertices(self):
        return set(self._adjdict.keys())

    def edges(self):
        es = set()
        for (a, bs) in self._adjdict.items():
            for b in bs:
                if a <= b:
                    es.add((a, b))
        return es

    # code above is copied from L04

    def __str__(self):
        """string representation of object"""
        return f"Graph <vertices: {len(self.vertices())}, edges: {len(self.edges())}>"

    def __len__(self):
        """length of graph is the number of vertices"""
        return len(self._adjdict)

    def __gt__(self, other):
        """greater than (>)"""
        return len(self) > len(other)

    def __ge__(self, other):
        """greater than or equal (>=)"""
        return len(self) >= len(other)

    def __contains__(self, a):
        """membership (in)"""
        return a in self.vertices()

    def __add__(self, other):
        """combine two graphs together"""
        ng = Graph()
        ng._adjdict = self._adjdict | other._adjdict
        return ng

# Test code
G = Graph()
G.add_edge("A", "B")
G.add_edge("A", "D")
G.add_edge("A", "E")
G.add_edge("B", "C")
G.add_edge("B", "E")
G.add_edge("C", "D")
G.add_edge("D", "E")

H = Graph()
H.add_edge(1, 2)
H.add_edge(2, 3)
H.add_edge(3, 1)

"""
>>> G
<__main__.Graph object at 0x10a03bed0>
>>> print(G)
Graph <vertices: 5, edges: 7>
>>> len(G)
5
>>> len(H)
3
>>> G > H
True
>>> I = G + H
>>> I
<__main__.Graph object at 0x109e39d10>
>>> print(I)
Graph <vertices: 8, edges: 10>
"""

