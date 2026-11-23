import networkx as nx 
import json 


type Vertex = int | float | str 
type Edge = tuple[Vertex, Vertex] # ('A', 'B')

class Graph(nx.Graph):
    def __init__(self, initial_graph: list[Edge] | None = None):
        super().__init__(initial_graph)

    def vertices(self) -> set[Vertex] | None:
        return set( self.nodes() )

    def add_vertex(self, vertex: Vertex) -> None:
        self.add_node(vertex)

    def add_vertex_value(self, vertex: Vertex, value: object) -> None:
        self.nodes[vertex]["value"] = value

    def get_vertex_value(self, vertex: Vertex) -> object:
        return self.nodes[vertex]["value"]

class WeightedGraph(Graph):
    def set_weight(self, src: Vertex, dst: Vertex, weight: float) -> None:
        edge = (src, dst)
        self.edges[edge]['weight'] = weight 

    def get_weight(self, src: Vertex, dst: Vertex) -> float:
        return self.edges[(src, dst)]['weight']

              
class CampusNetwork(WeightedGraph):
    def __init__(self, routes: dict[str, list[Vertex]] | None = None):
        super().__init__()
        self._routes = routes 

    def place_info(self, place: Vertex) -> object:
        return self.get_vertex_value(place)
     
    def walking_time(self, src, dst):
        return self.get_weight(src, dst)
     
    def places_on_route(self, route):
        return self._routes[route]

    def routes_through_place(self, place):
        if place not in self._routes():
            raise KeyError(place)

        return [route for route, places in self._routes if place in places ]

    

if __name__ == '__main__':
    my_campus = CampusNetwork()

    with open('./fictional_campus_network.json', 'r', encoding='utf-8') as infile:
        campus_data = json.load(infile)

    for node in campus_data['places']:
        my_campus.add_vertex(node)

    for element in campus_data['segments']:
        src = element['from']
        dst = element['to']
        wt = element['weight']
        my_campus.add_edge(src, dst)
        my_campus.set_weight(src, dst, wt)


