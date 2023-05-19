from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from queue import Queue
from collections.abc import Iterable

import networkx as nx
import yaml

from src.plotting import plot_tree


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def to_networkx(self) -> nx.DiGraph:
        q = Queue()
        q.put(self.root)
        g = nx.DiGraph()
        while not q.empty():
            next_node: Node = q.get()
            if next_node is None:
                continue
            for child in (next_node.left, next_node.right):
                if child is not None:
                    g.add_edge(next_node.key, child.key)
                    q.put(child)
        return g


def add_children(n: Node, nodes_info: list[Any]) -> None:
    for node_info, child_attr in zip(nodes_info, ("left", "right")):
        if node_info:
            if isinstance(node_info, Iterable):
                key = next(iter(node_info))
                setattr(n, child_attr, Node(key=key))
                # n.left = Node(key=key)
                add_children(getattr(n, child_attr), node_info[key])
            else:
                setattr(n, child_attr, Node(key=node_info))


if __name__ == "__main__":
    # Let's instantiate a binary tree and then implement its traversal
    # First, implement add_children() as a recursive function filling
    # in a binary tree from a tree-like dictionary (that's what is called
    # case in the code below)
    # Second, implement BinaryTree.to_networkx() as an iterative function
    # converting BinaryTree to nx.DiGraph for plotting

    with open("practicum_6/binary_tree_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for c in cases:
        bt = BinaryTree()
        if c is None:
            print("Binary tree is empty")
            continue
        key = next(iter(c.keys()))
        bt.root = Node(key=key)
        add_children(bt.root, c[key])
        plot_tree(bt.to_networkx())
        print()
        # print(
        #    f"Input: a = {c['input']['a']}, b = {c['input']['b']}. "
        #    f"Output: {l_sum}. "
        #    f"Expected output: {l_sum_true}"
        # )
