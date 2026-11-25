"""
property-based testing for graphs
"""

type Vertex = str
type Edge = tuple[Vertex, Vertex]

class Graph:
    """
    Directed graph represented by sets of vertices and edges.
    """

    def __init__(self):
        self._vertices: set[Vertex] = set()
        self._edges: set[Edge] = set()

    def add_vertex(self, a: Vertex) -> None:
        "Add a vertex a"
        self._vertices.add(a)

    def add_edge(self, a: Vertex, b: Vertex) -> None:
        "Add an edge from vertex a and b"
        self.add_vertex(a)
        self.add_vertex(b)
        self._edges.add((a,b))
        # self._edges.add((b,a)) # 🐞

    def vertices(self) -> set[Vertex]:
        "Return all vertices"
        return self._vertices

    def edges(self) -> set[Edge]:
        "Return all edges"
        return self._edges

    def neighbours(self, a: Vertex) -> set[Vertex]:
        "Return vertices directly reachable from a"
        return { y for x,y in self._edges if x == a } 

# Test code
import unittest
from hypothesis import given, strategies as st

class TestGraphMethods(unittest.TestCase):

    def test_empty(self):
        """Simple test (no property)"""
        G = Graph()
        self.assertEqual(len(G.vertices()), 0)

    @given(st.sets(st.characters()))
    def test_add_vertex(self, vertices: set[Vertex]):
        """
        Given a set of vertices, add them all to a Graph,
        and ensure they are all returned by vertices() getter.
        """
        G = Graph()
        for v in vertices:
            G.add_vertex(v)
        self.assertSetEqual(G.vertices(), vertices)

    @given(st.sets(st.tuples(st.characters(), st.characters())))
    def test_add_edge(self, edges: set[Edge]):
        """
        Given a set of edges, add them all to a Graph,
        and ensure they are all returned by edges() getter.
        HINT: uncomment the buggy line 🐞 above to break this property.
        """
        G = Graph()
        for a,b in edges:
            G.add_edge(a,b)
        self.assertEqual(len(G.edges()), len(edges))

if __name__ == '__main__':
    unittest.main()
