import graphviz

class Graph:
    "Undirected graph represented by an adjacency dictionary"

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

        # Using comprehension
        # return {
        #     (a, b)
        #     for (a, bs) in self._adjdict.items()
        #     for b in bs
        #     if a <= b
        # }

    def neighbours(self, a):
        "Return neighbours of vertex a"
        return self._adjdict.get(a, set())

    def visualise(self):
        "Visualise graph using graphviz library"
        dot = graphviz.Graph()
        dot.attr(rankdir='LR')
        for a in self.vertices():
            dot.node(str(a))
        for a, b in self.edges():
            dot.edge(str(a), str(b))
        dot.render('_intrograph.gv', view=True)

# Test code
G = Graph()

G.add_edge("A", "B")
G.add_edge("A", "D")
G.add_edge("A", "E")
G.add_edge("E", "A") # ignored as A-E already exists
G.add_edge("B", "C")
G.add_edge("B", "E")
G.add_edge("C", "D")
G.add_edge("D", "E")

print(G.vertices())
print(G.edges())
print(G.neighbours("B"))

G.visualise()

