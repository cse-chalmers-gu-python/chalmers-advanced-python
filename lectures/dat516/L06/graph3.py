class Graph:
    """
    Undirected graph represented by sets of vertices and edges.

    It has the exact same internal implementation as graph1.Graph,
    but its API is different.
    """

    def __init__(self):
        self._vertices = set() # {A,B,C}
        self._edges = set() # {(A,B),(A,C)}

    def set_neighbours(self, a, neighbours):
        "Add edges from vertex a to all neighbours"
        self._vertices.add(a)
        for n in neighbours:
            self._vertices.add(n)
            if (n,a) not in self._edges:
                self._edges.add((a,n))

    def vertices(self):
        "Return all vertices"
        return self._vertices

    def edges(self):
        "Return all edges"
        return self._edges

    def neighbours(self, a):
        "Return neighbours of vertex a"
        ns = set()
        for x,y in self._edges:
            if x == a: ns.add(y)
            if y == a: ns.add(x)
        return ns

# Test code
G = Graph()

G.set_neighbours("A", ["B"])
G.set_neighbours("B", ["A", "X", "C"])
G.set_neighbours("C", ["B"])
G.set_neighbours("X", ["B", "Y"])
G.set_neighbours("Y", ["X"])

print(G.vertices())
print(G.edges())

for v in G.vertices():
    print(v, G.neighbours(v))
