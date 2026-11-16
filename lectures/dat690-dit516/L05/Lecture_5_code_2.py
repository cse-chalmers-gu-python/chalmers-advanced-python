'''
Inheritence 
We use Graph class as the base-class and create its child named WeightedGraph
Some of Graph methods are overridden in WeightedGraph
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
        return f' In graph class \nVertices are {self.vertices()} \nEdges are {self.edges()}'

    def __add__(self, other):
        temp = Graph()
        temp._adjdict = self._adjdict | other._adjdict
        return temp 
        # return self._adjdict | other._adjdict 


    def __eq__(self, other):
        return f'equal' if self._adjdict == other._adjdict else f'not equal'

    def __len__(self):
        counter = 0
        for egde in self.edges():
            counter += 1

        return counter
        # return len()

# Inheritance 

#       child (parent)
class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()
        self._weightdict = {}

    def add_edge(self, a, b, w):
        super().add_edge(a, b)
        self.add_weight(a,b,w)

    def add_weight(self, a, b, w):
        self._weightdict[(a,b)] = w

    def edges(self):
        return self._weightdict
    
    def __str__(self):
        return f"This is in Wieghted graph class"

    def draw(self):
        dot = graphviz.Graph()

        for a in self.vertices():
            dot.node = (str(a))

        for (a,b), w in self._weightdict.items():
            dot.edge(str(a), str(b), label=str(w))

        dot.render('Tree', view=True)

if __name__ == '__main__':

    WG1 = WeightedGraph()
    WG1.add_edge('A', 'B', 25)
    WG1.add_edge('A', 'C', 20)
    WG1.add_edge('A', 'D', 25)
    WG1.add_edge('D', 'B', 23)

    WG1.draw()

# print(WG1.edges())

# print(WG1)
# print(help(WeightedGraph))
# print(WeightedGraph.mro())

# G1 = Graph()
# G1.add_edge('A', 'B')
# G1.add_edge('A', 'C')
# G1.add_edge('A', 'C')
# G1.add_edge('A', 'D')
# G1.add_edge('C', 'D')

# G2 = Graph()
# G2.add_edge('M', 'N')
# G2.add_edge('M', 'O')
# G2.add_edge('M', 'P')
# G2.add_edge('O', 'P')
# G2.add_edge('N', 'P')

# G3 = Graph()
# G3.add_edge('A', 'B')
# G3.add_edge('A', 'C')
# G3.add_edge('A', 'C')
# G3.add_edge('A', 'D')
# G3.add_edge('C', 'D')

# print(G1 == G2)
# print(G1 == G3)
# print(G1)
# len(print)