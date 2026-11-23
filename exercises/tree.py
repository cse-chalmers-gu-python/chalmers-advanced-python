import copy 
import graphviz
import os 
from typing import Never

type Vertex = str 
type Edge = tuple[Vertex, Vertex]
type AdjDict = dict[Vertex, set[Vertex]]

class Graph:
    def __init__(self, adjdict: AdjDict | None = None) -> None:
        if adjdict is not None: 
            self._adjdict = adjdict
        else:
            self._adjdict: AdjDict = {}

    def add_vertex(self, a: Vertex) -> None:
        self._adjdict.setdefault(a, set())

    def add_edge(self, a: Vertex, b: Vertex) -> None:
        self.add_vertex(a)
        self.add_vertex(b)
        a, b = sorted([a, b])
        self._adjdict[a].add(b)
        self._adjdict[b].add(a)

    def vertices(self) -> set[Vertex]:
        return set(self._adjdict.keys())

    def edges(self) -> set[Edge]:
        return {
            (a, b)
            for a, bs in self._adjdict.items()
            for b in bs if a <= b
        }

    def draw(self):
        dot = graphviz.Graph()
        for a in self.vertices():
            dot.node(str(a))
        for a,b in self.edges():
            dot.edge(str(a), str(b))
        dot.render(view=True)

class Tree(Graph):
    def __init__(self, root: Vertex) -> None:
        super().__init__()
        self._adjdict[root] = set()

    def add_vertex(self, vertex: Vertex) -> Never:
        raise NotImplementedError("Standalone vertices can't be added to a Tree, use add_edge() instead")

    def add_edge(self, parent: Vertex, child: Vertex) -> None:
        if parent not in self._adjdict:
            raise ValueError("Parent does not exist")
        elif child in self._adjdict:
            raise ValueError("Child already exists")
        else:
            self._adjdict[parent].add(child)
            self._adjdict[child] = set()

    def edges(self) -> set[Edge]:
        return {
            (parent, child)
            for parent, children in self._adjdict.items()
            for child in children
        }
    
    def leaves(self) -> set[Vertex]:
        return {
            vertex
            for vertex in self._adjdict
            if self._adjdict[vertex] == set()
        }
        
    def dfs(self, start):
        if start not in self._adjdict:
            raise ValueError("Starting vertex does not exist")

        visited = []

        def visit(vertex):
            visited.append(vertex)
            for child in self._adjdict[vertex]:
                visit(child)

        visit(start)
        return visited

