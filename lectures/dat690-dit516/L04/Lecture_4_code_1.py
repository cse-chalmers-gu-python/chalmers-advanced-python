'''
Two graph classes with the same API.

Both classes provide the same methods and return the same results.
This means code that uses a graph does not need to change when we
replace one internal graph representation with the other.

Try it yourself: rename one class to Graph and the other to Graph2,
then run the code again. Switch their names and observe that the
rest of the program still works without changes.

Keeping API same is important
so that outside functions/programs using our class/program does 
not need to change when we change our code  
'''

import graphviz 

class Graph1:
    '''
    Implements basic undirected graph
    stores graph as two sets, a set of vertices and a set of edges
    '''
    def __init__(self):        
        # _ preceeding variable names tells other programmers that 
        # this data is private and shall only be accessed through 
        # getter/setter methods 
        self._vertices = set()
        self._edges = set()


    # Setter methods 
    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices.add(vertex)

    def add_edge(self, a, b):
        # When we add an edge from a to b, we need to make sure that
        # these vertices also exist in our set of vertices 
        # We can add a and b directly to self._vertices, but a better way
        # is to call our setters 

        # self._vertices.add(a)
        # self._vertices.add(b)
        self.add_vertex(a)
        self.add_vertex(b)

        # sorting ensures that edges are not redundant, i.e. (1,2) and (2,1)
        # become the same edge, because when sorted([2,1]) becomes (1,2) 
        a, b = sorted([a, b])
        self._edges.add((a,b))

    # Getter methods
    def vertices(self):
        return self._vertices

    def edges(self):
        return self._edges

    def neighbors(self, n):
        # returns set of vertices connected to node n

        neighbor_set = set ( a if b==n else b                  
                            for (a,b) in self._edges
                            if a == n or b == n  )


        # Simple for-loop which is equivalent to the 
        # comprehension above to construct set of neighbors       
        # neighbor_set = set()
        # for edge in self._edges:            
        #     a,b = edge      # unpack edge into (a,b) [for example a,b = (2,4)]
        #     if a == n or b == n: 
        #         if a==n:
        #             neighbor_set.add(b)
        #         else: 
        #             neighbor_set.add(a)
            
        return neighbor_set

class Graph:
    '''
    Implements basic undirected graph with an adjacency dictionary, instead 
    of storing set of vertices and set of edges 
    '''
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
        # {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
        edges = set( (a, b)
            for a,bs in self._adjdict.items()
            for b in bs 
            if a <= b )

        return edges

    def neighbors(self, n):
    # returns set of vertices connected to node n
        return self._adjdict.get(n, set())

''' 
Using Graph class API
to create a graph, <graph_name> = Graph()
to add vertices, <graph_name>.add_vertex(<vertex>)
to add edge, <graph_name>.add_edge(<vertex a>, <vertex b>)
to get set of edges, <graph_name>.edges()
to get set of vertices, <graph_name>.vertices()
to get set of neighbors of a vertex, <graph_name>.neighbors(<vertex>)
'''



# Create a graph. See how it does not change when you switch your 
# implementation of Graph class between two different Graph classes 

G1 = Graph()

G1.add_vertex(1)
G1.add_vertex(2)
G1.add_vertex(3)
G1.add_vertex(4)

G1.add_edge(1, 2)
G1.add_edge(1, 3)
G1.add_edge(2, 4)
G1.add_edge(3, 5)
G1.add_edge(2, 1)

# print(G1._edges)          # we shall not access internal variables directly
# print(G1._vertices)       # we shall not access internal variables directly

# we shall not access internal variables directly, 
# instead we better call getters/setters 
print('G1 edges: ', G1.edges())
print('G1 nodes: ', G1.vertices())
print('G1, neighbors of node 2: ', G1.neighbors(2))

G2 = Graph() 

G2.add_vertex(1)
G2.add_edge(1, 2)
G2.add_edge(1, 3)
G2.add_edge(2, 3)

# print(G2._adjdict)        # we shall not access internal variables directly
print('G2 edges: ', G2.edges())
print('G2 nodes: ', G2.vertices())
print('G2, neighbors of node 1: ', G2.neighbors(1))

'''
use graphviz to visualize the graph. This function can also be defined 
as a method inside graph class. Give it a try yourself.
To use graphviz, you need to install its software, as well as its library
'''
def viz(graph, name):
    dot = graphviz.Graph()

    # add visualization attributes to change appearance 
    # dot.attr(rankdir='LR')
    # dot.attr()

    for a in graph.vertices():
        dot.node(str(a))

    for a,b in graph.edges():
        dot.edge(str(a), str(b))

    dot.render(name, view=True) 

viz(G1, 'Graph G1')
viz(G2, 'Graph G2')