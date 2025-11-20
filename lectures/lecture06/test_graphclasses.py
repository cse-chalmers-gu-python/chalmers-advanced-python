# lecture 6, 2025-11-19 / 2025-11-20

import unittest
from hypothesis import given as gv, strategies as st 

from graphclasses import Graph


# ################## hypothesis testing 
class TestGraphClassProperties(unittest.TestCase):
    '''
    This class will provide a test case for ouR Graph class with randomly 
    generated (fuzzed) input data. The basic testing paradigm now builds on 
    properties like symmetry, consistency etc., instead of testing individual
    methods based on data input like behvior on dictionary, negative integers
    or so. The result may be the same, but the basic philosophy is different.
    Here we are using hypothesis library on top of unittest.TestCase, 
    but we can also use it on top of pytest (in which case it will not
    inherit from unittest.TestCase), or on its own.
    '''

    @gv(st.lists(st.tuples(st.integers(min_value=1, max_value=8),
                           st.integers(min_value=1, max_value=8)) ))
    def test_graph_init_behavior(self, edges):
        '''
        Test case to verify if graph init behaves correctly with a broad range
        of randomly generated edges data
        '''

        self.G = Graph(edges)

        expect_edges = { (min(a, b), max(a, b)) for a,b in edges} 
        # expect_edges = set(edges)
        expect_vertices = { node for (a,b) in edges for node in (a, b)}

        self.assertSetEqual(self.G.edges(), expect_edges, 'the edges do not match')
        self.assertSetEqual(self.G.vertices(), expect_vertices, 'the nodes do not match')


    @gv(st.lists(st.tuples(st.integers(min_value=0, max_value=9),
                           st.integers(min_value=0, max_value=9)) ))
    def test_graph_symmetry(self, edges):
        ''' 
        if there is an edge (a, b) then a shall be in b's neighbours
        and b shall be present in a's neighbours        
        '''
        
        self.G = Graph(edges)
        for a, b in edges:
            self.assertIn(a, self.G._adjdict.get(b, set()), 'a is not found in neighbours of b')
            self.assertIn(b, self.G._adjdict.get(a, set()), 'b is not found in neighbours of a')

    # def test_graph_consistency ... 


# ################## unit testing 
class TestGraphClass(unittest.TestCase):
    '''
    This is our unittest class [test case] which tests our graphclasses class
    '''

#     # def setUp(self):
    ''' we use setUp method when test methods need to share objects and data 
    which is to be tested.     '''
#     #     self.testObj = Graph() 

    def test_init_graph_empty(self):
        '''
        This test method tests if empty initialization of our graph works correctly
        '''
        
        self.G = Graph()

        # we typically do not want to use assert, we use assert methods instea
        # assert self.G.edges() == set()
        # assert self.G.vertices() == set()

        self.assertEqual(self.G1.edges(), set(),
                          'the returned edges are not an empty set')
        self.assertSetEqual(self.G1.vertices(), set(),
                             'the returned vertices are not an empty set')

    def test_init_graph_with_values(self):
        '''
        This test method tests if initialization of our graph with a list of 
        edges creates a graph as intended
        '''
        edges = [(1,2), (2,3), (1, 3), (2,5), (2,4)]
        self.G = Graph(edges)
        
        expect_edges = set(edges)
        expect_vertices = {1, 2, 3, 4, 5}

        # assert self.G.edges() == expect_edges
        self.assertSetEqual(self.G.edges(), expect_edges, 'mismatch in edges')

        self.assertEqual(self.G.vertices(), expect_vertices, 'mismatch in vertices')
        self.assertIsInstance(self.G.vertices(), set, 'set is not returned')        

    def test_add_vertex(Self):
        pass
    
    def test_remove_vertex(Self):
        pass
    

if __name__=='__main__':
    unittest.main()