"""
Initial version of graph testing code for L07.
This is the version to use during the lecture 👍🏻
"""

class Graph:
    """
    Directed graph represented by sets of vertices and edges.
    """

    def __init__(self):
        self._vertices = set() # {A,B,C}
        self._edges = set() # {(A,B),(A,C)}

    def add_vertex(self, a):
        "Add a vertex a"
        self._vertices.add(a)

    def add_edge(self, a, b):
        "Add an edge from vertex a and b"
        self.add_vertex(a)
        self.add_vertex(b)
        self._edges.add((a,b))
        self._edges.add((b,a))

    def vertices(self):
        "Return all vertices"
        return self._vertices

    def edges(self):
        "Return all edges"
        return self._edges

    def neighbours(self, a):
        "Return vertices directly reachable from a"
        return { (x,y) for x,y in self._edges if x == a }

    # def islands(self):
    #     "Return vertices without edges"
    #     ...

    # def reachable(self, a, b):
    #     "Return a path from vertex a to b, if one exists"
    #     visited = set()
    #     def visit(v):
    #         if v == b: return [v]
    #         for n in self.neighbours(v):
    #             if n in visited: break
    #             visited.add(n)
    #             if r := visit(n):
    #                 return [v, r]
    #     return visit(a)
