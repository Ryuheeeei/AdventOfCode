#!usr/bin/env python3
# coding: utf-8

import networkx as nx
import matplotlib.pyplot as plt     # For drawing graph

all_parents = []
all_children = []


def graph_setting(graph, filename):
    """
    This file reads file and return all nodes
    @param graph: graph instance
    @param filename: input_text
    @return: graph already initial set
    """
    with open(filename) as f:
        content = f.read().split()

    for i, sentence in enumerate(content):
        temp = sentence.split(")")
        parent, child = temp[0], temp[1]
        all_parents.append(parent)
        all_children.append(child)

    all_nodes = set(all_parents + all_children)
    graph.add_nodes_from(all_nodes)
    for edge in zip(all_parents, all_children):
        graph.add_edge(edge[0], edge[1])

    return graph


def example_graph_draw():
    """
    This file is just for drawing network
    """
    g = nx.DiGraph()
    g = graph_setting(g, "data/day6_test.txt")
    nx.draw_networkx(g)
    plt.show()
    return None


def solution():
    g = nx.DiGraph()
    g = graph_setting(g, "data/day6.txt")
    all_path = nx.shortest_path(g)
    all_nodes = nx.nodes(g)

    path_count = 0

    for node in all_nodes:
        path_count += len(all_path[node])

    path_count -= len(all_nodes)

    print(path_count)
    return None


def solution_part2():
    g = nx.Graph()
    g = graph_setting(g, "data/day6.txt")
    all_path = nx.shortest_path(g)
    all_nodes = nx.nodes(g)

    answer = len(nx.shortest_path(g, "YOU", "SAN")) - 3
    print(answer)
    return None


if __name__ == '__main__':
    # example_graph_draw()      # Just for visualizing
    # solution()    # Part 1
    solution_part2()    # Part 2
