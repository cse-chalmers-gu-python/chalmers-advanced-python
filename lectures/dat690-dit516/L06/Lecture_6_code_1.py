import networkx as nx 
import json 

''' Type hinting makes our code more readable. It has no functionality in our program, it is just a nice way to tell people what type of variables are being used '''
# Type Hinting or Type Aliases  
type Vertex = int | float | str 
type Edge = tuple[Vertex, Vertex] # ('A', 'B')

''' Though nx.Graph is sufficient for all the work we want to do, but we will implement our own classes derived from nx.Graph. The main reason for this decision is to keep our API unchanged from our previous work. 
An example is as following: 
nx.Graph provides nodes() method, while our ealier designs called it vertices() method. Therefore, we will inherit our Graph class from nx.Graph, and we will write our own method which will simply call nx.Graph method. 
In this way, we will keep our API un-changed. 

'''
class Graph(nx.Graph):
    '''Our Graph class which inherits from nx.Graph
    Please note the type hint for self, we actually do not write type hints for self variable because it is obvious from class itself. In this example, we just wrote it to show how type hints are wrote, but we will stop writing type hints for self in future. 
    '''
    def __init__(self: Graph, initial_graph: list[Edge] | None = None):
        super().__init__(initial_graph)

    def vertices(self: Graph) -> set[Vertex] | None:
        ''' This method has no functionality of its own, it simply calls nodes method from parent to keep API signature consistent with our earlier examples. 
        Also, the output of parent method nodes is not consistent with our API, so we convert it to set becfore returning  '''
        return set( self.nodes() )

    def add_vertex(self: Graph, vertex: Vertex) -> None:
        # Method has no functionality of its own, simply calles parent's method 
        self.add_node(vertex)

class WeightedGraph(Graph):
    # No __init__ needed here because the data we want to add can be added to Graph instance made by parent class  

    def set_weight(self, src: Vertex, dst: Vertex, weight: float) -> None:
        edge = (src, dst)
        self.edges[edge]['weight'] = weight 

    def get_weight(self, src: Vertex, dst: Vertex) -> float:
        return self.edges[(src, dst)]['weight']

              
class CampusNetwork(WeightedGraph):
    '''
    Class to model weighted graph for our fictional campus netwrok. 
    '''

    def __init__(self):
        '''
        We instentiate WeightedGraph by calling super(), and add more information to store _routes
        '''
        super().__init__()
        self._routes: dict[str, list[Vertex]]
        # example_route: {'blue': [lib, cafe, gym, studio]}

    def place_inf(self, place):
        ... 
    def walking_time(self, src, dst):
        pass 
    def places_on_route(self, route):
        pass
    def routes_though_place(self, place):
        pass
    def fastest_path(self, src, dst):
        pass


# Create a graph of type CampusNetwork, i.e. A graph which is WeightedGraph (parent) plus route storage 
my_campus = CampusNetwork()

# Open and load json which contains campus network data 
with open('./fictional_campus_network.json', 'r', encoding='utf-8') as infile:
    campus_data = json.load(infile)

# print(campus_data)

for node in campus_data['places']:
    # Create vertices, Although it is only needed if you have standalone nodes in your graph. Otherwise, adding edges will automatically add all vertices 
    my_campus.add_vertex(node)

for element in campus_data['segments']:
    # Add edges and their weights. Please note that nx.Graph itself can add edge weight, but we used this multi-inheritence structure to keep our API consistent 

    src = element['from']
    dst = element['to']
    wt = element['weight']
    my_campus.add_edge(src, dst)
    my_campus.set_weight(src, dst, wt)


print(my_campus.edges(data=True))
print(my_campus.edges())


# print(my_campus.vertices())    


# my_graph = WeightedGraph()
# # my_graph = Graph()
# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('D', 'B')

# print(my_graph.edges)

# # print(my_graph.edges [ ('A', 'D') ]  ) 
# my_graph.set_weight( 'A', 'D', 25)
# my_graph.set_weight( 'A', 'B', 45)
# print(my_graph.get_weight('A', 'D'))
# print(my_graph.get_weight('A', 'B'))
# # print(my_graph.edges [ ('A', 'D') ]  ) 