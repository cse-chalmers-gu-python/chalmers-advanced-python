'''
Testing our code with plain assertions 
'''
from campus_network import * 

my_graph = Graph()
# print(my_graph)


# Assertions - 

assert my_graph.vertices() == set()
assert my_graph.edges() != set()

my_graph.add_edge('Library', 'Cafe')

assert my_graph.vertices() == {'Library', 'Cafe'}
assert my_graph.edges() == { ('Library', 'Cafe') }

print("Starting tests for WG")
my_WG = WeightedGraph()

...

# assert WG.edges ... 