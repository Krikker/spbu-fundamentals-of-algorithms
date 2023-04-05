from typing import Any

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import sys, os
sys.path.append(os.getcwd())
from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    mst_set.add(start_node)
    rest_set.remove(start_node)
    considered_edges = {(start_node, x) for x in G.neighbors(start_node)}
    while len(rest_set) > 0:
        min_edge = {
            "edge": (None, None),
            "weight": np.inf
        }
        for e in considered_edges:
            if G[e[0]][e[1]]["weight"] < min_edge["weight"]:
                min_edge["edge"] = e
                min_edge["weight"] = G[e[0]][e[1]]["weight"]
        mst_edges.add(min_edge["edge"])
        new_node = min_edge["edge"][1]
        mst_set.add(new_node)
        rest_set.remove(new_node)
        for n in G.neighbors(new_node):
            if n in mst_set:
                considered_edges.remove((n, new_node))
            else:
                considered_edges.add((new_node, n))

    return mst_edges

if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
