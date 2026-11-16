''' 
operator overloading and method overriding 
defining and using dunder methods in class
'''
import graphviz

class Graph:
    def __init__(self):
        self._adjdict = {}

    def add_vertex(self, a):
        self._adjdict.setdefault(a, set())

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)

        a, b = sorted([a, b])
        self._adjdict.setdefault(a, set()).add(b)
        self._adjdict.setdefault(b, set()).add(a)

    def vertices(self):
        return set(self._adjdict.keys())

    def edges(self):
        return set( (a, b) for a,bs in self._adjdict.items()
            for b in bs if a <= b )

    def neighbors(self, n):
        return self._adjdict.get(n, set())

    def draw(self):
        dot = graphviz.Graph()

        for a in self.vertices():
            dot.node = (str(a))

        for a,b in self.edges():
            dot.edge(str(a), str(b))

        dot.render('Tree', view=True)

    # dunder method, magic methods 
    # Overloading operators in the following 

    def __str__(self):
        return f'Vertices are {self.vertices()} \n Edges are {self.edges()}'

    def __add__(self, other):
        temp = Graph()
        temp._adjdict = self._adjdict | other._adjdict
        return temp 

    def __eq__(self, other):
        return f'equal' if self._adjdict == other._adjdict else f'not equal'


G1 = Graph()
G1.add_edge('A', 'B')
G1.add_edge('A', 'C')
G1.add_edge('A', 'C')
G1.add_edge('A', 'D')
G1.add_edge('C', 'D')

G2 = Graph()
G2.add_edge('M', 'N')
G2.add_edge('M', 'O')
G2.add_edge('M', 'P')
G2.add_edge('O', 'P')
G2.add_edge('N', 'P')

print(G1._adjdict)
print(G2._adjdict)

print(G1 == G1)

