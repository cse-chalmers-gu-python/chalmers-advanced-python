class Graph:
    """
    Undirected graph represented by an adjacency dictionary.

    It has the exact same API as graph1.Graph,
    but the internal implemenation is different.
    """

    def __init__(self):
        self._adjdict = {} # {A: {B,C}}

    def add_vertex(self, a):
        "Add a vertex a"
        self._adjdict.setdefault(a, set())

    def add_edge(self, a, b):
        "Add an edge between vertex a and b"
        self.add_vertex(a)
        self.add_vertex(b)
        self._adjdict[a].add(b)
        self._adjdict[b].add(a)

    def vertices(self):
        "Return all vertices"
        return set(self._adjdict.keys())

    def edges(self):
        "Return all edges"
        es = set()
        for (a, bs) in self._adjdict.items():
            for b in bs:
                if a <= b:
                    es.add((a, b))
        return es

    def neighbours(self, a):
        "Return neighbours of vertex a"
        return self._adjdict.get(a, set())

# Test code
G = Graph()

G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("X", "B")
G.add_edge("X", "Y")

print(G.vertices())
print(G.edges())

for v in ["A","B","C","X","Y"]:
    print(v, G.neighbours(v))

