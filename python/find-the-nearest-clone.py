#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


class Node:

    def __init__(self, node_id, color_id, neighbors):
        self.node_id = node_id
        self.color_id = color_id
        self.neighbors = neighbors
        self.marked_to_visit = False

    def add_neighbor(self, neighbors):
        self.neighbors.append(neighbors)

    def __repr__(self):
        return "Node({}, {}, {})".format(self.node_id, self.color_id, self.neighbors)

class Graph:

    def __init__(self, num_nodes, num_edges, edges, color_ids):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.edges = edges
        self.color_ids = color_ids

        self.nodes = []

        self.initialize_nodes()
        self.initialize_edges()

    def initialize_nodes(self):
        for i in range(self.num_nodes):
            self.nodes.append(Node(i, self.color_ids[i], []))

    def initialize_edges(self):
        for edge_a, edge_b in self.edges:
            node_a = self.nodes[edge_a - 1]
            node_b = self.nodes[edge_b - 1]

            node_a.add_neighbor(node_b)
            node_b.add_neighbor(node_a)

    def smallest_path_length(self, color_to_find):
        self.mark_all_nodes_unvisited()
        to_visit = deque()
        initial_node = self.nodes[self.color_ids.index(color_to_find)]
        to_visit.append((initial_node, -1))
        initial_node.marked_to_visit = True

        while to_visit:
            current, depth = to_visit.popleft()
            if current != initial_node and current.color_id == color_to_find:
                return depth + 1
            else:
                for neighbor in current.neighbors:
                    if neighbor.marked_to_visit == False:
                        to_visit.append((neighbor, depth + 1))
                        neighbor.marked_to_visit = True

        return -1

    def mark_all_nodes_unvisited(self):
        for node in self.nodes:
            node.marked_to_visit = False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_nodes, num_edges = map(int, input().split())
    edges = []

    for i in range(num_edges):
        edge = list(map(int, input().split()))
        edges.append(edge)

    color_ids = list(map(int, input().rstrip().split()))
    color_to_find = int(input())

    graph = Graph(num_nodes, num_edges, edges, color_ids)
    print(graph.nodes)
    result = graph.smallest_path_length(color_to_find)

    fptr.write(str(result) + '\n')
    fptr.close()
