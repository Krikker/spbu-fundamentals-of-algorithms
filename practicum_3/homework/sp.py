from typing import Any

import networkx as nx
import numpy as np
from queue import PriorityQueue

import sys, os
sys.path.append(os.getcwd())
from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {source_node : [source_node]}  # key = destination node, value = list of intermediate nodes
    dists = {n: np.inf for n in G}
    dists[source_node] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, source_node))

    while not pq.empty():
        mon_dist, node = pq.get()
        if node in visited:
            continue
        visited.add(node)
        for n in G.neighbors(node):
            if n in visited:
                continue
            dist = G[n][node]["weight"] + mon_dist
            if dist < dists[n]:
                dists[n] = dist
                shortest_paths[n] = shortest_paths[node] + [n]
                pq.put((dist, n))

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
