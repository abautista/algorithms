#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../..")
print sys.path

from algorithms.graphs.graph import Graph


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
