# 1

"""
>>> {1, 2, 3}.add(3)

>>> {1, 2, 3} + {3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'

>>> set(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 argument, got 2

>>> [len(range(n)) for n in range(4)]
[0, 1, 2, 3]

>>> range(8)[-2]
6

>>> {} is not {}
True

>>> (lambda x, y: x(y))(lambda x: x, 8)
8

>>> {2%x: x for x in range(1, 100)}
{0: 2, 2: 99}

>>> len([2%x: x for x in range(100)])
  File "<stdin>", line 1
    len([2%x: x for x in range(100)])
            ^
SyntaxError: invalid syntax

>>> sum(range(1, 101))
5050
"""

# 2

import json

with open('tramnetwork.json') as file:
    tramnetwork = json.load(file)


q2_a = {stop for stop, pos in tramnetwork['stops'].items()
          if pos['lat'] < tramnetwork['stops']['Chalmers']['lat']}

print(q2_a)

q2_b = {stop for stop in tramnetwork['stops']
        if stop in tramnetwork['times']['Järntorget'] or 'Järntorget' in tramnetwork['times'][stop]}

print(q2_b)


# 3

class Graph:
    def __init__(self):
        self.adjdict = {}
        
    def add_edge(self, a, b):
        "store new edge in the adjacency dict"
        if a <= b:
            self.adjdict[a] = self.adjdict.get(a, set())
            self.adjdict[a].add(b)
            # not required in the exam
            # added 2026-01-05, to satisfy that every vertex is in adjdict:
            self.adjdict[b] = self.adjdict.get(b, set())

        else:
            self.adjdict[b] = self.adjdict.get(b, set())
            self.adjdict[b].add(a)
            # not required in the exam
            # added 2026-01-05, to satisfy that every vertex is in adjdict():
            self.adjdict[a] = self.adjdict.get(a, set())

    def edges(self):
        "all edges but only in one direction"
        return {(a, b) for a, bs in self.adjdict.items() for b in bs}
    
    def remove_vertex(self, a):
        "remove vertex and all the edges that contain it"
        if a in self.adjdict:
            self.adjdict.pop(a)

    def remove_vertex_corrected(self, a):
        "remove vertex and all the edges that contain it"
        if a in self.adjdict:
            self.adjdict.pop(a)
        for b in self.adjdict:
            if a in self.adjdict[b]:
                self.adjdict[b].remove(a)


G = Graph()
G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(3, 4)
G.add_edge(1, 3)
G.add_edge(5, 3)

print("3a:", G.edges())
# {(1, 2), (3, 4), (2, 3), (1, 3), (3, 5)}

print("adjdict in 3a:", G.adjdict)


G.remove_vertex(3)

print("3b:", G.edges())
# {(2, 3), (1, 2), (1, 3)}

G = Graph()
G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(3, 4)
G.add_edge(1, 3)
G.add_edge(5, 3)
G.remove_vertex_corrected(3)

print("edges in corrected 3c:", G.edges())
print("adjdict in corrected 3c:", G.adjdict)


# 4

class Tree(Graph):
    "trees whose adjdict is like in the Graoh of Q3 but has at least a root node"
    def __init__(self, root):
        self.adjdict = {root: set()}

    def add_edge(self, a, b):
        if a in self.adjdict and b not in self.adjdict:
            self.adjdict[a].add(b)
            self.adjdict[b] = set()

    def remove_vertex(self, a):
        "to remove a vertex, collect the set of its descendants and remove them all"
        
        def desc(a):
            chs = {a}
            for b in self.adjdict[a]:
                for c in desc(b):
                    chs.add(c)
            return chs
        
        for d in desc(a):
            del self.adjdict[d]

        # correction to Monday lecture: also delete a when appearing as a child node
        for b in self.adjdict:
            self.adjdict[b] = {c for c in self.adjdict[b] if c != a}


T = Tree(1)
T.add_edge(1, 2)
T.add_edge(1, 3)
T.add_edge(2, 4)
T.add_edge(3, 4)
T.add_edge(5, 6) 
T.add_edge(2, 5)

# add these better to show the effect of recursive removal of vertices
# T.add_edge(5, 6) 
# T.add_edge(6, 7) 

print("4b:", T.adjdict)
# {1: {2, 3}, 2: {4, 5}, 3: set(), 4: set(), 5: set()}

T.remove_vertex(2)
print("4c:", T.adjdict)
# {1: {3}, 3: set()}


# 5

def my_decorator(f):
    def my_f(*args):
        val = f(*args)
        if isinstance(val, int):
            return val * val
        else:
            return val
    return my_f

@my_decorator
def square(n):
    return n*n

    
print("5a: ", square(3))
# the solution to 5a is: 81

@my_decorator
def full_name(firstname, familyname):
    return f'{firstname} {familyname}'

print("5b: ", full_name('Jane', 'Austen'))
# the solution to 5b is: Jane Austen


# this function is the solution to 5c:
def repeat(f):
    def my_f(*args):
        for i in range(4):
            f(*args)
    return my_f


@repeat
def hello(x):
    print('hello', x)

hello('World')

