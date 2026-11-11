import graphviz

class Graph:
    "Undirected graph represented by sets of vertices and edges"

    def __init__(self):
        self._vertices = set() # {A,B,C}
        self._edges = set() # {(A,B),(A,C)}

    def add_vertex(self, a):
        "Add a vertex a"
        self._vertices.add(a)

    def add_edge(self, a, b):
        "Add an edge between vertex a and b"
        self.add_vertex(a)
        self.add_vertex(b)
        if (b,a) not in self._edges:
            self._edges.add((a,b))

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

        # Using comprehension
        # return {
        #     x if y == a else y
        #     for x,y in self._edges
        #     if a in [x,y]
        # }
    
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

