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

    def add_vertex_value(self, vertex: Vertex, attribute: str, value: object) -> None:
        self.nodes[vertex][attribute] = value

    def get_vertex_value(self, vertex: Vertex, attribute: str) -> object:
        return self.nodes[vertex][attribute]

    def get_distance(self, a: Vertex, b: Vertex):
        (x1, y1) = self.get_vertex_value(a, 'position')
        (x2, y2) = self.get_vertex_value(b, 'position')

        return ((x2-x1)**2 + (y2-y1)**2)**0.5


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
     
    def places_on_route(self, route: str) -> list[Vertex]:
        if route not in self._routes:
            raise ValueError
        return self._routes[route]

    def routes_through_place_bug(self, place):
        if place not in self._routes:
            raise KeyError(place)

        return [route for route, places in self._routes if place in places ]

    def routes_through_place(self, place):
        if place not in self.vertices():
            raise KeyError(place)

        return [route for route, places in self._routes.items() if place in places]
    

if __name__ == '__main__':
    my_campus = CampusNetwork()

    with open('./campus_network.json', 'r', encoding='utf-8') as infile:
        campus_data = json.load(infile)

    for node, data in campus_data['places'].items():
        # print(node)
        # print(data)
        my_campus.add_vertex(node)
        for attribute, value in data.items():
            my_campus.add_vertex_value(node, attribute, value)

    for element in campus_data['segments']:
        src = element['from']
        dst = element['to']
        wt = element['weight']
        my_campus.add_edge(src, dst)
        my_campus.set_weight(src, dst, wt)

    # for vertex in campus_data['places']:
    #     print(my_campus.get_vertex_value(vertex, 'position'))
    #     print(my_campus.get_vertex_value(vertex, 'category'))

    print(my_campus.get_distance('Library', 'Cafe'))
    # def add_vertex_value(self, vertex: Vertex, value: object) -> None:
    #     self.nodes[vertex]["value"] = value