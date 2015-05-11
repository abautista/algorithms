from unittest import TestCase, main

from algorithms.graphs.graph import Graph


class GraphTest(TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(0, 3)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 3)

    def test_get_edges(self):
        edges = self.graph.get_edges()
        print(edges)
        
    def test_contract_nodes(self):
        print(self.graph.g)
        self.graph.contract_nodes(0, 2)
        print(self.graph.g)

if __name__ == '__main__':
    main()
