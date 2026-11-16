"""
An implementation of graphs where we have one object per _vertex_.
"""

import graphviz

class Vertex:
    """A vertex has a name and a set of neighbours."""

    def __init__(self, name):
        self._name = name # "A"
        self._neighbours = set()  # { <Vertex object at 0x10a234690>, <Vertex object at 0x10a183820> }

    def add_edge(self, other_vertex):
        """Add an edge between this vertex and another vertex."""
        self._neighbours.add(other_vertex)
        other_vertex._neighbours.add(self)

    def add_edges(self, *other_vertices):
        """Add edges between this vertex and other vertices."""
        for other in other_vertices:
            self._neighbours.add(other)
            other._neighbours.add(self)

    def edges(self):
        """Return edges of this vertex"""
        return {
            (self._name, n._name) if self._name < n._name else (n._name, self._name)
            for n in self._neighbours
        }

    def neighbours(self):
        """Return neighbours of this vertex"""
        return { n._name for n in self._neighbours }

def visualise(edges):
    """Visualise graph using graphviz library"""
    dot = graphviz.Graph()
    dot.attr(rankdir='LR')
    for a, b in edges:
        dot.edge(str(a), str(b))
    dot.render(view=True)

# Test code
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")

a.add_edges(b, d, e)
b.add_edges(c, e)
c.add_edges(d)
d.add_edges(e)

print(a._neighbours)

all_edges = set()
for v in [a,b,c,d,e]:
    all_edges = all_edges | v.edges()
print(all_edges)

for v in [a,b,c,d,e]:
    print(v._name, v.neighbours())

visualise(all_edges)
