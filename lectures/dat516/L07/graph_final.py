"""
Final version of graph testing code for L07.
If you are viewing this during a lecture, open graph.py instead ⚠️

The ladybird 🐞 indicates lines which were buggy in the initial version.
"""

Vertex = str
Edge = tuple[Vertex, Vertex]

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
        # self._edges.add((b,a)) 🐞

    def vertices(self) -> set[Vertex]:
        "Return all vertices"
        return self._vertices

    def edges(self) -> set[Edge]:
        "Return all edges"
        return self._edges

    def neighbours(self, a: Vertex) -> set[Vertex]:
        "Return vertices directly reachable from a"
        # return { (x,y) for x,y in self._edges if x == a } 🐞
        return { y for x,y in self._edges if x == a } 

    def is_connected(self) -> bool:
        "Are all vertices in graph connected?"
        groups = [ {v} for v in self.vertices() ]
        def find_group_index(v: Vertex) -> int:
            ix = 0
            for g in groups:
                if v in g: return ix
                ix += 1
            return -1
        for a,b in self.edges():
            ixa = find_group_index(a)
            ixb = find_group_index(b)
            groups[ixa] |= groups[ixb]
            groups.pop(ixb)
        return len(groups) <= 1

    def islands(self) -> set[Vertex]:
        "Return vertices without edges"
        islands = set()
        for v in self.vertices():
            is_island = True
            # for a,b in self.edges():
            #     if v == a: is_island = False 🐞
            for e in self.edges():
                if v in e: is_island = False
            if is_island: islands.add(v)
        return islands

    # def reachable0(self, a: Vertex, b: Vertex) -> list[Vertex] | None:
    #     "Buggy version of reachable()"
    #     visited = set()
    #     def visit(v: Vertex) -> list[Vertex] | None:
    #         if v == b: return [v]
    #         for n in self.neighbours(v):
    #             if n in visited: continue
    #             # visited.add(n) 🐞
    #             if r := visit(n):
    #                 return [v, *r]
    #     return visit(a)

    def reachable(self, a: Vertex, b: Vertex) -> list[Vertex] | None:
        "Return a path from vertex a to b, if one exists"
        visited = set()
        def visit(v: Vertex) -> list[Vertex] | None:
            if v == b: return [v]
            for n in self.neighbours(v):
                if n in visited: continue
                visited.add(n)
                if r := visit(n):
                    return [v, *r]
        return visit(a)


# Test code
import unittest

class TestGraphMethods(unittest.TestCase):
    """
    In unittest, our test suite should be a class inheriting from TestCase.
    Each method in this class starting with `test_` is an individual test.
    """

    def setUp(self):
        """
        Create test fixture for use in test cases.
        This is run before every test.
        """
        G = Graph()
        G.add_edge("A", "B")
        G.add_edge("B", "C")
        G.add_edge("X", "B")
        G.add_edge("X", "Y")
        G.add_edge("B", "X")
        self.example = G

    def test_empty(self):
        G = Graph() # create local graph object
        self.assertEqual(len(G.vertices()), 0)

    def test_add_vertex(self):
        G = Graph()
        G.add_vertex("A")
        self.assertEqual(len(G.vertices()), 1)

    def test_add_vertex_twice(self):
        G = Graph()
        G.add_vertex("A")
        G.add_vertex("A")
        self.assertEqual(len(G.vertices()), 1)

    def test_adding_edges_adds_vertex(self):
        G = Graph()
        self.assertEqual(len(G.vertices()), 0)
        G.add_edge("A", "B")
        self.assertIn("A", G.vertices())
        self.assertIn("B", G.vertices())

    def test_neighbours(self):
        G = self.example # use test fixture
        self.assertEqual(G.neighbours("A"), {"B"})
        self.assertEqual(G.neighbours("B"), {"C", "X"})
        self.assertEqual(G.neighbours("C"), set())
        self.assertEqual(G.neighbours("X"), {"B", "Y"})
        self.assertEqual(G.neighbours("Y"), set())

    def test_is_connected_true(self):
        G = Graph()
        G.add_edge("1", "2")
        G.add_edge("2", "3")
        G.add_edge("3", "4")
        self.assertTrue(G.is_connected())

    def test_is_connected_false(self):
        G = Graph()
        G.add_edge("1", "2")
        G.add_edge("3", "4")
        self.assertFalse(G.is_connected())

    def test_islands(self):
        G = Graph()
        G.add_edge("1", "2")
        G.add_vertex("3")
        self.assertSetEqual(G.islands(), {"3"})
        G.add_edge("1", "3")
        self.assertSetEqual(G.islands(), set())

    def test_reachable(self):
        G = self.example
        self.assertEqual(G.reachable("A", "B"), ["A","B"])
        self.assertEqual(G.reachable("A", "C"), ["A","B","C"])
        self.assertEqual(G.reachable("A", "X"), ["A","B","X"])
        self.assertEqual(G.reachable("A", "Y"), ["A","B","X","Y"])
        self.assertIsNone(G.reachable("Y", "A"))
        self.assertIsNone(G.reachable("Y", "B"))
        self.assertIsNone(G.reachable("Y", "C"))
        self.assertIsNone(G.reachable("C", "A"))

    # def test_reachable0(self):
    #     "Works with buggy implementation when graph is acyclic"
    #     G = Graph()
    #     G.add_edge("A", "B")
    #     G.add_edge("B", "C")
    #     G.add_edge("X", "B")
    #     G.add_edge("X", "Y")
    #     # G.add_edge("B", "X")  # triggers bug (sometimes, depending on neighbour order)
    #     self.assertEqual(G.reachable0("A", "C"), ["A","B","C"])
    #     self.assertIsNone(G.reachable0("Y", "A"))

if __name__ == '__main__':
    # Run tests if running module as main (i.e. not importing it)
    unittest.main()

