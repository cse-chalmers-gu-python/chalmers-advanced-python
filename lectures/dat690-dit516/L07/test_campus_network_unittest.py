'''
Testing our code with unittest framework 
'''
from campus_network import * 
import unittest 

# A Class is a Test Case 
class TestGraph(unittest.TestCase):

    def setUp(self):
        self.test_graph = Graph()

    # A Method is a Test Method 
    def test_new_graph_is_empty(self):
        # self.assertEqual(actual, expected)
        self.assertEqual(self.test_graph.vertices(), set())

    def test_add_edge_adds_new_vertices_also(self):
        self.test_graph.add_edge("Library", "Cafe")
        self.assertEqual(self.test_graph.vertices(), {"Library", "Cafe"})
        # self.assertIn(("Library", "Cafe"), my_graph.edges())

    def test_add_edge_returns_None(self):
        self.assertEqual (
        self.test_graph.add_edge('Library', 'Gym'),
        None )

# TestCase for CampusNetwork 

import json 

class TestCampusNetwork(unittest.TestCase):
    def setUp(self):
        with open('campus_network.json', 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        
        self.campus = CampusNetwork(data['routes'])

        for place, information in data['places'].items():
            self.campus.add_vertex(place)
            self.campus.add_vertex_value(place, information)

        for element in data['segments']:
            src = element['from']
            dst = element['to']
            wt = element['weight']
            self.campus.add_edge(src, dst)
            self.campus.set_weight(src, dst, wt)


    def test_places_on_blue_route_correctly_ordered(self):
        self.assertEqual(
            self.campus.places_on_route('Blue'), 
            ["Library", "Cafe", "Gym", "Studio"]
        )

    def test_unknown_route_raises_key_error(self):
        with self.assertRaises(ValueError):
            self.campus.places_on_route('Yellow')


    def test_routes_through_cafe(self):
        self.assertEqual(self.campus.routes_through_place('Cafe'), ['Blue', 'Red'])

        
    # assert something is in anotherthing
