'''Hypothesis library is used to test properties. For example, we want to test properties of our Graph.get_distance() method. 

Please note that the test class(es) remain the same as we designed in case of unittest. Also, testing methods also remain the same. The only thing that changes is now we have given decorators sitting on top of each of our test method. This way, we generate lots of random input data for the target code, and test it over and over again with random data.

'''
from hypothesis import given as gv, strategies as st 

import unittest 

from campus_network import *
                # lat           # lon 
pos = st.tuples( st.floats(10.9, 24.0), st.floats(55.3, 69.1) )

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.test_graph = Graph()
        for node in {'A', 'B', 'C', 'D'}:
            self.test_graph.add_vertex(node)

    @gv(pos_a=pos, pos_b=pos)
    def test_distance_is_symmetric(self, pos_a, pos_b):

        self.test_graph.add_vertex_value('A', 'position', pos_a)
        self.test_graph.add_vertex_value('B', 'position', pos_b)

        print(pos_a, pos_b)
        self.assertGreater(
            self.test_graph.get_distance('A', 'B'), 
            self.test_graph.get_distance('B', 'A')
        )
        self.assertAlmostEqual(
            self.test_graph.get_distance('A', 'B'),
            self.test_graph.get_distance('B', 'A')
        )

    # def test_distance_preserves_identify(self): ... 

    # def test_distance_is_always_positive(self): ...

