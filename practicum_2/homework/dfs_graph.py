import queue
from typing import Any

import networkx as nx

import sys, os
sys.path.append(os.getcwd())
print(sys.path)
from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    stack = {node}
    while len(stack) > 0:
        nd = stack.pop()
        visit(nd)
        visited[nd] = True
        for x in G.neighbors(nd):
            if not visited[x]: stack.add(x)

def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}
    stack = [node]
    sorted_stack = []
    while len(stack) > 0:
        unvisited = [n for n in G.neighbors(stack[-1]) if not visited[n] and not n in stack]
        if len(unvisited) == 0:
            n = stack.pop()
            visited[n] = True
            sorted_stack.append(n)
        else:
            stack += unvisited
    m = dict()
    for i in range(len(sorted_stack)):
        m.update({sorted_stack.pop(): str(i)})
    return nx.relabel.relabel_nodes(G, m)


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "graph_2.edgelist", create_using=nx.DiGraph
    )
    print("-" * 32)
    print("Topological sort")
    print("-" * 32)
    sorted_nodes = topological_sort(G, node='0')
    for node in sorted_nodes:
        print(f"Wow, it is {node} right here!")

    plot_graph(G)
    plot_graph(topological_sort(G, node="0"))
