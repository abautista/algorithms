#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import random


class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, u, v):
        self.g.setdefault(u, []).append(v)
        self.g.setdefault(v, []).append(u)
        
    def add_single_edge(self, u, v):
        self.g.setdefault(u, []).append(v)
        
    def get_edges(self):
        aux = copy.deepcopy(self.g)
        edges = []
        for node, adjs in aux.items():
            for adj in adjs:
                edges.append([node, adj])
                aux[adj].remove(node)
        return edges
        
    def contract_nodes(self, u, v):
        combined_adjs = self.g[u] + self.g[v]
        self.g[u] = list(filter(lambda x: x != u and x != v, combined_adjs))
        del self.g[v]
        
        for node, adjs in self.g.items():
            self.g[node] = [u if adj == v else adj for adj in adjs]        

    def minimal_cut(self):
        edges = self.get_edges()
        while len(self.g.keys()) > 2:
            u, v = random.choice(edges)
            self.contract_nodes(u, v)
            edges = self.get_edges()

            
def create_graph_from_file():
    f = open("karger_min_cut.txt", "r")
    lines = f.readlines()
    g = Graph()
    for line in lines:
        line = line.replace("\r", "").replace("\n", "").split("\t")
        node = line[0]
        adjs = line[1:len(line) - 1]
        for adj in adjs:
            g.add_single_edge(int(node), int(adj))
    f.close()
    return g


if __name__ == '__main__':
    min = 10000
    for i in range(1, 1000):
        print i
        graph = create_graph_from_file()
        graph.minimal_cut()
        min_cut = len(graph.g[graph.g.keys()[0]])
        if min_cut < min:
            min = min_cut
            print "min cut: %d" %min
