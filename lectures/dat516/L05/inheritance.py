from dunder import Graph

class WeightedGraph(Graph):
    """a weighted undirected graph, inheriting from class Graph"""

    def __init__(self):
        super().__init__() # call initialisation method in superclass
        self._weights = {} # {(A,B): 4}  add an additional instance variable

    def set_weight(self, a, b, w):
        """set weight for an edge"""
        if (b,a) in self._weights:
            self._weights[(b,a)] = w
        else:
            self._weights[(a,b)] = w

    def get_weight(self, a, b, default=None):
        """get the weight for an edge"""
        if (b,a) in self._weights:
            return self._weights[(b,a)]
        elif (a,b) in self._weights:
            return self._weights[(a,b)]
        else:
            return default

        # one-liner using dict.get():
        # return self._weights.get((a,b), self._weights.get((b,a), default))

# Test code

W = WeightedGraph()
W.add_edge("X", "Y")
W.add_edge("X", "Z")
W.add_edge("Y", "Z")
W.add_edge("Y", "Å")
W.add_edge("Å", "Å")

assert len(W) == 4
assert len(W.edges()) == 5

W.set_weight("X", "Y", 8)
W.set_weight("Y", "Z", 3)

assert W.get_weight("X", "Y") == 8
assert W.get_weight("Z", "Y") == 3
assert W.get_weight("Z", "Å", False) == False
